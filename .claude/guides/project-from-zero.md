# Project From Zero Guide

## Purpose

Use this guide when starting a software project from a raw idea.

The goal is to turn an idea into a clear foundation for multi-agent development:

```txt
idea -> product vision -> business rules -> conceptual architecture -> technical architecture -> flows -> roadmap -> specs -> tasks -> implementation
```

Do **not** implement functional code while using this guide.

---

## Context Budget Rule

This guide is on demand.

Do not import it into `.claude/CLAUDE.md`.

Read it only when the user is starting or restructuring a project.

---

## Agent and Skill Routing

Use the smallest useful team.

| Work | Usually Use |
| --- | --- |
| Product goal and scope | Orchestrator, optionally product-owner role if project clone defines one |
| Architecture concept | `software-architect` |
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

## Expected Output

Create these project-local files when useful:

```txt
.specs/PROJECT-BRIEF.md
.specs/PRODUCT-VISION.md
.specs/BUSINESS-RULES.md
.specs/CONCEPTUAL-ARCHITECTURE.md
.specs/TECHNICAL-ARCHITECTURE.md
.specs/DOMAIN-MODEL.md
.specs/UI-UX-FLOWS.md
.specs/INTEGRATIONS.md
.specs/SECURITY-MODEL.md
.specs/FEATURE-ROADMAP.md
.specs/STATE.md
```

Use fewer files for very small projects. Use all files for serious products, SaaS apps, ERP systems, internal platforms, or multi-module applications.

---

# Phase 1: Project Brief

## Goal

Define what the project is, who it serves, and why it exists.

## Questions

```txt
What is the system?
Who will use it?
What problem does it solve?
What is the expected MVP?
What is out of scope?
What would make the project successful?
```

## Output

`.specs/PROJECT-BRIEF.md`

```md
# Project Brief

## Project Name

## Short Description

## Problem Statement

## Target Users

| User Type | Description | Main Need |
| --- | --- | --- |

## Main Goals

- [ ]

## Out of Scope

| Item | Reason |
| --- | --- |

## Success Criteria

- [ ]

## Assumptions

| Assumption | Reason | Needs Confirmation? |
| --- | --- | --- |
```

---

# Phase 2: Product Vision

## Goal

Define the product direction before technical decisions.

## Questions

```txt
What should the product become?
What is the first usable version?
What should not be built yet?
What is the business value?
What is the user value?
```

## Output

`.specs/PRODUCT-VISION.md`

```md
# Product Vision

## Vision

## MVP Definition

## Future Vision

## User Value

## Business Value

## Non-Goals

## Product Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
```

---

# Phase 3: Business Rules

## Goal

Capture rules before implementation.

Business rules should not be hidden inside UI, controllers, ORM models, or database triggers unless explicitly designed that way.

## Questions

```txt
What actions are allowed or blocked?
What validations are mandatory?
What statuses exist?
What transitions are allowed?
Who can do what?
What exceptions exist?
```

## Output

`.specs/BUSINESS-RULES.md`

```md
# Business Rules

## Core Rules

| Rule ID | Rule | Applies To | Priority |
| --- | --- | --- | --- |

## Validations

| Validation | When | Error Behavior |
| --- | --- | --- |

## Statuses and Transitions

| Entity | From | To | Allowed? | Rule |
| --- | --- | --- | --- | --- |

## Permissions

| Role | Can Do | Cannot Do |
| --- | --- | --- |

## Open Questions

| Question | Default Assumption | Blocks Development? |
| --- | --- | --- |
```

---

# Phase 4: Conceptual Architecture

## Goal

Describe the system shape without committing to every technical implementation detail.

## Questions

```txt
What are the main modules?
What are the boundaries?
What owns which data?
What external systems exist?
What parts must be independent?
What are the main user and data flows?
```

## Output

`.specs/CONCEPTUAL-ARCHITECTURE.md`

```md
# Conceptual Architecture

## System Overview

## Main Modules

| Module | Responsibility | Owns Data? | Depends On |
| --- | --- | --- | --- |

## Boundaries

| Boundary | Rule |
| --- | --- |

## External Systems

| System | Purpose | Integration Type |
| --- | --- | --- |

## Conceptual Flow

```txt
User -> Interface -> Application -> Domain -> Infrastructure -> External Systems
```

## Architecture Decisions

| Decision | Reason | Trade-off |
| --- | --- | --- |
```

---

# Phase 5: Technical Architecture

## Goal

Define how the system will be implemented.

## Questions

```txt
What stack will be used?
What architecture style fits the project?
How will modules be organized?
How will the database be accessed?
How will authentication and authorization work?
How will integrations be isolated?
How will tests be organized?
How will deployment work?
```

## Output

`.specs/TECHNICAL-ARCHITECTURE.md`

```md
# Technical Architecture

## Stack

| Area | Choice | Reason |
| --- | --- | --- |

## Architecture Style

- [ ] Clean Architecture
- [ ] Hexagonal Architecture
- [ ] DDD
- [ ] CQRS
- [ ] Modular Monolith
- [ ] Other

## Layering

| Layer | Responsibility | Must Not Depend On |
| --- | --- | --- |

## Module Structure

```txt
src/
  modules/
    [module]/
      domain/
      application/
      infrastructure/
      interface/
