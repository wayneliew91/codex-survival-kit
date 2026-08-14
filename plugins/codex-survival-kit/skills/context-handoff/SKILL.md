---
name: context-handoff
description: Use when a long Codex task is approaching context or session limits, moving to a fresh chat, handing work to another agent, or needing a durable checkpoint after substantial project work.
---

# Context Handoff

## Overview

Create a continuation artifact that lets a fresh session resume from verified state instead of replaying the conversation. Preserve current truth and execution edges; discard conversational bulk.

## Handoff Contract

Produce these fields in this order:

1. **Goal** — the active outcome, not the project's entire history.
2. **Current Truth** — accepted facts that materially constrain the next step.
3. **Completed** — changes actually made, with file/commit/issue references when available.
4. **Open Issues** — unresolved blockers and hypotheses. Label hypotheses explicitly; never promote them to facts.
5. **Next Exact Action** — one concrete continuation edge: command, file, test, issue, or decision to execute next.
6. **Files / Refs** — only the paths, symbols, branches, commits, PRs, or documents the next session is likely to need.
7. **Verification** — exact checks that passed, failed, or were not run.
8. **Protected Constraints** — behavior, data, scope, or safety boundaries that must not regress.

Use [assets/handoff-template.md](assets/handoff-template.md) as the output skeleton when a file artifact is useful.

## Compression Rules

- Summarize state; do not copy a transcript.
- Keep decisions that still affect the task. Drop superseded discussion unless the supersession itself matters.
- Prefer stable repository identifiers over prose descriptions.
- Record disproven hypotheses only when repeating them would waste work.
- Omit secrets, credentials, tokens, private keys, and unnecessary personal data. Refer to protected configuration abstractly when needed.
- If evidence is incomplete, say `UNVERIFIED` or `UNKNOWN` rather than filling gaps.

## Completion Check

Before handing off, confirm that a fresh agent can answer:

| Question | Must be present |
|---|---|
| What are we doing? | Goal |
| What is definitely true now? | Current Truth |
| What changed? | Completed |
| What is still uncertain? | Open Issues |
| What do I do first? | Next Exact Action |
| What proof exists? | Verification |
| What must I not break? | Protected Constraints |

## Common Mistakes

- Writing a chronological recap instead of state.
- Saying “tests pass” without naming the tests.
- Mixing a suspected cause into Current Truth.
- Listing ten possible next steps instead of one exact continuation edge.
- Embedding secret values because they appeared earlier in context.
