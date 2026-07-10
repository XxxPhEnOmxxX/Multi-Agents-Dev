# Multi-Agents Dev Template

A reusable multi-agent development template for Claude Code, Codex, and other coding-agent workflows.

This repository provides a generic agent, skill, prompt, guide, and template structure that can be cloned into different software projects, then adapted with project-specific rules only when the real project needs them.

The template is intentionally domain-neutral. It is not tied to ERP systems, telecom systems, SaaS products, marketplaces, mobile apps, infrastructure vendors, automation platforms, or any specific company workflow.

---

## Core Idea

Use a small stable set of specialist agents and reusable skills to support software delivery without overloading model context.

```txt
AGENTS.md -> thin Codex-compatible entrypoint
.claude/CLAUDE.md -> short Claude Code orchestration kernel
agents -> recurring specialist roles
skills -> reusable practices and workflows
prompts -> reusable session bootstrap policies
guides -> short on-demand planning spines
templates -> fill-in documents loaded only when needed
reference docs -> detailed guidance loaded only when needed
```

Principles:

1. Keep always-loaded context small.
2. Use agents for recurring responsibilities.
3. Use skills for repeatable practices invoked on demand.
4. Use guides and templates for project/feature planning without bloating `CLAUDE.md`.
5. Use `AGENTS.md` only as a thin Codex adapter, not a duplicate of `.claude/`.

---

## Repository Structure

```txt
AGENTS.md
.claude/
  CLAUDE.md
  agents/
  skills/
  prompts/
  guides/
  templates/
    project/
    feature/
  architecture-skill-matrix.md
  agent-skill-governance.md
  context-audit.md
  template-usage.md
```

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Thin Codex-compatible repository entrypoint. Keep minimal. |
| `.claude/CLAUDE.md` | Always-loaded orchestration kernel for Claude Code. Keep short. |
| `.claude/agents/` | Specialist subagents with role prompts, tool permissions, and one preloaded primary skill. |
| `.claude/skills/` | Reusable workflows, architecture practices, quality practices, and operational skills. |
| `.claude/prompts/` | Reusable session bootstrap policies loaded only when needed. |
| `.claude/guides/` | Short on-demand guides for project inception and feature planning. |
| `.claude/templates/` | Fill-in project and feature templates opened only when needed. |
| `.claude/architecture-skill-matrix.md` | Human-readable map of agents, preloaded skills, on-demand skills, and tool tiers. |
| `.claude/agent-skill-governance.md` | Rules for deciding when to add an agent, skill, global rule, or reference document. |
| `.claude/context-audit.md` | Documentation of context economy decisions and always-loaded vs on-demand content. |
| `.claude/template-usage.md` | Detailed guide for cloning, adapting, and maintaining this template. |

---

## Included Agents

The template keeps the number of agents stable. Add a new agent only when a project introduces a recurring responsibility that cannot be represented well as a skill.

| Agent | Role | Default tier |
| --- | --- | --- |
| `software-architect` | Architecture, boundaries, trade-offs, DDD, Clean Architecture, Hexagonal Architecture, CQRS. | Review/planning |
| `backend-specialist` | APIs, services, validation, persistence, jobs, integrations, backend tests. | Implementation |
| `frontend-specialist` | UI, UX, responsive behavior, accessibility, design systems, frontend review. | Implementation |
| `security-engineer` | Defensive security review, threat modeling, auth, secrets, sensitive data, release risk. | Review/planning |
| `qa-engineer` | Test strategy, acceptance criteria, CI diagnosis, regression analysis, release readiness. | Review/planning |
| `devops-engineer` | Infrastructure, cloud/VPS/bare metal, containers, orchestration, CI/CD, networking, DNS/TLS, observability, backups, production ops. | Implementation |

---

## Included Skills

Each agent preloads only one primary operational skill. Architecture, practice, and delivery workflow skills stay available on demand through the `Skill` tool.

| Skill | Purpose |
| --- | --- |
| `orchestrating-agents` | Task intake, issue strategy, delegation, PR flow, permission gates, continuity notes. |
| `smart-dispatch` | Model/task routing and choosing the smallest useful agent team. |
| `architecting-systems` | System architecture, trade-offs, module boundaries, migrations, runtime views. |
| `building-backend-apis` | Backend APIs, services, validation, persistence, integrations, jobs. |
| `designing-frontend` | Product UI, UX, responsive behavior, interface states, design system consistency. |
| `securing-apps` | Defensive application security review and validation. |
| `qa-github-actions` | QA workflow, CI evidence, GitHub Actions checks, release readiness. |
| `managing-infrastructure` | Infrastructure, deployment, runtime, CI/CD, networking, secrets, backups, observability, and production operations. |
| `ddd-modeling` | Domain language, bounded contexts, aggregates, value objects, invariants. |
| `clean-architecture` | Layer ownership and dependency direction. |
| `hexagonal-architecture` | Ports, adapters, gateways, repositories, and anti-corruption layers. |
| `cqrs` | Command/query separation and read/write flow design. |
| `code-quality` | Maintainability, naming, cohesion, error handling, type safety. |
| `security-by-design` | Auth, permissions, secrets, validation, logging, sensitive data boundaries. |
| `testing-strategy` | Tests for domain rules, use cases, handlers, adapters, security, regressions. |
| `tlc-spec-driven` | Spec-driven feature delivery with requirements, design, task breakdown, gates, `.specs/` continuity, independent validation, and lessons. |

