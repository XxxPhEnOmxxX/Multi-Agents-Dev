# Template Usage Guide

Issue: #5

## Purpose

This guide explains how to use this repository as a reusable Claude Code multi-agent template for software development projects.

The goal is not to predict every possible project domain. The goal is to provide a strong generic foundation that can be cloned into a real project and then adapted with project-specific skills, agents, references, and rules.

## Design Philosophy

This template is built around context economy and separation of responsibility.

A Claude Code setup can become expensive and unreliable when too much information is loaded too early. The template avoids that by separating content into four layers:

| Layer | Loaded by default? | Purpose |
| --- | --- | --- |
| `CLAUDE.md` | Yes | Small orchestration kernel and global rules. |
| Agents | When delegated | Specialist roles with focused instructions and tool permissions. |
| Skills | On demand or preloaded by an agent | Reusable workflows and practices. |
| Reference docs | Only when read | Detailed documentation for maintainers and project adaptation. |

The main idea is simple:

```txt
Load the minimum context needed now.
Keep detailed knowledge available, but not always loaded.
```

## What This Template Is

This template is:

- a reusable Claude Code development team structure;
- a generic multi-agent setup for software engineering;
- a context-conscious organization of agents and skills;
- a foundation for DDD, Clean Architecture, Hexagonal Architecture, CQRS, security, QA, frontend, backend, and DevOps work;
- a starting point that should be adapted after being cloned into a real project.

## What This Template Is Not

This template is not:

- a finished architecture for every project;
- a replacement for project-specific documentation;
- a place for ERP, telecom, finance, mobile, or vendor-specific rules;
- a place to preload every useful skill;
- a reason to create an agent for every specialization;
- a substitute for human review and validation.

## First-Time Setup in a Project

When using this template in a real project, follow this sequence.

### 1. Copy the Claude Code structure

Copy the `.claude/` directory into the target project.

Recommended result:

```txt
project-root/
  .claude/
    CLAUDE.md
    agents/
    skills/
    architecture-skill-matrix.md
    agent-skill-governance.md
    context-audit.md
    template-usage.md
```

### 2. Read the existing project

Before adapting anything, inspect the target project:

```txt
- language and framework;
- package manager;
- test commands;
- build commands;
- deployment model;
- architecture style;
- existing docs;
- security boundaries;
- data model;
- domain language;
- CI/CD workflow;
- production risks.
```

Do not write project-specific instructions before understanding the project.

### 3. Update CLAUDE.md carefully

Use `.claude/CLAUDE.md` only for rules that are always relevant.

Good additions:

```txt
- Required package manager.
- Required test command.
- Required build command.
- Project-wide forbidden operations.
- Required branch and PR policy.
- High-level architecture summary.
- Short routing hints for agents.
```

Bad additions:

```txt
- Long framework tutorials.
- Full database schema explanations.
- Full API documentation.
- Vendor manuals.
- Large examples.
- Secrets or credentials.
- Long troubleshooting logs.
```

If a rule is long, put it in a skill or reference document.

### 4. Add project-specific skills only when needed

Do not add project-specific skills just because they might be useful one day.

Add a skill when:

```txt
- the workflow repeats;
- multiple agents can benefit from it;
- the trigger condition is clear;
- the content is too detailed for CLAUDE.md;
- it improves consistency or safety.
```

Examples:

```txt
.claude/skills/payment-provider-integration/
.claude/skills/mobile-release-checklist/
.claude/skills/legacy-database-migration/
.claude/skills/observability-review/
.claude/skills/erp-adapter-integration/
```

### 5. Add project-specific agents only when a real role appears

Do not create new agents just to organize topics.

Add an agent when the project has a recurring role that needs:

```txt
- distinct responsibility;
- distinct judgment;
- distinct tool permissions;
- distinct output format;
- recurring use across many tasks.
```

Examples:

