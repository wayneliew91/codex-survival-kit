---
name: repo-first-debugging
description: Use when debugging a repository bug, failing test, CI error, runtime failure, or stale diagnosis where guessing, broad edits, repeated hypotheses, or old conversation context could mislead the investigation.
---

# Repo-First Debugging

## Overview

Debug from the current repository state and reproducible evidence. Familiar symptoms may suggest a hypothesis; they do not justify a fix before inspecting the code that currently owns the behavior.

## Workflow

1. **Resolve operating state.** Identify repository, branch/commit, failing command or user-visible symptom, and the narrow reproduction. If the repository changed since earlier discussion, current repository evidence controls present implementation state.
2. **Inspect the smallest causal surface.** Open the failing test/error location, owning symbol/config, and direct dependencies before searching broadly.
3. **Write one active hypothesis.** State the proposed cause and what observation would distinguish it from alternatives. Track previous results using [references/evidence-loop.md](references/evidence-loop.md) when the diagnosis has multiple turns.
4. **Run a discriminating test.** Choose the smallest command, probe, diff, or reproduction that can falsify the active hypothesis.
5. **Change one causal dimension.** If evidence supports the hypothesis, make the minimum relevant change. Do not patch several suspected causes at once.
6. **Reproduce again.** Confirm the original failure changes in the predicted direction. Then run the affected tests and any broader repository-required verification.
7. **Widen deliberately.** Search adjacent or repository-wide surfaces only when the evidence loop shows the narrow model is insufficient.

## Hypothesis States

| State | Meaning |
|---|---|
| `ACTIVE` | Current explanation with a discriminating test |
| `SUPPORTED` | Evidence moved in the predicted direction |
| `DISPROVEN` | Test contradicted the explanation |
| `BLOCKED` | Required evidence cannot currently be obtained |

Do not recycle a `DISPROVEN` hypothesis without new evidence that changes its premises.

## Scope Control

- Record unrelated defects as `OUT-OF-SCOPE FINDING` unless they block reproduction or directly share the causal path.
- Keep refactors separate from diagnosis unless the refactor is required to expose or fix the proven cause.
- If reproduction is impossible, state what evidence is missing instead of editing speculatively.

## Hard Bounds

- Never edit from an error-message memory alone when repository evidence is available.
- Never treat old chat, cached explanations, or a previous branch as proof of current code ownership.
- Never change multiple independent suspects and call the result root-cause confirmation.
- Never repeat failed fixes without recording what the prior attempt disproved.
- Never call the bug fixed until the original reproduction and required verification pass.

## Common Mistakes

- Searching the whole repository before opening the failing path.
- Converting every plausible explanation into a simultaneous patch.
- Chasing unrelated lint or cleanup during diagnosis.
- Confusing “the error disappeared” with proof of the identified cause.
