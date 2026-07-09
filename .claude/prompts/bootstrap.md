# Bootstrap Policy for LLM Multi-Agent Sessions

## Purpose

This file defines the standard bootstrap policy for starting, resuming, reviewing, or handing off work in a multi-agent LLM development structure.

It exists to make development:

- traceable;
- secure;
- architecture-aligned;
- testable;
- reviewable;
- resumable across sessions and models.

The repository is the source of truth. Chat memory is temporary.

---

## Core Principle

Do not start by coding.

Every new LLM session must first rebuild project context from the repository, identify the exact work unit, verify the current state, and only then act.

Default flow:

```txt
read context -> inspect state -> choose task -> plan -> issue -> branch -> change -> validate -> commit -> PR -> handoff
```

---

## Source of Truth Order

Read these files first when they exist:

```txt
.claude/CLAUDE.md
AGENTS.md
PROMPT.md
README.md
.specs/STATE.md
.specs/PROJECT-SCAN.md
.specs/FEATURE-ROADMAP.md
.specs/NEXT-SESSIONS.md
.specs/PROMPT-NEXT-IMPLEMENTATION.md
docs/adr/
.github/workflows/
package.json
.env.example
```

For a specific feature, also read:

```txt
.specs/features/[feature]/spec.md
.specs/features/[feature]/design.md
.specs/features/[feature]/tasks.md
.specs/features/[feature]/context.md
.specs/features/[feature]/validation.md
```

If a file does not exist, register it as a gap. Do not invent project facts.

---

## Session Modes

Every session must declare one mode before acting.

| Mode | Use When | Functional Code Allowed? |
| --- | --- | --- |
| `bootstrap` | Creating the first project continuity/spec layer | No |
| `scan` | Understanding repository, stack, risks, and commands | No |
| `spec` | Creating or updating feature specs | No |
| `implement` | Implementing one atomic task | Yes, scoped |
| `review` | Reviewing code, architecture, PRs, or specs | Only if requested |
| `reconcile` | Aligning specs with recent code/PR changes | No, until clear |
| `handoff` | Recording what changed and what comes next | Docs/specs only |

If the correct mode is unclear, use `scan` or `reconcile` first.

---

## Required Start Report

Before implementing, the model must produce:

```md
# Session Bootstrap Report

## Project

## Session Mode

## Current Branch

## Default Branch

## Git Status Summary

## Multi-Agent Structure Detected

## Specs Detected

## Last Handoff

## Target Feature

## Target Task

## Relevant Files Read

## Risks or Blockers

## Recommended Next Action

## Scope Confirmation
```

No implementation should happen before this report.

---

## Required End Report

Every session must end with:

```md
# Session Complete

## Mode

## Issue

## Branch

## Commit

## PR

## Files Changed

## What Changed

## What Did Not Change

## Tests and Gates

## Architecture Notes

## Security Notes

## Specs Updated

## STATE.md Handoff

## Next Recommended Session

## Risks Remaining
```

If no functional code was changed, state:

```txt
No functional code was implemented.
```

---

## Multi-Agent Rules

Agents are responsibilities, not personalities.

Recommended responsibilities:

| Agent | Responsibility |
| --- | --- |
| `software-architect` | architecture decisions, module boundaries, dependency rules |
| `backend-specialist` | domain, application services, APIs, persistence, integrations |
| `frontend-specialist` | UI, frontend state, accessibility, API integration |
| `security-engineer` | auth, permissions, secrets, privacy, threat modeling |
| `qa-engineer` | test strategy, acceptance criteria, regression risk, gates |
| `devops-engineer` | CI/CD, Docker, environments, deploy, observability |
| `product-owner` | scope, value, priority, user stories |
| `technical-writer` | documentation, handoff, operational clarity |

Do not create a new agent unless the responsibility is recurring, distinct, and useful across multiple tasks.

---

## Skill Rules

Skills are reusable workflows.

Use skills for repeatable work such as:

- spec-driven development;
- architecture review;
- backend API implementation;
- frontend implementation;
- security review;
- testing strategy;
- infrastructure planning;
- code quality review.

Rules:

1. Do not preload every skill.
2. Load only the skill required for the current task.
3. Keep `.claude/CLAUDE.md` short.
4. Put detailed workflows in skills, reference docs, or prompts.
5. Do not duplicate long instructions across many files.
6. Do not use a skill to bypass project architecture rules.

---

## Context Rules

LLMs must treat context as limited.

Load context in this priority:

1. current task;
2. relevant spec;
3. relevant design;
4. relevant tasks file;
5. current code paths;
6. architecture decisions;
7. project scan;
8. broader docs only when needed.

Do not load unrelated files. Do not scan the whole repository without need.

---

## Specification Rules

Every significant feature should have:

```txt
.specs/features/[feature]/spec.md
.specs/features/[feature]/design.md
.specs/features/[feature]/tasks.md
```

Use `context.md` for ambiguity, legacy behavior, external dependencies, or conflicts.

Use `validation.md` when evidence must be recorded.

