---
name: token-efficient-codex
description: Use when Codex work is consuming excessive context or tokens, repeatedly rereading files, broad-searching a repository, reprinting large outputs, or approaching context limits during a long task.
---

# Token-Efficient Codex

## Overview

Reduce avoidable context while preserving the evidence needed to be correct. Token efficiency is scope discipline, not permission to weaken correctness, security, or required verification.

## Workflow

1. **Start narrow.** Resolve the current task, repository surface, and smallest likely evidence set before searching broadly.
2. **Reuse established facts.** Do not reread unchanged files or repeat explanations already supported in the active context. Reopen only the lines needed to edit, resolve uncertainty, or verify changed state.
3. **Extract, do not dump.** Keep command output, logs, diffs, and search results outside model context when possible; bring back the smallest excerpt that changes the next decision.
4. **Widen on evidence.** Expand search scope only after a concrete dependency, unresolved hypothesis, or failed discriminating test shows the narrow scope is insufficient.
5. **Test in layers.** During iteration, run the smallest test that can discriminate the current hypothesis. Before claiming completion, run every broader check required by the repository or task.
6. **Checkpoint before saturation.** When continuity is at risk, create a compact checkpoint: goal, current truth, completed work, unresolved items, next exact action, touched files/refs, verification state, and protected constraints.

For detailed patterns and examples, read [references/efficiency-patterns.md](references/efficiency-patterns.md) only when the current task needs them.

## Hard Bounds

- Never omit security review, required tests, source verification, or user-requested evidence to save tokens.
- Never replace an unresolved fact with a guess because lookup is expensive.
- Never treat a short answer as proof of efficient work; reduce irrelevant input and repeated work first.
- If `$context-handoff` is installed and a fresh-session continuation is needed, use it for the checkpoint artifact.

## Quick Reference

| Symptom | Action |
|---|---|
| Huge repo, narrow bug | Inspect direct surface first |
| Same file already known | Reopen only changed/relevant lines |
| Large log | Extract discriminating lines |
| Repeated full test suite | Targeted test while iterating; full required gate at finish |
| Context nearly full | Write checkpoint before continuing |
| Safety-critical task | Spend the tokens needed for proof |

## Common Mistakes

- Broad search “just in case” before identifying the task boundary.
- Re-reading entire files after a small edit.
- Pasting full logs when one error block is decisive.
- Skipping final verification because targeted tests passed.
- Calling an incomplete investigation “token efficient.”
