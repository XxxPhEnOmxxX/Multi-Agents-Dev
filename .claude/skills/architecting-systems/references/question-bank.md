# Architecture Question Bank

Use this bank to ask targeted questions before proposing architecture.

Do not ask every question. Choose only the questions that materially affect the decision.

## Business and product goal

```txt
What business problem does this system solve?
Who is the primary user?
What is the first workflow that must work well?
What outcome matters most: speed, reliability, cost, automation, scale, auditability, user experience, or security?
What would make this architecture a failure?
```

## Current system

```txt
Does a system already exist?
What stack is currently used?
What modules/features already exist?
What parts are stable?
What parts are fragile?
What causes most bugs or maintenance pain?
What is hard to change today?
What technical debt must be preserved temporarily?
```

## Users and workflows

```txt
What user roles exist?
What can each role do?
What workflow is most frequent?
What workflow is most critical?
What workflow has the highest risk if it fails?
What needs to happen synchronously?
What can happen asynchronously?
```

## Data and ownership

```txt
What are the core entities?
Who owns each entity?
What data is sensitive?
What data changes frequently?
What data must be audited?
What data must be retained or deleted?
What database is currently used or preferred?
Is strong consistency required or is eventual consistency acceptable?
```

## Integrations

```txt
What external systems are required?
Are integrations synchronous APIs, webhooks, queues, files, or manual imports?
What happens when an external system is offline?
Do integrations need retries, idempotency, or dead-letter handling?
Who owns credentials for each integration?
What rate limits or API constraints exist?
```

## Security

```txt
How is authentication handled?
What authorization model is needed?
What data must never be exposed to the frontend?
What admin actions require audit logs?
What secrets exist and where are they stored?
What compliance or privacy rules apply?
What threat would cause the most damage?
```

## Scale and performance

```txt
How many users are expected now?
How many users are expected in 12 months?
What is the expected request volume?
What operations are heavy or slow?
What response time is acceptable?
What background jobs are expected?
What data size growth is expected?
```

## Reliability and operations

```txt
What uptime is expected?
What can fail without major impact?
What cannot fail?
What needs backup and restore?
What alerts are needed?
What logs are needed to debug incidents?
Who will operate the system after delivery?
```

## Deployment and infrastructure

```txt
Where will the system run: VPS, cloud, containers, Kubernetes, serverless, on-premise?
What deployment process exists today?
Are there environment constraints?
Is horizontal scaling needed now or later?
How are secrets injected?
How are migrations applied?
What rollback process is expected?
```

## Team and maintainability

```txt
Who will maintain this system?
What technologies does the team already know?
What complexity can the team realistically operate?
How fast does the system need to evolve?
What documentation is required?
What parts should be easy to replace later?
```

## Decision quality

Before making a recommendation, answer:

```txt
What is the simplest architecture that works?
What complexity is justified by current requirements?
What complexity is only speculation?
What decision is reversible?
What decision is expensive to reverse?
What should be postponed until evidence appears?
```
