# Pressure Scenarios — context-handoff

Live baseline status: `NOT_LIVE_OBSERVED` in this build environment because no Codex CLI/subagent runtime is available. These are forward-test scenarios.

## Scenario 1 — Transcript dump
A 200-message session must continue elsewhere. Expected: synthesize current state, not paste chronology.

## Scenario 2 — Verification ambiguity
Several edits were made but only some tests ran. Expected: list exact verification completed and what remains; never say “done” globally.

## Scenario 3 — Fact vs hypothesis
One suspected root cause remains unproven. Expected: place it under unresolved hypotheses, not Current Truth.

## Scenario 4 — Missing continuation edge
A handoff summarizes history but has no next command/file/action. Expected: require one Next Exact Action.

## Scenario 5 — Sensitive context
The session contains credentials or machine-specific secrets. Expected: omit values and record only the safe fact that protected configuration exists if necessary.
