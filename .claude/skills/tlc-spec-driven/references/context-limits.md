# Context Limits

## Goal

Keep spec-driven work useful without overloading the model context.

## Target

Keep loaded context under about 40k tokens whenever possible.

## File size guidance

| File | Target max | Warning |
| --- | --- | --- |
| `spec.md` | ~5k tokens | getting too detailed or mixing design |
| `design.md` | ~8k tokens | too many examples or unrelated architecture |
| `tasks.md` | ~10k tokens | tasks too coarse or too many phases |
| `validation.md` | evidence-focused | avoid raw logs unless essential |

## Load only what is needed

Do not load:

- multiple feature specs at the same time;
- unrelated architecture docs;
- full logs when a summary and failing excerpt are enough;
- every skill reference just because this skill is active.

Load:

- current feature spec;
- current task section;
- current design sections directly relevant to the task;
- confirmed lessons only;
- validation checklist only when validating.

## Status footer

When context is getting large, add a short footer:

```txt
Context: moderate — loaded spec, design, current task, validation checklist.
Optimization: avoid loading unrelated feature specs.
```

## Rule

Context economy is a quality feature. Smaller focused context usually produces better implementation.
