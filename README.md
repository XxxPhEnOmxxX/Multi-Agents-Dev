# Multi-Agents Dev Template

A reusable Claude Code multi-agent template for software development work.

This repository provides a generic agent and skill structure that can be cloned into different software projects, then adapted with project-specific rules, skills, and agents only when the real project needs them.

The template is intentionally domain-neutral. It is not tied to ERP systems, telecom systems, SaaS products, marketplaces, mobile apps, or any specific company workflow.

## Core Idea

Use a small stable set of specialist agents and reusable skills to support software delivery without overloading Claude Code context.

```txt
CLAUDE.md -> short orchestration kernel
agents -> recurring specialist roles
skills -> reusable practices and workflows
reference docs -> detailed guidance loaded only when needed
```

The template follows three principles:

1. Keep the always-loaded context small.
2. Use agents for recurring responsibilities.
3. Use skills for repeatable practices that can be invoked on demand.

## Repository Structure

```txt
.claude/
  CLAUDE.md
  agents/
  skills/
  architecture-skill-matrix.md
  agent-skill-governance.md
  context-audit.md
  template-usage.md
```

| Path | Purpose |
| --- | --- |
| `.claude/CLAUDE.md` | Always-loaded orchestration kernel for Claude Code. Keep this short. |
| `.claude/agents/` | Specialist subagents with role prompts, tool permissions, and one preloaded primary skill. |
| `.claude/skills/` | Reusable workflows, architecture practices, quality practices, and operational skills. |
| `.claude/architecture-skill-matrix.md` | Human-readable map of agents, preloaded skills, on-demand skills, and tool tiers. |
| `.claude/agent-skill-governance.md` | Rules for deciding when to add an agent, skill, global rule, or reference document. |
| `.claude/context-audit.md` | Documentation of context economy decisions and always-loaded vs on-demand content. |
| `.claude/template-usage.md` | Detailed guide for cloning, adapting, and maintaining this template. |

## Included Agents

The template keeps the number of agents stable. Add a new agent only when a project introduces a recurring responsibility that cannot be represented well as a skill.

| Agent | Role | Default tier |
| --- | --- | --- |
| `software-architect` | Architecture, boundaries, trade-offs, DDD, Clean Architecture, Hexagonal Architecture, CQRS. | Review/planning |
| `backend-specialist` | APIs, services, validation, persistence, jobs, integrations, backend tests. | Implementation |
| `frontend-specialist` | UI, UX, responsive behavior, accessibility, design systems, frontend review. | Implementation |
| `security-engineer` | Defensive security review, threat modeling, auth, secrets, sensitive data, release risk. | Review/planning |
| `qa-engineer` | Test strategy, acceptance criteria, CI diagnosis, regression analysis, release readiness. | Review/planning |
| `devops-engineer` | Docker, n8n, infrastructure, reverse proxy, deploys, logs, backups, production ops. | Implementation |

## Included Skills

Each agent preloads only one primary operational skill. Architecture and practice skills stay available on demand through the `Skill` tool.

| Skill | Purpose |
| --- | --- |
| `orchestrating-agents` | Task intake, issue strategy, delegation, PR flow, permission gates, continuity notes. |
| `smart-dispatch` | Model/task routing and choosing the smallest useful agent team. |
| `architecting-systems` | System architecture, trade-offs, module boundaries, migrations, runtime views. |
| `building-backend-apis` | Backend APIs, services, validation, persistence, integrations, jobs. |
| `designing-frontend` | Product UI, UX, responsive behavior, interface states, design system consistency. |
| `securing-apps` | Defensive application security review and validation. |
| `qa-github-actions` | QA workflow, CI evidence, GitHub Actions checks, release readiness. |
| `managing-docker-n8n-infra` | Docker, n8n, proxy, deploy, volume, log, and operational workflows. |
| `ddd-modeling` | Domain language, bounded contexts, aggregates, value objects, invariants. |
| `clean-architecture` | Layer ownership and dependency direction. |
| `hexagonal-architecture` | Ports, adapters, gateways, repositories, and anti-corruption layers. |
| `cqrs` | Command/query separation and read/write flow design. |
| `code-quality` | Maintainability, naming, cohesion, error handling, type safety. |
| `security-by-design` | Auth, permissions, secrets, validation, logging, sensitive data boundaries. |
| `testing-strategy` | Tests for domain rules, use cases, handlers, adapters, security, regressions. |

