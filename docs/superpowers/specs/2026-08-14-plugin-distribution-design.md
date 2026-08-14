# Codex Survival Kit Plugin Distribution Design

## Goal

Add an official-style Codex plugin distribution layer without changing the behavior of the five existing skills or exposing any private project content.

## Current truth

- `skills/` remains the canonical, human-maintained source for all five skills.
- Existing direct skill installation paths must keep working.
- The plugin is skill-only: no app connector, MCP server, hook, credential, or external permission is required.
- The two private repositories are out of scope.

## Options considered

### A. Treat repository root as the plugin

This would add `.codex-plugin/plugin.json` at the repository root and reuse `skills/` directly. It is the smallest file change, but Codex marketplace entries currently expect a plugin beneath the marketplace root and repo-root local paths such as `./` are not reliably accepted. This would weaken installability.

### B. Move canonical skills under `plugins/codex-survival-kit/`

This matches the standard marketplace layout, but it breaks the existing public paths under `skills/<name>/` and makes individual skill installation less stable.

### C. Generated plugin mirror — selected

Keep `skills/` canonical. Add `plugins/codex-survival-kit/` containing a generated mirror of those skill directories plus `.codex-plugin/plugin.json`. Add `.agents/plugins/marketplace.json` pointing to `./plugins/codex-survival-kit`. A deterministic sync script copies canonical skills into the plugin package, and CI fails if the mirror differs.

This keeps both distribution modes valid while avoiding symlinks and preventing silent drift.

## Plugin structure

```text
.
├── .agents/plugins/marketplace.json
├── skills/                              # canonical source
├── plugins/codex-survival-kit/
│   ├── .codex-plugin/plugin.json
│   └── skills/                          # generated mirror
├── scripts/sync_plugin_skills.py
├── scripts/validate_skills.py
└── tests/test_plugin_distribution.py
```

## Manifest

`plugins/codex-survival-kit/.codex-plugin/plugin.json` will use:

- name: `codex-survival-kit`
- version: `0.2.0`
- license: `MIT`
- skills path: `./skills/`
- category: `Developer Tools`
- capabilities: `Interactive`, `Read`, `Write`
- no apps, MCP servers, hooks, or authentication dependencies
- up to three short starter prompts covering token efficiency, continuation handoff, and regression/debugging safety

The marketplace will use the local source path `./plugins/codex-survival-kit`, `AVAILABLE` installation policy, `ON_INSTALL` authentication timing, and `Developer Tools` category.

## Synchronization contract

`skills/` is authoritative. `scripts/sync_plugin_skills.py` replaces only `plugins/codex-survival-kit/skills/` from canonical source. The generated plugin copy must never become a second source of truth.

A check mode compares file paths and bytes and exits non-zero on any mismatch. CI runs check mode after unit tests.

## Validation

Tests must prove:

1. the plugin manifest exists and declares all required metadata;
2. the marketplace points to the standard nested plugin path;
3. plugin version matches root `VERSION`;
4. the plugin mirror exactly matches canonical `skills/`;
5. no unexpected apps/MCP/hooks are declared;
6. existing standalone skill validation still passes;
7. README documents both individual-skill and plugin installation paths.

## Versioning

This is a new distribution capability, so the repository version advances from `0.1.0` to `0.2.0`. Skill bodies remain unchanged.

## Release safety

Implementation occurs on `agent/plugin-distribution`. The branch must pass local unit tests and validator checks, then GitHub Actions on the PR/branch, before it can be merged to `main`.