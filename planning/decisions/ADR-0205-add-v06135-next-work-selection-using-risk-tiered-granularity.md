# ADR-0205: Add v0.6.135 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-10

## Context

v0.6.134 closed the request/decision constraint-diff enforcement work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select external_discovery=true fail-closed behavior as the next work item.

Classify the selected work item as High risk because it can affect target-boundary gate behavior and evidence interpretation. Use three checkpoints: readiness, candidate implementation, then review and decision.

This v0.6.135 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.136 should prepare external discovery fail-closed behavior readiness. No external_discovery behavior is modified by this v0.6.135 checkpoint.
