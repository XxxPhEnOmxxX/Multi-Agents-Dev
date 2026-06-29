---
name: managing-infrastructure
description: Use this skill when designing, reviewing, operating, deploying, hardening, or troubleshooting infrastructure across cloud, VPS, bare metal, containers, orchestration platforms, CI/CD, networking, secrets, backups, observability, and production runtime reliability.
---

# Managing Infrastructure

## Purpose

Guide infrastructure and DevOps work in a technology-neutral way.

This skill is intentionally generic. It applies to Docker, Kubernetes, cloud platforms, VPS, bare metal, serverless, CI/CD systems, reverse proxies, queues, databases, storage, monitoring, backups, and production operations.

## Core Rule

Infrastructure must be safe, reproducible, observable, recoverable, and documented.

Do not make production changes blindly. Do not destroy data, secrets, databases, volumes, state, or runtime configuration without explicit approval and rollback thinking.

## Use When

Use this skill when the task involves:

- deployment or release infrastructure;
- cloud, VPS, bare metal, container, serverless, or orchestrator runtime;
- CI/CD pipelines;
- environment variables, secrets, credentials, or config management;
- reverse proxy, ingress, TLS, DNS, ports, firewall, or routing;
- logs, metrics, tracing, alerts, health checks, or observability;
- backups, restores, migrations, persistence, or disaster recovery;
- production troubleshooting;
- infrastructure security and operational hardening;
- rollback, blue/green, canary, or zero-downtime deployment concerns.

## Do Not Use When

Do not use this skill for:

- application business logic unless runtime behavior is involved;
- frontend UI decisions;
- pure domain modeling;
- one-off project-specific deploy commands that belong in a project reference doc;
- vendor-specific platform procedures unless the project clone adds a dedicated skill.

## Workflow

### 1. Understand the Environment

Identify:

```txt
System:
Environment: local / development / staging / production
Runtime: cloud / VPS / bare metal / container / orchestrator / serverless / hybrid
Services involved:
Deployment method:
CI/CD workflow:
Network entrypoints:
DNS/TLS/proxy/ingress:
Data stores and persistent state:
Secrets/config handling:
Backup and restore status:
Observability status:
Blast radius:
Rollback path:
Risk level:
```

If production is involved, start with read-only inspection and reversible steps.

### 2. Classify the Work

Classify the request before acting:

```txt
- design/review;
- deployment/change;
- incident/troubleshooting;
- security hardening;
- migration;
- automation;
- cost/performance optimization;
- backup/restore validation;
- CI/CD failure diagnosis.
```

The class determines the risk level, validation plan, and approval gates.

### 3. Identify State and Blast Radius

Before changes, identify what can be affected:

```txt
- databases;
- object storage;
- queues;
- volumes;
- secrets;
- certificates;
- DNS;
- public routes;
- customer traffic;
- scheduled jobs;
- background workers;
- external integrations;
- monitoring and alerting.
```

If the change can affect customer traffic, data, secrets, or production availability, require a rollback plan.

### 4. Prefer Safe Inspection First

Use low-risk inspection before changing runtime state.

Examples:

```txt
- read config;
- inspect service status;
- inspect logs with safe limits;
- inspect recent deploy history;
- validate syntax/configuration;
- check health endpoints;
- check CI/CD logs;
- check DNS/TLS/proxy behavior;
- verify backup existence.
```

Do not jump to restart, recreate, delete, prune, migrate, or rotate operations without evidence.

### 5. Design for Reliability

Prefer infrastructure that has:

```txt
- explicit versioning;
- repeatable deploys;
- environment separation;
- least privilege;
- secrets outside version control;
- health checks;
- logs and metrics;
- backup and restore plan;
- rollback path;
- documented operational commands;
- clear ownership of stateful services;
- minimal public exposure.
```

### 6. Validate Changes

After infrastructure work, validate with evidence:

```txt
- configuration parses;
- deployment completes;
- services are healthy;
- logs do not show repeated errors;
- expected routes are reachable;
- TLS/DNS/proxy behavior is correct when relevant;
- persistence remains available;
- background jobs/workers are running when relevant;
- CI/CD checks pass when relevant;
- rollback path remains known.
```

## Approval Gates

Ask explicit approval before:

```txt
- deleting or overwriting persistent data;
- removing volumes, buckets, disks, databases, or queues;
- rotating production secrets or certificates;
- changing production DNS, ingress, proxy, firewall, or public routes;
- applying database migrations in production;
- restarting critical production services;
- scaling down production capacity;
- changing CI/CD secrets or deployment credentials;
- running destructive cleanup commands;
- disabling monitoring, alerting, backups, or access controls.
```

## Infrastructure Principles

Prefer:

```txt
- boring and documented infrastructure;
- small reversible changes;
- immutable or repeatable deployment when practical;
- explicit versions and pinned dependencies;
- least privilege access;
- private-by-default networking;
- HTTPS/TLS for public endpoints;
- clear separation of app, data, network, and secrets;
- monitoring before automation;
- backup before risky change;
- tested rollback for high-risk changes.
```

Avoid:

```txt
- committing secrets;
- exposing databases publicly;
- relying on manual state that is not documented;
- changing many infrastructure layers at once;
- deleting data to fix unknown problems;
- using broad admin credentials casually;
- assuming a process is healthy because it is running;
- applying production changes without evidence and rollback thinking;
- making vendor-specific assumptions in the base template.
```

## Output: Starting Infrastructure Work

```txt
Infrastructure scope:
Environment:
Runtime/platform:
Services involved:
Risk level:
Stateful resources:
Inspection plan:
Potential impact:
Approval gates:
Rollback/backup need:
Skills used:
```

## Output: Infrastructure Review

```txt
Infrastructure review:
Runtime/deploy model:
Networking/DNS/TLS:
Secrets/config:
Persistence/backups:
Observability:
CI/CD:
Security posture:
Risks:
Recommended changes:
Validation plan:
Skills used:
```

## Output: Troubleshooting

```txt
Incident/problem:
Observed symptoms:
Likely layer: app / runtime / network / DNS / TLS / proxy / database / storage / secrets / CI/CD / external dependency
Evidence:
Next safe checks:
Recommended fix:
Rollback plan:
Validation after fix:
Skills used:
```

## Output: Change Completion

```txt
Infrastructure result:
What changed:
Environment:
Validation evidence:
Data/persistence impact:
Secrets impact:
Rollback notes:
Residual risks:
Next operational improvement:
Skills used:
```
