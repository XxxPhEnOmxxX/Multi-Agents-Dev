# Tasks

## Goal

Break an approved spec/design into granular, sequential, independently verifiable tasks.

Skip this phase when the feature has three or fewer obvious implementation steps. In that case, Execute must still list inline atomic steps before writing code.

## Task rule

One task should usually be one of these:

- one component;
- one function;
- one API endpoint;
- one migration;
- one adapter;
- one cohesive file change.

Avoid vague tasks like `implement auth` or `create dashboard`. Split them until each task has a clear done condition and gate.

## Process

1. Read `spec.md` and `design.md`.
2. Discover project test/build/lint commands from project files or CI.
3. Generate a Test Coverage Matrix.
4. Generate Gate Check Commands.
5. Break work into atomic tasks.
6. Define dependencies.
7. Group tasks into ordered phases.
8. Validate granularity, dependencies, and test co-location before approval.

## Test Coverage Matrix

Every task that creates/modifies a code layer requiring tests must include those tests in the same task. Do not create separate `write tests later` tasks.

```markdown
## Test Coverage Matrix

| Code Layer | Required Test Type | Coverage Expectation | Location Pattern | Run Command |
| --- | --- | --- | --- | --- |
| Domain / business logic | unit | ACs and edge cases mapped 1:1 where applicable | [project pattern] | [command] |
| API / controller / route | integration/e2e | happy path, edge cases, and error paths | [project pattern] | [command] |
| Repository / adapter | integration/unit | key paths and failures | [project pattern] | [command] |
| Config / schema / entity | none/build | build/lint gate only unless behavior exists | [project pattern] | [command] |
```

## Gate Check Commands

```markdown
## Gate Check Commands

| Gate Level | When to Use | Command |
| --- | --- | --- |
| Quick | unit-only task | [unit command] |
| Full | integration/e2e task | [unit + integration/e2e command] |
| Build | phase end or config-only task | [build + lint + all tests] |
```

Do not invent commands. Discover them from the repository or ask the user.

## Output: `.specs/features/[feature]/tasks.md`

```markdown
# [Feature] Tasks

**Spec:** `.specs/features/[feature]/spec.md`
**Design:** `.specs/features/[feature]/design.md`
**Status:** Draft | Approved | In Progress | Done

## Test Coverage Matrix

[Generated from project conventions and spec.]

## Gate Check Commands

[Generated from project commands.]

## Execution Plan

### Phase 1: Foundation

T1 -> T2 -> T3

### Phase 2: Core Implementation

T4 -> T5 -> T6

## Task Breakdown

### T1: [Task title]

**What:** [exact deliverable]
**Where:** `path/to/file`
**Depends on:** None | T[N]
**Reuses:** [existing code/pattern]
**Requirement:** FEAT-01

**Tools:**

- MCP: [tool or NONE]
- Skill: [skill or NONE]

**Done when:**

- [ ] [binary criterion]
- [ ] Gate check passes: `[command]`
- [ ] Test count: [N] tests pass with no silent deletion/skip

**Tests:** unit | integration | e2e | none
**Gate:** quick | full | build
**Commit:** `feat(scope): description`
```

## Pre-approval validation

Before showing tasks as ready, produce these checks:

### Task Granularity Check

| Task | Scope | Status |
| --- | --- | --- |
| T1 | one endpoint | ok |

### Diagram-Definition Cross-Check

| Task | Depends on | Diagram shows | Status |
| --- | --- | --- | --- |
| T2 | T1 | T1 -> T2 | match |

### Test Co-location Validation

| Task | Code Layer | Matrix Requires | Task Says | Status |
| --- | --- | --- | --- | --- |
| T1 | service | unit | unit | ok |

Any failing row means the task plan must be fixed before execution.