## Tool Permission Model

The template separates review/planning agents from implementation agents.

| Tier | Agents | Default behavior |
| --- | --- | --- |
| Review/planning | `software-architect`, `security-engineer`, `qa-engineer` | Inspect, test, review, and recommend without directly editing files. |
| Implementation | `backend-specialist`, `frontend-specialist`, `devops-engineer` | Apply scoped changes after planning and delegation. |

Review/planning agents do not include `Edit`, `MultiEdit`, or `Write` by default. This keeps the base template safer and encourages implementation to happen through executor agents.

## Recommended Workflow

For every development task:

```txt
Understand -> plan -> create/update issue -> delegate agents -> branch -> PR -> validate -> document outcome
```

Recommended behavior:

1. Start with the main orchestrator.
2. Use `smart-dispatch` to choose the smallest useful agent team.
3. Use `software-architect` first for high-impact architecture decisions.
4. Delegate implementation to backend, frontend, or DevOps agents.
5. Use QA and security agents as reviewers when risk justifies it.
6. Keep evidence in the issue or PR.
7. Do not merge without validation.

## How to Use This Template

1. Clone or copy this repository's `.claude/` directory into a software project.
2. Keep the base agents unless the project clearly needs a new recurring role.
3. Keep `.claude/CLAUDE.md` short and global.
4. Add project-specific skills under `.claude/skills/` only after the project domain is known.
5. Add project-specific reference documents instead of bloating `CLAUDE.md`.
6. Update `.claude/context-audit.md` when changing always-loaded context, agent topology, or skill preload policy.
7. Use `.claude/agent-skill-governance.md` before adding new agents or changing permissions.

See `.claude/template-usage.md` for the full guide.

## What Belongs in the Base Template

Good candidates for the base template:

- universal software engineering roles;
- reusable architecture practices;
- security, testing, and quality practices;
- generic GitHub issue and PR workflow;
- generic context economy rules;
- generic agent and skill governance.

Poor candidates for the base template:

- ERP-specific instructions;
- telecom-specific instructions;
- payment-provider-specific instructions;
- company-specific deployment commands;
- project-specific environment variables;
- product-specific domain language;
- one-off workflow details.

Project-specific knowledge should be added after cloning the template into a real project.

## When to Add a Skill

Add a skill when the behavior is repeatable and can be reused by one or more agents.

Good examples:

```txt
payment-provider-integration
mobile-release-checklist
accessibility-review
legacy-migration-plan
observability-review
```

Avoid adding a skill when the behavior is only a one-time note or a project-specific instruction better stored in documentation.

## When to Add an Agent

Add an agent only when there is a recurring role with distinct responsibility, tool needs, and output expectations.

Good examples in a project clone:

```txt
mobile-specialist
compliance-reviewer
data-engineer
telecom-network-specialist
ai-rag-engineer
```

Avoid adding an agent when a skill or short instruction is enough.

## How to Adapt CLAUDE.md

Use `.claude/CLAUDE.md` only for rules that must apply to every task.

Good additions:

```txt
- Required issue/PR workflow.
- Safety gates.
- Mandatory validation style.
- Project-wide forbidden operations.
- Short routing map.
```

Avoid adding:

```txt
- Long coding standards.
- Full API documentation.
- Domain manuals.
- Large examples.
- Vendor-specific payloads.
- Environment-specific secrets or credentials.
```

Put detailed guidance in skills or reference docs instead.

## Maintenance Checklist

Before merging changes to this template, check:

```txt
- Is this generic enough for many software projects?
- Does it increase always-loaded context?
- Does any agent preload more than one primary skill?
- Did tool permissions become broader than necessary?
- Should this be a skill instead of an agent?
- Should this be a reference doc instead of CLAUDE.md content?
- Are project-specific examples avoided or clearly marked?
- Is the PR validation evidence documented?
```

## Current Status

This template is designed as a reusable foundation. The best next improvements should come from real project usage, not speculative additions.

When a project needs domain-specific behavior, clone the template and extend the clone rather than expanding the base template.