```txt
mobile-specialist
compliance-reviewer
data-engineer
telecom-network-specialist
ai-rag-engineer
```

Do not create a new agent when a skill is enough.

## Base Agent Responsibilities

### software-architect

Use for:

```txt
- architecture decisions;
- module boundaries;
- DDD modeling;
- Clean Architecture decisions;
- Hexagonal Architecture boundaries;
- CQRS trade-offs;
- migrations;
- scalability and reliability trade-offs.
```

Default behavior:

```txt
Review, reason, recommend, and delegate implementation.
```

This agent is read-oriented by default. It should not directly edit files in the base template.

### backend-specialist

Use for:

```txt
- API design;
- services and use cases;
- validation;
- persistence;
- transactions;
- integrations;
- jobs and queues;
- backend tests.
```

Default behavior:

```txt
Implement scoped backend changes after planning.
```

### frontend-specialist

Use for:

```txt
- UI implementation;
- UX flow;
- responsive behavior;
- accessibility;
- design system consistency;
- interface copy;
- loading, empty, error, success states.
```

Default behavior:

```txt
Implement scoped frontend changes after planning.
```

### security-engineer

Use for:

```txt
- defensive security review;
- threat modeling;
- authentication;
- authorization;
- secrets;
- sensitive data;
- public APIs;
- CORS and headers;
- webhooks;
- deploy risk;
- release security validation.
```

Default behavior:

```txt
Inspect, validate, classify risk, recommend fixes, and block release when justified.
```

This agent is read-oriented by default. It should not directly edit files in the base template.

### qa-engineer

Use for:

```txt
- acceptance criteria;
- test strategy;
- regression analysis;
- GitHub Actions diagnosis;
- CI evidence;
- release readiness;
- merge recommendation.
```

Default behavior:

```txt
Run or review checks, document evidence, recommend fixes, and decide readiness.
```

This agent is read-oriented by default. It should not directly edit files in the base template.

### devops-engineer

Use for:

```txt
- Docker;
- Docker Compose;
- n8n;
- reverse proxy;
- deployment;
- volumes;
- networks;
- logs;
- backups;
- production operations.
```

Default behavior:

```txt
Implement scoped infrastructure changes with explicit safety gates.
```

## Skill Loading Strategy

Claude Code skills can be invoked on demand. Subagent `skills:` frontmatter preloads skill content into the subagent context.

Because preloaded skill content consumes context, this template uses this rule:

```txt
One primary preloaded skill per agent.
Everything else should be invoked on demand.
```

This keeps subagent context smaller while preserving access to specialized practices.

## Preloaded Skills

| Agent | Preloaded skill |
| --- | --- |
| `software-architect` | `architecting-systems` |
| `backend-specialist` | `building-backend-apis` |
| `frontend-specialist` | `designing-frontend` |
| `security-engineer` | `securing-apps` |
| `qa-engineer` | `qa-github-actions` |
| `devops-engineer` | `managing-docker-n8n-infra` |

## On-Demand Practice Skills

These skills are not preloaded everywhere. They should be used when the task requires them.

| Skill | Use when |
| --- | --- |
| `ddd-modeling` | The task involves domain language, bounded contexts, entities, value objects, aggregates, or invariants. |
| `clean-architecture` | The task involves layer ownership, dependency direction, use cases, controllers, repositories, or boundaries. |
| `hexagonal-architecture` | The task involves ports, adapters, gateways, external systems, repositories, or anti-corruption layers. |
| `cqrs` | The task involves command/query separation, read models, write flows, handlers, or idempotent command behavior. |
| `code-quality` | The task involves maintainability, naming, cohesion, type safety, errors, duplication, or readability. |
| `security-by-design` | The task involves auth, authorization, secrets, sensitive data, validation, logs, or trust boundaries. |
| `testing-strategy` | The task involves domain tests, use case tests, handler tests, adapter tests, regression tests, or security tests. |

## Recommended Task Flow

Use this flow for most development work:

