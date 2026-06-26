# Data Access and Migrations

Use this reference when backend work touches persistence, database schema, repositories, ORM models, migrations, indexes, or data integrity.

## Data ownership

Before changing data access, identify:

```txt
- Which module owns the data?
- Which service is allowed to change it?
- Which routes/jobs read it?
- Which frontend screens depend on it?
- Which external integrations depend on it?
```

Avoid unrelated modules writing directly to data they do not own unless the existing architecture requires it.

## Query safety

Prefer:

```txt
- parameterized queries;
- ORM query builders used safely;
- explicit selected fields when returning sensitive objects;
- pagination/limits on list queries;
- indexes for common filters/sorts;
- transactions for dependent writes.
```

Avoid:

```txt
- string-concatenated SQL with user input;
- returning whole records with sensitive fields;
- unbounded list endpoints;
- updating records without ownership/permission conditions;
- hiding database errors without logs.
```

## Transaction guidance

Use transactions when:

```txt
- multiple writes must succeed or fail together;
- creating parent and child records;
- updating balance/counter/status with dependent records;
- writing audit log tied to critical state change;
- processing webhook/event exactly once or safely many times.
```

Consider idempotency when retry is possible.

## Migration rules

Before creating a migration, answer:

```txt
What schema changes?
Is data migration required?
Is the migration backward compatible?
Can old code and new schema coexist during deploy?
Can new code run before migration?
Can rollback safely undo this?
Is backup needed?
```

## Safer migration pattern

For risky production systems, prefer expand-and-contract:

```txt
1. Add new nullable column/table/index.
2. Deploy code that writes both old and new format if needed.
3. Backfill data safely.
4. Read from new format after validation.
5. Remove old column/table only after confidence.
```

## Destructive changes

Treat these as high risk:

```txt
- dropping columns or tables;
- changing column type with data loss risk;
- renaming columns used by running code;
- deleting data;
- changing unique constraints;
- changing primary/foreign keys;
- removing indexes used by hot queries.
```

Require explicit approval and rollback/backup plan before destructive migrations.

## Indexes and constraints

Use constraints to protect invariants where possible:

```txt
- unique email/user identifier;
- foreign keys for relationships;
- not-null for required data;
- check constraints for bounded values when supported;
- indexes for frequent lookup fields.
```

Application validation is useful, but database constraints protect against race conditions and unexpected paths.

## Review output

```txt
Data access review:
- Data owner:
- Queries affected:
- Migration needed:
- Transaction needed:
- Index/constraint impact:
- Backward compatibility:
- Rollback/mitigation:
- Tests needed:
```
