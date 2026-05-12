# ADR-0258: Add v0.6.188 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-12

## Context

v0.6.187 reviewed and accepted the Safe Demo Artifact Planning candidate and closed the Medium-risk work item. The next safe step is to plan the fixture set that could later support that accepted artifact plan without creating fixture files or public samples yet.

## Decision

Select Safe Demo Fixture Set Planning as the next work item.

Classify the selected work item as Medium risk because it defines the plan that later fixture files may follow and can influence repository structure, public reviewer navigation, evidence trace shape, static validation expectations, and the boundary between demonstration data and execution.

Use two checkpoints: candidate implementation, then review and decision.

This v0.6.188 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.189 should create the Safe Demo Fixture Set Planning candidate and tests. No fixture files are created by this v0.6.188 checkpoint.
