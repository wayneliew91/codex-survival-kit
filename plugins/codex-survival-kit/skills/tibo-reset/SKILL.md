---
name: tibo-reset
description: Use when a user asks whether Codex usage limits were reset, mentions a Tibo reset, shares a reset rumor or staff post, or wants a usage plan based on uncertain reset information.
---

# Tibo Reset

## Overview

Treat “Tibo reset” as a community nickname for a reset claim, not as proof. Verify time-sensitive quota information from current sources, report confidence explicitly, then plan work from what is actually known.

## Workflow

1. **Define the claim.** Capture the reported reset time, Codex surface, user plan, quota/limit type, and source being discussed. Do not silently assume any missing field.
2. **Use current-source tools.** Check current first-party OpenAI product, help, status, or developer information when available. Then check attributable OpenAI staff statements if needed. Treat community posts as leads only.
3. **Match applicability.** A real reset for another plan, quota, region, surface, or time window does not prove the user's quota reset.
4. **Assign one status:**
   - `CONFIRMED` — current authoritative evidence explicitly matches the claim and applicability.
   - `PROBABLE` — credible evidence supports a reset, but one applicability detail remains unresolved.
   - `UNCONFIRMED` — evidence is missing, indirect, stale, or community-only.
   - `CONTRADICTED` — stronger/current evidence conflicts with the claim.
5. **Show the evidence boundary.** State timestamp, affected scope, source class, missing facts, and confidence. If live/current access is unavailable, return `UNCONFIRMED`; do not verify from memory.
6. **Plan usage conservatively.** For `CONFIRMED`, schedule the highest-value work first. For `PROBABLE` or `UNCONFIRMED`, preserve headroom and apply token-efficient work patterns rather than consuming quota on the assumption of a reset.

Read [references/source-confidence.md](references/source-confidence.md) when sources conflict or applicability is unclear.

## Hard Bounds

- This skill cannot trigger, request, force, grant, or guarantee a reset.
- Never convert repeated community reports into confirmation.
- Never present an attributable staff statement as broader than its actual wording or scope.
- Never fabricate remaining quota, reset time, or plan eligibility.
- Do not encourage wasteful usage merely because a reset appears likely.

## Quick Reference

| Evidence | Default treatment |
|---|---|
| Matching current first-party statement | Candidate for `CONFIRMED` |
| Attributable staff statement, exact scope | Strong signal; verify applicability |
| Staff statement, vague scope | Usually `PROBABLE` at most |
| Community reports only | `UNCONFIRMED` |
| Newer authoritative contradiction | `CONTRADICTED` |
| No current-source access | `UNCONFIRMED` |

## Common Mistakes

- Treating “Tibo said reset” as universal eligibility.
- Ignoring the difference between plan, surface, and quota type.
- Reusing yesterday's confirmation for today's status.
- Planning a large workload around an unconfirmed rumor.