```txt
1. Understand the request.
2. Identify assumptions and unknowns.
3. Create or update a GitHub issue.
4. Decide which agents are needed.
5. Plan implementation and validation.
6. Create a branch.
7. Delegate implementation to executor agents.
8. Use QA/security review when risk justifies it.
9. Open or update a pull request.
10. Validate with evidence.
11. Document the result.
```

## Choosing Agents

Use the smallest useful set of agents.

| Task type | Usually use |
| --- | --- |
| Architecture decision | `software-architect` |
| Backend implementation | `backend-specialist` |
| Frontend implementation | `frontend-specialist` |
| Security-sensitive change | `security-engineer` plus relevant executor |
| Test planning or CI failure | `qa-engineer` |
| Docker, deploy, n8n, proxy | `devops-engineer` |
| Full-stack feature | `software-architect`, `backend-specialist`, `frontend-specialist`, `qa-engineer` as needed |
| High-risk release | `qa-engineer`, `security-engineer`, relevant executor |

Avoid summoning every agent by default.

## Choosing Skills

Use a skill when the task needs a repeatable practice.

Examples:

```txt
Use ddd-modeling when naming domain concepts.
Use clean-architecture when deciding where behavior belongs.
Use hexagonal-architecture when adding an external integration.
Use cqrs when separating writes from reads.
Use security-by-design when auth or sensitive data is involved.
Use testing-strategy when deciding coverage and validation evidence.
```

Do not use a skill just because it exists. Use it when it changes the quality of the answer or implementation.

## Agent vs Skill Rule

Use this rule when extending the template:

```txt
Agent = recurring role with responsibility, judgment, permissions, and output.
Skill = reusable practice, workflow, standard, or knowledge package.
Reference doc = detailed information that should not always be loaded.
CLAUDE.md = global rule that must always apply.
```

Examples:

| Need | Best fit | Reason |
| --- | --- | --- |
| Review every payment integration for provider-specific edge cases | Skill | Repeatable workflow used by backend and security agents. |
| Mobile app development across many tasks | Agent | Recurring role with distinct expertise. |
| Project deploy commands | Reference doc or CLAUDE.md summary | Detailed commands should not bloat CLAUDE.md. |
| Rule that all tasks need a PR | CLAUDE.md | Always relevant. |
| Domain glossary | Reference doc or DDD skill extension | Useful on demand, not always needed. |

## Skill Authoring Pattern

Recommended structure for a new skill:

```md
---
name: clear-kebab-name
description: Use this skill when <specific trigger condition>.
---

# Skill Title

## Purpose

What this skill helps with.

## Use When

- Trigger condition 1.
- Trigger condition 2.
- Trigger condition 3.

## Do Not Use When

- Non-trigger 1.
- Non-trigger 2.

## Workflow

1. Step one.
2. Step two.
3. Step three.

## Expected Output

- Output item 1.
- Output item 2.
```

Good skill descriptions are specific. The description is important because it helps Claude decide when to invoke the skill.

## Skill Size Guidance

Prefer a small `SKILL.md` as the workflow spine.

Good:

```txt
SKILL.md -> purpose, triggers, workflow, expected output
references/*.md -> long examples, templates, domain glossary, payload details
scripts/* -> deterministic helpers when useful
```

Avoid:

```txt
One huge SKILL.md containing every example, every edge case, every domain glossary, and every vendor detail.
```

## Adapting the Template for Project Types

### SaaS or web app

Possible additions after clone:

```txt
.claude/skills/subscription-billing/
.claude/skills/admin-dashboard-review/
.claude/skills/product-analytics/
```

Potential new agent only if recurring:

```txt
product-engineer
```

### Mobile app

Possible additions after clone:

```txt
.claude/skills/mobile-release-checklist/
.claude/skills/offline-sync-review/
.claude/skills/app-store-submission/
```

Potential new agent only if recurring:

```txt
mobile-specialist
```

