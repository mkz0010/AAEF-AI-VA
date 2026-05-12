# ADR-0252: Add v0.6.182 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-12

## Context

v0.6.181 deferred Commercial Inquiry Response Boundary before candidate creation because the project should first improve demo/story readiness. v0.6.179 accepted Public Demo Positioning. v0.6.173 recorded the safe demo layer as a near-term candidate while deferring runtime/scanner and customer PoC layers.

## Decision

Select Safe Demo Scenario Definition as the next work item.

Classify the selected work item as Medium risk because it defines the scenario that later implementation may follow and can influence public interpretation of demo readiness, runtime/scanner boundaries, customer target activity, and production maturity.

Use two checkpoints: candidate implementation, then review and decision.

This v0.6.182 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.183 should create the Safe Demo Scenario Definition candidate and tests. No demo artifact is created by this v0.6.182 checkpoint.
