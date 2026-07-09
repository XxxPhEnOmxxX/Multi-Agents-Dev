# Multi-Agent Development Guides

## Purpose

This directory contains on-demand guides for using the multi-agent template as both:

- a software delivery system;
- a learning system for software engineering practice.

These guides are intentionally **not imported by `.claude/CLAUDE.md`**. They should be read only when the current session needs them.

This protects token budget and context-window quality.

---

## Available Guides

| Guide | Use When |
| --- | --- |
| `project-from-zero.md` | Starting a new software project from a raw idea and turning it into architecture, roadmap, specs, and implementation plan. |
| `feature-planning.md` | Planning one feature before implementation by defining spec, design, tasks, validation gates, and handoff. |

---

## Relationship With Existing Files

| File / Area | Responsibility |
| --- | --- |
| `.claude/CLAUDE.md` | Always-loaded orchestration kernel. Keep short. |
| `.claude/prompts/bootstrap.md` | Session bootstrap policy for Claude Code, Codex, or other implementation models. |
| `.claude/guides/project-from-zero.md` | Project inception guide used before coding a new project. |
| `.claude/guides/feature-planning.md` | Feature planning guide used before implementing a feature. |
| `.claude/skills/tlc-spec-driven/` | Spec-driven workflow for specification, design, tasks, execution, and verification. |
| `.claude/skills/orchestrating-agents/` | Issue, branch, PR, delegation, permission gates, and completion reporting. |

---

## Usage Rule

Use guides only when needed.

Do not preload all guides into every session.

Use this order:

```txt
new session -> bootstrap.md
new project -> project-from-zero.md
new feature -> feature-planning.md
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
