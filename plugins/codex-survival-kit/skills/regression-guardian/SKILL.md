---
name: regression-guardian
description: Use when a fix, refactor, migration, rename, or release may affect previously accepted behavior, frozen capabilities, compatibility guarantees, or a bug that must not return.
---

# Regression Guardian

## Overview

Protect accepted behavior from accidental reversion. Build a small evidence-backed regression contract for the surface being changed, then prove the candidate still satisfies it.

## Workflow

1. **Find protected behavior.** Before editing, inspect the closest reliable evidence: current tests, accepted specs, release notes, issue/PR decisions, compatibility contracts, or explicit user requirements.
2. **Write the regression contract.** Record only behavior materially exposed to the change: inputs, expected outputs/effects, identity/naming constraints, data invariants, and required historical compatibility. Use [references/regression-contract.md](references/regression-contract.md) when the surface is complex.
3. **Resolve conflicts.** If evidence disagrees, determine whether newer evidence explicitly supersedes the older rule. A later timestamp alone is not supersession.
4. **Edit within the contract.** Keep unrelated protected behavior unchanged. If the requested change intentionally replaces a protected rule, mark that boundary as `SUPERSESSION` instead of hiding it as a refactor.
5. **Prove the touched behavior.** Run or add targeted regression tests that would fail if the protected behavior reverted.
6. **Run completion gates.** Execute the broader checks required by the repository/task. A generic green suite does not prove a protected behavior if no test covers it.
7. **Report evidence.** Use `VERIFIED` only when direct checks support the contract. Otherwise state `PARTIALLY_VERIFIED`, `UNVERIFIED`, or the concrete failure.

## Quick Reference

| Situation | Required response |
|---|---|
| Fix touches accepted edge case | Add/identify targeted regression proof |
| Old test conflicts with accepted newer rule | Establish supersession before changing test |
| Rename has user-visible/history impact | Put identity/naming in contract |
| Intentional rule replacement | Record `SUPERSESSION` |
| Full suite green, protected case absent | Not enough for `VERIFIED` |

## Hard Bounds

- Never preserve stale behavior solely because an old test asserts it.
- Never delete a failing regression test merely to make a candidate green.
- Never infer protected behavior from memory when repository evidence is available.
- Never call intentional supersession a regression fix; make the change in authority explicit.
- Never claim `VERIFIED` from compilation, smoke tests, or unrelated passing tests alone.

## Common Mistakes

- Treating regression as “tests failed” instead of “accepted behavior changed unintentionally.”
- Building a contract so broad that every edit becomes blocked.
- Ignoring labels, IDs, ordering, or data semantics because the main calculation still works.
- Running only the new happy-path test.
