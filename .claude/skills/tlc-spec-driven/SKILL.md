---
name: tlc-spec-driven
description: Spec-driven feature delivery workflow for Claude Code. Use when planning, designing, breaking down, implementing, validating, verifying, pausing, or resuming a feature that needs traceable requirements, atomic tasks, test gates, PR evidence, or UAT. Do not use as a replacement for the main orchestrator, architecture decomposition skills, or project-specific technical design docs.
license: CC-BY-4.0
metadata:
  source: https://github.com/tech-leads-club/agent-skills/tree/main/packages/skills-catalog/skills/(development)/tlc-spec-driven
  adapted_for: Multi-Agents-Dev template
  author_attribution: Felipe Rodrigues - github.com/felipfr
  version: 3.2.0-adapted
---

# TLC Spec-Driven Development

Plan and deliver features through an adaptive flow:

```txt
Specify -> Design -> Tasks -> Execute -> Verify
```

This skill is intentionally **on demand**. It must not be preloaded by every agent and must not bloat `.claude/CLAUDE.md`.

## Position in this template

The global orchestrator still owns issue, branch, PR, permission gates, agent routing, and completion reporting.

Use this skill **inside** that orchestration flow when the work needs feature-level discipline:

```txt
orchestrating-agents
  -> smart-dispatch
    -> tlc-spec-driven
      -> specialist agents as needed
```

## Critical rules

1. Specify what must be built before implementation.
2. Tests derive from acceptance criteria, not from the current implementation.
3. A task is not done until its gate passes.
4. Use one atomic commit per task whenever implementation occurs.
5. The final feature validation must be independent from the author of the implementation.
6. Never weaken, skip, or delete tests to force a pass.
7. Keep `.specs/STATE.md` writes section-scoped.
8. Keep this skill stack-agnostic and project-neutral.

## Auto-sizing

| Scope | Use |
| --- | --- |
| Small | Inline one-liner spec, inline atomic steps, execute and verify. |
| Medium | Brief spec, inline design, implicit tasks, execute with evidence. |
| Large | Full spec, design, tasks, test matrix, execute task-by-task. |
| Complex | Full spec, gray-area discussion, design research, phased tasks, validation/UAT. |

Specify and Execute are always required. Design and Tasks are included only when the scope justifies them.

## `.specs/` structure

```txt
.specs/
  STATE.md
  LESSONS.md
  lessons.json
  features/
    [feature]/
      spec.md
      context.md
      design.md
      tasks.md
      validation.md
```

## References

Read the reference file completely before acting on that phase:

| Trigger | Reference |
| --- | --- |
| specify feature, define requirements | `references/specify.md` |
| discuss feature, gray areas | `references/discuss.md` |
| design feature, architecture | `references/design.md` |
| break into tasks | `references/tasks.md` |
| implement, execute | `references/implement.md` |
| validate, verify, UAT | `references/validate.md` |
| record decision, pause, resume | `references/memory.md` |
| load or record lessons | `references/lessons.md` |
| sub-agent batching and Verifier | `references/sub-agents.md` |
| coding behavior | `references/coding-principles.md` |
| context budget | `references/context-limits.md` |
| code search | `references/code-analysis.md` |

## Knowledge verification chain

When a technical decision is needed, use this order:

```txt
Codebase -> Project docs -> Context7 MCP -> Web/official docs -> Flag uncertainty
```

Never fabricate APIs, commands, project conventions, or library behavior.

## Output contract

When this skill is used, report:

```txt
Feature:
Scope size:
Spec artifacts:
Design artifacts:
Task artifacts:
Agents used:
Gates run:
Validation evidence:
Remaining risks:
Next step:
```
