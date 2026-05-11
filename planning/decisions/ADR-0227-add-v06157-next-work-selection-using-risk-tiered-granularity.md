# ADR-0227: Add v0.6.157 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-11

## Context

v0.6.156 closed the Reviewer Walkthrough work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select External Review Package Integration as the next work item.

Classify the selected work item as Medium risk because it is external-review-facing documentation that can influence buyer, technical reviewer, sponsor, maintainer, and commercial-reviewer interpretation, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.157 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.158 should create the External Review Package Integration candidate and tests. No External Review Package is created by this v0.6.157 checkpoint.