### ERP or external integration platform

Possible additions after clone:

```txt
.claude/skills/erp-adapter-integration/
.claude/skills/capability-driven-integration/
.claude/skills/webhook-reliability/
```

Potential new agent only if recurring:

```txt
integration-specialist
```

### Telecom or ISP operations

Possible additions after clone:

```txt
.claude/skills/isp-field-operations/
.claude/skills/olt-network-diagnostics/
.claude/skills/geospatial-network-mapping/
```

Potential new agent only if recurring:

```txt
telecom-network-specialist
```

### AI or RAG system

Possible additions after clone:

```txt
.claude/skills/rag-evaluation/
.claude/skills/mcp-server-design/
.claude/skills/prompt-regression-testing/
```

Potential new agent only if recurring:

```txt
ai-rag-engineer
```

## Adapting CLAUDE.md After Clone

When adapting `.claude/CLAUDE.md`, keep it short.

Recommended sections:

```txt
- Project summary.
- Core workflow.
- Required commands.
- Architecture summary.
- Safety rules.
- Agent routing notes.
- Completion report format.
```

Example project-specific addition:

```txt
## Project Commands

- Install: npm install
- Test: npm test
- Lint: npm run lint
- Build: npm run build
```

Bad project-specific addition:

```txt
A 400-line explanation of every route, database table, status code, and vendor payload.
```

Use references for detailed content.

## Maintaining Context Economy

Every new instruction has a context cost.

Before adding content, ask:

```txt
- Must this be loaded for every task?
- Can this be discovered on demand?
- Is this a repeatable workflow?
- Is this a domain detail?
- Is this better as a skill, reference, or README?
```

Default choice:

```txt
Global always-needed rule -> CLAUDE.md
Repeatable workflow -> skill
Detailed background -> reference doc
Recurring specialist role -> agent
One-time note -> issue or PR
```

## Safety and Permissions

The template uses two permission tiers.

Review/planning agents:

```txt
software-architect
security-engineer
qa-engineer
```

These should inspect, review, test, and recommend.

Implementation agents:

```txt
backend-specialist
frontend-specialist
devops-engineer
```

These can apply scoped changes after planning.

Do not broaden permissions just because it is convenient. Broaden permissions only when the project adaptation explicitly changes the agent role.

## Documentation Rules

Use documentation intentionally.

| Document | Purpose |
| --- | --- |
| `README.md` | Human entrypoint for the repository. |
| `.claude/CLAUDE.md` | Always-loaded Claude Code orchestration rules. |
| `.claude/context-audit.md` | Context economy and loading policy. |
| `.claude/architecture-skill-matrix.md` | Agent and skill distribution. |
| `.claude/agent-skill-governance.md` | Template maintenance rules. |
| `.claude/template-usage.md` | Full usage and adaptation guide. |

## Pre-Merge Checklist for Template Changes

Use this checklist before merging changes to the base template:

```txt
- The change is generic enough for many software projects.
- The change does not add domain-specific behavior to the base template.
- CLAUDE.md remains short.
- No agent preloads more than one primary skill.
- Review/planning agents remain read-oriented unless intentionally changed.
- New skills have specific descriptions and clear triggers.
- New agents have distinct recurring responsibilities.
- Long instructions are placed in skills or reference docs.
- The architecture-skill matrix is updated.
- The context audit is updated.
- The PR documents validation evidence and residual risk.
```

## Recommended Evolution Path

The best way to evolve this template is through real use.

Recommended sequence:

```txt
1. Merge the generic base.
2. Clone it into a real project.
3. Use it for real development tasks.
4. Record friction points.
5. Add project-specific skills in the clone.
6. Only promote a pattern back to the base template if it is clearly reusable across many project types.
```

Avoid speculative expansion. A template becomes powerful when it stays clear, not when it tries to contain every future possibility.

## Final Rule

When in doubt, keep the base template smaller and extend the project clone later.