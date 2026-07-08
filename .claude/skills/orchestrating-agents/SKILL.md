---
name: orchestrating-agents
description: Orchestrates specialized agents through issue-first planning, safe permission gates, task decomposition, delegation, PR-based implementation, documentation requirements, review gates, and continuity across sessions. Use when receiving any user task, planning multi-agent work, creating issues, delegating to specialists, handling sensitive access, or coordinating pull requests.
---

# Orchestrating Agents

Use this skill when receiving, planning, delegating, coordinating, reviewing, or completing any development task with specialized agents.

The orchestrator must understand the request, preserve context in GitHub issues, ask for permission before sensitive access, delegate deliberately, and require evidence before merge/release decisions.

## Core rule

Do not execute before planning.

Every task must become traceable through GitHub issues and pull requests.

```txt
User request -> clarify/plan -> create or update issue -> delegate agents -> implement in branch -> open PR -> review/QA/security as needed -> document outcome
```

## Task intake

For every user request, identify:

```txt
Request summary:
Target repository/project:
Task type:
Risk level:
Sensitive access needed:
Production impact:
Required agents:
Issue strategy:
PR strategy:
Open questions:
```

If the request is unclear, ask only questions that materially affect scope, safety, or architecture.

## Mandatory GitHub issue rule

Every task must be represented by a GitHub issue before implementation.

Use an existing issue only if it clearly matches the task. Otherwise create a new issue.

The issue must contain:

```txt
Goal:
Context:
Scope:
Out of scope:
Acceptance criteria:
Agent plan:
Sensitive access needs:
Risks:
Validation plan:
Continuity notes:
```

For complex tasks, create one parent issue plus smaller child issues or task checklist items.

The issue exists so the work can continue in another chat/session if credits or context run out.

## Planning before delegation

Before delegating, produce a concise plan:

```txt
What will be done:
Why:
Agents needed:
Order of execution:
Files/areas likely affected:
Risks:
Permission gates:
Expected PR outcome:
```

Use `software-architect` for planning when architecture, modules, service boundaries, data ownership, or major trade-offs are involved.

Use `devops-engineer` for planning when infrastructure, production, deploy, proxy, DNS, TLS, volumes, backups, or platform operations are involved.

Use `security-engineer` before implementation when the task touches auth, permissions, secrets, sensitive data, public APIs, webhooks, CORS, headers, deploy, or production access.

## Sensitive access permission gate

Before reading, modifying, exposing, or using sensitive resources, ask the user for explicit permission.

Sensitive resources include:

```txt
- .env files;
- private keys;
- API tokens;
- passwords;
- production credentials;
- production databases;
- customer/personal data;
- billing/payment data;
- production logs that may contain secrets;
- SSH keys;
- certificate private keys;
- automation/integration platform credentials and encryption keys;
- cloud provider credentials;
- deploy secrets;
- GitHub secrets;
- destructive production operations.
```

Permission request must specify:

```txt
Resource needed:
Why it is needed:
Exact access requested:
Read or write:
Risk:
Safer alternative:
```

If permission is denied or absent, use a safer alternative such as code/config review, placeholder examples, redacted logs, staging, or documented manual steps.

## Delegation matrix

Default agents:

```txt
software-architect:
Architecture, modules, system design, trade-offs, migration design.

frontend-specialist:
UI, UX, responsive layout, visual hierarchy, interface copy, design system.

backend-specialist:
API, services, business rules, database access, validation, webhooks, jobs.

security-engineer:
Auth, authorization, secrets, sensitive data, API exposure, CORS, headers, security review.

qa-engineer:
Acceptance criteria, tests, GitHub Actions, CI diagnosis, release/merge evidence.

devops-engineer:
Infrastructure, containers, automation platforms, proxy, deploy, volumes, logs, backups, production operations.
```

Do not involve every agent by default. Use the smallest useful team.

## PR rule

All code changes must be committed through a branch and pull request.

A PR must include:

```txt
Linked issue:
Summary:
Scope:
Files changed:
Validation:
Screenshots/logs when relevant:
Risk notes:
Rollback notes:
Follow-up work:
```

Do not push directly to the default branch unless the user explicitly instructs and understands the risk.

## Documentation rule

Code must be maintainable, scalable, and easy to change later.

Document:

```txt
- why the change exists;
- important architecture decisions;
- environment variables;
- commands needed to run/test/deploy;
- API contract changes;
- database/migration notes;
- operational runbooks for infrastructure and automation platforms;
- non-obvious business rules.
```

Do not over-document obvious code. Document decisions, boundaries, and operational knowledge.

## Completion rule

A task is complete only when the orchestrator can report:

```txt
Issue:
Branch:
PR:
Agents used:
What changed:
Validation evidence:
Risks remaining:
Documentation updated:
Next steps:
```

## References

- Delegation matrix: `references/delegation-matrix.md`
- Sensitive access policy: `references/sensitive-access-policy.md`
- Orchestration plan example: `examples/orchestration-plan.md`
