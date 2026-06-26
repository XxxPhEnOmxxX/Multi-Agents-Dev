# QA Strategy Reference

Use this reference to decide what to test and how much validation is enough.

## Test levels

```txt
Static checks:
Lint, typecheck, formatting, schema validation.

Unit tests:
Small logic, pure functions, services, validators.

Integration tests:
API + database, service interaction, external adapters with mocks.

End-to-end tests:
User workflows through UI or API.

Smoke tests:
Fast verification that the main flow still works.

Regression tests:
Tests for previously broken behavior.
```

## Validation by change type

### Documentation or text-only change

```txt
- Review clarity.
- Check links/commands if applicable.
- No full test suite required unless docs include executable examples.
```

### Frontend UI change

```txt
- Lint/build/typecheck.
- Visual inspection.
- Responsive check for impacted breakpoints.
- Basic accessibility check.
- Loading/empty/error/success states when relevant.
- E2E or smoke test for critical user flow.
```

### Backend/API change

```txt
- Unit or integration tests for changed behavior.
- API contract check.
- Error handling check.
- Auth/authorization check if relevant.
- Migration check if database changes exist.
```

### Database change

```txt
- Migration applies cleanly.
- Rollback or mitigation exists.
- Data integrity is preserved.
- Indexes/constraints match expected query patterns.
- Backward compatibility considered when deploy is staged.
```

### Auth/security-sensitive change

```txt
- Security engineer review required.
- Positive and negative auth tests.
- Role/permission boundary tests.
- Session/token/cookie behavior check.
- No sensitive data in logs or frontend.
```

### Docker/deploy change

```txt
- docker compose config or equivalent validation.
- Healthcheck behavior.
- Exposed ports reviewed.
- Environment/secrets handling reviewed.
- Rollback path documented.
```

## Acceptance criteria mapping

Every important acceptance criterion should map to evidence:

```txt
Criterion:
Validation method:
Evidence:
Status:
```

Bad:

```txt
Looks good.
Tests passed.
```

Good:

```txt
Criterion: unauthenticated users cannot access /admin
Validation method: smoke test with no session
Evidence: API returned 401 and UI redirected to login
Status: passed
```

## Risk-based testing

Increase validation when the change touches:

```txt
- authentication;
- authorization;
- payments/billing;
- customer data;
- public API;
- deployment;
- database migration;
- background jobs;
- queue/webhook behavior;
- high-traffic workflows;
- shared components used in many screens.
```

Reduce validation when:

```txt
- change is documentation-only;
- change is isolated and low risk;
- no runtime behavior changed;
- existing CI already covers the affected area.
```

## QA decision guide

```txt
Pass:
Required evidence exists and risk is acceptable.

Pass with notes:
Core criteria passed, but non-blocking limitations remain.

Blocked:
Critical evidence is missing or required checks failed.

Needs investigation:
Failure exists but cause is unclear.
```
