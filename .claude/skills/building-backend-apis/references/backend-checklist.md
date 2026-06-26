# Backend Checklist

Use this checklist when implementing or reviewing backend changes.

## Scope

```txt
- What behavior is being added or fixed?
- Which route, service, job, or integration is affected?
- What is explicitly out of scope?
- What client/frontend depends on this behavior?
```

## API contract

```txt
- Route path is correct.
- HTTP method is correct.
- Request body/query/params are validated.
- Response status codes are predictable.
- Response JSON shape is stable or documented if changed.
- Error response shape is consistent.
- Pagination, sorting, and filtering are bounded when relevant.
- Public API changes have migration notes.
```

## Validation

```txt
- Required fields are enforced server-side.
- Types and formats are validated.
- String lengths and numeric ranges are bounded.
- Enum/status values are restricted.
- Unexpected fields are handled intentionally.
- IDs are validated before use.
- File upload rules are enforced when applicable.
```

## Authentication and authorization

```txt
- Route requires authentication when needed.
- Role checks are server-side.
- Object ownership is checked for ID-based resources.
- Admin-only actions cannot be performed by normal users.
- Negative authorization tests exist for risky paths.
- Security-sensitive changes involve security-engineer review.
```

## Business rules

```txt
- Rule is implemented in backend, not only frontend.
- Edge cases are handled.
- Invalid state transitions are blocked.
- Idempotency is considered for retries/webhooks/jobs.
- Time/date logic is explicit about timezone when relevant.
```

## Persistence

```txt
- Query is safe and parameterized/ORM-backed.
- Transaction is used when multiple dependent writes happen.
- Unique constraints or indexes support important invariants.
- Migration is needed and included when schema changes.
- Destructive migration has explicit approval and rollback thinking.
- Data integrity is preserved on failures.
```

## Error handling

```txt
- User-facing errors are safe and useful.
- Internal errors are logged without leaking secrets.
- Production responses do not expose stack traces.
- External integration failures have fallback/retry behavior when needed.
- Background job failures are observable.
```

## Performance

```txt
- No obvious N+1 query introduced.
- List endpoints have limits/pagination.
- Heavy work is not done synchronously unless justified.
- External API calls have timeout/retry policy when relevant.
- Indexes support new query patterns.
```

## Tests

```txt
- Unit tests cover important business logic.
- Integration tests cover API + persistence when risk is meaningful.
- Negative tests cover invalid input and authorization denial.
- Regression test exists for bugfix.
- Existing tests still pass.
```

## Release readiness

```txt
- API changes documented when needed.
- Migration plan exists when needed.
- Rollback/mitigation is clear for risky changes.
- Logs/observability are enough to debug production issues.
- QA validation is available for merge/release decision.
```
