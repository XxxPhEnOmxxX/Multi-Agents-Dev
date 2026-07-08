---
name: security-by-design
description: Use this skill when reviewing or implementing authentication, authorization, secrets, input validation, logging, permissions, file uploads, integration credentials, or sensitive customer data handling.
---

# Security by Design

## Purpose

Build security into the design instead of treating it as a final review step.

## Checklist

- Authentication is explicit and tested.
- Authorization happens before returning customer data or other business-sensitive records.
- Secrets are loaded from secure configuration and never committed.
- Logs do not expose tokens, passwords, customer private data, or raw external responses.
- External input is validated before reaching use cases.
- SQL or ORM queries avoid injection-prone string construction.
- HTTP clients use timeouts and controlled retry behavior.
- File uploads validate type, size, storage path, and access control.
- Destructive operations require explicit permission and audit trail.
- Agent permissions should deny dangerous shell and git operations by default.

## Integration Security

- Store third-party integration credentials outside code.
- Mask credentials in errors and logs.
- Do not pass raw vendor payloads to clients unless explicitly sanitized.
- Treat webhooks and bot inputs as untrusted.

## Expected Output

- Finding severity.
- Affected boundary.
- Exploit or failure scenario.
- Concrete remediation.
- Test or control to prevent regression.
