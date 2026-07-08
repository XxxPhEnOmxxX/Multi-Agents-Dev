# Example: Orchestration Plan

Use this example as a shape for planning multi-agent work.

## User request

```txt
Add a customer dashboard with backend API, frontend screen, tests, and deploy configuration.
```

## Orchestrator intake

```txt
Request summary:
Add a customer dashboard spanning backend, frontend, tests, and deployment.

Target repository/project:
Current working repository.

Task type:
Full-stack feature.

Risk level:
Medium/high because it touches API, UI, data, tests, and deploy.

Sensitive access needed:
No secrets needed initially. Production access not approved.

Production impact:
Possible, but production deploy is out of scope until explicit approval.

Required agents:
- software-architect for boundaries and plan;
- backend-specialist for API/data;
- frontend-specialist for dashboard UI;
- qa-engineer for tests and GitHub Actions;
- devops-engineer if deploy config changes are required;
- security-engineer if customer data/auth is involved.

Issue strategy:
Create parent issue with acceptance criteria and child task checklist.

PR strategy:
Create feature branch and PR linked to issue.
```

## Issue body

```txt
Goal:
Create a customer dashboard with backend data, frontend UI, tests, and deploy readiness.

Context:
The dashboard should help users view customer status and key operational information.

Scope:
- Backend endpoint for dashboard data.
- Frontend dashboard page.
- Validation/tests.
- Infrastructure/deploy review if needed.

Out of scope:
- Production deploy without explicit approval.
- Reading production secrets.
- Large architecture rewrite.

Acceptance criteria:
- API returns expected dashboard data for authorized user.
- UI renders loading, empty, error, and populated states.
- Unauthorized user cannot access protected data.
- Tests/checks pass locally or in GitHub Actions.
- PR documents validation and risks.

Agent plan:
1. software-architect defines module/data boundaries.
2. backend-specialist implements API.
3. frontend-specialist implements UI.
4. security-engineer reviews auth/data exposure.
5. qa-engineer validates tests/CI.
6. devops-engineer reviews infrastructure only if deploy config changes.

Sensitive access needs:
None initially.

Risks:
Customer data exposure, API contract mismatch, insufficient tests.

Validation plan:
Run lint/build/test and inspect GitHub Actions.

Continuity notes:
If context is lost, resume from this issue and linked PR.
```

## Final report shape

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
