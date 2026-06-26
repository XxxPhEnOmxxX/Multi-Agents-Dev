---
name: building-backend-apis
description: Designs, implements, reviews, and hardens backend APIs, services, database access, validation, domain rules, transactions, integrations, errors, logging, performance, and test strategy. Use when building or changing backend code, API contracts, persistence, business logic, background jobs, or server-side architecture.
---

# Building Backend APIs

Use this skill when the task involves backend implementation, API design, services, repositories/models, database access, validation, authentication/authorization integration, background jobs, webhooks, or server-side behavior.

The backend specialist must protect correctness, data integrity, maintainability, and clear contracts.

## Core rule

Backend code must make the system truthful and reliable.

Do not hide business rules in the frontend. Do not trust client input. Do not change API contracts or database behavior without understanding impact.

## Backend workflow

### 1. Understand the behavior

Before changing backend code, identify:

```txt
Feature/bugfix:
User or system actor:
Expected behavior:
Current behavior:
Business rule:
Affected API/route/job:
Affected data:
Risk level:
```

If the behavior is ambiguous, ask only the questions that change implementation.

### 2. Identify boundaries

Map where the change belongs:

```txt
Controller/route:
Request parsing and response shape.

Service/use case:
Business rules and orchestration.

Repository/model/query:
Persistence and data access.

DTO/schema/validator:
Input and output validation.

Job/worker:
Async work and retries.

Integration adapter:
External API, webhook, provider, or service boundary.
```

Do not create layers that the project does not use. Follow the existing architecture unless there is a clear reason to adjust it.

### 3. Preserve API contracts

Before changing a route or response, check:

```txt
- HTTP method;
- route path;
- request body/query/params;
- response status;
- response JSON shape;
- error shape;
- authentication requirements;
- authorization rules;
- frontend/client usage;
- backward compatibility.
```

If a public contract must change, document the change and migration path.

### 4. Validate input server-side

Backend must validate:

```txt
- required fields;
- types;
- string length;
- numeric ranges;
- enum/status values;
- date/time format;
- ownership IDs;
- file size/type when applicable;
- unexpected fields when relevant.
```

Client-side validation improves UX, but server-side validation is the source of truth.

### 5. Protect authorization and ownership

For protected resources, verify:

```txt
- user is authenticated;
- role has permission;
- user owns or can access the target object;
- admin-only actions are server-enforced;
- hidden frontend controls are not treated as security;
- tests cover negative permission paths when risk is meaningful.
```

Use the security engineer for sensitive auth, permissions, tokens, customer data, or public API exposure.

### 6. Handle persistence carefully

When changing database behavior, check:

```txt
- schema impact;
- migration requirement;
- indexes and constraints;
- transactions for dependent writes;
- uniqueness and race conditions;
- soft delete vs hard delete;
- audit/history needs;
- rollback or mitigation.
```

Never create destructive migrations without explicit approval and rollback/backup thinking.

### 7. Return useful errors

Errors should be consistent and safe.

Prefer:

```txt
- predictable status codes;
- user-safe messages;
- machine-readable codes when the project uses them;
- no stack traces in production responses;
- validation errors tied to fields when useful;
- logs with request correlation when available.
```

Avoid leaking internals, SQL errors, secrets, tokens, or sensitive data.

### 8. Add observability where useful

For important backend flows, consider:

```txt
- structured logs;
- request IDs/correlation IDs;
- audit logs for admin/security actions;
- metrics for jobs and integrations;
- clear error context without sensitive data;
- retry/dead-letter visibility for async work.
```

### 9. Validate the change

Choose validation proportional to risk:

```txt
- unit tests for business logic;
- integration tests for API + database behavior;
- contract tests when clients depend on response shape;
- smoke tests for critical routes;
- migration validation when database changes exist;
- lint/build/typecheck when available.
```

Do not claim success without evidence.

## Implementation principles

Prefer:

```txt
- small, focused changes;
- existing project patterns;
- explicit business rules;
- clear API contracts;
- server-side validation;
- safe database writes;
- readable errors;
- tests for risky behavior;
- simple code over speculative abstractions.
```

Avoid:

```txt
- drive-by refactors;
- generic services for one use case;
- changing contracts silently;
- trusting frontend validation;
- mixing feature, refactor, migration, and cleanup in one change;
- adding dependencies without justification;
- swallowing errors without logs;
- creating background jobs without idempotency thinking.
```

## Output format: starting backend work

```txt
Backend scope:
Behavior to implement/fix:
Affected routes/services/data:
Business rules:
Validation rules:
Auth/permission impact:
Database impact:
Risk level:
Planned checks:
```

## Output format: backend review

```txt
Backend review result:
API contract impact:
Data integrity impact:
Auth/authorization impact:
Error handling:
Tests/validation:
Risks:
Recommended changes:
```

## References

- Backend checklist: `references/backend-checklist.md`
- Data access and migrations: `references/data-access-and-migrations.md`
- Backend feature example: `examples/backend-feature-plan.md`
