# Coding Principles

Read before implementation.

## Before coding

- State assumptions explicitly.
- Name uncertainty instead of guessing.
- Present material alternatives when multiple valid interpretations exist.
- Push back on unnecessary complexity.
- Touch only the files required by the task.

## During implementation

### Simplicity

- No features beyond the task.
- No abstractions for single-use code.
- No speculative configurability.
- No error handling for impossible scenarios.
- Prefer the smallest code that satisfies the spec and tests.

### Surgical changes

- Do not refactor adjacent code unless the task requires it.
- Match existing project style.
- Do not delete unrelated dead code.
- Remove only imports, variables, or functions orphaned by your own changes.

### Test integrity

Never:

- weaken a test assertion to pass;
- delete a test to reduce failures;
- skip/disable/pending a failing test;
- modify a task's tests after implementation just to make code pass.

Tests represent spec behavior. Implementation conforms to tests that conform to the spec.

## After each change

Ask:

```txt
Would a senior engineer call this overcomplicated?
```

If yes, simplify before proceeding.
