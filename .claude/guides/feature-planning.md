# Feature Planning Guide

## Purpose

Use this guide when planning one feature before implementation.

The guide is intentionally short. Detailed fill-in files live in `.claude/templates/feature/` and should be opened only when needed.

Do **not** implement functional code while using this guide.

---

## Context Budget Rule

This guide is on demand.

Do not import it into `.claude/CLAUDE.md`.

Use only the target feature files and the templates required for the current planning phase.

---

## Flow

```txt
feature idea
-> intake/context
-> spec
-> design
-> tasks
-> implementation issue
-> implementation session prompt
-> PR
-> validation
-> handoff
```

---

## Relationship With Existing Workflow

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

## Feature Templates

Use these templates only as needed:

| Template | Output File | Use When |
| --- | --- | --- |
| `.claude/templates/feature/context.md` | `.specs/features/[feature]/context.md` | Capture ambiguity, legacy behavior, external context, or intake notes. |
| `.claude/templates/feature/spec.md` | `.specs/features/[feature]/spec.md` | Define behavior, goals, business rules, acceptance criteria, and traceability. |
| `.claude/templates/feature/design.md` | `.specs/features/[feature]/design.md` | Define architecture, layering, ports/adapters, data model, security, and risks. |
| `.claude/templates/feature/tasks.md` | `.specs/features/[feature]/tasks.md` | Break implementation into small task/PR units. |
| `.claude/templates/feature/validation.md` | `.specs/features/[feature]/validation.md` | Record test evidence, independent verification, UAT, and risks. |

---

## Implementation Issue Shape

Create or update a GitHub issue before implementation.

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

## Agent Plan

## Validation Plan

## Risks

## Handoff Notes
```

---

## Implementation Session Prompt Shape

Use this when moving from planning to code:

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
```

---

## Learning Notes

Feature planning should teach architecture when it matters.

Use this format:

```md
## Learning Notes

### Concept Used

### Simple Explanation

### Why We Use It Here

### Common Mistake

### How to Validate
```

Keep learning notes short and tied to the current feature.

---

## Checklist Before Implementation

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
