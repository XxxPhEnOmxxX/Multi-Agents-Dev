# Specify

## Goal

Capture **what** must be built as testable, traceable requirements before any implementation starts.

## When to use

Use when the user asks to define, plan, specify, discuss, or start a feature.

## Process

1. Scan nearby code and project docs lightly before asking questions.
2. Ask only questions that affect scope, behavior, safety, data, architecture, or validation.
3. Convert vague language into concrete behavior.
4. Define user stories by priority:
   - P1: MVP / must ship
   - P2: important but not MVP
   - P3: nice to have
5. Write acceptance criteria in `WHEN / THEN / SHALL` form.
6. Record assumptions and out-of-scope items explicitly.
7. Assign requirement IDs that can trace into design, tasks, tests, and validation.

## Implicit requirement sweep

For medium, large, or complex features, check the dimensions that apply:

| Dimension | What to decide |
| --- | --- |
| Input validation | limits, formats, sanitization |
| Failure states | timeout, partial save, rollback, fallback |
| Idempotency | retry behavior, deduplication, duplicate commands |
| Auth boundaries | roles, ownership, rate limits |
| Concurrency | race conditions, ordering, locks, conflicts |
| Data lifecycle | retention, deletion, archival, TTL |
| Observability | logs, metrics, trace points |
| External dependency failure | unavailable APIs, circuit breakers, retries |
| State transitions | allowed states, invalid transitions, guards |

If a dimension does not apply, write `N/A because ...`. Do not invent requirements just to fill a table.

## Output: `.specs/features/[feature]/spec.md`

```markdown
# [Feature] Specification

## Problem Statement

[Problem, user pain, and why this matters now.]

## Goals

- [ ] [Measurable goal]

## Out of Scope

| Item | Reason |
| --- | --- |
| [Excluded item] | [Why excluded] |

## Assumptions & Open Questions

| Assumption / decision | Chosen default | Rationale | Confirmed? |
| --- | --- | --- | --- |
| [ambiguity] | [default] | [reason] | y/n |

## User Stories

### P1: [Story title]

**User Story**: As a [role], I want [capability] so that [benefit].

**Acceptance Criteria**:

1. WHEN [event/action] THEN system SHALL [specific behavior].
2. WHEN [edge case] THEN system SHALL [specific handling].

**Independent Test**: [How to prove this story works alone.]

## Edge Cases

- WHEN [condition] THEN system SHALL [behavior].

## Requirement Traceability

| Requirement ID | Story | Status |
| --- | --- | --- |
| FEAT-01 | P1: [Story] | Pending |

## Success Criteria

- [ ] [Observable success condition]
```

## Closure gate

Before moving forward, every acceptance criterion must have one clear interpretation and a spec-defined expected outcome. If not, resolve it with the user or record the chosen assumption.
