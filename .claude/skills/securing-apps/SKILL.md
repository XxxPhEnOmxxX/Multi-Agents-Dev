---
name: securing-apps
description: Reviews application security and runs safe, authorized security checks for web apps, APIs, authentication, authorization, configuration, dependencies, Docker, secrets, headers, CORS, logging, and deployment risk. Use when analyzing security posture, preparing a security review, testing a system you are authorized to assess, or validating fixes before release.
---

# Securing Apps

Use this skill to analyze and test the security of systems the user owns or is explicitly authorized to assess.

The goal is defensive: find realistic weaknesses, explain impact, recommend fixes, and provide safe validation evidence without causing disruption.

## Safety boundaries

Before any test, confirm scope.

Do not perform or suggest:

```txt
- testing systems without authorization;
- credential theft, phishing, persistence, stealth, malware, or backdoors;
- brute force, password spraying, or account takeover attempts;
- destructive fuzzing, denial-of-service, or high-volume scanning;
- data exfiltration beyond minimal proof of impact;
- bypassing rate limits, WAFs, monitoring, or legal controls;
- publishing sensitive findings without permission.
```

When in doubt, choose static review, local testing, or low-risk validation.

## Required starting context

Before testing, identify:

```txt
System:
Owner/authorization:
Environment: local / staging / production
Allowed targets:
Forbidden targets:
Authentication method:
User roles:
Sensitive data involved:
Acceptable test intensity:
Rollback/contact plan:
```

If the target is production, prefer read-only and low-impact tests.

## Security review workflow

### 1. Map the attack surface

Identify:

```txt
- public routes and APIs;
- authentication and session flows;
- user roles and authorization boundaries;
- file upload/download paths;
- webhooks and callbacks;
- admin panels;
- database access patterns;
- third-party integrations;
- exposed ports and services;
- secrets and environment handling;
- Docker, reverse proxy, TLS, and deployment configuration.
```

### 2. Classify risk areas

Review at least:

```txt
Authentication:
- login, logout, password reset, session expiry, token storage, MFA if present.

Authorization:
- horizontal access, vertical access, admin-only actions, object ownership checks.

Input validation:
- server-side validation, schema validation, type coercion, unexpected fields.

Injection risk:
- database queries, shell commands, templates, logs, redirects, headers.

API security:
- method handling, status codes, error shape, pagination, rate limits, CORS.

Frontend security:
- token exposure, unsafe HTML, open redirects, mixed content, sensitive data in client state.

Configuration:
- security headers, TLS assumptions, debug mode, CORS, cookies, proxy trust.

Secrets:
- .env, keys, tokens, credentials, service accounts, logs and build artifacts.

Dependencies:
- vulnerable packages, outdated runtimes, risky transitive dependencies.

Infrastructure:
- Docker privileges, exposed ports, volumes, network boundaries, root containers.

Logging and audit:
- security events, sensitive log leakage, traceability, admin actions.
```

### 3. Choose safe tests

Prefer tests that are:

```txt
- authorized;
- reproducible;
- low-impact;
- rate-limited;
- scoped to local/staging when possible;
- focused on proving risk without extracting real data.
```

Examples of safe validation types:

```txt
- static code review;
- dependency audit;
- configuration review;
- HTTP header inspection;
- CORS preflight check;
- auth/session behavior check with test accounts;
- authorization check using owned test records;
- input validation check using harmless malformed data;
- Docker Compose configuration inspection;
- secret scanning of repository history and current files.
```

### 4. Report findings clearly

For each finding, use:

```txt
Title:
Severity: critical / high / medium / low / info
Area:
Evidence:
Impact:
Affected component:
Safe reproduction summary:
Recommended fix:
Validation after fix:
Residual risk:
```

Do not include real secrets, tokens, customer data, or exploit-ready payload collections in the final report.

### 5. Prioritize remediation

Prioritize by:

```txt
1. Exposure to unauthenticated users
2. Authentication/authorization bypass
3. Sensitive data exposure
4. Remote code or command execution risk
5. Production misconfiguration
6. Dependency with known exploitability
7. Missing logs or weak detection
8. Defense-in-depth improvements
```

## Severity guide

```txt
Critical:
Unauthenticated control, sensitive data exposure at scale, code execution, credential compromise.

High:
Privilege escalation, broken authorization, account takeover path, sensitive admin function exposure.

Medium:
Important misconfiguration, weak validation, limited data exposure, missing protection with realistic abuse path.

Low:
Hardening issue, missing non-critical header, minor information disclosure, low-impact dependency.

Info:
Observation, best-practice improvement, documentation gap, future hardening.
```

## Validation commands

Use commands that exist in the project. Do not invent successful results.

Common examples:

```bash
git status
git diff --stat
git diff --check
npm audit --audit-level=moderate
npm run lint
npm test
npm run build
pip-audit
safety check
pytest
docker compose config
```

For HTTP checks, prefer low-impact requests and document exactly what was checked.

## Output format

When starting:

```txt
Security scope:
Environment:
Allowed tests:
Forbidden tests:
Main risk areas:
Planned checks:
Safety constraints:
```

When finishing:

```txt
Security review summary:
Findings by severity:
Evidence collected:
Tests executed:
Fixes recommended:
Validation plan:
Risks that remain:
```

## References

- Security checklist: `references/security-checklist.md`
- Safe test commands: `references/safe-test-commands.md`
- Report example: `examples/security-review-report.md`
