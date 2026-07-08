# Sensitive Access Policy

Use this policy whenever a task may require secrets, production access, customer data, destructive commands, or privileged infrastructure operations.

## Sensitive resources

Treat these as sensitive:

```txt
- .env files;
- production credentials;
- API tokens;
- passwords;
- private keys;
- SSH keys;
- certificate private keys;
- OAuth client secrets;
- cloud provider credentials;
- GitHub secrets;
- automation/integration platform credentials and encryption keys;
- database dumps;
- production databases;
- production logs that may include private data;
- customer data;
- payment/billing data;
- personal data;
- deploy keys;
- backup archives.
```

## Permission request format

Before accessing sensitive resources, ask:

```txt
I need permission to access a sensitive resource.

Resource:
Reason:
Access type: read / write / execute
Environment: local / staging / production
Risk:
Safer alternative:
Exact action I will take if approved:
```

Do not proceed until permission is explicit.

## Safer alternatives

When permission is absent, prefer:

```txt
- redacted logs;
- `.env.example` instead of `.env`;
- staging instead of production;
- code review instead of live access;
- user-provided sanitized excerpts;
- manual command instructions for the user to run;
- placeholder secrets in examples;
- screenshots with sensitive values hidden.
```

## Production operations

Production changes require extra caution.

Ask for approval before:

```txt
- restarting production services;
- deploying to production;
- changing proxy/TLS/domain config;
- changing database schema;
- reading production secrets;
- running migrations;
- changing automation platform encryption keys or credentials;
- deleting containers, volumes, networks, backups, or database data;
- running destructive cleanup commands.
```

## Never expose secrets

When reporting back:

```txt
- do not print full tokens;
- do not paste private keys;
- do not include full credentials;
- redact customer data;
- summarize sensitive logs instead of quoting them fully;
- show only the minimum evidence needed.
```

## Approval is scoped

Permission applies only to the exact resource and action approved.

If the task later requires broader access, ask again.

## Emergency fallback

If the system is down and sensitive access is not approved, provide a safe checklist the user can run manually and ask them to paste redacted output.
