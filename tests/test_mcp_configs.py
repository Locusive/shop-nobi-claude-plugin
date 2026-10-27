"""Check installable MCP connections without contacting Shop Nobi or a model."""

import ast
import base64
import json
from pathlib import Path
import re
import unittest
from urllib.parse import parse_qs, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class McpConfigurationTest(unittest.TestCase):
    """Keep installed URLs, client identity and copyable examples consistent."""

    def test_installed_connections_preserve_transport_and_client_identity(self):
        """Each package reports its source without replacing its client identity."""
        configurations = [
            ("plugins/shop-nobi/.mcp.json", "claude_plugin", None),
            ("mcp.json", "cursor_plugin", "shop-nobi-cursor"),
        ]
        for filename, source, client in configurations:
            with self.subTest(package=source):
                server = json.loads((ROOT / filename).read_text())["mcpServers"]["shop-nobi"]
                self.assertEqual(server["type"], "http")
                self.assert_connection_url(server["url"], source)
                self.assertEqual(server.get("headers", {}).get("x-nobi-mcp-client"), client)

    def test_cursor_install_link_and_manual_configuration_match_package(self):
        """Cursor's link and manual setup install the packaged connection."""
        readme = (ROOT / "README.md").read_text()
        encoded = re.search(r"https://cursor.com/install-mcp\?name=shop-nobi&config=([^)]*)", readme)
        self.assertIsNotNone(encoded)
        installed = json.loads(base64.b64decode(unquote(encoded.group(1))))
        packaged = json.loads((ROOT / "mcp.json").read_text())["mcpServers"]["shop-nobi"]
        self.assertEqual(installed, packaged)
        manual = re.search(r"```json\n(.*?)\n```", readme, re.DOTALL)
        self.assertIsNotNone(manual)
        self.assertEqual(json.loads(manual.group(1))["mcpServers"]["shop-nobi"], packaged)

    def test_executable_examples_identify_their_configuration(self):
        """Recipes and the standalone demo retain valid syntax and source labels."""
        examples = list((ROOT / "examples").glob("*_shop_agent.py"))
        examples.extend([ROOT / "examples/vercel_ai_sdk_shop_agent.ts", ROOT / "examples/try-search.mjs"])
        self.assertEqual(len(examples), 5)
        for path in examples:
            with self.subTest(example=path.name):
                content = path.read_text()
                urls = re.findall(r'"(https://api\.nobi\.ai/v1/shop/mcp[^"\s]*)"', content)
                self.assertEqual(len(urls), 1)
                self.assert_connection_url(urls[0], "framework_example")
                if path.suffix == ".py":
                    ast.parse(content, filename=str(path))

    def assert_connection_url(self, value, source):
        """Require the public endpoint with exactly one explicit source tag."""
        url = urlsplit(value)
        self.assertEqual((url.scheme, url.netloc, url.path), ("https", "api.nobi.ai", "/v1/shop/mcp"))
        self.assertEqual(parse_qs(url.query), {"source": [source]})
        self.assertEqual(url.fragment, "")


if __name__ == "__main__":
    unittest.main()
