# Operational UI Reference

Use this reference when the frontend task involves dashboards, admin panels, CRMs, NOCs, telecom tools, internal systems, monitoring pages, forms, tables, or workflows used during real operation.

## Priority order

```txt
1. Clarity
2. Speed of use
3. Scanability
4. Consistency
5. Accessibility
6. Visual polish
7. Decorative expression
```

Distinctive design is still valuable, but not at the cost of operation.

## Good operational UI

A good operational interface should make it easy to answer:

```txt
What is happening?
What requires action?
What changed?
What is risky?
What can I do next?
What happened after my action?
```

## Layout guidance

Prefer:

```txt
- clear page title and primary action;
- filters close to the data they affect;
- tables for dense operational data;
- cards only when information is comparable and scannable;
- badges for true status, not decoration;
- consistent spacing and alignment;
- obvious empty, loading, error, and success states.
```

Avoid:

```txt
- decorative cards with weak information;
- hidden critical actions;
- excessive gradients;
- animations that delay work;
- vague icons without labels;
- tables that break on mobile without fallback;
- color-only status indicators.
```

## Status and severity

Operational systems usually need status hierarchy.

Example:

```txt
Normal     -> stable, no action needed
Warning    -> attention recommended
Critical   -> action required
Blocked    -> cannot continue
Pending    -> waiting for external event
Completed  -> finished successfully
```

Use labels and icons/text together when possible. Do not rely only on color.

## Forms

Forms should have:

```txt
- visible labels;
- field-level errors;
- validation before submit when useful;
- server/API validation for authority;
- disabled/loading submit state;
- confirmation after success;
- destructive actions protected by confirmation.
```

## Mobile

For mobile operational use:

```txt
- keep primary actions reachable;
- avoid wide tables without responsive strategy;
- use cards or stacked rows for dense data when needed;
- preserve filters and search;
- keep touch targets large enough;
- avoid hover-only interactions.
```

## Final review

Before finishing, check:

```txt
- Can the user understand the page in 5 seconds?
- Is the primary action obvious?
- Are risk states visible?
- Are labels clearer than icons alone?
- Does mobile preserve the core workflow?
- Are errors actionable?
- Did visual polish improve the task or just decorate it?
```
