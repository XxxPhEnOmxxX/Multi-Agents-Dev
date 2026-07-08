---
name: clean-architecture
description: Use this skill when organizing code by layers, enforcing dependency direction, deciding where business rules belong, or reviewing whether a change respects Clean Architecture.
---

# Clean Architecture

## Purpose

Protect business rules from frameworks, databases, UI, queues, HTTP clients, and external systems.

## Layer Responsibilities

- Domain: entities, value objects, domain services, domain events, invariants.
- Application: use cases, commands, queries, ports, transaction boundaries, orchestration.
- Interface: controllers, API routes, presenters, request validation, serializers.
- Infrastructure: database, ORM, external APIs, external system adapters, queues, storage, email, telemetry.

## Dependency Rule

Inner layers must not depend on outer layers.

```txt
Interface -> Application -> Domain
Infrastructure -> Application ports
Domain -> no outer layer
```

## Workflow

1. Identify the business rule or behavior.
2. Place invariants in the domain.
3. Place orchestration in the application layer.
4. Place transport concerns in the interface layer.
5. Place external system implementation in infrastructure.
6. Depend on abstractions at boundaries.
7. Verify imports follow the dependency rule.

## Review Checklist

- Domain imports no framework, ORM, HTTP, queue, or external system code.
- Use cases depend on ports, not concrete adapters.
- Controllers do not contain business rules.
- Infrastructure implements application ports.
- DTOs do not replace domain models.
- Tests can exercise domain rules without external services.

## Expected Output

- Layer placement decision.
- Dependency risks.
- Recommended file/module location.
- Tests needed to protect the boundary.
