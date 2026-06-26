# Security Checklist

Use this checklist during defensive review of applications, APIs, infrastructure configuration, and release changes.

## Scope and authorization

```txt
- Target belongs to the user or has explicit authorization.
- Environment is identified: local, staging, or production.
- Allowed test intensity is clear.
- Forbidden targets/actions are clear.
- Test accounts are available when needed.
- Production tests are low-impact and rate-limited.
```

## Authentication

```txt
- Login rejects invalid credentials safely.
- Error messages do not reveal whether user/email exists.
- Logout invalidates session/token where applicable.
- Password reset cannot be abused to enumerate users.
- Session/token expiry exists and is enforced.
- Cookies use secure attributes when applicable.
- Tokens are not stored in unsafe client-accessible places unless risk is accepted.
```

## Authorization

```txt
- User can only access own records.
- Non-admin cannot call admin routes.
- API validates authorization server-side, not only in frontend.
- Object ownership is checked by ID-based routes.
- Role changes require proper permission.
- Hidden UI buttons are not treated as security controls.
```

## Input validation

```txt
- Server validates required fields and data types.
- Unexpected fields are ignored or rejected consistently.
- Length limits exist for text fields.
- Numeric ranges are validated.
- File upload type, size, storage path, and access rules are validated.
- User-controlled values are encoded before rendering.
```

## Injection risk

```txt
- Database queries use parameterized patterns or ORM safeguards.
- Shell execution avoids user-controlled input.
- Template rendering avoids unsafe HTML injection.
- Logs do not execute or render untrusted content unsafely.
- Redirect targets are validated.
- Header values are not built directly from untrusted input.
```

## API security

```txt
- HTTP methods are restricted to intended behavior.
- Error responses do not leak stack traces or internals.
- Pagination and limits exist for list endpoints.
- Rate limits exist for sensitive routes.
- CORS allows only intended origins.
- Credentials with CORS are not allowed for arbitrary origins.
- API versioning and contracts are documented where needed.
```

## Frontend security

```txt
- No secrets are bundled into client code.
- Sensitive data is not exposed in localStorage/sessionStorage without reason.
- No unsafe HTML rendering unless sanitized and justified.
- Links with new tabs use safe rel attributes when applicable.
- Error details shown to users are limited and useful.
```

## Headers and browser controls

Review presence and correctness where applicable:

```txt
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options or frame-ancestors
- Referrer-Policy
- Permissions-Policy
- Strict-Transport-Security for HTTPS production
- Secure, HttpOnly, SameSite cookie attributes
```

## Secrets and sensitive data

```txt
- No .env files committed.
- No private keys or certificates committed.
- No real customer data in repository.
- No tokens in logs, frontend bundles, CI output, or screenshots.
- Example configs use placeholders only.
- Secret rotation plan exists if leakage is found.
```

## Dependencies

```txt
- Package manager lockfile exists.
- Dependency audit is reviewed.
- Runtime versions are supported.
- High/critical vulnerabilities are triaged.
- Unused risky dependencies are removed.
```

## Docker and infrastructure

```txt
- Containers avoid privileged mode unless justified.
- Ports are not exposed unnecessarily.
- Volumes do not mount sensitive host paths unnecessarily.
- Services have network separation when useful.
- Containers avoid running as root when practical.
- Healthchecks exist for important services.
- Reverse proxy forwards correct headers safely.
- TLS is terminated and redirected correctly in production.
```

## Logging and audit

```txt
- Auth events are logged without exposing secrets.
- Admin actions are auditable.
- Security-relevant failures are observable.
- Logs do not contain passwords, tokens, cookies, or private data.
- Error tracking avoids leaking sensitive request payloads.
```

## Release decision

Before approving release:

```txt
- Critical findings fixed or release blocked.
- High findings fixed or explicitly accepted by owner.
- Medium findings have remediation plan.
- Tests/validation are documented.
- Residual risks are clear.
```
