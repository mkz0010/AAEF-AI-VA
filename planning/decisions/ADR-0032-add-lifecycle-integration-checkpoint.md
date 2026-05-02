# ADR-0032: Add lifecycle integration checkpoint before local runtime work

## Status

Accepted

## Context

The project now includes Tool Gateway controls, readiness gates, evidence chain, reconstruction reports, sanitizer, finding review, report review, packet review, and delivery authorization.

Before moving toward controlled local tool runtime integration, the project needs a stable checkpoint that summarizes what exists and what remains explicitly out of scope.

## Decision

Add a lifecycle integration checkpoint for v0.1.30.

The checkpoint validates that real execution, network activity, delivery dispatch, customer delivery, report-ready status, and customer-delivery-ready status remain disabled.

The checkpoint also records stable capabilities and next phase candidates.

## Consequences

- v0.1.x gains a clear stability checkpoint.
- Future v0.2.x runtime work can start from a documented safety baseline.
- The project continues to avoid `final` lifecycle terminology.
- The checkpoint provides a generated JSON/Markdown summary for internal review.
