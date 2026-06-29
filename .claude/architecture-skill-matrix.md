# Architecture Skill Matrix

Issue: #3

## Purpose

This repository keeps the number of agents stable and distributes architecture practices through skills.

Skills represent engineering practices, not one-off tasks. Agents keep their specialist roles and invoke extra skills only when the task requires them.

## Token Economy Rule

Each agent preloads only its primary operational skill through the `skills:` frontmatter.

Architecture and practice skills stay available on demand through the `Skill` tool instead of being preloaded into every subagent context.

This keeps subagent context smaller while preserving access to DDD, Clean Architecture, Hexagonal Architecture, CQRS, security, testing, and capability guidance when needed.

## Practice Skills

| Skill | Practice | Use When |
| --- | --- | --- |
| `ddd-modeling` | Domain-Driven Design | Discovering domain language, bounded contexts, aggregates, value objects, and invariants. |
| `clean-architecture` | Clean Architecture | Placing behavior in the correct layer and protecting dependency direction. |
| `hexagonal-architecture` | Hexagonal Architecture | Designing ports, adapters, gateways, repositories, and anti-corruption layers. |
| `cqrs` | CQRS | Separating commands from queries and designing read/write flows. |
| `code-quality` | Engineering quality | Improving maintainability, naming, cohesion, error handling, and type safety. |
| `security-by-design` | Secure engineering | Reviewing auth, authorization, secrets, logs, validation, and sensitive data boundaries. |
| `testing-strategy` | Testing practice | Designing tests for domain rules, use cases, handlers, adapters, and regressions. |
| `capability-driven-integration` | Integration architecture | Modeling ERP/API support, optional features, fallback behavior, and module availability. |

## Preloaded Skill by Agent

| Agent | Preloaded Skill |
| --- | --- |
| `software-architect` | `architecting-systems` |
| `backend-specialist` | `building-backend-apis` |
| `frontend-specialist` | `designing-frontend` |
| `security-engineer` | `securing-apps` |
| `qa-engineer` | `qa-github-actions` |
| `devops-engineer` | `managing-docker-n8n-infra` |

## On-Demand Practice Skills by Agent

| Agent | On-Demand Skills |
| --- | --- |
| `software-architect` | `ddd-modeling`, `clean-architecture`, `hexagonal-architecture`, `cqrs`, `capability-driven-integration`, `security-by-design`, `testing-strategy` |
| `backend-specialist` | `clean-architecture`, `hexagonal-architecture`, `cqrs`, `code-quality`, `testing-strategy`, `capability-driven-integration`, `security-by-design` |
| `frontend-specialist` | `code-quality`, `capability-driven-integration`, `security-by-design`, `testing-strategy` |
| `security-engineer` | `security-by-design`, `clean-architecture`, `hexagonal-architecture`, `code-quality`, `testing-strategy` |
| `qa-engineer` | `testing-strategy`, `cqrs`, `ddd-modeling`, `capability-driven-integration`, `security-by-design` |
| `devops-engineer` | `security-by-design`, `code-quality`, `testing-strategy`, `hexagonal-architecture` |

## Operating Rule

Use the smallest useful set of agents. Do not summon every agent or preload every practice skill just because a task mentions architecture.

Architecture-heavy work usually starts with `software-architect`. Implementation usually moves to `backend-specialist`, `frontend-specialist`, or `devops-engineer`. Validation and risk review use `qa-engineer` and `security-engineer` when the risk justifies it.
