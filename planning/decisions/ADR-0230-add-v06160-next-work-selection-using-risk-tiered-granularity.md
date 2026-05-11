# ADR-0230: Add v0.6.160 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-11

## Context

v0.6.159 closed the External Review Package Integration work item. v0.6.120 requires future work to be selected by explicitly assigning risk tier and checkpoint count.

## Decision

Select Public Review Entry Point Polish as the next work item.

Classify the selected work item as Medium risk because public-facing entry-point wording can influence external reviewer, buyer, sponsor, maintainer, and commercial-reader interpretation, but should not change gate authorization semantics or runtime behavior. Use two checkpoints: candidate implementation, then review and decision.

This v0.6.160 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.161 should create the Public Review Entry Point Polish candidate and tests. No public review entry point is modified by this v0.6.160 checkpoint.