### `spec.md` must define

- problem;
- goals;
- out of scope;
- assumptions;
- open questions;
- user stories;
- acceptance criteria;
- edge cases;
- requirement traceability;
- success criteria.

### `design.md` must define

- architecture overview;
- layers;
- components;
- ports and adapters;
- data model notes;
- command/query notes;
- security notes;
- integration notes;
- risks;
- technical decisions.

### `tasks.md` must define

- atomic tasks;
- dependencies;
- suggested files;
- required tests;
- gate commands;
- suggested agent;
- done criteria;
- suggested commit message.

---

## Architecture Rules

When the project has no stronger local rule, prefer:

- modular architecture;
- explicit module boundaries;
- domain isolated from frameworks;
- application layer for use cases;
- infrastructure behind adapters;
- external systems behind ports;
- interface layer without business rules;
- tests close to the code they validate;
- documented architecture decisions.

When appropriate, use:

- Clean Architecture;
- Hexagonal Architecture;
- DDD;
- CQRS;
- modular monolith before distributed services;
- anti-corruption layers for external systems.

Do not introduce microservices, queues, event buses, Redis, S3, workers, or distributed infrastructure unless a spec or architecture decision justifies it.

---

## Git Delivery Rules

Default delivery flow:

```txt
understand -> plan -> issue -> branch -> implement -> validate -> commit -> PR -> handoff
```

Rules:

1. Check `git status` before editing.
2. Identify the default branch before branching.
3. Use one branch per task or tightly related task group.
4. Keep PRs small and reviewable.
5. Link PRs to issues.
6. Include validation evidence in the PR.
7. Update specs and `STATE.md` when behavior or decisions change.
8. Do not open PRs against the wrong branch.
9. Do not include unreviewed sensitive files.
10. Do not mix specs bootstrap with functional implementation.

---

## Security Rules

Treat the LLM as an automation assistant with limited trust.

Never expose, copy, commit, or summarize sensitive values from:

```txt
.env
.env.*
private keys
tokens
API credentials
cookies
session dumps
database backups
customer exports
internal API documents
production logs
```

If a potentially sensitive file is required:

1. stop;
2. report the risk;
3. request a sanitized version or explicit approval;
4. never paste secret values into chat or docs.

Commands requiring explicit approval:

- destructive file operations;
- production deploys;
- database migrations against real environments;
- credential changes;
- broad dependency upgrades;
- network operations against systems not confirmed as owned/authorized;
- commands copied from untrusted sources.

---

## Validation Rules

Before finishing a task, run the gates defined by the project.

Look for commands in:

```txt
package.json
README.md
.specs/PROJECT-SCAN.md
.github/workflows/
Makefile
justfile
docker-compose.yml
```

Common gates:

```txt
npm test
npm run test
npm run test:unit
npm run test:integration
npm run test:architecture
npm run lint
npm run typecheck
npm run build
pnpm test
pnpm lint
pnpm typecheck
pnpm build
```

If a gate is unavailable, write `not available`.

If a gate fails, report:

- command;
- summarized error;
- likely cause;
- recommended next action.

Do not hide failed validation.

---

## Handoff Rules

Every session must preserve continuity.

If `.specs/STATE.md` exists, update it before ending.

Recommended state structure:

```md
# STATE

## Decisions

### AD-001
- **Decision**:
- **Reason**:
- **Trade-off**:
- **Scope**:
- **Date**:
- **Status**:

## Handoff

- **Project**:
- **Feature**:
- **Phase / Task**:
- **Completed**:
- **In-progress**:
- **Next step**:
- **Blockers**:
- **Issue**:
- **PR**:
- **Branch**:
- **Commit**:
- **Files changed**:
- **Gates executed**:
- **Uncommitted files**:
- **Risks**:
```

Decisions should be append-only when possible.

The handoff should reflect the latest state of the project.

---

## Good Prompt Shape

Use structured prompts.

A good implementation prompt includes:

```txt
identity
mode
goal
target feature
target task
files to read
rules
out of scope
validation gates
expected output
handoff requirements
```

Avoid prompts like:

```txt
continue the project
finish the app
improve everything
refactor all architecture
```

Prefer prompts like:

```txt
Implement only [feature] [task] according to:
.specs/features/[feature]/spec.md
.specs/features/[feature]/design.md
.specs/features/[feature]/tasks.md
```

---

## Stop Conditions

Stop before changing files if:

- the branch is unclear;
- the target task is unclear;
- the spec conflicts with current code;
- there are unrelated uncommitted changes;
- sensitive files are required;
- the action may affect production;
- validation cannot be identified;
- the requested work is larger than one safe unit.

In these cases, produce a reconciliation report instead of implementing.

---

## Golden Rule

Do not work as if continuing a chat.

Work as if assuming a professional project with history, specs, decisions, branches, issues, PRs, and validation gates.

The repository is the memory.  
The specs are the plan.  
The `STATE.md` file is the resume point.  
The issue is the work contract.  
The PR is the auditable delivery.  
The gates are the evidence.
