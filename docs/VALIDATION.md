# Validation — v0.1.0

Date: 2026-08-14

## Local automated checks

```text
python3 -m unittest discover -s tests -v
Result: PASS — 18 tests, 0 failures, 0 errors.

python3 scripts/validate_skills.py .
Result: PASS.
```

Validated areas include:

- required `SKILL.md` structure and frontmatter;
- skill folder/name consistency;
- trigger-description convention;
- required `agents/openai.yaml` files;
- relative Markdown links;
- forbidden per-skill auxiliary documentation;
- obvious credential/private-path patterns within skill packages;
- initial five-skill repository contract;
- per-skill compact-content requirements;
- root public repository files and reset disclaimer.

## Pressure scenarios

Each skill has forward-test scenarios under `tests/pressure/`.

Live Codex behavioral replay was **not run** in the initial build environment because that environment did not provide a Codex CLI or subagent runtime. The repository does not claim those forward-tests as observed behavior. Contributors with a fresh Codex runtime are encouraged to run the scenarios and report reproducible before/after behavior.

## Release privacy check

The public release tree is built separately from internal design/planning history. It must contain no private repository history, credentials, customer data, personal machine paths, or organization-specific operational records.