---

## Tool Permission Model

| Tier | Agents | Default behavior |
| --- | --- | --- |
| Review/planning | `software-architect`, `security-engineer`, `qa-engineer` | Inspect, test, review, and recommend without directly editing files. |
| Implementation | `backend-specialist`, `frontend-specialist`, `devops-engineer` | Apply scoped changes after planning and delegation. |

Review/planning agents do not include `Edit`, `MultiEdit`, or `Write` by default. This keeps the base template safer and encourages implementation through executor agents.

---

## Recommended Workflow

For every development task:

```txt
Understand -> plan -> create/update issue -> delegate agents -> branch -> PR -> validate -> document outcome
```

Recommended behavior:

1. Start with the main orchestrator.
2. Use `smart-dispatch` to choose the smallest useful agent team.
3. Use `software-architect` first for high-impact architecture decisions.
4. Use `tlc-spec-driven` when a feature needs traceable specification, task breakdown, atomic implementation, validation, UAT, or resume/pause continuity.
5. Delegate implementation to backend, frontend, or DevOps agents.
6. Use QA and security agents as reviewers when risk justifies it.
7. Keep evidence in the issue or PR.
8. Do not merge without validation.

---

## How to Use This Template

1. Copy the `.claude/` directory into a target project.
2. Copy `AGENTS.md` only when Codex-compatible workflows are needed.
3. Keep the base agents unless the project clearly needs a new recurring role.
4. Keep `.claude/CLAUDE.md` short and global.
5. Use `.claude/prompts/bootstrap.md` to start/resume model sessions.
6. Use `.claude/guides/project-from-zero.md` when starting a project from zero.
7. Use `.claude/guides/feature-planning.md` when planning one feature.
8. Use `.claude/templates/` to create project and feature spec files without loading long guides.
9. Add project-specific skills only after the project domain is known.
10. Update `.claude/context-audit.md` when changing always-loaded context, agent topology, or skill preload policy.
11. Use `.claude/agent-skill-governance.md` before adding new agents or changing permissions.

See `.claude/template-usage.md` for the full guide.

---

## What Belongs in the Base Template

Good candidates:

- universal software engineering roles;
- reusable architecture practices;
- security, testing, infrastructure, and quality practices;
- generic GitHub issue and PR workflow;
- generic context economy rules;
- generic agent and skill governance;
- stack-neutral feature delivery workflows that remain on demand;
- small guide spines and reusable templates that remain on demand.

Poor candidates:

- ERP-specific instructions;
- telecom-specific instructions;
- payment-provider-specific instructions;
- Docker-only or n8n-only operational assumptions;
- cloud-vendor-specific deployment commands;
- company-specific deployment commands;
- project-specific environment variables;
- product-specific domain language;
- one-off workflow details.

Project-specific knowledge should be added after cloning the template into a real project.

---

## When to Add a Skill

Add a skill when the behavior is repeatable and can be reused by one or more agents.

Avoid adding a skill when the behavior is only a one-time note or a project-specific instruction better stored in documentation.

---

## When to Add an Agent

Add an agent only when there is a recurring role with distinct responsibility, tool needs, and output expectations.

Examples in a project clone:

```txt
mobile-specialist
compliance-reviewer
data-engineer
telecom-network-specialist
ai-rag-engineer
platform-engineer
```

Avoid adding an agent when a skill, guide, template, or short instruction is enough.

---

## Maintenance Checklist

Before merging changes to this template, check:

```txt
- Is this generic enough for many software projects?
- Does it increase always-loaded context?
- Does any agent preload more than one primary skill?
- Did tool permissions become broader than necessary?
- Should this be a skill instead of an agent?
- Should this be a guide/template/reference instead of CLAUDE.md content?
- Are project-specific examples avoided or clearly marked?
- Is the PR validation evidence documented?
```

---

## Current Status

This template is designed as a reusable foundation. The best next improvements should come from real project usage, not speculative additions.

When a project needs domain-specific behavior, clone the template and extend the clone rather than expanding the base template.
