# ADR-0233: Add v0.6.163 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-12

## Context

v0.6.162 closed the Public Review Entry Point Polish work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select Buyer-Facing Commercial Inquiry Boundary as the next work item.

Classify the selected work item as Medium risk because public buyer-facing and commercial-inquiry wording can influence external reader interpretation, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.163 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.164 should create the Buyer-Facing Commercial Inquiry Boundary candidate and tests. No commercial inquiry boundary is created by this v0.6.163 checkpoint.
