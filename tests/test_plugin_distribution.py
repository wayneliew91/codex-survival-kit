import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "codex-survival-kit"


class PluginDistributionTests(unittest.TestCase):
    def test_plugin_manifest_contract(self):
        manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
        self.assertEqual(manifest["name"], "codex-survival-kit")
        self.assertEqual(manifest["version"], (ROOT / "VERSION").read_text().strip())
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertNotIn("apps", manifest)
        self.assertNotIn("mcpServers", manifest)
        self.assertNotIn("hooks", manifest)
        self.assertEqual(manifest["interface"]["category"], "Developer Tools")

    def test_marketplace_points_to_nested_plugin(self):
        marketplace = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text())
        entry = marketplace["plugins"][0]
        self.assertEqual(entry["name"], "codex-survival-kit")
        self.assertEqual(entry["source"], {"source": "local", "path": "./plugins/codex-survival-kit"})
        self.assertEqual(entry["policy"], {"installation": "AVAILABLE", "authentication": "ON_INSTALL"})

    def test_plugin_skill_mirror_is_exact(self):
        canonical = ROOT / "skills"
        mirrored = PLUGIN / "skills"
        canonical_files = sorted(p.relative_to(canonical) for p in canonical.rglob("*") if p.is_file())
        mirrored_files = sorted(p.relative_to(mirrored) for p in mirrored.rglob("*") if p.is_file())
        self.assertEqual(canonical_files, mirrored_files)
        for rel in canonical_files:
            self.assertEqual((canonical / rel).read_bytes(), (mirrored / rel).read_bytes(), str(rel))

    def test_readme_documents_plugin_install(self):
        text = (ROOT / "README.md").read_text().lower()
        self.assertIn("codex plugin marketplace add", text)
        self.assertIn("codex plugin add codex-survival-kit@codex-survival-kit", text)


if __name__ == "__main__":
    unittest.main()
