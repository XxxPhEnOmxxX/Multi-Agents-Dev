# Agent and Skill Governance

Issue: #5

## Purpose

Keep this repository useful as a generic multi-agent software-development template.

The base template should stay small, reusable, and domain-neutral. Project-specific behavior should be added after cloning the template into a real project.

## Agent vs Skill Decision

| Create or update | Use when | Avoid when |
| --- | --- | --- |
| Agent | The work needs a recurring role, independent judgment, tool boundaries, review responsibility, or a distinct output format. | The need is only a reusable checklist, coding convention, or narrow workflow. |
| Skill | The work is a repeatable practice, workflow, standard, or knowledge package that one or more agents can invoke on demand. | The work requires a persistent role, separate permissions, or independent responsibility. |
| CLAUDE.md | The rule is global, always relevant, and affects orchestration or safety for every task. | The content is long, domain-specific, or only useful for a subset of tasks. |
| Reference doc | The content is useful for maintainers but should not be loaded every session. | The rule must always be followed during execution. |

## Base Template Boundary

The base template may include:

- universal software engineering roles;
- universal architecture and quality practices;
- generic orchestration and safety rules;
- token/context economy guidance;
- documentation for maintaining the agent topology.

The base template should not include:

- ERP-specific skills;
- telecom-specific skills;
- vendor-specific workflows;
- company-specific deploy commands;
- product-specific terminology;
- integration behavior that only applies to one project type.

## Tool Permission Tiers

| Tier | Agents | Default tools | Reason |
| --- | --- | --- | --- |
| Review/planning | `software-architect`, `security-engineer`, `qa-engineer` | `Read`, `Glob`, `Grep`, `Bash`, `Skill` | Inspect, test, review, and recommend without directly editing files. |
| Implementation | `backend-specialist`, `frontend-specialist`, `devops-engineer` | Read/search, shell, edit/write, and skills | Apply scoped changes after planning and delegation. |

If a review/planning agent must edit files, route the implementation to an executor agent or explicitly change the agent for that project adaptation.

## Skill Authoring Standard

A reusable skill should stay focused and should normally include:

```txt
---
name: short-kebab-name
description: Specific trigger phrase explaining when Claude should use this skill.
---

# Skill Name

## Purpose
## Use When
## Do Not Use When
## Workflow
## Expected Output
```

Guidelines:

- Keep the `description` specific because it drives automatic invocation.
- Keep `SKILL.md` as the spine of the workflow, not a large manual.
- Move long examples, templates, and references into supporting files when needed.
- Prefer one clear responsibility per skill.
- Do not preload a skill in an agent unless the agent needs it on most runs.

## Change Checklist

Before merging changes to the multi-agent template, verify:

```txt
- Does this belong in the generic template, not a project clone?
- Does the change increase always-loaded context?
- Does any agent preload more than one primary skill?
- Is a new agent truly a recurring role instead of a skill?
- Is a new skill reusable across multiple project types?
- Are tool permissions no broader than the agent needs?
- Are project-specific examples avoided or clearly marked as examples?
- Are validation and rollback notes documented in the PR?
```
