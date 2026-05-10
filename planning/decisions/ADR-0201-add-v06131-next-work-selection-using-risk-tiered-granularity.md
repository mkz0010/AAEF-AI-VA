# ADR-0201: Add v0.6.131 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-10

## Context

v0.6.130 closed the authorization expiry current-time check work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select request/decision constraint-diff enforcement as the next work item.

Classify the selected work item as High risk because it can affect gate behavior and evidence interpretation. Use three checkpoints: readiness, candidate implementation, then review and decision.

This v0.6.131 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.132 should prepare request/decision constraint-diff enforcement readiness. No constraint-diff behavior is modified by this v0.6.131 checkpoint.
