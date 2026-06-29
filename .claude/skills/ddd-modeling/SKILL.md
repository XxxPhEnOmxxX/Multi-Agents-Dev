---
name: ddd-modeling
description: Use this skill when discovering domain concepts, defining bounded contexts, modeling entities, value objects, aggregates, domain services, domain events, and ubiquitous language.
---

# DDD Modeling

## Purpose

Model software from the business domain before choosing technical structures.

Use this skill when the task touches:

- domain language;
- bounded contexts;
- entities and value objects;
- aggregates;
- domain services;
- domain events;
- business invariants;
- context mapping between modules.

## Workflow

1. Identify the business capability being changed.
2. Name the bounded context affected by the change.
3. Define the ubiquitous language for this area.
4. Separate domain concepts from external system concepts.
5. Decide whether behavior belongs in an entity, value object, aggregate, domain service, or application use case.
6. Identify invariants that must always hold.
7. Identify domain events that represent important business facts.
8. Keep persistence, HTTP, UI, and external payload details outside the model.

## Modeling Rules

- Use domain names, not database, UI, or vendor names.
- An entity has identity and lifecycle.
- A value object is defined by its attributes and should be immutable when practical.
- An aggregate protects consistency boundaries.
- A domain service exists only when behavior does not naturally belong to one entity or value object.
- A domain event describes something that already happened in the business.

## ISP Field-Service Examples

- `WorkOrder` is an entity.
- `Address` is a value object.
- `OpticalSignal` is a value object.
- `FieldVisit` can be an aggregate when it owns checklist, evidence, signature, and completion rules.
- `WorkOrderCompleted` is a domain event.
- `ErpTicketPayload` is not a domain concept.

## Expected Output

- Bounded context identified.
- Domain concepts named.
- Invariants listed.
- Aggregate boundary suggested.
- External concepts isolated from the domain.
