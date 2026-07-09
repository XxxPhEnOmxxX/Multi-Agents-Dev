# Execute / Implement

## Goal

Implement one task at a time with surgical changes, verification, and traceable commits.

## Before coding

Read `coding-principles.md` completely, then state:

```txt
Assumptions:
Files to touch:
Success criteria:
Gate command:
```

Do not write code before these are explicit.

## Sub-agent decision

If a formal `tasks.md` exists, count all tasks and pack phases into batches of about seven tasks each, without splitting phases. If that creates more than one batch, offer sub-agents before execution.

If there is no `tasks.md`, list inline atomic steps first:

```txt
1. [step] -> files: [files] -> verify: [gate] -> commit: [message]
2. [step] -> files: [files] -> verify: [gate] -> commit: [message]
```

If the inline list reveals more than five steps or complex dependencies, stop and create `tasks.md`.

## Per-task cycle

For each task:

1. Pick the next unblocked task.
2. Verify dependencies.
3. State implementation plan.
4. Write tests from spec acceptance criteria when the task requires tests.
5. Implement the minimum code needed.
6. Run the gate command.
7. Confirm test count did not shrink.
8. Run a post-gate adequacy review.
9. Commit only the task files.
10. Update task status and requirement traceability.

## Test integrity constraints

Never:

- weaken assertions to pass;
- delete tests to reduce failures;
- skip or mark tests pending to bypass failure;
- rewrite the spec-defined outcome silently;
- change unrelated files while implementing a task.

If a test appears wrong against the spec, stop and ask before changing it.

## Post-gate adequacy review

Produce evidence for task completion:

```markdown
## Implementing T[N]: [Title]

**Dependencies:** [ok/blocked]
**Tests:** [unit/integration/e2e/none]
**Gate:** [quick/full/build]

### Pre-Implementation

- **Assumptions:** [text]
- **Files to touch:** [files]
- **Success criteria:** [criteria]

### Verification

- **Command:** [gate command]
- **Result:** [passed/failed]
- **Test count:** [N]

### Coverage Evidence

| Criterion / AC / edge case | `file:line` + assertion | Spec-defined outcome | Covered? |
| --- | --- | --- | --- |
| [criterion] | `path:line` | [outcome] | yes/no/gap |

### Reverse Mapping

| Assertion | Maps to | Keep? |
| --- | --- | --- |
| `path:line` | FEAT-01 | yes |

**Status:** Complete | Blocked | Partial
```

## Commit rule

Use one atomic commit per task after verification passes.

Format:

```txt
<type>(<scope>): <imperative description>
```

Examples:

```txt
feat(auth): add login command handler
fix(bookings): prevent duplicate slot reservation
```

## Last task rule

After the last task in a feature or deliverable priority group, run independent validation. Execute is not complete until validation passes or gaps are routed into fix tasks.
