# GitHub Actions Checklist

Use this checklist when reviewing, operating, or debugging GitHub Actions workflows.

## Workflow file location

Workflow files usually live in:

```txt
.github/workflows/*.yml
.github/workflows/*.yaml
```

## Basic workflow review

Check:

```txt
- Workflow has a clear name.
- Trigger matches expected behavior.
- Pull request checks run before merge.
- Push checks run on protected branches.
- workflow_dispatch exists when manual execution is useful.
- Jobs have clear names.
- Steps have useful names.
```

## Permissions

Prefer explicit least privilege:

```yaml
permissions:
  contents: read
```

Only expand permissions when the workflow actually needs them.

Watch for risky defaults:

```txt
- broad write permissions;
- pull_request_target usage without strict controls;
- secrets exposed to untrusted forks;
- scripts that print env or secrets;
- third-party actions not pinned or reviewed.
```

## Runtime setup

Check:

```txt
- actions/checkout is present.
- Node/Python/Java/etc version matches the project.
- Package manager matches lockfile.
- Install command is correct.
- Cache key uses lockfile when possible.
- Build/test commands exist in the project.
```

Examples:

```yaml
- uses: actions/checkout@v4
- uses: actions/setup-node@v4
  with:
    node-version: 20
    cache: npm
```

## Common Node.js checks

```txt
- npm ci is used when package-lock.json exists.
- pnpm install --frozen-lockfile is used when pnpm-lock.yaml exists.
- yarn install --immutable is used when Yarn Berry is used.
- lint, test, build, and typecheck match package.json scripts.
```

## Common Python checks

```txt
- Python version is explicit.
- Dependencies are installed from the correct file or tool.
- pytest/ruff/mypy commands match project config.
- Virtual environment or tool cache is handled consistently.
```

## Failure triage

When a workflow fails, identify the first meaningful failure.

Do not stop at generic messages like:

```txt
Process completed with exit code 1
Error: Process completed with exit code 1
```

Find the real error above that line.

Classify failure:

```txt
Code failure
Test failure
Workflow configuration failure
Missing secret/environment failure
Dependency installation failure
Runner/infrastructure failure
Flaky test
```

## Rerun policy

Rerun only when:

```txt
- failure looks flaky;
- infrastructure failed;
- dependency registry/network failed;
- owner approves rerun;
- rerun is needed after a fix.
```

Do not hide failure by rerunning repeatedly.

## Artifacts and logs

Check artifacts when available:

```txt
- test reports;
- coverage reports;
- screenshots;
- playwright traces;
- build output;
- deployment logs.
```

Do not expose secrets from logs in user-facing reports.

## Release readiness

Before approving merge/release:

```txt
- required checks passed;
- failures are explained;
- acceptance criteria are validated;
- security-sensitive changes had security review;
- migrations/deploy risks are documented;
- flaky tests are not ignored without issue/ticket;
- rollback or mitigation exists for risky changes.
```
