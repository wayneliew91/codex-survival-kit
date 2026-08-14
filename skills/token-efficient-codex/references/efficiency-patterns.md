# Efficiency Patterns

Load this reference only when the compact workflow in `SKILL.md` is not enough.

## Evidence funnel

Use a funnel rather than a sweep:

1. user request and current known state;
2. exact file/symbol/error named by the request;
3. direct imports, callers, tests, or config dependencies;
4. adjacent subsystem search;
5. repository-wide search only when earlier layers fail to explain the behavior.

Record why each widening step is necessary. This prevents “search everything” from becoming the default.

## Read-delta rule

If a file was already read and has not changed, retain the established summary. Reopen the minimum range when:

- an edit needs exact syntax;
- a later tool changed the file;
- a claim depends on exact current lines;
- earlier context is ambiguous or incomplete.

Do not reread merely to recreate confidence.

## Output compression

Prefer deterministic filtering before placing tool output into model context. Examples:

```bash
# Find the first relevant error block, not the entire log.
rg -n -C 3 'ERROR|FAIL|panic|exception' build.log | head -n 80

# Inspect only changed paths before opening whole files.
git diff --name-only
```

Do not truncate blindly when omitted lines could change the diagnosis. Expand around the evidence when necessary.

## Layered verification

Iteration and completion have different goals:

- **Iteration:** choose the cheapest test that can falsify the active hypothesis.
- **Completion:** run the repository/task-required checks for the affected surface.

A full suite after every one-line edit can waste compute and context; never running it when required creates false confidence.

## Checkpoint compression

A useful checkpoint is a state vector, not a conversation summary. Keep:

- goal;
- accepted/current facts;
- completed changes;
- disproven hypotheses;
- unresolved blockers;
- next exact action;
- file/commit/issue references;
- verification results;
- constraints that must not regress.

Drop greetings, repeated rationale, obsolete hypotheses, and transcript chronology unless chronology itself is evidence.
