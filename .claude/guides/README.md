# Multi-Agent Development Guides

## Purpose

This directory contains short, on-demand guide spines for using the multi-agent template as both:

- a software delivery system;
- a learning system for software engineering practice.

Detailed fill-in documents live in `.claude/templates/`.

These guides are intentionally **not imported by `.claude/CLAUDE.md`**. They should be read only when the current session needs them.

This protects token budget and context-window quality.

---

## Available Guides

| Guide | Use When |
| --- | --- |
| `project-from-zero.md` | Starting a new software project from a raw idea and turning it into architecture, roadmap, specs, and implementation plan. |
| `feature-planning.md` | Planning one feature before implementation by defining spec, design, tasks, validation gates, and handoff. |

---

## Related Templates

| Template Directory | Use When |
| --- | --- |
| `.claude/templates/project/` | Creating `.specs/` foundation files for a new project. |
| `.claude/templates/feature/` | Creating `context.md`, `spec.md`, `design.md`, `tasks.md`, and `validation.md` for one feature. |

Open only the template needed for the current step. Do not load every template by default.

---

## Relationship With Existing Files

| File / Area | Responsibility |
| --- | --- |
| `.claude/CLAUDE.md` | Always-loaded orchestration kernel. Keep short. |
| `AGENTS.md` | Thin Codex-compatible entrypoint. Do not duplicate `.claude/` in full. |
| `.claude/prompts/bootstrap.md` | Session bootstrap policy for Claude Code, Codex, or other implementation models. |
| `.claude/guides/project-from-zero.md` | Project inception guide used before coding a new project. |
| `.claude/guides/feature-planning.md` | Feature planning guide used before implementing a feature. |
| `.claude/templates/` | Fill-in templates loaded only when needed. |
| `.claude/skills/tlc-spec-driven/` | Spec-driven workflow for specification, design, tasks, execution, and verification. |
| `.claude/skills/orchestrating-agents/` | Issue, branch, PR, delegation, permission gates, and completion reporting. |

---

## Usage Rule

Use guides only when needed.

Do not preload all guides or templates into every session.

Use this order:

```txt
new session -> bootstrap.md
Codex session -> AGENTS.md + bootstrap.md
new project -> project-from-zero.md + selected project templates
new feature -> feature-planning.md + selected feature templates
feature execution -> tlc-spec-driven + specialist agents
```

---

## Learning Rule

When the user is learning software development, agents should explain decisions briefly and practically.

Good learning explanations include:

```txt
Concept -> Why it matters -> Common mistake -> How this project applies it
```

Do not turn every implementation session into a long tutorial. Teach the concept only when it affects the current decision or task.
