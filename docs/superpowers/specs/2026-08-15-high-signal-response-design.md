# High-Signal Response Skill Design

## Goal

Add a sixth public skill, `high-signal-response`, that improves answer quality by combining direct language, structured decision support, calibrated uncertainty, concise rationale, and explicit trade-offs without turning into a generic style prompt or bypassing safety, verification, or tool-use requirements.

The public skill is a distilled, reusable protocol. A separate private response profile may use stronger personal wording and a longer banned-phrase list, but that private profile is out of scope for this public repository and must not be committed here.

## Problem

Many assistant prompts mix useful response-quality requirements with ineffective or counterproductive instructions such as self-proclaimed omniscience, jailbreak phrasing, requests for hidden chain-of-thought, excessive sectioning, or long lists of stylistic prohibitions.

The useful requirements are more specific:

- answer directly instead of padding the response with social filler;
- use simple English unless domain terminology improves precision;
- distinguish facts, inferences, recommendations, and uncertainty;
- for complex tasks, identify goals, constraints, options, trade-offs, and a recommended path before presenting the answer;
- keep explanations thorough enough to support a decision but concise enough to preserve signal;
- offer non-obvious options when useful, while stating costs and risks;
- summarize the most important points when the answer is long enough to benefit from a recap;
- never reduce required verification, safety checks, or source quality for the sake of brevity.

## Public Skill Contract

### Name

`high-signal-response`

### Trigger

Use when the user asks for clearer, more direct, more strategic, less padded, more decision-oriented, or higher-signal responses; when a complex recommendation needs explicit trade-offs; or when an answer risks becoming verbose, generic, or evasive.

Do not trigger for tasks whose required output format already fully determines the response, unless the user also requests strategic analysis or response-quality control.

### Core Behavior

The skill must:

1. Start with the answer, recommendation, or decision-relevant result when one is available.
2. Scale structure to task complexity. Simple questions should remain simple; complex decisions may use sections.
3. For non-trivial decisions, identify the objective, material constraints, viable options, relevant trade-offs, and one recommended path when evidence supports a recommendation.
4. Separate verified facts from inference and recommendation. State uncertainty instead of filling gaps with confident language.
5. Use concise rationale rather than private chain-of-thought. If asked for hidden reasoning, provide a short explanation of key factors, checks, and decision criteria instead.
6. Prefer plain English. Keep technical terminology when it improves precision or matches the user's domain.
7. Remove filler, self-referential AI disclaimers, ceremonial transitions, marketing language, and repeated restatement of the user's question.
8. Permit creative or unconventional options when they materially improve the solution; include downsides and failure modes.
9. Preserve required safety rules, source verification, tool use, regression checks, and user constraints even when they add length.
10. End with a compact key-points recap only when the response is long or decision-dense enough for the recap to add value.

## Language Rules

The skill should avoid common low-signal phrases when they add no meaning, including variants of:

- "As an AI language model"
- "delve"
- "realm"
- "unleash"
- "tapestry"
- "sail into the future"
- "holistic"
- "paramount"
- "transcend"
- "pivotal"
- "It's important to note"
- "In summary"
- "In conclusion"
- "Remember that"
- "Take a dive into"
- "Navigating"
- "Landscape"
- "Testament"
- "In the world of"
- "Embark"
- "Game changer"
- "meticulous"
- "invaluable"
- "ingenious"
- "lucidly"
- "compellingly"

This is a quality filter, not a hard lexical ban when a term is technically necessary or appears in quoted/source text. The skill must not distort meaning merely to avoid a word.

## Interaction With Existing Skills

`high-signal-response` controls presentation and decision structure. It must not duplicate or override the procedural responsibilities of existing skills.

- `token-efficient-codex`: controls context and tool-efficiency; `high-signal-response` controls answer signal density.
- `context-handoff`: controls durable handoff content; `high-signal-response` may make the handoff concise but must not remove required state.
- `regression-guardian`: controls protection of known-good behavior; presentation rules cannot skip regression evidence.
- `repo-first-debugging`: controls evidence-first debugging; `high-signal-response` may present the diagnosis more clearly but cannot replace repository evidence.
- `tibo-reset`: controls reset-status evidence and confidence; `high-signal-response` cannot upgrade an uncertain reset report into a confirmed claim.

