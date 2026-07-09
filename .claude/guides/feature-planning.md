# Feature Planning Guide

## Purpose

Use this guide when planning one feature before implementation.

The goal is to turn a feature idea into clear, testable, reviewable work:

```txt
feature idea -> problem -> rules -> design -> tasks -> tests -> implementation PRs
```

Do **not** implement functional code while using this guide.

---

## Context Budget Rule

This guide is on demand.

Do not import it into `.claude/CLAUDE.md`.

Read it only when planning a feature or reconciling a feature plan.

---

## Relationship With Existing Workflow

Use this guide with:

| Area | Role |
| --- | --- |
| `.claude/prompts/bootstrap.md` | Start or resume the session safely. |
| `orchestrating-agents` | Owns issue, branch, PR, permission gates, and completion report. |
| `smart-dispatch` | Chooses the smallest useful agent team. |
| `tlc-spec-driven` | Produces spec, design, tasks, execution gates, and validation flow. |
| Specialist agents | Implement or review the scoped task. |

---

## Agent Routing

Use the smallest useful team.

| Feature Concern | Usually Use |
| --- | --- |
| Domain/business rules | `software-architect` + `ddd-modeling` |
| Layering/dependency direction | `software-architect` + `clean-architecture` |
| Ports/adapters/integrations | `software-architect` or `backend-specialist` + `hexagonal-architecture` |
| Commands/queries/read models | `backend-specialist` + `cqrs` |
| API/backend implementation plan | `backend-specialist` |
| UI/UX flow | `frontend-specialist` |
| Auth/permissions/sensitive data | `security-engineer` |
| Test matrix and gates | `qa-engineer` + `testing-strategy` |
| Deploy/runtime impact | `devops-engineer` |

Do not involve every agent just because the feature is important.

---

# Phase 1: Feature Intake

## Goal

Understand the feature and its value before design.

## Questions

```txt
What is the feature?
Who needs it?
What problem does it solve?
What behavior is expected?
What is out of scope?
Which module owns it?
Does it require UI, backend, database, integration, security, or infrastructure?
```

## Output

A short intake summary inside the issue or feature `context.md`.

```md
# Feature Context

## Summary

## User / Actor

## Problem

## Expected Outcome

## Module Ownership

## Out of Scope

## Assumptions

## Open Questions
```

---

# Phase 2: Feature Specification

## Goal

Define what the system must do.

## Output

`.specs/features/[feature]/spec.md`

```md
# [Feature Name] Specification

## Problem Statement

## Goals

- [ ]

## Out of Scope

| Item | Reason |
| --- | --- |

## Users / Actors

| Actor | Need |
| --- | --- |

## User Stories

### P1: [Story Name]

**User Story**: As a [role], I want [capability] so that [benefit].

**Acceptance Criteria**:

1. WHEN [event] THEN system SHALL [behavior].
2. WHEN [edge case] THEN system SHALL [behavior].

**Independent Test**:

[How this can be validated.]

## Business Rules

| Rule ID | Rule | Applies To |
| --- | --- | --- |

## Edge Cases

| Case | Expected Behavior |
| --- | --- |

## Requirement Traceability

| Requirement ID | Source | Status |
| --- | --- | --- |

## Assumptions

| Assumption | Reason | Needs Confirmation? |
| --- | --- | --- |

## Open Questions

| Question | Blocks Implementation? | Default |
| --- | --- | --- |
```

---

# Phase 3: Feature Design

## Goal

Define how the feature fits the architecture.

## Output

`.specs/features/[feature]/design.md`

```md
# [Feature Name] Design

## Architecture Overview

## Affected Modules

| Module | Responsibility | Change |
| --- | --- | --- |

## Layering

| Layer | Responsibility |
| --- | --- |
| Domain | |
| Application | |
| Interface | |
| Infrastructure | |

## Ports and Adapters

| Port | Direction | Adapter | Purpose |
| --- | --- | --- | --- |

## Commands and Queries

| Type | Name | Purpose |
| --- | --- | --- |
| Command | | |
| Query | | |

## Data Model

| Entity / Table | Change | Reason |
| --- | --- | --- |

## API / UI Contract

| Surface | Contract |
| --- | --- |

## Security and Permissions

| Action | Required Permission |
| --- | --- |

## Validation Strategy

| Behavior | Test Type |
| --- | --- |

## Risks

| Risk | Mitigation |
| --- | --- |
```

