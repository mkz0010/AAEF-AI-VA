# ADR-0021: Add operator readiness review summary for real execution blockers

## Status

Accepted

## Context

The real execution readiness gate produces machine-readable blockers.

However, operators need a reviewable summary that explains why execution is blocked and what needs to happen next.

## Decision

Add an operator readiness review layer.

The layer converts readiness gate results into:

- review status,
- execution recommendation,
- categorized blockers,
- next actions,
- generated Markdown and JSON review outputs.

The current MVP recommendation remains `do_not_execute`.

## Consequences

- Operators can review readiness blockers without reading raw internal objects.
- Blockers become actionable remediation items.
- Future human approval workflows have a clearer artifact to build on.
- Real execution remains disabled by default.
