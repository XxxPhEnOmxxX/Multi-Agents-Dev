# Template Usage Guide

Issue: #5  
Related updates: #12, #14, #16

## Purpose

This guide explains how to use this repository as a reusable multi-agent template for software development projects.

The goal is not to predict every possible domain, platform, or infrastructure stack. The goal is to provide a strong generic foundation that can be cloned into a real project and then adapted with project-specific skills, agents, references, rules, specs, and templates.

---

## Design Philosophy

This template is built around context economy and separation of responsibility.

```txt
Load the minimum context needed now.
Keep detailed knowledge available, but not always loaded.
```

| Layer | Loaded by Default? | Purpose |
| --- | --- | --- |
| `AGENTS.md` | Yes for Codex-compatible workflows | Thin repository entrypoint. |
| `.claude/CLAUDE.md` | Yes for Claude Code | Small orchestration kernel and global rules. |
| Agents | When delegated | Specialist roles with focused instructions and tool permissions. |
| Skills | On demand or preloaded by one agent | Reusable workflows and practices. |
| Prompts | Only when read | Session bootstrap policies. |
| Guides | Only when read | Short planning spines for project/feature work. |
| Templates | Only when read | Fill-in structures for `.specs/` artifacts. |
| Reference docs | Only when read | Detailed documentation for maintainers and project adaptation. |

---

## What This Template Is

This template is:

- a reusable multi-agent development team structure;
- a generic setup for Claude Code, Codex, and similar coding-agent workflows;
- a context-conscious organization of agents, skills, prompts, guides, templates, and references;
- a foundation for DDD, Clean Architecture, Hexagonal Architecture, CQRS, security, QA, frontend, backend, infrastructure, and DevOps work;
- a starting point that should be adapted after being cloned into a real project.

## What This Template Is Not

This template is not:

- a finished architecture for every project;
- a replacement for project-specific documentation;
- a place for ERP, telecom, finance, mobile, vendor, cloud, Docker, Kubernetes, or n8n-specific rules;
- a place to preload every useful skill;
- a reason to create an agent for every specialization;
- a substitute for human review and validation.

---

## First-Time Setup in a Project

### 1. Copy the base structure

Recommended result:

```txt
project-root/
  AGENTS.md                     # optional, for Codex-compatible workflows
  .claude/
    CLAUDE.md
    agents/
    skills/
    prompts/
    guides/
    templates/
    architecture-skill-matrix.md
    agent-skill-governance.md
    context-audit.md
    template-usage.md
```

### 2. Read the existing project

Before adapting anything, inspect:

```txt
language and framework
package manager
test commands
build commands
deployment model
runtime and infrastructure platform
architecture style
existing docs
security boundaries
data model
domain language
CI/CD workflow
production risks
```

Do not write project-specific instructions before understanding the project.

### 3. Keep `CLAUDE.md` short

Use `.claude/CLAUDE.md` only for rules that are always relevant.

Good additions:

```txt
required package manager
required test command
required build command
project-wide forbidden operations
required branch and PR policy
short architecture summary
short routing hints
```

Bad additions:

```txt
long framework tutorials
full database schema explanations
full API documentation
vendor manuals
cloud provider manuals
large examples
secrets or credentials
long troubleshooting logs
```

### 4. Keep `AGENTS.md` thin

Use `AGENTS.md` as a Codex adapter, not as a duplicate of `.claude/CLAUDE.md`.

It should include only:

```txt
minimal workflow
minimal read order
context economy rules
security rules
pointers to .claude/ files
```

### 5. Use guides and templates only when needed

Use:

```txt
.claude/guides/project-from-zero.md -> when starting a project from a raw idea
.claude/templates/project/ -> fill-in files for project inception
.claude/guides/feature-planning.md -> when planning one feature
.claude/templates/feature/ -> fill-in files for feature specs/design/tasks
```

Do not load every guide and template by default.

### 6. Add project-specific skills only when needed

Add a skill when:

```txt
the workflow repeats
multiple agents can benefit from it
the trigger condition is clear
the content is too detailed for CLAUDE.md
it improves consistency or safety
```

Do not add project-specific skills just because they might be useful one day.

