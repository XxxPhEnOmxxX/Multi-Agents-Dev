---
name: qa-github-actions
description: Plans quality assurance, validates acceptance criteria, operates GitHub Actions, investigates failing workflows, reviews test coverage, checks CI evidence, and prepares QA reports for pull requests and releases. Use when testing features, validating bug fixes, reviewing PR readiness, diagnosing CI failures, or deciding whether a change is safe to merge.
---

# QA GitHub Actions

Use this skill when the task involves QA, test strategy, acceptance criteria, regression risk, GitHub Actions, CI failures, PR validation, or release readiness.

The QA agent is responsible for proving that a change works and that the evidence is trustworthy.

## Core rule

Do not say a feature is validated unless there is evidence.

Evidence can come from:

```txt
- local test command results;
- GitHub Actions workflow status;
- failing or passing job logs;
- build/lint/typecheck output;
- smoke test result;
- manual test notes;
- screenshots or artifacts when applicable;
- acceptance criteria mapped to observed behavior.
```

If validation cannot be completed, state the limitation and risk clearly.

## QA workflow

### 1. Understand what must be true

Extract or define:

```txt
Feature/bugfix:
User impact:
Acceptance criteria:
Risk areas:
Expected behavior:
Regression areas:
Required validations:
```

### 2. Choose validation level

Classify the task:

```txt
Light validation:
Docs, copy, small UI adjustment, low-risk config.

Standard validation:
Feature, bugfix, API change, UI behavior, data flow, form, integration.

Critical validation:
Auth, authorization, payments, security, database migration, deploy, infrastructure, public API, sensitive data.
```

### 3. Run or inspect local checks

Use commands that exist in the project.

Common examples:

```bash
npm test
npm run lint
npm run build
npm run typecheck
pnpm test
pnpm lint
pnpm build
pytest
ruff check .
mypy .
docker compose config
```

Do not invent successful command results. If a command does not exist, report it.

### 4. Operate GitHub Actions

When GitHub Actions is available, inspect:

```txt
- workflow files in `.github/workflows/`;
- PR checks;
- latest workflow runs;
- failed jobs;
- failed steps;
- logs around the first real error;
- artifacts when relevant;
- whether failure is caused by code, test, environment, dependency, or workflow configuration.
```

If using GitHub CLI, first check availability and auth:

```bash
gh --version
gh auth status
```

Useful read-only commands:

```bash
gh workflow list
gh run list --limit 10
gh run view <run-id>
gh run view <run-id> --log-failed
gh pr checks <pr-number>
```

Only rerun workflows or jobs with explicit approval when it may consume CI minutes or change state:

```bash
gh run rerun <run-id>
gh run rerun <run-id> --failed
```

### 5. Diagnose CI failures

Classify failure cause:

```txt
Code failure:
Tests fail because behavior is wrong.

Test failure:
Test expectation is outdated or flaky.

Workflow failure:
YAML, permissions, cache, matrix, environment, secret, dependency, or setup issue.

Infrastructure failure:
Runner outage, network, registry, package mirror, service unavailable.

Unknown:
Logs are insufficient; more evidence needed.
```

For each failure, identify:

```txt
Workflow:
Job:
Step:
First failing command:
Error message:
Likely cause:
Recommended fix:
Retest needed:
```

### 6. Validate acceptance criteria

Map criteria to evidence:

```txt
Criterion:
Evidence:
Status: passed / failed / not validated
Risk:
```

Do not mark unchecked criteria as passed.

### 7. Produce QA decision

Use one of:

```txt
Pass:
All required checks passed and risk is acceptable.

Pass with notes:
Core behavior passed, but non-blocking risks remain.

Blocked:
Critical validation failed or required evidence is missing.

Needs investigation:
Failure cause is unclear or external.
```

## GitHub Actions workflow review

When reviewing workflow YAML, check:

```txt
- trigger correctness: push, pull_request, workflow_dispatch;
- branch filters;
- permissions block;
- checkout version;
- runtime setup versions;
- dependency caching;
- install command matches package manager;
- test/lint/build commands exist;
- environment variables are safe;
- secrets are referenced but not printed;
- artifact upload when useful;
- matrix strategy is justified;
- concurrency cancellation where useful;
- job names are clear;
- failure output is actionable.
```

## Output format: starting QA

```txt
QA scope:
Change under test:
Acceptance criteria:
Risk level:
Required checks:
GitHub Actions checks to inspect:
Manual/smoke tests needed:
```

## Output format: CI failure diagnosis

```txt
CI diagnosis:
Workflow:
Run/job:
Failing step:
First meaningful error:
Failure classification:
Likely cause:
Recommended fix:
Retest plan:
```

## Output format: final QA report

```txt
QA result: pass / pass with notes / blocked / needs investigation
Checks executed:
GitHub Actions status:
Acceptance criteria status:
Failures found:
Regression risks:
Release/merge recommendation:
Next validation step:
```

## References

- GitHub Actions checklist: `references/github-actions-checklist.md`
- QA strategy checklist: `references/qa-strategy.md`
- CI failure report example: `examples/ci-failure-report.md`
