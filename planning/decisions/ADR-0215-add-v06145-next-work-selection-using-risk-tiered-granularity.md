# ADR-0215: Add v0.6.145 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-10

## Context

v0.6.144 closed the Enterprise Review Guide work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select Technical Due Diligence Summary as the next work item.

Classify the selected work item as Medium risk because it is technical reviewer-facing documentation that can affect interpretation and due-diligence framing, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.145 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.146 should create the Technical Due Diligence Summary candidate and tests. No Technical Due Diligence Summary is created by this v0.6.145 checkpoint.
