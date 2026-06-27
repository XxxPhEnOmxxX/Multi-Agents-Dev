# Docker Compose Checklist

Use this checklist when reviewing or changing Docker Compose infrastructure.

## Basic structure

```txt
- Services have clear names.
- Each service has one main responsibility.
- Compose file is valid: docker compose config.
- Environment-specific overrides are documented when used.
- No secrets are committed in compose files.
```

## Images and builds

```txt
- Image tags are explicit in production.
- `latest` is avoided for critical production services unless intentionally accepted.
- Build context is minimal.
- Dockerfile avoids copying unnecessary files.
- Base image version is known.
```

## Ports and networks

```txt
- Only public services expose host ports.
- Databases are not publicly exposed.
- Internal services communicate through Docker networks.
- Network names and boundaries are clear.
- Reverse proxy is the public entrypoint when applicable.
```

## Volumes and persistence

```txt
- Stateful services use named volumes or documented bind mounts.
- Volume paths are not accidentally temporary.
- Backup strategy exists for important volumes.
- Destructive operations require backup and approval.
- File permissions are compatible with container user.
```

## Environment and secrets

```txt
- `.env` is not committed.
- `.env.example` exists when useful.
- Required variables are documented.
- Secrets are not printed in logs.
- Production credentials are not reused in local/dev.
```

## Restart and health

```txt
- Critical services have restart policy.
- Healthchecks exist where useful.
- Dependencies are not trusted only through depends_on startup order.
- Application readiness is validated, not just container running.
```

## Security posture

```txt
- Containers do not run privileged unless required and justified.
- Host network is avoided unless required.
- Docker socket is not mounted unless explicitly needed and risk accepted.
- Containers avoid root when practical.
- Sensitive host paths are not mounted casually.
```

## Observability

```txt
- Logs are accessible.
- Log volume does not grow without control.
- Important services expose health/status.
- Troubleshooting commands are documented.
```

## Safe change checklist

Before applying changes:

```txt
- docker compose config passes.
- Current running services are known.
- Data volumes affected are identified.
- Backup/rollback need is clear.
- Change is scoped and reversible.
```

After applying changes:

```txt
- Services are running.
- Healthchecks pass or service responds.
- Logs do not show repeated errors.
- Public routes/proxy still work.
- Persistent data remains available.
```