### 7. Add project-specific agents only when a real role appears

Add an agent when the project has a recurring role that needs:

```txt
distinct responsibility
distinct judgment
distinct tool permissions
distinct output format
recurring use across many tasks
```

Do not create a new agent when a skill, guide, template, or reference document is enough.

---

## Base Agent Responsibilities

| Agent | Use For | Default Behavior |
| --- | --- | --- |
| `software-architect` | architecture decisions, module boundaries, DDD, Clean/Hexagonal/CQRS, scalability | review, reason, recommend, delegate implementation |
| `backend-specialist` | APIs, services, validation, persistence, integrations, backend tests | implement scoped backend changes after planning |
| `frontend-specialist` | UI, UX, responsive behavior, accessibility, interface copy | implement scoped frontend changes after planning |
| `security-engineer` | auth, authorization, secrets, sensitive data, public APIs, release risk | inspect, validate, recommend fixes |
| `qa-engineer` | acceptance criteria, test strategy, CI evidence, regression risk | validate and recommend readiness |
| `devops-engineer` | infrastructure, deploy, CI/CD, networking, TLS, observability, backups | implement scoped infrastructure changes with safety gates |

Review/planning agents are read-oriented by default. Implementation agents can edit after planning and delegation.

---

## Skill Loading Strategy

Rule:

```txt
One primary preloaded skill per agent.
Everything else should be invoked on demand.
```

Preloaded skills:

| Agent | Preloaded Skill |
| --- | --- |
| `software-architect` | `architecting-systems` |
| `backend-specialist` | `building-backend-apis` |
| `frontend-specialist` | `designing-frontend` |
| `security-engineer` | `securing-apps` |
| `qa-engineer` | `qa-github-actions` |
| `devops-engineer` | `managing-infrastructure` |

On-demand skills include DDD, Clean Architecture, Hexagonal Architecture, CQRS, code quality, security-by-design, testing strategy, and `tlc-spec-driven`.

Use a skill only when it changes the quality of the answer or implementation.

---

## Recommended Task Flow

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

Use the smallest useful set of agents.

Avoid summoning every agent by default.

---

## Context Budget Levels

| Level | Use When | Context Strategy |
| --- | --- | --- |
| S | one file or one small task | no subagent unless needed; read only touched file and immediate instructions |
| M | one feature task | read bootstrap, target spec/design/tasks, and touched code paths |
| L | new feature planning | use `feature-planning.md`, selected feature templates, and `tlc-spec-driven` if needed |
| XL | new project or major architecture | use `project-from-zero.md`, selected project templates, and `software-architect` |

Escalate only when risk or ambiguity requires it.

---

## Documentation Rules

| Document | Purpose |
| --- | --- |
| `README.md` | Human entrypoint for the repository. |
| `AGENTS.md` | Thin Codex-compatible entrypoint. |
| `.claude/CLAUDE.md` | Always-loaded Claude Code orchestration rules. |
| `.claude/prompts/bootstrap.md` | Session bootstrap policy. |
| `.claude/guides/` | Project and feature planning spines. |
| `.claude/templates/` | Fill-in project and feature documents. |
| `.claude/context-audit.md` | Context economy and loading policy. |
| `.claude/architecture-skill-matrix.md` | Agent and skill distribution. |
| `.claude/agent-skill-governance.md` | Template maintenance rules. |
| `.claude/template-usage.md` | Full usage and adaptation guide. |

---

## Pre-Merge Checklist for Template Changes

```txt
- The change is generic enough for many software projects.
- The change does not add domain-specific or platform-specific behavior to the base template.
- CLAUDE.md remains short.
- AGENTS.md remains thin.
- No agent preloads more than one primary skill.
- Review/planning agents remain read-oriented unless intentionally changed.
- New skills have specific descriptions and clear triggers.
- New agents have distinct recurring responsibilities.
- Long instructions are placed in skills, guides, templates, or reference docs.
- The architecture-skill matrix is updated if agent/skill mapping changes.
- The context audit is updated if loading behavior changes.
- The PR documents validation evidence and residual risk.
```

---

## Recommended Evolution Path

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
