# Lessons Layer

## Goal

Turn real validation failures into reusable, project-local guidance.

Lessons are not opinions. A lesson must be grounded in a validation signal.

## Files

| File | Owner | Purpose |
| --- | --- | --- |
| `.specs/lessons.json` | script | canonical machine state |
| `.specs/LESSONS.md` | script | rendered guidance |
| `scripts/lessons.py` | tool | mutate/list lessons |

Do not hand-edit `.specs/LESSONS.md` or `.specs/lessons.json` when the script is available.

## Read confirmed lessons

At Specify and Design, load only confirmed lessons:

```bash
python3 .claude/skills/tlc-spec-driven/scripts/lessons.py list --status confirmed
```

Or filter by scope/query:

```bash
python3 .claude/skills/tlc-spec-driven/scripts/lessons.py list --status confirmed --scope auth
python3 .claude/skills/tlc-spec-driven/scripts/lessons.py list --status confirmed --query idempotency
```

Do not load candidate or quarantined lessons as guidance.

## Write lessons

After `validation.md`, record lessons only for grounded signals:

| Signal in validation | `--signal` |
| --- | --- |
| acceptance criterion gap | `ac_gap` |
| surviving mutant | `surviving_mutant` |
| spec precision gap | `spec_precision_gap` |
| SPEC_DEVIATION | `spec_deviation` |
| build/test gate failure | `gate_fail` |

Command:

```bash
python3 .claude/skills/tlc-spec-driven/scripts/lessons.py add \
  --feature "[feature-folder]" \
  --signal "[signal]" \
  --source "[validation.md location, AC id, mutant id, or file:line]" \
  --text "[one terse reusable rule]" \
  --scope "[optional scope]"
```

## Phrasing rules

Good:

```txt
Assert the exact persisted status value, not just that a status field exists.
```

Bad:

```txt
The test on line 88 was weak.
```

A lesson should be codebase-general, terse, and actionable.

## Clean pass

If validation passes with no meaningful signal, write no lesson. That is correct.

## No-script fallback

If Python cannot run, maintain `.specs/LESSONS.md` manually using the same rules, and state that bookkeeping is degraded.
