# Sub-Agent Delegation

## Goal

Use sub-agents only when they reduce context pressure and improve execution discipline.

Sub-agents are not used to parallelize risky work blindly. They execute ordered batches and report compact evidence.

## Phase vs batch

- **Phase:** semantic/dependency unit from `tasks.md`.
- **Batch:** execution unit assigned to a worker, usually one or more consecutive phases.

Never split a phase across workers.

## When to offer workers

Count total tasks from `tasks.md`.

| Task count | Behavior |
| --- | --- |
| 1-8 | execute inline |
| 9+ | offer batched workers |

Offer first. Do not dispatch workers without user approval.

## Batching rule

Pack consecutive whole phases into about seven tasks per worker.

Example:

```txt
Phase 1: 3 tasks
Phase 2: 4 tasks
Phase 3: 6 tasks
Phase 4: 5 tasks

Batch 1: Phase 1 + Phase 2 = 7 tasks
Batch 2: Phase 3 = 6 tasks
Batch 3: Phase 4 = 5 tasks
```

If a phase has more than about ten tasks, the task plan is probably too coarse. Split the phase at a real cohesion/dependency boundary during Tasks.

## Worker input

Each worker receives only:

- assigned phase/task definitions;
- relevant `spec.md` and `design.md` excerpts;
- Test Coverage Matrix;
- Gate Check Commands;
- `coding-principles.md`;
- exact branch/commit expectations.

## Worker behavior

A worker:

1. Executes tasks in order.
2. Runs the required gate after each task.
3. Creates one atomic commit per task.
4. Stops on failure or blocker.
5. Reports compact evidence.
6. Never spawns another sub-agent.

## Worker summary

```txt
Batch [phases] complete:
- Tasks done: [T1 commit, T2 commit]
- Tests: [N passed, 0 failed]
- Deviations/blockers: [none or details]
```

## Verifier

The Verifier always runs after the final task of a feature or deliverable priority group.

The Verifier is separate from the author. It validates the implementation against the spec and does not fix code.

Verifier input:

- `spec.md`;
- feature diff or commit range;
- test files in scope;
- `validate.md`.

Verifier output:

```txt
Validation: [feature] — PASS/FAIL
Spec-anchored check: [N/N]
Gate: [passed/failed]
Sensor: [N mutations, N killed, N survived]
Report: .specs/features/[feature]/validation.md
Ranked gaps: [if any]
```

If validation fails, the orchestrator turns ranked gaps into fix tasks and re-runs validation. Stop after three fix/verify loops and escalate.
