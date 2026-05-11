# ADR-0221: Add v0.6.151 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-11

## Context

v0.6.150 closed the Safe PoC Boundary Template work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select Control Matrix as the next work item.

Classify the selected work item as Medium risk because it is reviewer-facing documentation that can affect interpretation and may resemble a compliance or audit matrix if poorly scoped, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.151 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.152 should create the Control Matrix candidate and tests. No Control Matrix is created by this v0.6.151 checkpoint.
