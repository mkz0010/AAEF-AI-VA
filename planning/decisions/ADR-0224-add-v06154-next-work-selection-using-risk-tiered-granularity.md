# ADR-0224: Add v0.6.154 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-11

## Context

v0.6.153 closed the Control Matrix work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select Reviewer Walkthrough as the next work item.

Classify the selected work item as Medium risk because it is reviewer-facing documentation that can influence buyer, technical reviewer, sponsor, and maintainer interpretation, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.154 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.155 should create the Reviewer Walkthrough candidate and tests. No Reviewer Walkthrough is created by this v0.6.154 checkpoint.
