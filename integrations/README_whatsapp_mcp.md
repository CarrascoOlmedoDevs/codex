# MCP + WhatsApp bridge

Este bridge conecta mensajes de WhatsApp con comandos controlados para Codex vía MCP.

## Requisitos
- Python 3.10+
- (Opcional para modo MCP) `pip install mcp`
- Número de WhatsApp en Twilio (sandbox o productivo)

## Variables de entorno
```bash
export WHATSAPP_ALLOWED_NUMBERS="whatsapp:+34111222333"
export WHATSAPP_COMMAND_TIMEOUT="20"
export WHATSAPP_ALLOWED_COMMANDS_JSON='{"status":"python main.py --fast"}'
export WHATSAPP_LOG_FILE="integrations/whatsapp_events.jsonl"
```

## Ejecución
Webhook para Twilio:
```bash
python integrations/whatsapp_mcp_bridge.py webhook --port 8080
```

Servidor MCP (stdio):
```bash
python integrations/whatsapp_mcp_bridge.py mcp
```

Ambos a la vez:
```bash
python integrations/whatsapp_mcp_bridge.py both --port 8080
```

## Formato de mensajes de WhatsApp
- `/cmd status`
- `cmd:status`

## Seguridad mínima recomendada
- Usa solo números permitidos (`WHATSAPP_ALLOWED_NUMBERS`).
- No agregues comandos peligrosos en `WHATSAPP_ALLOWED_COMMANDS_JSON`.
- Expón el webhook solo detrás de HTTPS y autenticación de proveedor.
