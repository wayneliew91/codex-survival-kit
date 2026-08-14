# Reset Source Confidence

Use this reference only when the compact status rules in `SKILL.md` are insufficient.

## Source classes

Rank evidence by its ability to establish the specific current claim, not by popularity.

1. **First-party current product evidence** — OpenAI account/product UI information directly describing the user's applicable quota or reset state, when available.
2. **First-party current published information** — OpenAI status, help, product, or developer documentation that explicitly names the relevant limit/reset and scope.
3. **Attributable OpenAI staff statement** — useful when clear and current, but do not broaden beyond what the statement actually covers.
4. **Reputable reporting with primary-source attribution** — corroboration, not a substitute for current first-party product state.
5. **Community posts, screenshots, reposts, trackers, and hearsay** — discovery leads only unless independently confirmed.

A lower-ranked source can reveal a newer claim worth checking, but repetition does not increase authority by itself.

## Applicability matrix

Before `CONFIRMED`, match every material dimension that the available evidence exposes:

| Dimension | Question |
|---|---|
| Time | Is this reset current for the requested date/time? |
| Product | Is it Codex rather than another OpenAI product? |
| Surface | App, CLI, web, API, or another surface? |
| Plan | Does the statement cover the user's plan/tier? |
| Limit | Which weekly/daily/other quota was affected? |
| Geography/account | Is eligibility account- or region-specific? |

If a material dimension is unknown, state it instead of filling the gap by inference.

## Status examples

- Official current notice: “limit X reset for plan Y at time Z,” and user matches Y → `CONFIRMED`.
- Staff says “we reset some affected users,” but user eligibility is unknown → `PROBABLE` or `UNCONFIRMED`, depending on supporting evidence.
- Ten community posts repeat the same unsourced claim → `UNCONFIRMED`.
- Old reset announcement conflicts with a newer first-party schedule → old current-status claim is `CONTRADICTED`.

## Workload planning after verification

Use confirmed capacity for work with high interruption cost: repository-wide migrations, release closure, broad regression suites, or long investigation chains. When capacity is uncertain, prefer bounded tasks, compact checkpoints, targeted tests during iteration, and avoid speculative bulk scanning.
