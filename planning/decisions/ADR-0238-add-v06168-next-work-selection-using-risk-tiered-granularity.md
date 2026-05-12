# ADR-0238: Add v0.6.168 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-12

## Context

v0.6.167 closed the Maintainer Inquiry Address Publication work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select Public Entry and Inquiry Route Consistency Review as the next work item.

Classify the selected work item as Medium risk because public-facing route consistency can influence external reader interpretation, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.168 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.169 should create the Public Entry and Inquiry Route Consistency Review candidate and tests. No consistency review is created by this v0.6.168 checkpoint.
