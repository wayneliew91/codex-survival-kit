# High-Signal Response Plan Amendment

This amendment closes one dependency discovered during clean-baseline execution.

`tests/test_repository_package.py` currently locks the exact five-skill set through `EXPECTED_SKILLS` and `test_exact_initial_skill_set_exists`. Adding `high-signal-response` requires updating that contract as part of the RED/GREEN cycle.

Required implementation change:

```python
EXPECTED_SKILLS = {
    "token-efficient-codex",
    "tibo-reset",
    "context-handoff",
    "regression-guardian",
    "repo-first-debugging",
    "high-signal-response",
}
```

Rename `test_exact_initial_skill_set_exists` to `test_exact_skill_set_exists` so the test no longer describes the old five-skill baseline.

This change belongs to Task 1/Task 2 verification. The RED state must remain local; the public feature branch should receive only GREEN implementation commits.