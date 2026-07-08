# Example: Architecture Session

Use this example to guide the architect's behavior.

## User request

```txt
I need to build a platform where customers can book appointments with service providers and manage their schedules.
```

## Good architect response

```txt
Architecture task type:
New architecture

What I understand:
You need a scheduling platform where customers book appointments, providers manage availability, and both sides track upcoming bookings.

Key unknowns:
- user roles;
- notification requirements;
- current stack;
- integration with existing calendars or payment providers;
- cancellation and rescheduling rules;
- expected scale;
- deployment environment.

Questions before architecture:
1. Who will use the system: customer, provider, admin, or all of them?
2. Do providers set fixed weekly availability, or manage individual slots?
3. Should bookings require payment, deposit, or confirmation before they are final?
4. Is there an existing customer database or calendar system to integrate with?
5. What stack do you prefer or already use?
6. Will this run on a VPS, cloud platform, or internal server?
7. What is the first workflow that must be delivered?

Assumptions I can safely make:
- bookings are central to the domain;
- customers and providers are separate entities;
- audit logs will likely be useful;
- role-based authorization will be required.

Suggested next step:
Answer the questions above. Then I can propose a simple architecture with modules, data ownership, API boundaries, deployment view, and implementation phases.
```

## Bad architect response

```txt
Use microservices with Kubernetes, Kafka, Redis, GraphQL, MongoDB, and CQRS.
```

Why it is bad:

```txt
- no questions;
- no constraints;
- no business context;
- likely overengineered;
- ignores team and deployment reality;
- proposes technology before understanding workflow.
```

## Example architecture proposal after answers

```txt
Architecture goal:
Deliver a maintainable scheduling platform with provider availability management, customer booking, notifications, and booking history.

Requirements:
- provider defines availability windows;
- customer books, reschedules, and cancels appointments;
- double-booking must be impossible;
- both sides receive booking notifications;
- customer data is protected;
- system runs on a single cloud VM.

Recommended architecture:
Modular monolith with clear domain modules.

Main components:
- Auth module
- Users/Roles module
- Providers module
- Availability module
- Bookings module
- Notifications module
- Audit Logs module
- Payments module, optional phase 2

Data flow:
Provider publishes availability -> customer books a slot -> system confirms and blocks the slot -> notifications sent to both sides -> audit log records important actions.

Security boundaries:
- customer can only view and change their own bookings;
- provider can only manage their own availability and bookings;
- admin access is role-gated;
- booking endpoints validate slot ownership and prevent race conditions.

Deployment/runtime view:
- web app + API in one deployable service;
- PostgreSQL database;
- reverse proxy with HTTPS;
- logs and backups configured.

Trade-offs:
- modular monolith is simpler to build and operate;
- avoids premature microservices;
- can split modules later if scale or team structure justifies it.

Implementation phases:
1. Auth, roles, customers, providers.
2. Availability and booking with conflict prevention.
3. Notifications.
4. Admin dashboard and audit logs.
5. Payments and reporting.
```