---

# Phase 4: Task Breakdown

## Goal

Break the feature into safe implementation units.

Each task should be:

```txt
small
scoped
testable
reviewable
safe for one PR
clear enough for another session/model
```

## Output

`.specs/features/[feature]/tasks.md`

```md
# [Feature Name] Tasks

## Execution Order

```txt
T1 -> T2 -> T3
```

## Test Coverage Matrix

| Layer | Test Type | Required? | Command |
| --- | --- | --- | --- |
| Domain | Unit | Yes | |
| Application | Unit/Integration | Yes | |
| Interface | Integration/E2E | If applicable | |
| Infrastructure | Integration | If applicable | |

## Gates

| Gate | Command | Required? |
| --- | --- | --- |
| Architecture | | Yes |
| Unit Tests | | Yes |
| Lint | | If available |
| Typecheck | | If available |
| Build | | Before merge |

## Tasks

### T1: [Task Name]

**Goal**:

**Scope**:

**Files likely affected**:

```txt
[path]
```

**Depends on**:

**Requirement IDs**:

**Suggested agent**:

**Done when**:

- [ ]
- [ ]
- [ ] Gate passes

**Tests**:

**Out of scope**:

**Suggested commit**:

```txt
feat(scope): description
```
```

---

# Phase 5: Implementation Issue

## Goal

Create a GitHub issue that acts as the work contract.

## Issue Template

```md
# [Feature] [Task]

## Goal

## Context

## Scope

## Out of Scope

## Spec References

- `.specs/features/[feature]/spec.md`
- `.specs/features/[feature]/design.md`
- `.specs/features/[feature]/tasks.md`

## Acceptance Criteria

- [ ]

## Agent Plan

| Agent | Responsibility |
| --- | --- |

## Validation Plan

## Risks

## Handoff Notes
```

---

# Phase 6: Implementation Session Prompt

Use this prompt when moving from planning to code:

```md
You are working inside the multi-agent project structure.

Implement only:

Feature: [feature-name]
Task: [task-id]

Before editing, read:

1. `.claude/CLAUDE.md`
2. `.claude/prompts/bootstrap.md`
3. `.specs/STATE.md`
4. `.specs/features/[feature-name]/spec.md`
5. `.specs/features/[feature-name]/design.md`
6. `.specs/features/[feature-name]/tasks.md`

Rules:

- Do not implement the whole feature.
- Do not touch unrelated modules.
- Do not refactor opportunistically.
- Do not access secrets.
- Use or create a GitHub issue.
- Create a branch from the default branch.
- Implement only the selected task.
- Add or update tests required by the task.
- Run the required gates.
- Update `tasks.md`.
- Update `STATE.md`.
- Open a PR.

Final response must include:

## Issue
## Branch
## PR
## Files Changed
## What Changed
## What Did Not Change
## Gates Executed
## Handoff
## Next Recommended Task
```

---

## Learning Notes Pattern

Feature planning should teach architecture when it matters.

Use this format:

```md
## Learning Notes

### Concept Used

[Example: use case, port, adapter, aggregate, command, query, repository, DTO.]

### Simple Explanation

### Why We Use It Here

### Common Mistake

### How to Validate
```

Keep learning notes short and tied to the current feature.

---

## Feature Planning Checklist

Before implementation, confirm:

```txt
- The feature has a clear problem statement.
- Goals are measurable.
- Out of scope is explicit.
- Business rules are documented.
- Architecture impact is clear.
- Permissions are defined.
- Data model impact is known.
- UI/API contract is known.
- Tasks are atomic.
- Tests are planned.
- Gates are known.
- Risks are documented.
- STATE.md can guide the next session.
```

If any item is unclear, do not implement yet. Reconcile or ask for clarification.
