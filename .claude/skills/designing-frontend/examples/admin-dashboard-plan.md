# Example: Admin Dashboard Design Plan

Use this example as a shape, not as a template to copy blindly.

## Prompt

```txt
Build a dashboard for an operations team that monitors customers, alerts, agents, and pending tickets.
```

## Design plan

```txt
Screen/component:
Operations dashboard

User:
Coordinator, support analyst, or technical lead

Main task:
See what needs attention and act quickly

Visual direction:
Calm operational command center. Dense enough for real work, but not visually noisy.

Palette/tokens:
background: neutral dark or light, depending on existing system
surface: slightly elevated cards/table containers
text: high-contrast neutral
muted: secondary labels and helper text
accent: used only for primary actions and selected states
severity: success/warning/danger with labels, not color alone

Typography hierarchy:
Page title: direct and compact
Section title: medium weight
Body: readable at operational distance
Labels: small but legible
Data: tabular/monospace only where alignment matters

Layout concept:
Top summary row -> risk/action queue -> operational table -> recent activity

Signature element:
A prioritized action queue showing what requires immediate attention, not just decorative stats.

States needed:
loading, empty, error, populated, stale data, retrying

Mobile behavior:
Summary stays first. Tables collapse into stacked rows. Filters remain reachable.

Risks of looking generic:
Avoid random metric cards that do not lead to action. Avoid chart decoration without operational value.
```

## Self-critique

```txt
Does this fit the product?
Yes. It prioritizes triage and action.

What feels generic?
A basic metric card row could be generic.

Revision:
Turn the first section into an action queue: critical alerts, delayed tickets, agents offline, pending approvals.

What can hurt usability?
Too much animation or hiding filters on mobile.

Decision:
Use subtle state changes only. Keep filters visible or one tap away.
```

## Final direction

Build a dashboard that helps the user decide what to do next, not a decorative executive overview.
