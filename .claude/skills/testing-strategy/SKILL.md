---
name: testing-strategy
description: Use this skill when designing or writing tests for domain rules, use cases, commands, queries, adapters, mappers, security checks, and regression coverage.
---

# Testing Strategy

## Purpose

Prove behavior with the narrowest useful test and increase coverage where risk is highest.

## Test Priority

1. Domain invariants.
2. Application use cases.
3. Command handlers.
4. Query handlers.
5. Mappers and error mappers.
6. Adapter contract behavior.
7. API/interface behavior.
8. End-to-end flows only for critical paths.

## Rules

- Do not mock the domain.
- Mock external systems behind ports.
- Test unsupported capabilities explicitly.
- Test failure paths, not only success paths.
- Keep fixtures small and meaningful.
- Use regression tests for fixed bugs.
- Prefer deterministic tests over timing-dependent tests.

## CQRS Test Guidance

- Commands: success, validation failure, invariant failure, authorization failure, idempotent retry when applicable.
- Queries: shape, filters, permissions, empty state, pagination, sorting.

## Expected Output

- Test scope.
- Test cases.
- Required fixtures.
- Verification command.
- Remaining risk if full verification cannot run.
