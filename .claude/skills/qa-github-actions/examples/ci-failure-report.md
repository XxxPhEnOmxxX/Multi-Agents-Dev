# Example: CI Failure Report

Use this format when diagnosing a failed GitHub Actions run.

## CI diagnosis

```txt
Workflow: CI
Run/job: build-and-test / test
Failing step: Run tests
First meaningful error: Expected status 200, received 500 in auth.spec.ts
Failure classification: Code failure
Likely cause: Recent auth middleware change breaks valid test login flow.
Recommended fix: Review middleware user extraction and update regression test if behavior intentionally changed.
Retest plan: Run npm test locally and rerun failed GitHub Actions job after fix.
```

## Evidence summary

```txt
The workflow reached dependency installation and build successfully.
The first failing command was npm test.
The failure is not a runner or cache issue because dependencies installed and the test runner executed.
```

## QA decision

```txt
QA result: blocked
Reason: Required automated tests failed.
Merge recommendation: Do not merge until failing test is resolved or intentionally updated with explanation.
```

## Bad report example

```txt
CI failed. Fix tests.
```

Why it is bad:

```txt
- no workflow/job/step;
- no first meaningful error;
- no classification;
- no recommended fix;
- no retest plan;
- no merge decision.
```

## Pass with notes example

```txt
QA result: pass with notes
Checks executed:
- npm run lint: passed
- npm test: passed
- npm run build: passed
- GitHub Actions CI: passed

Acceptance criteria status:
- Admin can create user: passed via e2e smoke test
- Non-admin cannot create user: passed via integration test
- Error message appears for invalid email: passed via unit test

Notes:
- No visual regression artifact is configured yet.
- Recommend adding Playwright screenshot artifacts for future UI-heavy PRs.

Merge recommendation:
Safe to merge.
```
