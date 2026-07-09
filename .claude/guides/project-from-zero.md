# Project From Zero Guide

## Purpose

Use this guide when starting a software project from a raw idea.

The guide is intentionally short. Detailed fill-in files live in `.claude/templates/project/` and should be opened only when needed.

Do **not** implement functional code while using this guide.

---

## Context Budget Rule

This guide is on demand.

Do not import it into `.claude/CLAUDE.md`.

Use the smallest useful set of templates. Do not load every project template for small projects.

---

## Flow

```txt
idea
-> project brief
-> product vision
-> business rules
-> conceptual architecture
-> technical architecture
-> domain model
-> UI/UX flows
-> integrations
-> security model
-> feature roadmap
-> STATE.md handoff
-> feature specs
-> implementation
```

---

## Agent and Skill Routing

Use the smallest useful team.

| Work | Usually Use |
| --- | --- |
| Product goal and scope | Orchestrator; optional product-owner role only in project clones that define it |
| Conceptual architecture | `software-architect` |
| Domain model and business rules | `software-architect` + `ddd-modeling` |
| Technical architecture | `software-architect` + relevant practice skills |
| Backend/API planning | `backend-specialist` |
| UI/UX flows | `frontend-specialist` |
| Security model | `security-engineer` |
| Testing strategy | `qa-engineer` |
| Runtime/deploy model | `devops-engineer` |
| Spec/task breakdown | `tlc-spec-driven` |

Do not summon all agents by default.

---

## Project Templates

Use these templates only as needed:

| Template | Output File | Use When |
| --- | --- | --- |
| `.claude/templates/project/PROJECT-BRIEF.md` | `.specs/PROJECT-BRIEF.md` | Define what the project is and who it serves. |
| `.claude/templates/project/PRODUCT-VISION.md` | `.specs/PRODUCT-VISION.md` | Define MVP, future vision, and product value. |
| `.claude/templates/project/BUSINESS-RULES.md` | `.specs/BUSINESS-RULES.md` | Capture rules, statuses, validations, and permissions. |
| `.claude/templates/project/CONCEPTUAL-ARCHITECTURE.md` | `.specs/CONCEPTUAL-ARCHITECTURE.md` | Define modules, boundaries, ownership, and external systems. |
| `.claude/templates/project/TECHNICAL-ARCHITECTURE.md` | `.specs/TECHNICAL-ARCHITECTURE.md` | Define stack, layers, dependency rules, testing, and deployment strategy. |
| `.claude/templates/project/DOMAIN-MODEL.md` | `.specs/DOMAIN-MODEL.md` | Model domain language, entities, value objects, aggregates, and invariants. |
| `.claude/templates/project/UI-UX-FLOWS.md` | `.specs/UI-UX-FLOWS.md` | Plan user journeys, screens, states, and permission-based UI behavior. |
| `.claude/templates/project/INTEGRATIONS.md` | `.specs/INTEGRATIONS.md` | Define external systems, ports/adapters, failure behavior, and data ownership. |
| `.claude/templates/project/SECURITY-MODEL.md` | `.specs/SECURITY-MODEL.md` | Define auth, authorization, sensitive data, audit, and threats. |
| `.claude/templates/project/FEATURE-ROADMAP.md` | `.specs/FEATURE-ROADMAP.md` | Prioritize foundation, MVP core, integrations, and future work. |
| `.claude/templates/project/STATE.md` | `.specs/STATE.md` | Make the project resumable across sessions and models. |

---

## Learning Notes

This template is also for learning software development.

For important decisions, add short learning notes:

```md
## Learning Notes

### Concept

### Why It Matters

### Common Mistake

### How This Project Applies It
```

Keep learning notes short. Teach concepts only when they affect a real project decision.

---

## Completion Checklist

Before moving to implementation, confirm:

```txt
- Project problem is clear.
- MVP is clear.
- Business rules are documented.
- Conceptual architecture is documented.
- Technical architecture is documented.
- Main flows are documented.
- Security model exists.
- Roadmap exists.
- STATE.md can guide the next session.
- No functional code was implemented during project inception.
```
