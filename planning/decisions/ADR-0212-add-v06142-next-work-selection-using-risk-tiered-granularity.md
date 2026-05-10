# ADR-0212: Add v0.6.142 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-10

## Context

v0.6.141 closed the mock/dry-run `completed` status terminology cleanup work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select Enterprise Review Guide as the next work item.

Classify the selected work item as Medium risk because it is buyer/reviewer-facing documentation that can affect interpretation and claim boundaries, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.142 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.143 should create the Enterprise Review Guide candidate and tests. No Enterprise Review Guide is created by this v0.6.142 checkpoint.
