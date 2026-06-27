# n8n Deployment Checklist

Use this checklist when deploying, reviewing, or troubleshooting n8n in Docker-based infrastructure.

## Deployment model

```txt
- Environment is identified: local, staging, production.
- n8n runs behind reverse proxy when public.
- Public URL/domain is known.
- HTTPS is enabled for public access.
- Webhook URL matches the public domain.
- Timezone is configured intentionally.
```

## Persistence

```txt
- n8n data is persisted in a named volume or documented bind mount.
- Database choice matches environment risk.
- SQLite is accepted only for simple/local/small deployments.
- PostgreSQL is preferred for serious production.
- Backup exists for n8n data and database.
- Restore procedure is documented or tested.
```

## Secrets and credentials

```txt
- Encryption key is set and persisted safely.
- `.env` is not committed.
- Credentials are not printed in logs or reports.
- API keys, OAuth secrets, tokens, and webhook secrets are stored securely.
- Changing encryption key is treated as high risk.
```

## Reverse proxy and webhooks

```txt
- Proxy forwards correct host/proto headers.
- HTTP redirects to HTTPS when public.
- Webhook path reaches the n8n container.
- Websocket or long-running request needs are considered.
- Timeout/body-size limits do not break workflows.
- Public webhook tests use harmless payloads.
```

## Execution and scaling

```txt
- Execution mode is appropriate for workload.
- Long-running workflows are understood.
- Queue/worker mode is considered only when needed.
- Redis or worker services are not added without operational need.
- Workflow concurrency and resource usage are monitored.
```

## Updates and rollback

Before updating n8n:

```txt
- Current version is known.
- Target version is known.
- Changelog/risk is considered when available.
- Backup is completed.
- Rollback plan exists.
- Workflows and credentials are protected.
```

After updating:

```txt
- UI loads.
- Credentials decrypt correctly.
- Existing workflows are visible.
- Critical workflows execute.
- Webhooks respond.
- Logs are clean.
```

## Security

```txt
- Public editor access is protected.
- User management/authentication is enabled when needed.
- Admin access is restricted.
- n8n is not exposed directly without proxy/TLS in production.
- Database is not publicly exposed.
- Secrets are not stored in repository.
```

## Troubleshooting focus

When n8n fails, identify the layer:

```txt
- container not running;
- app boot error;
- database connection issue;
- volume/permission issue;
- encryption key mismatch;
- reverse proxy issue;
- webhook URL/domain mismatch;
- TLS/certificate issue;
- workflow credential issue;
- external API integration issue.
```
