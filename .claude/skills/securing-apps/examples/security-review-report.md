# Example: Security Review Report

Use this as a reporting shape. Do not copy findings that were not actually verified.

## Security review summary

```txt
System:
Environment:
Date:
Reviewer:
Authorization:
Allowed tests:
Forbidden tests:
```

## Executive summary

```txt
Overall risk:
Main concern:
Release recommendation:
```

Example:

```txt
Overall risk: Medium
Main concern: Authorization checks need stronger server-side validation on record-specific API routes.
Release recommendation: Do not release admin features until high-risk authorization checks are fixed and retested.
```

## Findings by severity

```txt
Critical: 0
High: 1
Medium: 2
Low: 3
Info: 2
```

## Finding format

### Finding 1 — User can access another user's test record

```txt
Severity: High
Area: Authorization
Affected component: GET /api/records/:id
Evidence: Using two authorized test accounts, account A could request a test record owned by account B.
Impact: A normal user may view data belonging to another user if they know or guess an ID.
Safe reproduction summary: Verified with test records only. No real customer data accessed.
Recommended fix: Enforce object ownership server-side before returning the record.
Validation after fix: Repeat the same test and confirm account A receives 403 or 404 for account B's record.
Residual risk: Check other ID-based routes for the same pattern.
```

## Tests executed

```txt
- Static route review
- Authenticated test account checks
- CORS preflight check
- Security header review
- Dependency audit
- Deployment config review
```

## Commands/evidence

```txt
Command: npm audit --audit-level=moderate
Result: completed, 0 high/critical findings

Command: deployment config validation (platform equivalent of a config lint/dry-run)
Result: completed, config parsed successfully

Command: curl -I https://example.com/
Result: headers reviewed; HSTS missing in production HTTPS response
```

Do not paste secrets, cookies, tokens, private customer data, or sensitive logs.

## Recommended remediation plan

```txt
1. Fix high severity authorization issue.
2. Add regression tests for object ownership checks.
3. Add missing security headers at reverse proxy/app layer.
4. Review similar routes for repeated authorization pattern.
5. Re-run validation before release.
```

## Release recommendation

```txt
Block release until high severity findings are fixed.
Medium and low findings can be tracked if the owner accepts residual risk.
```
