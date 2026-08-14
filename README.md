# Codex Survival Kit

Practical Codex skills for **token efficiency, context recovery, regression safety, repo-first debugging, and usage-reset verification**.

This repository is for maintainers who want Codex to stay useful during long, messy, quota-constrained software work without replacing verification with shortcuts.

## Skills

| Skill | Use it when... |
|---|---|
| [`token-efficient-codex`](skills/token-efficient-codex/SKILL.md) | context or token use is bloating from broad searches, repeated reads, huge outputs, or long sessions |
| [`tibo-reset`](skills/tibo-reset/SKILL.md) | a Codex usage-reset claim needs current verification before you plan work around it |
| [`context-handoff`](skills/context-handoff/SKILL.md) | a long task needs a compact continuation checkpoint for a fresh session or another agent |
| [`regression-guardian`](skills/regression-guardian/SKILL.md) | a fix/refactor/release could silently revert behavior that was already accepted |
| [`repo-first-debugging`](skills/repo-first-debugging/SKILL.md) | debugging is drifting into guesses, broad edits, stale context, or repeated hypotheses |

## Why these exist

Agentic coding gets expensive and unreliable when the working set grows faster than the evidence. The kit applies three recurring principles:

- **Correctness before savings.** Save context by removing irrelevant work, not by skipping proof.
- **Evidence before guesses.** Current repository/product evidence outranks remembered explanations.
- **State before transcript.** Carry forward the smallest verified state that lets the next action begin.

## Install

Codex's `$skill-installer` can download skills from other repositories for local setup and experimentation. Ask it to install the desired path from this repository, for example `skills/token-efficient-codex`.

For manual user-level installation, copy each desired skill directory under `$HOME/.agents/skills/`, for example:

```text
$HOME/.agents/skills/token-efficient-codex/
```

For repository-scoped installation, place the desired skill directories under `.agents/skills/` in that repository. Keep each skill as its own direct child directory.

For broad reusable distribution, OpenAI currently recommends packaging skills as a plugin. This repository remains the transparent source and local/repository-install collection; a plugin can be added later as a distribution layer without changing the individual skill sources.

## Examples

### Spend less context without cutting proof

```text
$token-efficient-codex Fix this parser regression. Start from the failing test and do not reread unrelated packages.
```

### Check a reported usage reset

```text
$tibo-reset Verify whether this reported Codex reset applies to my plan today, and separate confirmed facts from rumors.
```

`Tibo Reset` is a community-facing name for a verification workflow. The skill **cannot trigger, request, force, grant, or guarantee a Codex usage reset**.

### Move a long task into a fresh session

```text
$context-handoff Create a continuation checkpoint for this branch with exact verification state and the next action.
```

### Protect a previously fixed behavior

```text
$regression-guardian Refactor this module without reintroducing the edge case fixed in the linked issue.
```

### Stop debugging by guesswork

```text
$repo-first-debugging Diagnose this CI failure from the current branch and use one discriminating test at a time.
```

## Design

Each skill follows Codex's progressive-disclosure model:

```text
skills/<skill-name>/
├── SKILL.md
├── agents/openai.yaml
└── references/ or assets/   # only when needed
```

The trigger lives in the `SKILL.md` frontmatter. Longer material stays in focused references so it is not injected unless the active task needs it.

## Validate

No third-party Python packages are required.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_skills.py .
```

The validator checks skill structure, frontmatter, naming, relative links, required UI metadata, forbidden per-skill clutter, and obvious sensitive-data patterns.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). New skills should solve one recurring problem, include a realistic pressure scenario, keep the default context small, and make uncertainty explicit.

## Status

Initial release target: `0.1.0`.

The pressure scenarios in this repository are forward-test definitions. The initial build environment did not include a Codex CLI/subagent runtime, so live behavioral replay is not claimed where it was not run.

## License

MIT. See [`LICENSE`](LICENSE).

## Disclaimer

Community-maintained project. Not affiliated with or endorsed by OpenAI. Codex, OpenAI, and related product names belong to their respective owners.
