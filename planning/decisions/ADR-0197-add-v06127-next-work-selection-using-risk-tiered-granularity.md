# ADR-0197: Add v0.6.127 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-10

## Context

v0.6.126 closed the SECURITY.md reporting-channel consistency work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select authorization expiry checked against current time as the next work item.

Classify the selected work item as High risk because it can affect authorization gate behavior and evidence interpretation. Use three checkpoints: readiness, candidate implementation, then review and decision.

This v0.6.127 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.128 should prepare authorization expiry current-time check readiness. No authorization behavior is modified by this v0.6.127 checkpoint.
