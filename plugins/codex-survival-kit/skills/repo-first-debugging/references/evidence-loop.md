# Debugging Evidence Loop

Use this ledger when a diagnosis spans more than one hypothesis or tool cycle.

```text
Symptom / reproduction:
Repository state:

Hypothesis:
State: ACTIVE | SUPPORTED | DISPROVEN | BLOCKED
Evidence for:
Evidence against:
Discriminating test:
Observed result:
Decision:
Next hypothesis or action:
```

## Discriminating tests

A useful test changes the probability of competing explanations. Prefer:

- one targeted test case over an unrelated full suite;
- one config/value probe over a broad rewrite;
- a minimal reproduction over a production-scale run;
- a diff/blame/dependency check when ownership is uncertain;
- a known-good comparison when environment or version drift is suspected.

After the cause is supported and the fix is implemented, broader completion checks still apply.

## Widening ladder

1. exact failure/test;
2. owning symbol/config;
3. direct callers/dependencies;
4. subsystem search;
5. repository-wide search;
6. external dependency/runtime evidence.

Move down the ladder only when the previous level cannot explain the observation.

## Loop breaker

Before retrying a previous idea, ask: **what new observation changes the premises of the disproven hypothesis?** If the answer is “none,” do not retry it. Choose a new hypothesis or obtain missing evidence.
