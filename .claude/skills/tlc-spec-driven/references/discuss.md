# Discuss Gray Areas

## Goal

Capture user decisions for ambiguous behavior before design or implementation guesses incorrectly.

This phase is triggered inside Specify. It clarifies **how the feature should behave**, not whether unrelated features should be added.

## Trigger

Use when the feature has ambiguous user-facing, API, CLI, data, state, auth, error, persistence, or external-integration behavior.

Skip only for genuinely trivial changes with no meaningful behavior choices.

## Process

1. Read the feature spec.
2. Identify 3-4 concrete gray areas specific to this feature.
3. Present the feature boundary and the gray areas.
4. Ask focused questions with concrete options.
5. Capture decisions in `context.md`.
6. Any declined or undiscussed gray area becomes an explicit assumption in the spec.

## Guardrail

Discussion clarifies implementation decisions inside the approved feature boundary. It must not add new capabilities.

If scope creep appears, record it under Deferred Ideas and return to the current feature.

## Output: `.specs/features/[feature]/context.md`

```markdown
# [Feature] Context

**Gathered:** YYYY-MM-DD
**Spec:** `.specs/features/[feature]/spec.md`
**Status:** Ready for design

## Feature Boundary

[Clear scope anchor.]

## Implementation Decisions

### [Area]

- [Decision]

### Agent's Discretion

- [Areas where the user allowed the agent to choose.]

### Declined / Undiscussed Gray Areas -> Assumptions

- [Gray area]: [chosen default] because [reason].

## Specific References

- [Any product, behavior, UX, API, or workflow reference the user mentioned.]

## Deferred Ideas

- [Ideas captured but out of scope.]
```
