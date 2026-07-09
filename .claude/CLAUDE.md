# Master Agent Orchestrator

This file is the always-loaded orchestration kernel. Keep it short. Detailed behavior lives in skills and agents.

## Core flow

For every task:

```txt
Understand -> plan -> create/update issue -> delegate agents -> branch -> PR -> validate -> document outcome
```

Use `orchestrating-agents` for full intake, issue strategy, delegation, permission gates, PR flow, and continuity notes.

Use `smart-dispatch` for model/task routing and choosing the smallest useful agent team.

Use `tlc-spec-driven` when a feature needs spec-driven planning, requirement traceability, task breakdown, atomic implementation, UAT, independent verification, or `.specs/` continuity. It is an on-demand delivery workflow, not a replacement for `orchestrating-agents`.

Use architecture practice skills only when the task touches that practice:

```txt
ddd-modeling -> domain language, bounded contexts, aggregates, invariants
clean-architecture -> layer boundaries and dependency direction
hexagonal-architecture -> ports, adapters, gateways, external integrations
cqrs -> command/query separation, read/write flows, idempotent commands
code-quality -> maintainability, naming, cohesion, error handling
security-by-design -> auth, permissions, secrets, validation, sensitive data
testing-strategy -> domain/use-case/adapter/regression test planning
```

Do not preload every practice skill by default. Agents should preload only their primary operational skill and invoke extra skills on demand. Project-specific skills can be added later for a product domain, platform, vendor, or integration style.

Use `.claude/template-usage.md` when cloning or adapting this template into a real project.
Use `.claude/agent-skill-governance.md` when changing the template's agent topology, tool permissions, skill policy, or project adaptation rules.

## Non-negotiable rules

```txt
- Do not execute before planning.
- Every task must be represented by a GitHub issue before implementation.
- Code changes must go through a branch and pull request.
- Ask permission before accessing secrets, production, customer data, private keys, automation platform credentials, GitHub secrets, or destructive operations.
- Prefer read-only inspection before production changes.
- Validate with evidence before marking work complete.
- Document decisions, operational knowledge, API/data changes, and non-obvious behavior.
```

## Required planning shape

```txt
Task summary:
Assumptions:
Open questions:
Risk level:
Agents needed:
Execution order:
Issue/branch/PR plan:
Validation plan:
Permission gates:
```

Ask only questions that materially affect scope, safety, architecture, data, production, or implementation.

## Agent routing

```txt
software-architect -> architecture, DDD, Clean/Hexagonal/CQRS, trade-offs, modules, migrations
frontend-specialist -> UI, UX, responsive layout, design system, interface copy
backend-specialist -> APIs, services, validation, persistence, jobs, integrations, Clean/Hexagonal/CQRS implementation
security-engineer -> auth, permissions, secrets, sensitive data, public APIs, CORS, headers, security-by-design
qa-engineer -> tests, acceptance criteria, GitHub Actions, CI, merge/release evidence, testing strategy
devops-engineer -> infrastructure, cloud/VPS/bare metal, containers, CI/CD, networking, DNS/TLS, observability, backups, production ops
```

Use the smallest useful set of agents. Add reviewers when risk requires them.

## Sensitive access gate

Before sensitive access, ask with this format:

```txt
Resource:
Reason:
Access type: read / write / execute
Environment:
Risk:
Safer alternative:
Exact action if approved:
```

If permission is not granted, use safer alternatives: redacted logs, `.env.example`, staging, code review, placeholders, or manual commands for the user to run.

## Completion report

```txt
Issue:
Branch:
PR:
Agents used:
Skills used:
What changed:
Validation evidence:
Documentation updated:
Risks remaining:
Next steps:
```
