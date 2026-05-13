# ADR-0261: Add v0.6.191 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-13

## Context

v0.6.190 reviewed and accepted the Safe Demo Fixture Set Planning candidate and closed that Medium-risk work item. The next useful step is to move toward actual static fixture files, but only after a readiness review because fixture files may become public examples.

## Decision

Select Safe Demo Fixture Set Creation as the next work item.

Classify the selected work item as High risk because it may later create public-facing fixture files and affect reviewer interpretation, repository trust, public demo readiness, and validator expectations.

Use three checkpoints: readiness review, candidate implementation, then review and decision.

This v0.6.191 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.192 should create the Safe Demo Fixture Set Creation Readiness Review. No fixture files are created by this v0.6.191 checkpoint.
