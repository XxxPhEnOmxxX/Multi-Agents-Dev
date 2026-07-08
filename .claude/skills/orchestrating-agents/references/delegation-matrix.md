# Agent Delegation Matrix

Use this matrix to decide which specialist agents to involve.

Do not spawn every agent by default. Use the smallest useful team.

## Default routing

| Task area | Primary agent | Review agents |
|---|---|---|
| Architecture, module boundaries, system design | software-architect | security-engineer, devops-engineer, qa-engineer |
| UI, UX, responsive frontend, visual polish | frontend-specialist | qa-engineer, security-engineer when data/auth involved |
| API, services, business rules, persistence | backend-specialist | security-engineer, qa-engineer, software-architect when structural |
| Auth, permissions, secrets, sensitive data | security-engineer | backend-specialist, qa-engineer |
| Infrastructure, containers, proxy, deploy, automation platforms | devops-engineer | security-engineer, qa-engineer |
| Tests, GitHub Actions, release readiness | qa-engineer | backend/frontend/devops/security depending on failure |

## Risk-based escalation

Use additional reviewers when the task touches:

```txt
Auth/permissions -> security-engineer required
Database migration -> backend-specialist + qa-engineer; architect if structural
Production deploy -> devops-engineer + qa-engineer; security if public/sensitive
Public API/webhook -> backend-specialist + security-engineer + qa-engineer
Frontend with customer data -> frontend-specialist + security-engineer + qa-engineer
Automation platform credentials/workflows -> devops-engineer + security-engineer
Major refactor -> software-architect + qa-engineer
```

## Planning agent selection

Use `software-architect` to plan when:

```txt
- the task changes architecture;
- modules/services need to be split;
- data ownership is unclear;
- there are multiple implementation strategies;
- migration path matters.
```

Use `devops-engineer` to plan when:

```txt
- infrastructure, containers, proxy, TLS, production, volumes, backups, or deploy are involved;
- operational safety matters;
- rollback is needed.
```

Use `security-engineer` to plan when:

```txt
- secrets, auth, customer data, production, public API, webhook, CORS, headers, or permissions are involved.
```

Use `qa-engineer` to plan when:

```txt
- acceptance criteria are vague;
- GitHub Actions or CI is relevant;
- release/merge safety depends on evidence.
```

## Sequential vs parallel

Use sequential delegation when:

```txt
- one agent's output defines the next step;
- same files will be edited;
- task is small;
- production/sensitive access requires approval;
- architecture is unclear.
```

Use parallel delegation when:

```txt
- agents can investigate independent areas;
- frontend/backend/test work can be split cleanly;
- multiple reviewers can inspect one PR from different lenses;
- root cause has competing hypotheses.
```

## Anti-patterns

Avoid:

```txt
- involving every agent for a small change;
- letting agents edit the same files without coordination;
- delegating implementation before issue and plan exist;
- skipping security review for auth/secrets/data;
- skipping QA evidence before PR completion;
- making architecture decisions without explicit trade-offs.
```
