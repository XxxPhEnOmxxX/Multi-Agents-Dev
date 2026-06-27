# Example: Infrastructure Troubleshooting

Use this as a reporting shape when diagnosing Docker, n8n, proxy, or infrastructure problems.

## User request

```txt
n8n is running in Docker, but webhooks are not working through my domain.
```

## Good DevOps response

```txt
Incident/problem:
n8n UI may be running, but public webhook callbacks are not reaching the expected endpoint.

Observed symptoms:
- UI status unknown
- webhook public URL unknown
- proxy behavior unknown
- container logs not checked yet

Likely layer:
proxy / domain / webhook URL / n8n environment

Evidence needed:
1. docker compose ps
2. docker compose logs --tail=100 n8n
3. reverse proxy route for the n8n domain
4. public webhook URL configured in n8n environment
5. curl test to harmless webhook/test endpoint if available

Next safe checks:
- validate compose: docker compose config
- check container status: docker compose ps
- inspect recent logs: docker compose logs --tail=100 n8n
- verify proxy host routing and HTTPS
- verify webhook public URL/domain match

Recommended fix:
Depends on evidence. Common fixes include correcting the public webhook URL, proxy forwarded headers, HTTPS route, timeout, or domain DNS.

Rollback plan:
Do not change volume or database. Keep previous compose/proxy config before edits. Restart only n8n/proxy service if config changes are minimal and reversible.
```

## Bad DevOps response

```txt
Run docker compose down -v and recreate everything.
```

Why it is bad:

```txt
- destroys volumes;
- may delete n8n data and workflows;
- no evidence;
- no backup;
- no rollback;
- treats unknown issue as destructive rebuild.
```

## Example review summary

```txt
Infrastructure review:
Docker/Compose:
- n8n service uses persistent volume.
- Database is internal only.
- Compose config passes.

n8n:
- Public domain configured.
- Webhook URL needs verification.
- Encryption key is present via environment variable, not committed.

Proxy/TLS:
- Domain routes to proxy.
- HTTPS certificate present.
- Forwarded headers need review.

Persistence/backups:
- Volume exists.
- Backup procedure not documented.

Secrets:
- .env must not be committed.
- Do not print credentials in logs.

Risks:
- Webhook failure may be caused by public URL/proxy mismatch.
- No confirmed restore test.

Recommended changes:
1. Document backup/restore.
2. Verify webhook public URL.
3. Validate proxy forwarded headers.
4. Add healthcheck if absent.

Validation plan:
- docker compose config
- docker compose ps
- n8n UI loads
- harmless test workflow webhook receives request
- logs show no repeated proxy/app errors
```
