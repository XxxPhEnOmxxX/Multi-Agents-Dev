---
name: architecting-systems
description: Designs, reviews, and adjusts software architecture through a question-driven process. Use when defining system architecture, changing architecture, choosing patterns, splitting modules/services, designing integrations, planning scalability, or evaluating technical trade-offs.
---

# Architecting Systems

Use this skill when the task involves defining, reviewing, or changing the architecture of a software system.

The architect must not jump directly to a solution. Architecture decisions must start with questions, constraints, trade-offs, and explicit assumptions.

## Core rule

Architecture is developed through guided questioning.

Before proposing or changing architecture, ask questions that clarify:

```txt
- business objective;
- current system state;
- users and workflows;
- functional requirements;
- non-functional requirements;
- integrations;
- data model and ownership;
- deployment/runtime constraints;
- security and compliance needs;
- expected scale;
- team capacity;
- budget and delivery urgency;
- migration/rollback constraints.
```

If the user has already provided enough information, do not ask generic questions. Ask only the missing questions that materially affect the architecture.

## Operating mode

Classify the architecture task first:

```txt
New architecture:
Designing a system or major module from zero.

Architecture adjustment:
Changing an existing system, module boundary, data flow, deployment model, or integration.

Architecture review:
Evaluating the current design and identifying risks, simplifications, and improvement paths.

Decision support:
Comparing options such as monolith vs microservices, REST vs GraphQL, SQL vs NoSQL, queue vs direct call, Docker Compose vs Kubernetes.
```

## Question-first workflow

### 1. Understand the goal

Ask:

```txt
What problem is this architecture solving?
Who uses the system?
What workflow must work first?
What is the most important business outcome?
What must not break?
```

### 2. Understand the current state

Ask when adjusting/reviewing an existing system:

```txt
What stack is currently used?
What modules already exist?
What database is used?
How is authentication handled?
How is the system deployed?
What are the current pain points?
What parts are fragile or hard to change?
```

### 3. Identify constraints

Ask:

```txt
What deadline exists?
What team will maintain this?
What budget/infrastructure limits exist?
What data is sensitive?
What integrations are required?
What traffic/volume is expected?
What observability exists today?
```

### 4. Separate requirements

Organize requirements into:

```txt
Functional requirements:
What the system must do.

Non-functional requirements:
Performance, security, reliability, maintainability, scalability, observability, cost.

Constraints:
Stack, hosting, team knowledge, legacy systems, deadlines, compliance.

Out of scope:
What should not be solved now.
```

### 5. Propose architecture options

Do not present only one design when the decision has meaningful trade-offs.

Prefer this format:

```txt
Option A: simplest viable architecture
Option B: more scalable architecture
Option C: future/advanced architecture
Recommendation: choose one and explain why
```

### 6. Make trade-offs explicit

For each important decision, explain:

```txt
Decision:
Why this option:
Benefits:
Costs:
Risks:
What it makes easier:
What it makes harder:
When to revisit:
```

### 7. Produce the architecture output

Depending on the task, produce one or more:

```txt
- system context;
- module boundaries;
- API/integration map;
- data ownership model;
- deployment view;
- security boundaries;
- sequence/data flow;
- migration plan;
- architecture decision record;
- implementation phases.
```

## Architecture principles

Prefer:

```txt
- simple architecture that solves the current problem;
- clear module boundaries;
- explicit data ownership;
- boring technology when it reduces risk;
- incremental migration over big-bang rewrite;
- observable services and flows;
- security boundaries designed early;
- reversible decisions when uncertainty is high;
- documentation that explains why, not only what.
```

Avoid:

```txt
- microservices without operational maturity;
- abstractions before real repetition;
- event-driven architecture without clear need;
- shared database across unrelated modules;
- hidden business logic in frontend only;
- architecture driven only by trends;
- redesigning everything when a small adjustment solves the pain;
- decisions without migration and rollback thinking.
```

## When to stop and ask before proceeding

Stop and ask follow-up questions when the decision affects:

```txt
- authentication or authorization model;
- database schema and ownership;
- payment, billing, or financial data;
- customer-sensitive data;
- deployment topology;
- service boundaries;
- public API contracts;
- migration from legacy system;
- irreversible or expensive infrastructure choices.
```

## Output format: starting an architecture task

```txt
Architecture task type:
What I understand:
Key unknowns:
Questions before architecture:
Assumptions I can safely make:
Suggested next step:
```

## Output format: architecture proposal

```txt
Architecture goal:
Requirements:
Constraints:
Recommended architecture:
Main components:
Data flow:
Security boundaries:
Deployment/runtime view:
Trade-offs:
Risks:
Open questions:
Implementation phases:
Validation plan:
```

## References

- Question bank: `references/question-bank.md`
- ADR template: `references/adr-template.md`
- Architecture session example: `examples/architecture-session.md`
