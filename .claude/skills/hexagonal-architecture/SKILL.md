---
name: hexagonal-architecture
description: Use this skill when designing ports, adapters, external integrations, repositories, gateways, message handlers, or anti-corruption layers.
---

# Hexagonal Architecture

## Purpose

Connect the application to the outside world through explicit ports and adapters.

## Core Idea

The application owns the contracts. External tools adapt to those contracts.

```txt
External system -> Adapter -> Port -> Application -> Domain
```

## Port Types

- Inbound port: operation the application exposes, such as a use case or command handler.
- Outbound port: capability the application needs, such as repository, payment gateway, storage, notification, queue, or external system access.

## Adapter Types

- Inbound adapter: HTTP controller, CLI command, worker, webhook, chat bot, mobile BFF endpoint.
- Outbound adapter: payment gateway client, database repository, object storage, external API adapter, notification provider.

## Workflow

1. Identify whether the external dependency is inbound or outbound.
2. Define the application-owned port.
3. Implement an adapter that translates external details into internal contracts.
4. Keep raw payloads, endpoint paths, headers, and vendor status names inside adapters.
5. Add mapper and error mapper when integrating external APIs.
6. Test the adapter against the port contract.

## Rules

- The port name should describe the business capability, not the vendor.
- The adapter name may describe the vendor.
- Adapters translate; they do not own business rules.
- Use cases must not know HTTP paths, auth headers, or vendor-specific fields.

## Expected Output

- Port definition.
- Adapter responsibility.
- Mapping rules.
- Error translation rules.
- Contract tests or mapper tests needed.
