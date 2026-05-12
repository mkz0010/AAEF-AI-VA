# ADR-0247: Add v0.6.177 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-12

## Context

v0.6.176 reviewed and accepted the Current-State Executive Summary candidate and closed the Medium-risk work item. v0.6.173 identified the safe demo layer as a near-term candidate while deferring runtime/scanner and customer PoC layers. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select Public Demo Positioning as the next work item.

Classify the selected work item as Medium risk because it will create public-facing demo-positioning language that can influence external interpretation of demo readiness, runtime authority, scanner activity, customer PoC boundaries, and production maturity.

Use two checkpoints: candidate implementation, then review and decision.

This v0.6.177 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.178 should create the Public Demo Positioning candidate and tests. No demo artifact is created by this v0.6.177 checkpoint.
