"""Puente WhatsApp <-> MCP para ejecutar comandos de forma controlada.

Flujo recomendado:
1. Exponer `run_webhook_server` detrás de HTTPS (por ejemplo con ngrok).
2. Configurar el webhook de WhatsApp (Twilio Sandbox o número productivo) a ese endpoint.
3. Ejecutar `run_mcp_server` para que Codex/cliente MCP consuma herramientas.

Este módulo prioriza seguridad básica:
- Lista blanca de comandos permitidos.
- Lista blanca de números autorizados.
- Timeout por comando.
- Registro local de eventos.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs


DEFAULT_ALLOWED_COMMANDS = {
    "help": "echo 'Comandos permitidos: status, partido, jugadores'",
    "status": "python main.py --fast",
    "partido": "python main.py --fast",
    "jugadores": "python team_editor.py",
}


@dataclass
class BridgeConfig:
    allowed_numbers: set[str]
    allowed_commands: dict[str, str]
    command_timeout_seconds: int = 20
    log_file: Path = Path("integrations/whatsapp_events.jsonl")


def normalize_number(number: str) -> str:
    """Normaliza número de WhatsApp estilo Twilio: 'whatsapp:+34123456'."""
    cleaned = number.strip()
    if not cleaned:
        return ""
    if not cleaned.startswith("whatsapp:"):
        return f"whatsapp:{cleaned}"
    return cleaned


def build_config_from_env() -> BridgeConfig:
    raw_numbers = os.getenv("WHATSAPP_ALLOWED_NUMBERS", "")
    numbers = {normalize_number(part) for part in raw_numbers.split(",") if part.strip()}
    raw_commands = os.getenv("WHATSAPP_ALLOWED_COMMANDS_JSON", "")

    allowed_commands = dict(DEFAULT_ALLOWED_COMMANDS)
    if raw_commands.strip():
        allowed_commands.update(json.loads(raw_commands))

    timeout = int(os.getenv("WHATSAPP_COMMAND_TIMEOUT", "20"))
    log_file = Path(os.getenv("WHATSAPP_LOG_FILE", "integrations/whatsapp_events.jsonl"))
    return BridgeConfig(
        allowed_numbers=numbers,
        allowed_commands=allowed_commands,
        command_timeout_seconds=timeout,
        log_file=log_file,
    )


def is_sender_allowed(sender: str, allowed_numbers: Iterable[str]) -> bool:
    normalized = normalize_number(sender)
    allowed = {normalize_number(n) for n in allowed_numbers}
    return normalized in allowed


def parse_command(body: str) -> str | None:
    """Extrae un comando de un mensaje de WhatsApp.

    Formatos:
    - /cmd status
    - cmd:status
    """
    text = body.strip()
    if text.startswith("/cmd "):
        return text[5:].strip().split()[0]
    if text.lower().startswith("cmd:"):
        return text[4:].strip().split()[0]
    return None


def execute_mapped_command(command_key: str, config: BridgeConfig) -> tuple[int, str]:
    if command_key not in config.allowed_commands:
        return 2, f"Comando no permitido: {command_key}"

    shell_command = config.allowed_commands[command_key]
    try:
        completed = subprocess.run(
            shlex.split(shell_command),
            capture_output=True,
            text=True,
            timeout=config.command_timeout_seconds,
            check=False,
        )
        output = (completed.stdout + "\n" + completed.stderr).strip()
        safe_output = output[:1000] if output else "(sin salida)"
        return completed.returncode, safe_output
    except subprocess.TimeoutExpired:
        return 124, f"Timeout: comando excedió {config.command_timeout_seconds}s"


def append_event(log_file: Path, payload: dict) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    with log_file.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(payload, ensure_ascii=False) + "\n")


def twiml_message(message: str) -> bytes:
    escaped = (
        message.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    xml = f"<?xml version='1.0' encoding='UTF-8'?><Response><Message>{escaped}</Message></Response>"
    return xml.encode("utf-8")


class WhatsAppWebhookHandler(BaseHTTPRequestHandler):
    config = build_config_from_env()

    def do_POST(self) -> None:  # noqa: N802
        content_length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(content_length).decode("utf-8", errors="replace")
        params = parse_qs(body)

        sender = params.get("From", [""])[0]
        text = params.get("Body", [""])[0]
        command_key = parse_command(text)

        event = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "sender": sender,
            "text": text,
            "command": command_key,
        }

        if not is_sender_allowed(sender, self.config.allowed_numbers):
            reply = "Número no autorizado."
            event["result"] = "unauthorized"
        elif not command_key:
            reply = "Usa /cmd <comando>. Ejemplo: /cmd status"
            event["result"] = "invalid_format"
        else:
            code, output = execute_mapped_command(command_key, self.config)
            reply = f"[{command_key}] exit={code}\n{output}"
            event["result"] = {"exit_code": code, "output": output}

        append_event(self.config.log_file, event)
        payload = twiml_message(reply)

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/xml; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


def run_webhook_server(host: str, port: int) -> None:
    server = ThreadingHTTPServer((host, port), WhatsAppWebhookHandler)
    print(f"Webhook escuchando en http://{host}:{port}/")
    server.serve_forever()


def run_mcp_server(config: BridgeConfig) -> None:
    try:
        from mcp.server.fastmcp import FastMCP
    except Exception as exc:  # pragma: no cover
        raise SystemExit(
            "No se pudo importar mcp.server.fastmcp. Instala el SDK: pip install mcp"
        ) from exc

    mcp = FastMCP("whatsapp-bridge")

    @mcp.tool()
    def whatsapp_bridge_status() -> dict:
        return {
            "allowed_numbers": sorted(config.allowed_numbers),
            "allowed_commands": sorted(config.allowed_commands.keys()),
            "log_file": str(config.log_file),
        }

    @mcp.tool()
    def whatsapp_bridge_execute(command: str) -> dict:
        code, output = execute_mapped_command(command, config)
        event = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "sender": "mcp-tool",
            "text": f"/cmd {command}",
            "command": command,
            "result": {"exit_code": code, "output": output},
        }
        append_event(config.log_file, event)
        return {"exit_code": code, "output": output}

    mcp.run(transport="stdio")


def main() -> None:
    parser = argparse.ArgumentParser(description="WhatsApp MCP bridge")
    parser.add_argument("mode", choices=["webhook", "mcp", "both"])
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()

    config = build_config_from_env()
    WhatsAppWebhookHandler.config = config

    if args.mode == "webhook":
        run_webhook_server(args.host, args.port)
        return

    if args.mode == "mcp":
        run_mcp_server(config)
        return

    thread = threading.Thread(target=run_webhook_server, args=(args.host, args.port), daemon=True)
    thread.start()
    run_mcp_server(config)


if __name__ == "__main__":
    main()
