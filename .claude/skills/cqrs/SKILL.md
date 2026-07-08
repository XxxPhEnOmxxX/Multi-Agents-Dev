---
name: cqrs
description: Use this skill when separating commands from queries, creating command/query handlers, modeling write and read flows, or designing idempotent offline sync operations.
---

# CQRS

## Purpose

Separate state-changing operations from read-only operations so each side can be designed clearly.

## Decision Rule

- Command: changes state or triggers a side effect.
- Query: reads data and must not change state.

## Command Workflow

1. Name the command with an imperative business action.
2. Validate input at the boundary.
3. Load required state.
4. Execute domain behavior or application orchestration.
5. Persist the result through a port.
6. Emit domain or integration events when appropriate.
7. Return only what the caller needs.

## Query Workflow

1. Define the read model needed by the screen or API.
2. Apply authorization and filters.
3. Avoid side effects.
4. Shape data for the consumer without exposing internal write models unnecessarily.
5. Add pagination and sorting explicitly when needed.

## Offline Sync Rules

- Retryable commands should be idempotent.
- Commands should carry stable operation IDs when replayed.
- Store enough audit context to diagnose failed sync.
- Do not hide integration failure as business success.

## Examples

- `PlaceOrderCommand` changes state.
- `ListCustomerOrdersQuery` reads state.
- `GetOrderDetailsQuery` reads state.
- `SyncOfflineDraftCommand` changes state and must be idempotent.

## Expected Output

- Command/query classification.
- Handler responsibility.
- Idempotency strategy.
- Read/write model decision.
- Tests for success, failure, and retry behavior.
