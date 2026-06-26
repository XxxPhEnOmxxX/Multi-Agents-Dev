# Example: Backend Feature Plan

Use this as a shape for backend planning. Do not copy blindly.

## User request

```txt
Add an endpoint to create service orders for customers and assign them to technicians.
```

## Backend plan

```txt
Backend scope:
Create service order API and assignment logic.

Behavior to implement/fix:
Admin can create a service order for an existing customer and optionally assign it to a technician.

Affected routes/services/data:
- POST /api/service-orders
- ServiceOrderService
- CustomerRepository
- TechnicianRepository
- ServiceOrderRepository

Business rules:
- customer must exist;
- technician must exist if provided;
- normal users cannot create service orders;
- initial status is pending or assigned depending on technician;
- service order creation should be audited.

Validation rules:
- customerId required;
- technicianId optional but must be valid if present;
- description required with max length;
- priority must be one of allowed values;
- scheduledDate must be a valid date if present.

Auth/permission impact:
Admin or dispatcher role required. Technician cannot create service order for another technician.

Database impact:
May need service_orders table and index on customerId, technicianId, status, scheduledDate.

Risk level:
Medium, because it creates operational records and role-based behavior.

Planned checks:
- unit tests for service rules;
- integration test for POST /api/service-orders;
- negative test for non-admin;
- migration validation;
- lint/build/test.
```

## Backend review example

```txt
Backend review result:
Needs adjustment.

API contract impact:
New endpoint is acceptable, but response shape needs documented id/status/createdAt fields.

Data integrity impact:
Creation should use transaction if audit log is written in the same flow.

Auth/authorization impact:
Admin check exists, but dispatcher role is missing.

Error handling:
Customer not found should return 404. Invalid technicianId should return 400 or 404 consistently with project convention.

Tests/validation:
Add negative authorization test and invalid customer test.

Risks:
Without transaction, service order may be created without audit record if audit write fails.

Recommended changes:
Add transaction, dispatcher permission, and integration tests.
```
