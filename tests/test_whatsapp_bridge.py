import unittest

from integrations.whatsapp_mcp_bridge import (
    BridgeConfig,
    is_sender_allowed,
    normalize_number,
    parse_command,
    execute_mapped_command,
)


class WhatsAppBridgeTests(unittest.TestCase):
    def test_normalize_number(self):
        self.assertEqual(normalize_number("+34123"), "whatsapp:+34123")
        self.assertEqual(normalize_number("whatsapp:+34123"), "whatsapp:+34123")

    def test_parse_command(self):
        self.assertEqual(parse_command("/cmd status"), "status")
        self.assertEqual(parse_command("cmd:status"), "status")
        self.assertIsNone(parse_command("hola"))

    def test_sender_allowed(self):
        allowed = {"whatsapp:+34123"}
        self.assertTrue(is_sender_allowed("+34123", allowed))
        self.assertFalse(is_sender_allowed("+34999", allowed))

    def test_execute_allowed_and_blocked(self):
        config = BridgeConfig(
            allowed_numbers={"whatsapp:+34123"},
            allowed_commands={"ok": "echo ok"},
            command_timeout_seconds=5,
        )
        code, output = execute_mapped_command("ok", config)
        self.assertEqual(code, 0)
        self.assertIn("ok", output)

        blocked_code, blocked_output = execute_mapped_command("rm", config)
        self.assertEqual(blocked_code, 2)
        self.assertIn("no permitido", blocked_output)


if __name__ == "__main__":
    unittest.main()
