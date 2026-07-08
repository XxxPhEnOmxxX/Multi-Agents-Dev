# Example: Backend Feature Plan

Use this as a shape for backend planning. Do not copy blindly.

## User request

```txt
Add an endpoint to create bookings for customers and assign them to staff members.
```

## Backend plan

```txt
Backend scope:
Create booking API and assignment logic.

Behavior to implement/fix:
Admin can create a booking for an existing customer and optionally assign it to a staff member.

Affected routes/services/data:
- POST /api/bookings
- BookingService
- CustomerRepository
- StaffMemberRepository
- BookingRepository

Business rules:
- customer must exist;
- staff member must exist if provided;
- normal users cannot create bookings;
- initial status is pending or assigned depending on staff member;
- booking creation should be audited.

Validation rules:
- customerId required;
- staffMemberId optional but must be valid if present;
- description required with max length;
- priority must be one of allowed values;
- scheduledDate must be a valid date if present.

Auth/permission impact:
Admin or coordinator role required. A staff member cannot create a booking for another staff member.

Database impact:
May need bookings table and index on customerId, staffMemberId, status, scheduledDate.

Risk level:
Medium, because it creates operational records and role-based behavior.

Planned checks:
- unit tests for service rules;
- integration test for POST /api/bookings;
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
Admin check exists, but coordinator role is missing.

Error handling:
Customer not found should return 404. Invalid staffMemberId should return 400 or 404 consistently with project convention.

Tests/validation:
Add negative authorization test and invalid customer test.

Risks:
Without transaction, booking may be created without audit record if audit write fails.

Recommended changes:
Add transaction, coordinator permission, and integration tests.
```
