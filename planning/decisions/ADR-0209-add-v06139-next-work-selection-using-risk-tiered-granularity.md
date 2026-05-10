# ADR-0209: Add v0.6.139 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-10

## Context

v0.6.138 closed the external_discovery=true fail-closed behavior work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select mock/dry-run `completed` status terminology cleanup as the next work item.

Classify the selected work item as Medium risk because it can affect reviewer interpretation and status wording, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.139 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.140 should implement the candidate terminology cleanup and tests. No mock/dry-run status wording is changed by this v0.6.139 checkpoint.
