---
name: code-quality
description: Use this skill when improving maintainability, naming, structure, duplication, error handling, readability, type safety, or general engineering quality.
---

# Code Quality

## Purpose

Keep code understandable, testable, maintainable, and aligned with existing project patterns.

## Principles

- Prefer clear names over comments that explain unclear code.
- Keep functions small enough to reason about.
- Keep modules cohesive.
- Avoid premature abstractions.
- Remove meaningful duplication, not harmless similarity.
- Make invalid states hard to represent.
- Prefer explicit errors over silent failures.
- Match the existing style of the repository.

## Workflow

1. Read nearby code before changing style.
2. Identify the smallest maintainability problem.
3. Check whether an abstraction already exists.
4. Refactor only within the task scope.
5. Preserve behavior with tests.
6. Avoid broad formatting churn.

## Review Checklist

- Names reflect domain intent.
- Error paths are handled.
- Types or schemas prevent invalid inputs.
- Functions have one clear responsibility.
- No hidden coupling to external payloads.
- No unnecessary global state.
- No unrelated refactors.

## Expected Output

- Quality issue.
- Reason it matters.
- Minimal correction.
- Verification performed.
