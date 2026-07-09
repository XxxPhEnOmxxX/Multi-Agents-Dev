# Memory Layer

## Goal

Persist project-level decisions and pause/resume state without loading a full conversation history.

## File

`.specs/STATE.md`

## Shape

```markdown
# STATE

## Decisions

[AD-NNN entries]

## Handoff

[current pause/resume snapshot]
```

## Decisions section

Use for project-level decisions only: conventions, constraints, patterns, technology choices, cross-cutting rules, or architecture decisions that future features must respect.

Format:

```markdown
### AD-001

- **Decision:** [one sentence]
- **Reason:** [why]
- **Trade-off:** [what is given up]
- **Scope:** [layers/features/packages]
- **Date:** YYYY-MM-DD
- **Status:** active | superseded by AD-NNN
```

Feature-local decisions belong in that feature's `design.md`, not in `STATE.md`.

## Handoff section

Use when pausing, ending, or resuming work.

Format:

```markdown
## Handoff

- **Feature:** [feature name / .specs path]
- **Phase / Task:** [current phase or task]
- **Completed:** [task IDs or none]
- **In-progress:** [file:line or none]
- **Next step:** [one exact next step]
- **Blockers:** [none or blocker]
- **Uncommitted files:** [files or none]
- **Branch:** [branch]
```

## Section-scoped write rule

Never overwrite the whole file for a section update.

- Design appends only to `## Decisions`.
- Pause replaces only `## Handoff`.
- Resume reads both sections.

Destroying the Decisions section during a handoff is data loss. Reordering decision IDs is also data loss.

## Resume procedure

1. Read `.specs/STATE.md`.
2. Confirm active decisions.
3. Read Handoff.
4. Open the referenced feature files only as needed.
5. Propose the next step before writing.
