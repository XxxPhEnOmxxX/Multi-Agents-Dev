---
name: capability-driven-integration
description: Use this skill when modeling ERP/API feature support, module availability, optional integrations, fallback behavior, and compatibility matrices.
---

# Capability-Driven Integration

## Purpose

Make optional ERP and external API features explicit so modules can be enabled or disabled safely.

## Core Idea

Do not assume every external system supports every operation. Model supported capabilities as data.

## Capability Examples

- `workOrders.read`
- `workOrders.start`
- `workOrders.close`
- `workOrders.uploadPhotos`
- `customers.read`
- `customers.updateContact`
- `inventory.read`
- `inventory.consumeMaterial`
- `network.readOnuSignal`
- `network.rebootOnu`

## Workflow

1. Identify the module or workflow.
2. List the required capabilities.
3. Identify which capabilities the ERP/API actually supports.
4. Define fallback behavior for unsupported capabilities.
5. Expose module availability through a stable internal model.
6. Test both supported and unsupported paths.

## Rules

- Unsupported capability is not an unexpected error.
- Read support does not imply write support.
- Partial support must be modeled explicitly.
- UI module visibility must depend on capabilities and permissions.
- Capabilities should be cached carefully and refreshed when integration config changes.

## Expected Output

- Capability list.
- Module availability decision.
- Fallback behavior.
- Tests for supported and unsupported paths.
