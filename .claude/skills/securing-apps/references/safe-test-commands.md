# Safe Test Commands Reference

Use these examples only on systems the user owns or is authorized to assess.

Prefer local or staging environments. For production, use low-impact checks and avoid high volume.

## Repository checks

```bash
git status
git diff --stat
git diff --check
git grep -n "TODO\|FIXME\|password\|secret\|token\|api_key" -- .
```

Use grep results carefully. Do not print or repeat real secrets in reports.

## Node.js projects

```bash
npm audit --audit-level=moderate
npm run lint
npm test
npm run build
```

If the project uses pnpm or yarn, prefer the matching package manager.

```bash
pnpm audit --audit-level moderate
pnpm lint
pnpm test
pnpm build
```

```bash
yarn npm audit --severity moderate
yarn lint
yarn test
yarn build
```

## Python projects

```bash
pytest
ruff check .
mypy .
pip-audit
```

Only use commands that are installed or documented in the project.

## Docker and Compose

```bash
docker compose config
docker compose ps
docker compose logs --tail=100
```

Avoid destructive commands unless explicitly approved.

Do not run by default:

```bash
docker compose down -v
docker volume rm
docker system prune -a
```

## HTTP header inspection

Use low-impact requests:

```bash
curl -I https://example.com/
```

For API endpoints, prefer known safe routes such as health/status endpoints.

```bash
curl -i https://example.com/health
```

Check for:

```txt
- status code
- security headers
- redirects
- server leakage
- cache behavior for sensitive routes
```

## CORS preflight check

Use only to verify whether an API allows unexpected origins.

```bash
curl -i -X OPTIONS "https://example.com/api/path" \
  -H "Origin: https://example.invalid" \
  -H "Access-Control-Request-Method: POST"
```

Risk signal:

```txt
Access-Control-Allow-Origin reflects arbitrary Origin
and
Access-Control-Allow-Credentials: true
```

Do not treat CORS as vulnerable without understanding the auth model and whether browser credentials are involved.

## Authentication behavior checks

Use test accounts only.

Check safely:

```txt
- invalid login returns generic error;
- logout ends session;
- protected route denies unauthenticated access;
- normal user cannot access admin route;
- user A cannot access user B's test-owned object.
```

Do not perform brute force, password spraying, or real account takeover attempts.

## Final note

Commands are evidence helpers, not proof by themselves. Always interpret results in context and recommend practical fixes.
