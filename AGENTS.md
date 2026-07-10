# AGENTS.md

## Purpose

This file is a thin Codex-compatible adapter for this multi-agent development template.

Claude Code uses `.claude/CLAUDE.md` as the main orchestration kernel. Codex-compatible agents should use this file as the repository entrypoint, then read only the extra files needed for the current task.

Do not duplicate the full `.claude/` system here.

---

## Core Workflow

```txt
understand -> plan -> issue -> branch -> implement -> validate -> PR -> handoff
```

Rules:

- Do not implement before planning.
- Use one task per branch/PR when possible.
- Keep changes scoped and reviewable.
- Do not access secrets, production data, private keys, customer data, or real credentials without explicit approval.
- Do not run destructive commands without explicit approval.
- Validate with evidence before reporting completion.
- Update handoff state when `.specs/STATE.md` exists.

---

## Read Order

Read the smallest useful set of files.

Always use this file as the Codex entrypoint.

Read additional files only when the current task needs them:

```txt
.claude/CLAUDE.md -> when Claude Code orchestration details, agent routing, or skill policy are needed
.claude/prompts/bootstrap.md -> when starting, resuming, reconciling, or handing off a session
README.md -> when a human-level repository overview is needed
```

When `.specs/` exists and the task depends on project state, read:

```txt
.specs/STATE.md
.specs/PROJECT-SCAN.md
.specs/FEATURE-ROADMAP.md
```

For a specific feature, read only that feature's files:

```txt
.specs/features/[feature]/spec.md
.specs/features/[feature]/design.md
.specs/features/[feature]/tasks.md
```

For project inception or feature planning, read the matching guide spine and only the templates needed:

```txt
.claude/guides/project-from-zero.md
.claude/guides/feature-planning.md
.claude/templates/project/[needed-template].md
.claude/templates/feature/[needed-template].md
```

Do not load entire guide, template, agent, or skill directories by default.

---

## Context Economy

Do not load all agents, skills, guides, references, or templates by default.

Use this rule:

```txt
small task -> relevant spec/task + touched files
feature planning -> guide spine + selected templates
feature delivery -> tlc-spec-driven + selected specialist agents
new project -> project-from-zero guide + selected project templates
```

Avoid broad repository scans unless the task requires them.

---

## Multi-Agent Responsibility Map

Use roles as responsibilities. Do not invent new agents unless a project clone defines them.

| Role | Use For |
| --- | --- |
| `software-architect` | architecture, boundaries, DDD, Clean/Hexagonal/CQRS decisions |
| `backend-specialist` | backend APIs, services, domain/application code, persistence, integrations |
| `frontend-specialist` | UI, UX flows, frontend state, accessibility, API integration |
| `security-engineer` | auth, permissions, secrets, privacy, threat modeling |
| `qa-engineer` | tests, acceptance criteria, CI, validation evidence |
| `devops-engineer` | CI/CD, runtime, Docker, deploy, observability, backups |

Use the smallest useful set of agents.

---

## Completion Report

End each task with:

```md
# Session Complete

## Issue

## Branch

## PR

## Files Changed

## What Changed

## What Did Not Change

## Tests and Gates

## Security Notes

## Handoff

## Next Step
```
