# Validate / Verify

## Goal

Verify that the implementation satisfies the spec, has meaningful tests, and remains inside scope.

Validation is part of Execute. It is not optional after the final task.

## Verification levels

1. **Per-task verification:** implementer checks each task before commit.
2. **Feature-level validation:** independent verifier checks the complete feature after the final task.
3. **Interactive UAT:** only for user-facing behavior where human judgment matters.

## Independent verifier contract

The verifier must be fresh relative to the author of the implementation.

The verifier receives:

- `spec.md` as source of truth;
- `tasks.md` if it exists;
- commit range or feature branch diff;
- test files in scope;
- this validation checklist.

The verifier does **not** fix code. It reports gaps and creates fix-task recommendations.

## Process

1. Confirm all tasks are complete or identify partial/blocking items.
2. Run the build-level gate command from `tasks.md` or discovered project commands.
3. Re-derive acceptance criteria coverage from the spec.
4. Apply evidence-or-zero: no `file:line` assertion means not covered.
5. Confirm asserted values match spec-defined expected outcomes.
6. Check edge cases.
7. Run a discrimination sensor in scratch state.
8. Check coding principles and scope boundaries.
9. Write `validation.md`.
10. Distill lessons if the validation found grounded failures.

## Discrimination sensor

The goal is to prove tests can detect meaningful regressions.

Use a scratch state only:

- temp worktree;
- temp copy;
- stash/apply/restore;
- other safe throwaway method.

Inject 1-3 behavior-level faults for normal features:

- flip a condition;
- change a return value;
- remove a required side effect;
- introduce an off-by-one bug;
- change a status or state transition.

Run the relevant tests. A good test suite should fail. Restore the scratch state afterward.

If the mutant survives, create a fix task to strengthen behavior coverage.

## Validation report

Write `.specs/features/[feature]/validation.md`:

```markdown
# [Feature] Validation

**Date:** YYYY-MM-DD
**Spec:** `.specs/features/[feature]/spec.md`
**Diff range:** [branch or commit range]
**Verifier:** independent verifier

## Task Completion

| Task | Status | Notes |
| --- | --- | --- |
| T1 | done | - |

## Spec-Anchored Acceptance Criteria

| Criterion | Spec-defined outcome | `file:line` + assertion | Result |
| --- | --- | --- | --- |
| WHEN X THEN Y | [outcome] | `path:line` | pass/gap |

## Edge Cases

| Edge case | Evidence | Result |
| --- | --- | --- |
| [case] | [file:line] | pass/gap |

## Gate Check

- **Command:** [command]
- **Result:** [passed/failed]
- **Test count before:** [N]
- **Test count after:** [N]
- **Skipped tests:** [list or none]

## Discrimination Sensor

| Mutation | Location | Killed? | Notes |
| --- | --- | --- | --- |
| [mutation] | `path:line` | yes/no | [notes] |

## Code Quality

| Principle | Status |
| --- | --- |
| Minimum code | pass/fail |
| Surgical changes | pass/fail |
| No scope creep | pass/fail |
| Tests map to spec | pass/fail |

## Fix Plans

[Only if gaps exist.]

## Summary

**Overall:** Ready | Issues | Not Ready
**Spec check:** [N/N]
**Gate:** [passed/failed]
**Sensor:** [N/N killed]
```

## Chat summary

Return a compact result:

```txt
Validation: [feature] — PASS/FAIL
Spec-anchored check:
Gate:
Sensor:
Report:
Ranked gaps:
```
