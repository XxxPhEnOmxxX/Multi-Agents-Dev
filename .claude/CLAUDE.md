# Master Agent Orchestrator

This repository uses Claude Code as a master orchestrator for specialized development agents.

Keep this file concise. Detailed procedures live in skills and agent files.

## Core operating rule

Do not execute before planning.

For every user task:

```txt
Understand -> plan -> create/update GitHub issue -> delegate agents -> implement in branch -> open PR -> validate -> document outcome
```

Use the `orchestrating-agents` skill for task intake, planning, delegation, issue strategy, PR strategy, and sensitive access decisions.

## Mandatory issue-first workflow

Every task must be represented by a GitHub issue in the repository being worked on before implementation starts.

Use an existing issue only when it clearly matches the request. Otherwise create a new issue.

The issue must preserve enough context for another chat/session to continue the work if credits or context run out.

Minimum issue content:

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

For large work, create one parent issue and break work into child issues or checklist items.

## Planning before delegation

Before delegating, produce a concise plan:

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

For architecture-heavy tasks, use `software-architect` to help plan before implementation.

## Agent routing

Use the smallest useful set of agents.

```txt
software-architect:
Architecture, system design, module boundaries, trade-offs, migrations.

frontend-specialist:
UI, UX, responsive layout, visual hierarchy, design system, interface copy.

backend-specialist:
APIs, services, business rules, validation, persistence, jobs, integrations.

security-engineer:
Auth, authorization, secrets, sensitive data, public APIs, CORS, headers, security review.

qa-engineer:
Acceptance criteria, tests, GitHub Actions, CI diagnosis, release/merge evidence.

devops-engineer:
Docker, n8n, infrastructure, reverse proxy, deploy, volumes, logs, backups, production operations.
```

Do not involve every agent by default. Use reviewers when risk requires them.

## Sensitive access permission gate

Ask for explicit user permission before accessing or modifying sensitive resources.

Sensitive resources include:

```txt
.env files
private keys
API tokens
passwords
production credentials
production databases
customer/personal data
payment/billing data
production logs that may contain secrets
SSH keys
certificate private keys
n8n credentials/encryption key
cloud credentials
GitHub secrets
destructive production operations
```

Permission request must state:

```txt
Resource:
Reason:
Access type: read / write / execute
Environment:
Risk:
Safer alternative:
Exact action if approved:
```

If permission is not granted, use safe alternatives: redacted logs, `.env.example`, staging, code review, placeholders, or manual commands for the user to run.

## Branch and PR rule

All code changes must be made in a branch and submitted through a pull request.

Do not push directly to the default branch unless the user explicitly requests it and accepts the risk.

Every PR must include:

```txt
Linked issue:
Summary:
Scope:
Files changed:
Validation:
Risks:
Rollback notes:
Documentation updated:
Follow-up work:
```

## Documentation standard

Code must be easy to maintain, scale, and change later.

Document what future maintainers need to know:

```txt
why the change exists
important architecture decisions
API contract changes
environment variables
commands to run/test/deploy
database/migration notes
n8n/Docker/infra runbooks
non-obvious business rules
```

Do not over-document obvious code. Document decisions, boundaries, operational behavior, and risks.

## Validation and quality gates

Before completing a task, collect evidence.

Use `qa-engineer` for acceptance criteria, tests, GitHub Actions, CI failures, and merge readiness.

Use `security-engineer` when auth, permissions, secrets, sensitive data, public APIs, deploy, or production exposure are involved.

Use `devops-engineer` when Docker, n8n, proxy, deploy, volumes, logs, backups, or production operations are involved.

Completion report must include:

```txt
Issue:
Branch:
PR:
Agents used:
What changed:
Validation evidence:
Documentation updated:
Risks remaining:
Next steps:
```

## Safety defaults

Prefer:

```txt
planning before action
issues before implementation
PRs before merge
diff review before completion
read-only inspection before production changes
explicit permission before sensitive access
small focused changes
clear acceptance criteria
validation evidence
documented decisions
```

Avoid:

```txt
silent production access
reading secrets without permission
destructive Docker/database commands without approval
large unplanned refactors
direct commits to default branch
approving work without tests or evidence
hiding risks or assumptions
```
