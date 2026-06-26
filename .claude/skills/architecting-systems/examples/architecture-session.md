# Example: Architecture Session

Use this example to guide the architect's behavior.

## User request

```txt
I need to build a system to manage technicians, service orders, customers, and field check-ins.
```

## Good architect response

```txt
Architecture task type:
New architecture

What I understand:
You need an operational system for managing field service workflows involving technicians, customers, service orders, and check-ins.

Key unknowns:
- user roles;
- offline/mobile requirements;
- current stack;
- integration with existing ERP/CRM;
- location data rules;
- expected scale;
- deployment environment.

Questions before architecture:
1. Who will use the system: admin, dispatcher, technician, customer, or all of them?
2. Does the technician need to use it from mobile in the field?
3. Should check-in require GPS, photo, QR code, or manual confirmation?
4. Is there already a customer database/ERP to integrate with?
5. What stack do you prefer or already use?
6. Will this run in Docker, VPS, cloud, or internal server?
7. What is the first workflow that must be delivered?

Assumptions I can safely make:
- service orders are central to the domain;
- technicians and customers are separate entities;
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
Deliver a maintainable field service system with admin scheduling, technician mobile check-in, customer records, and service order tracking.

Requirements:
- admin creates and assigns service orders;
- technician views assigned work;
- technician checks in with GPS and timestamp;
- admin tracks status;
- customer data is protected;
- system runs in Docker on VPS.

Recommended architecture:
Modular monolith with clear domain modules.

Main components:
- Auth module
- Users/Roles module
- Customers module
- Technicians module
- Service Orders module
- Check-ins module
- Audit Logs module
- Notification module, optional phase 2

Data flow:
Admin creates OS -> system assigns technician -> technician updates status/check-in -> admin monitors progress -> audit log records important actions.

Security boundaries:
- admin can manage all service orders;
- technician can only view assigned orders;
- customer data restricted by role;
- check-in endpoint validates technician ownership.

Deployment/runtime view:
- web app + API in one deployable service;
- PostgreSQL database;
- Docker Compose;
- reverse proxy with HTTPS;
- logs and backups configured.

Trade-offs:
- modular monolith is simpler to build and operate;
- avoids premature microservices;
- can split modules later if scale or team structure justifies it.

Implementation phases:
1. Auth, roles, customers, technicians.
2. Service orders and assignment.
3. Technician mobile check-in.
4. Admin dashboard and audit logs.
5. Notifications and reporting.
```
