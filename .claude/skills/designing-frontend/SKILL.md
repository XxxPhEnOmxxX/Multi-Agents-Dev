---
name: designing-frontend
description: Creates or reviews frontend UI with intentional visual direction, product-specific identity, clear UX, responsive behavior, and non-generic interface choices. Use when building or reshaping pages, dashboards, admin panels, landing pages, forms, cards, design systems, or important visual components.
license: Apache-2.0 derivative; see LICENSE.txt and ATTRIBUTION.md
---

# Designing Frontend

This skill adapts the official Anthropic `frontend-design` skill for practical software engineering workflows.

Use it when the task involves frontend design, UI implementation, UX polish, visual hierarchy, responsive layout, interface copy, forms, dashboards, admin panels, landing pages, or design system decisions.

## Core principle

Design must be specific to the product, not a generic template.

Before building, identify:

```txt
Product:
Primary user:
Main job of the screen:
Operational context:
What the interface must communicate:
```

A strong UI should make deliberate choices about layout, typography, spacing, color, copy, and interaction based on the real product and user task.

## Practical frontend rules

1. Start from the screen's job.
   The UI exists to help the user complete a task. Visual style serves that task.

2. Avoid generic AI-looking defaults.
   Do not automatically use the same hero, gradient, card grid, large numbers, and vague subtitle pattern unless it truly fits the brief.

3. Spend boldness in one place.
   Choose one memorable visual or interaction idea. Keep the rest disciplined.

4. Structure must carry information.
   Cards, numbers, dividers, badges, tables, timelines, and sections should represent real meaning, not decoration.

5. Typography must create hierarchy.
   Define clear roles for title, section title, body, label, data, and caption.

6. Motion must help usability.
   Use animation for feedback, state changes, reveal, or flow clarity. Avoid motion that distracts from operation.

7. Copy is part of design.
   Buttons, labels, empty states, errors, and success messages should use clear user-facing language.

8. Operational systems need restraint.
   For admin panels, operational dashboards, CRMs, internal tools, and monitoring systems, prioritize clarity, speed, scanability, accessibility, and consistency over decorative creativity.

## Two-pass workflow

### Pass 1 — Design plan

Before coding, produce a compact plan:

```txt
Screen/component:
User:
Main task:
Visual direction:
Palette/tokens:
Typography hierarchy:
Layout concept:
Signature element:
States needed:
Mobile behavior:
Risks of looking generic:
```

### Pass 2 — Self-critique before build

Review the plan before implementation:

```txt
Does this design fit this specific product?
What part feels generic?
What can be simplified?
What can be made clearer?
What visual choice is justified by the subject?
What could hurt usability on mobile?
```

Revise the plan before writing code if the design feels like a reusable template rather than a product-specific interface.

## UI copy rules

Write from the user's side of the screen.

Prefer:

```txt
Save changes
Create customer
Enable notification
View details
Clear filters
```

Avoid implementation-facing labels such as:

```txt
Submit
Process data
Webhook config
Execute action
```

Keep action vocabulary consistent through the flow. If the button says `Publish`, the loading and success states should use the same action language.

## Empty and error states

Treat failure and emptiness as guidance moments.

A good empty state should explain:

```txt
What is missing?
Why is the screen empty?
What should the user do next?
```

A good error should explain:

```txt
What failed?
What can the user do?
Whether retrying is safe?
```

Avoid vague errors like:

```txt
Something went wrong.
Invalid input.
Error.
```

## Implementation checklist

Before finishing, verify:

```txt
- The screen has a clear purpose.
- The design is specific to the product and user.
- The layout does not look like a default template.
- Typography has clear hierarchy.
- Visual structure represents real information.
- UI copy is clear and action-oriented.
- Loading, empty, error, success, and populated states are considered.
- Mobile layout is usable.
- Keyboard focus remains visible.
- Motion is purposeful and not excessive.
- The design does not add complexity without value.
```

## References

- Operational UI guidance: `references/operational-ui.md`
- Design planning example: `examples/admin-dashboard-plan.md`
