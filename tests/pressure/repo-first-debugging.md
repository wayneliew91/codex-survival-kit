# Pressure Scenarios — repo-first-debugging

Live baseline status: `NOT_LIVE_OBSERVED` in this build environment because no Codex CLI/subagent runtime is available. These are forward-test scenarios.

## Scenario 1 — Guess before inspection
A familiar error message appears. Expected: resolve current repo/branch and inspect the failing path before applying a remembered fix.

## Scenario 2 — Multiple simultaneous edits
Three causes seem plausible. Expected: choose a discriminating test and change one causal dimension at a time rather than patching all three.

## Scenario 3 — Unrelated failure discovered
While debugging the target, another lint problem appears elsewhere. Expected: record it as an out-of-scope finding and keep the active diagnosis bounded unless it blocks reproduction.

## Scenario 4 — Repeated failed hypothesis
A hypothesis has already been disproven twice. Expected: record the result and stop retrying variants without new evidence.

## Scenario 5 — Stale conversation context
Old chat says file A owns the behavior, but the repository has since changed. Expected: current repository evidence wins for present implementation state.
