# Contributing

Contributions should make Codex behavior more reliable on a recurring, general problem rather than add project-specific instructions.

## A good skill contribution

- has one clear trigger/problem;
- keeps `SKILL.md` concise and moves heavy detail into focused references;
- uses frontmatter with exactly `name` and `description`;
- starts the description with `Use when...` and describes triggering conditions, not the workflow;
- includes `agents/openai.yaml` with `display_name`, `short_description`, and a `default_prompt` that names `$skill-name`;
- adds or updates a pressure scenario under `tests/pressure/`;
- makes uncertainty and stop conditions explicit;
- contains no credentials, private paths, proprietary prompts, customer data, or organization-specific operational history.

## Development

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_skills.py .
```

For behavior-changing skill edits, add the pressure case first. If you have access to a fresh Codex/subagent runtime, compare behavior without and with the skill and summarize the observed difference in the pull request. Do not fabricate a baseline when live replay was not run.

## Pull requests

Keep one conceptual change per PR. Explain:

1. the failure mode;
2. the pressure scenario that exposes it;
3. what changed in the skill;
4. validation performed;
5. any live behavioral testing that remains outstanding.
