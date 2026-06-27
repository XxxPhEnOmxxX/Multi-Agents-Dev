---
name: managing-docker-n8n-infra
description: Designs, reviews, operates, and hardens Docker-based infrastructure, Docker Compose stacks, n8n deployments, reverse proxies, volumes, networks, secrets, backups, observability, CI/CD, and production runtime reliability. Use for Docker, n8n, infrastructure, deploy, proxy, logs, volumes, networking, automation platforms, and operational troubleshooting.
---

# Managing Docker n8n Infrastructure

Use this skill when the task involves Docker, Docker Compose, n8n, reverse proxy, infrastructure, deployment, networking, volumes, environment variables, backups, monitoring, CI/CD, or operational troubleshooting.

The DevOps engineer must prioritize reliability, reproducibility, security, observability, and safe operations.

## Core rule

Infrastructure must be boring, recoverable, observable, and documented.

Do not make production changes blindly. Do not destroy volumes, secrets, databases, or runtime state without explicit approval and rollback thinking.

## DevOps workflow

### 1. Understand the environment

Before changing infrastructure, identify:

```txt
System:
Environment: local / staging / production
Runtime: Docker / Docker Compose / VPS / cloud / bare metal
Services involved:
Ports exposed:
Domains/proxy:
Volumes/data paths:
Secrets/env handling:
Backup status:
Monitoring/logging:
Risk level:
```

If production is involved, prefer inspection and reversible changes first.

### 2. Review Docker and Compose

Check:

```txt
- service names and responsibilities;
- image tags and update strategy;
- restart policies;
- healthchecks;
- networks and isolation;
- exposed ports vs internal ports;
- volumes and persistence;
- environment variables and secrets;
- user/root permissions;
- resource limits when relevant;
- dependency ordering;
- logs and troubleshooting path.
```

Use `docker compose config` before applying changes when possible.

### 3. Review n8n deployments

For n8n, check:

```txt
- persistent volume for n8n data;
- database strategy: SQLite only for simple/local use, PostgreSQL preferred for serious production;
- webhook URL and public domain correctness;
- reverse proxy and HTTPS;
- execution mode and queue needs;
- credentials encryption key handling;
- environment variables;
- workflow backups/exports;
- user access and authentication;
- logs for failed executions;
- update/rollback plan.
```

Never expose credentials, workflow secrets, or encryption keys in logs or reports.

### 4. Review reverse proxy and TLS

Check:

```txt
- correct host routing;
- HTTP to HTTPS redirect;
- TLS certificate source and renewal;
- forwarded headers;
- websocket support when needed;
- upload/body size limits when relevant;
- timeout settings for long-running workflows;
- security headers when appropriate;
- access logs and error logs.
```

### 5. Review persistence and backups

For every stateful service, identify:

```txt
Data location:
Backup method:
Restore method:
Backup frequency:
Retention:
Last restore test:
Risk if volume is deleted:
```

Before any destructive operation, require explicit approval and backup/rollback plan.

### 6. Diagnose operational issues

Start with low-risk inspection:

```bash
docker ps
docker compose ps
docker compose config
docker compose logs --tail=100
```

Then inspect specific service logs, health, networks, ports, proxy, DNS, TLS, and environment assumptions.

Do not run destructive cleanup commands unless explicitly approved.

### 7. Validate changes

After changes, validate:

```txt
- compose config parses;
- services start;
- healthchecks pass;
- expected ports are reachable;
- proxy routes correct domain;
- n8n UI loads;
- webhook endpoint is reachable when applicable;
- logs do not show repeated errors;
- persistent data remains available;
- rollback path is known.
```

## Safe command policy

Prefer inspection commands first:

```bash
docker ps
docker compose ps
docker compose config
docker compose logs --tail=100
docker network ls
docker volume ls
```

Use caution with:

```bash
docker compose down
docker compose pull
docker compose up -d
docker compose restart <service>
```

Require explicit approval for destructive commands:

```bash
docker compose down -v
docker volume rm
docker system prune -a
rm -rf <data-volume-path>
```

## Infrastructure principles

Prefer:

```txt
- explicit Docker Compose files;
- stable image tags instead of accidental latest in production;
- named volumes for persistent data;
- clear network boundaries;
- reverse proxy in front of public services;
- HTTPS for public endpoints;
- secrets outside version control;
- healthchecks and logs;
- backup before risky changes;
- incremental deploys with rollback.
```

Avoid:

```txt
- exposing databases publicly;
- committing .env or credentials;
- deleting volumes to fix unknown problems;
- running everything on host network without reason;
- changing many infrastructure layers at once;
- upgrading n8n or database without backup;
- ignoring webhook/domain mismatch;
- assuming container running means service healthy.
```

## Output format: starting DevOps work

```txt
DevOps scope:
Environment:
Services involved:
Risk level:
Current assumption:
Inspection plan:
Potential impact:
Rollback/backup need:
```

## Output format: infrastructure review

```txt
Infrastructure review:
Docker/Compose:
n8n:
Proxy/TLS:
Persistence/backups:
Secrets:
Observability:
Risks:
Recommended changes:
Validation plan:
```

## Output format: troubleshooting

```txt
Incident/problem:
Observed symptoms:
Likely layer: app / container / network / proxy / DNS / TLS / database / volume / credentials
Evidence:
Next safe checks:
Recommended fix:
Rollback plan:
```

## References

- Docker Compose checklist: `references/docker-compose-checklist.md`
- n8n deployment checklist: `references/n8n-deployment-checklist.md`
- Infrastructure troubleshooting example: `examples/infra-troubleshooting.md`
