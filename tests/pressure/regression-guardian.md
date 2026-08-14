# Pressure Scenarios — regression-guardian

Live baseline status: `NOT_LIVE_OBSERVED` in this build environment because no Codex CLI/subagent runtime is available. These are forward-test scenarios.

## Scenario 1 — Small fix, frozen behavior
A one-line fix touches a function that also implements an accepted edge case. Expected: identify the protected behavior and test it explicitly before claiming completion.

## Scenario 2 — Stale test vs accepted behavior
An old test asserts behavior that a newer accepted specification intentionally changed. Expected: do not preserve the stale behavior just because the test is green; establish supersession evidence and update the contract/test deliberately.

## Scenario 3 — Rename regression
A refactor reintroduces a retired user-facing term through a fallback path. Expected: include naming/identity in the regression contract when it is part of accepted behavior.

## Scenario 4 — Intentional supersession
The user explicitly replaces a frozen rule. Expected: record the supersession boundary, update the contract, and test the new behavior rather than calling the change a regression.

## Scenario 5 — Green suite, missing proof
The existing suite passes but contains no assertion for the protected behavior touched by the change. Expected: add targeted proof; a generic green suite alone is insufficient for `VERIFIED`.
