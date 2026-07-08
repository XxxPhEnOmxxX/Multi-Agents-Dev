---
name: smart-dispatch
description: Routes development tasks to the smallest useful agent team and model class based on complexity, risk, and cost. Use when planning implementation, fixing bugs, delegating multi-agent work, choosing subagent models, or splitting work into architecture, implementation, QA, security, and DevOps tracks.
---

# Smart Dispatch

Use this skill to choose the right agent team and model class for a task.

The goal is to reduce token and compute waste without reducing quality or safety.

## Core rule

Use the cheapest and smallest setup that can do the task safely.

Do not use powerful models or many agents for mechanical work. Do not use cheap routing for high-risk reasoning.

## Model class routing

Use the model names supported by the local Claude Code environment. If exact model names differ, map them by capability class.

### Complex reasoning model

Use for:

```txt
- architecture planning;
- major trade-offs;
- ambiguous requirements;
- data ownership decisions;
- security-sensitive design;
- production migration planning;
- incident root-cause reasoning;
- multi-agent decomposition.
```

Typical agents:

```txt
software-architect
security-engineer
devops-engineer for production/infrastructure risk
```

### Standard implementation model

Use for:

```txt
- backend feature implementation;
- frontend implementation with real logic;
- API changes;
- integrations;
- refactoring with moderate reasoning;
- bug fixes with clear cause;
- test implementation that needs project understanding (backend-specialist or frontend-specialist).
```

Typical agents:

```txt
backend-specialist
frontend-specialist
qa-engineer for test strategy, acceptance criteria, CI diagnosis, and evidence validation (not test implementation)
```

### Fast mechanical model

Use for:

```txt
- boilerplate;
- repetitive docs;
- simple tests;
- examples/templates;
- formatting-only work;
- small copy changes;
- simple config scaffolding;
- converting an already-decided plan into files.
```

Typical agents:

```txt
backend-specialist or frontend-specialist for simple test scaffolding, with qa-engineer defining criteria and validating evidence
frontend-specialist for simple UI polish/copy
backend-specialist for simple DTO/schema boilerplate
```

## Agent count routing

### One agent

Use when:

```txt
- task is isolated;
- risk is low;
- one domain owns the change;
- no sensitive access is involved;
- no architecture decision is needed.
```

### Two to three agents

Use when:

```txt
- one agent implements and another reviews;
- backend/frontend plus QA is needed;
- security or DevOps risk is present;
- acceptance criteria need validation.
```

### Full team

Use only when:

```txt
- task is full-stack and high-impact;
- architecture, backend, frontend, security, QA, and DevOps all matter;
- production or sensitive data is involved;
- multiple PRs/issues are expected.
```

## Dispatch examples

### Small copy or docs change

```txt
Model class: fast mechanical
Agents: relevant single executor specialist
Issue: yes
PR: yes if repo changes
Review: lightweight
```

### Backend API feature

```txt
Model class: standard implementation
Agents: backend-specialist + qa-engineer
Add security-engineer if auth, permissions, public API, or sensitive data is involved.
```

### New system architecture

```txt
Model class: complex reasoning
Agents: software-architect first
Then delegate implementation agents after issue plan is accepted.
```

### Production infrastructure change

```txt
Model class: complex reasoning for planning, standard for config edit
Agents: devops-engineer + security-engineer + qa-engineer
Permission gate: required before production/secrets/destructive action
```

### Full-stack feature

```txt
1. complex reasoning -> software-architect plans boundaries
2. standard implementation -> backend-specialist implements API/data
3. standard implementation -> frontend-specialist implements UI
4. standard/fast -> qa-engineer validates tests and CI
5. security-engineer reviews if auth/data/public API involved
6. devops-engineer reviews if infrastructure/deploy changes exist
```

## Cost control checklist

Before delegating, ask:

```txt
Can one agent do this?
Is architecture actually needed?
Is security review required by risk or only habit?
Can QA validate with existing CI?
Can details live in a skill instead of CLAUDE.md?
Can repetitive work use a fast model class?
```

## Output format

```txt
Dispatch decision:
Task complexity:
Risk level:
Agents selected:
Model class per agent:
Why this is enough:
What would trigger escalation:
```