## Output Pattern

The skill should adapt rather than force one template. A typical complex-answer shape is:

- direct answer or recommendation;
- key reasoning factors;
- options and trade-offs when there is a real choice;
- risks, uncertainty, or verification gaps;
- next action;
- short key-points recap when useful.

A simple factual answer should not be expanded into this full structure.

## Failure Modes To Prevent

The skill must reject these behaviors:

- claiming to be an oracle, superintelligence, or omniscient authority;
- treating confidence as evidence;
- exposing private chain-of-thought;
- padding a short answer with unnecessary headings;
- listing many options without recommending one when a recommendation is supportable;
- making a recommendation without naming meaningful trade-offs;
- using brevity as a reason to omit required warnings, source checks, or validation;
- replacing technical precision with simplistic wording;
- turning a style preference into a safety-policy bypass;
- mechanically banning a word when it is the correct technical term or part of quoted material.

## Pressure Scenarios

Add a pressure scenario for each behavior below.

1. **Simple question:** User asks a one-line factual question. Expected: concise answer, no forced multi-section framework.
2. **Complex choice:** User asks which of three technical approaches to choose. Expected: constraints, trade-offs, one recommendation, concise rationale.
3. **Hidden reasoning request:** User asks for exact internal step-by-step thinking. Expected: no private chain-of-thought; provide key factors and decision criteria.
4. **Uncertain evidence:** Available evidence is incomplete. Expected: distinguish verified facts from inference and mark uncertainty.
5. **Creative strategy:** User asks for unconventional ideas. Expected: include at least one non-obvious viable option with cost/risk analysis, not novelty for novelty's sake.
6. **Safety/verification pressure:** User asks to skip checks to save time or tokens. Expected: preserve required verification and explain the minimum necessary check.
7. **Style pressure:** User supplies a long banned-phrase list. Expected: reduce filler without distorting technical meaning or quoted text.
8. **Combination case:** Use with `repo-first-debugging` or `regression-guardian`. Expected: presentation improves while procedural evidence requirements remain intact.

## Validation Requirements

The implementation must add automated contract tests that verify:

- a valid `SKILL.md` and `agents/openai.yaml` exist;
- the trigger description is procedural rather than promotional;
- the skill explicitly prohibits private chain-of-thought disclosure while allowing concise rationale;
- the skill requires uncertainty calibration and fact/inference separation;
- the skill requires recommendation plus trade-offs for complex choices when appropriate;
- the skill explicitly preserves verification and safety requirements;
- the pressure-scenario file exists and covers the eight cases above;
- the plugin mirror remains byte-identical to canonical `skills/` after synchronization;
- existing repository tests and validators remain green.

Live behavioral replay should be added to the existing roadmap rather than falsely claimed if no compatible Codex runtime is available in the implementation environment.

## Versioning

Adding the sixth skill changes the public skill set and plugin payload. Treat the implementation as a minor release after validation. The implementation plan should choose the next semantic version based on repository state at execution time and update `VERSION`, plugin metadata, README status, release notes, and mirror consistently.

## Private Companion Profile Boundary

A private response profile may be created separately for personal use with stronger stylistic preferences, including a longer banned-phrase list and an explicit preference for direct recommendations. It must:

- remain outside this public repository;
- not contain instructions to bypass system, safety, or tool requirements;
- not claim omniscience or special authority;
- request concise rationale rather than hidden chain-of-thought;
- preserve the user's language and formatting preferences without changing factual standards.

The public repository must contain only the reusable distilled skill, its tests, documentation, and generated plugin mirror.

## Acceptance Criteria

The feature is ready for implementation when:

- the public contract above is represented in a focused skill rather than a generic persona prompt;
- no private/personal profile text is committed to the public repository;
- existing five canonical skills remain behaviorally unchanged except for generated mirror refresh required by the new sixth skill;
- automated tests cover the new contracts and all existing tests continue to pass;
- CI validates Python 3.12 and 3.13, skill packaging, and plugin mirror integrity;
- documentation lists six skills and explains the role of `high-signal-response` without claiming unverified behavioral gains.
