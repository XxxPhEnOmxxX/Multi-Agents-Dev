# [Feature Name] Tasks

## Execution Order

```txt
T1 -> T2 -> T3
```

## Test Coverage Matrix

| Layer | Test Type | Required? | Command |
| --- | --- | --- | --- |
| Domain | Unit | Yes | |
| Application | Unit/Integration | Yes | |
| Interface | Integration/E2E | If applicable | |
| Infrastructure | Integration | If applicable | |

## Gates

| Gate | Command | Required? |
| --- | --- | --- |
| Architecture | | Yes |
| Unit Tests | | Yes |
| Lint | | If available |
| Typecheck | | If available |
| Build | | Before merge |

## Tasks

### T1: [Task Name]

**Goal**:

**Scope**:

**Files likely affected**:

```txt
[path]
```

**Depends on**:

**Requirement IDs**:

**Suggested agent**:

**Done when**:

- [ ]
- [ ]
- [ ] Gate passes

**Tests**:

**Out of scope**:

**Suggested commit**:

```txt
feat(scope): description
```

## Handoff Notes
