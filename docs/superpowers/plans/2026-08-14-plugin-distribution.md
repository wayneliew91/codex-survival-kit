# Plugin Distribution Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Codex Survival Kit as a skill-only Codex plugin marketplace package while preserving standalone skill installation.

**Architecture:** Keep top-level `skills/` canonical. Generate `plugins/codex-survival-kit/skills/` from that source, declare the plugin with `.codex-plugin/plugin.json`, and expose it through `.agents/plugins/marketplace.json`. CI validates manifest shape and byte-for-byte mirror integrity.

**Tech Stack:** JSON, Python 3.12/3.13 standard library, GitHub Actions.

## Global Constraints

- Do not modify the five existing skill bodies.
- Do not reference or access private repositories.
- No apps, MCP servers, hooks, credentials, or external runtime dependencies.
- Plugin version is `0.2.0` and must match root `VERSION`.
- `skills/` is the only human-maintained skill source.
- `plugins/codex-survival-kit/skills/` is generated and must remain byte-identical.

---

### Task 1: Add failing plugin distribution contracts

**Files:**
- Create: `tests/test_plugin_distribution.py`

**Interfaces:**
- Consumes: canonical `skills/`, root `VERSION`.
- Produces: executable contract for manifest, marketplace, mirror, and documentation.

- [ ] **Step 1: Write the failing test**

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_plugin_distribution -v`
Expected: FAIL because plugin manifest and marketplace do not exist.

- [ ] **Step 3: Commit the RED test**

```bash
git add tests/test_plugin_distribution.py
git commit -m "test: define plugin distribution contract"
```

---

### Task 2: Implement deterministic plugin package and validation

**Files:**
- Create: `.agents/plugins/marketplace.json`
- Create: `plugins/codex-survival-kit/.codex-plugin/plugin.json`
- Create: `scripts/sync_plugin_skills.py`
- Modify: `scripts/validate_skills.py`
- Generate: `plugins/codex-survival-kit/skills/**`

**Interfaces:**
- Consumes: top-level `skills/`.
- Produces: `sync_plugin_skills.py --check` and plugin manifest validation through `validate_repo()`.

- [ ] **Step 1: Implement mirror synchronization**

```python
from pathlib import Path
import argparse
import filecmp
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGET = ROOT / "plugins" / "codex-survival-kit" / "skills"


def file_map(root: Path):
    return {p.relative_to(root): p for p in root.rglob("*") if p.is_file()}


def is_synced() -> bool:
    source = file_map(SOURCE)
    target = file_map(TARGET) if TARGET.exists() else {}
    return source.keys() == target.keys() and all(filecmp.cmp(source[k], target[k], shallow=False) for k in source)


def sync() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    shutil.copytree(SOURCE, TARGET)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        return 0 if is_synced() else 1
    sync()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Add plugin manifest**

Use `.codex-plugin/plugin.json` with name/version/license/repository metadata, `"skills": "./skills/"`, `Developer Tools` category, no app/MCP/hook fields, and three starter prompts.

- [ ] **Step 3: Add marketplace**

Use marketplace name `codex-survival-kit`, display name `Codex Survival Kit`, local source `./plugins/codex-survival-kit`, `AVAILABLE`, `ON_INSTALL`, and `Developer Tools`.

- [ ] **Step 4: Extend repository validator**

Add JSON parsing and checks for plugin name, version equality with `VERSION`, skill path, absence of app/MCP/hook fields, exact marketplace source/policy, and mirror integrity.

- [ ] **Step 5: Generate the mirror**

Run: `python scripts/sync_plugin_skills.py`

- [ ] **Step 6: Run GREEN verification**

Run:

```bash
python -m unittest discover -s tests -v
python scripts/validate_skills.py .
python scripts/sync_plugin_skills.py --check
```

Expected: all pass.

- [ ] **Step 7: Commit implementation**

```bash
git add .agents plugins scripts tests
git commit -m "feat: add Codex plugin distribution"
```

---

### Task 3: Document distribution and wire CI

**Files:**
- Modify: `README.md`
- Modify: `VERSION`
- Modify: `.github/workflows/validate.yml`
- Modify: `CONTRIBUTING.md`

**Interfaces:**
- Consumes: plugin ID `codex-survival-kit@codex-survival-kit`.
- Produces: public install instructions and CI drift gate.

- [ ] **Step 1: Set version**

Write `0.2.0` to `VERSION`.

- [ ] **Step 2: Document plugin installation**

README must retain individual `$skill-installer` and manual skill instructions, then add:

```bash
codex plugin marketplace add wayneliew91/codex-survival-kit
codex plugin add codex-survival-kit@codex-survival-kit
```

State that the plugin is skill-only and requests no apps, MCP servers, credentials, or external permissions.

- [ ] **Step 3: Document contributor sync rule**

Add to `CONTRIBUTING.md`:

```bash
python scripts/sync_plugin_skills.py
python scripts/sync_plugin_skills.py --check
```

Contributors edit top-level `skills/` only, then regenerate the plugin mirror.

- [ ] **Step 4: Add CI mirror check**

Append after skill validation:

```yaml
- name: Verify plugin mirror
  run: python scripts/sync_plugin_skills.py --check
```

- [ ] **Step 5: Run full verification**

```bash
python -m unittest discover -s tests -v
python scripts/validate_skills.py .
python scripts/sync_plugin_skills.py --check
```

Expected: all pass with no warnings/errors.

- [ ] **Step 6: Commit documentation and CI**

```bash
git add README.md VERSION CONTRIBUTING.md .github/workflows/validate.yml
git commit -m "docs: publish plugin install workflow"
```