```

## Dependency Rules

## Database Strategy

## API Strategy

## Authentication and Authorization Strategy

## Integration Strategy

## Testing Strategy

## Deployment Strategy

## Architecture Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
```

---

# Phase 6: Domain Model

## Goal

Model the core business concepts.

## Questions

```txt
What are the main entities?
What are the value objects?
What are the aggregates?
What invariants must always be true?
What domain events may exist?
```

## Output

`.specs/DOMAIN-MODEL.md`

```md
# Domain Model

## Domain Language

| Term | Meaning |
| --- | --- |

## Entities

| Entity | Responsibility | Identity |
| --- | --- | --- |

## Value Objects

| Value Object | Fields | Invariant |
| --- | --- | --- |

## Aggregates

| Aggregate | Root | Owns |
| --- | --- | --- |

## Invariants

| Invariant | Applies To |
| --- | --- |

## Domain Events

| Event | When It Happens | Consumers |
| --- | --- | --- |
```

---

# Phase 7: UI/UX Flows

## Goal

Design user journeys before building screens.

## Questions

```txt
What does the user need to accomplish?
What screens are needed?
What are the happy paths?
What are the loading, empty, error, and success states?
What permissions affect the UI?
```

## Output

`.specs/UI-UX-FLOWS.md`

```md
# UI/UX Flows

## User Roles

| Role | Main Workflows |
| --- | --- |

## Main Journeys

### Journey: [Name]

```txt
Step 1 -> Step 2 -> Step 3 -> Done
```

## Screens

| Screen | Purpose | User Role | Data Needed |
| --- | --- | --- | --- |

## UI States

| Screen | Loading | Empty | Error | Success |
| --- | --- | --- | --- | --- |

## Permission-Based UI Rules

| Role | Visible Actions | Hidden/Disabled Actions |
| --- | --- | --- |

## UX Risks

| Risk | Mitigation |
| --- | --- |
```

---

# Phase 8: Integrations

## Goal

Define external systems without coupling the domain to them.

## Questions

```txt
What external systems will be integrated?
What data comes from each system?
What happens if the external system fails?
What belongs to the internal domain vs external adapter?
```

## Output

`.specs/INTEGRATIONS.md`

```md
# Integrations

## External Systems

| System | Purpose | Direction | Critical? |
| --- | --- | --- | --- |

## Integration Boundaries

| Internal Port | External Adapter | Purpose |
| --- | --- | --- |

## Failure Behavior

| Failure | Expected Behavior |
| --- | --- |

## Data Ownership

| Data | Owner | Internal Copy? |
| --- | --- | --- |

## Security Concerns

| Concern | Mitigation |
| --- | --- |
```

---

# Phase 9: Security Model

## Goal

Define auth, permissions, sensitive data, audit needs, and risks before implementation.

## Questions

```txt
How does login work?
How are permissions checked?
What data is sensitive?
What must never be logged?
What actions require audit?
What threats are most relevant?
```

## Output

`.specs/SECURITY-MODEL.md`

```md
# Security Model

## Authentication

## Authorization

## Roles and Permissions

| Role | Permissions |
| --- | --- |

## Sensitive Data

| Data | Why Sensitive | Protection |
| --- | --- | --- |

## Audit Events

| Event | Reason |
| --- | --- |

## Threats

| Threat | Risk | Mitigation |
| --- | --- | --- |
```

---

# Phase 10: Feature Roadmap

## Goal

Define implementation order.

## Output

`.specs/FEATURE-ROADMAP.md`

```md
# Feature Roadmap

## Foundation

| Feature | Why | Depends On |
| --- | --- | --- |

## MVP Core

| Feature | Why | Depends On |
| --- | --- | --- |

## Operational Modules

| Feature | Why | Depends On |
| --- | --- | --- |

## Integrations

| Feature | Why | Depends On |
| --- | --- | --- |

## Scale/Future

| Feature | Why | Depends On |
| --- | --- | --- |
```

---

# Phase 11: State and Handoff

## Goal

Make the project resumable across sessions, models, and agents.

## Output

`.specs/STATE.md`

```md
# STATE

## Decisions

### AD-001
- **Decision**:
- **Reason**:
- **Trade-off**:
- **Scope**:
- **Status**:

## Handoff

- **Project**:
- **Current phase**:
- **Completed**:
- **In progress**:
- **Next step**:
- **Blockers**:
- **Branch**:
- **Issue**:
- **PR**:
- **Risks**:
```

---

## Learning Notes Pattern

This template is also for learning.

For important decisions, include a short learning note:

```md
## Learning Notes

### Concept

### Why It Matters

### Common Mistake

### How This Project Applies It
```

Use learning notes for architecture, domain modeling, permissions, testing, integrations, UI/UX, deployment, and observability.

Keep learning notes short. Do not turn every file into a tutorial.

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
