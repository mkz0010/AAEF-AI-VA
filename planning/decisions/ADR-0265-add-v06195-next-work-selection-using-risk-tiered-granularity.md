# ADR-0265: Add v0.6.195 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-13

## Context

v0.6.194 reviewed and accepted the static, mock, non-execution Safe Demo Fixture Set candidate and closed the High-risk work item. The accepted fixture set now needs repository landing and demo path clarity so reviewers can find and understand it without mistaking it for an executable demo, scanner, production readiness evidence, customer PoC path, or authorization to test third-party systems.

## Decision

Select Repository Landing and Demo Path Clarity as the next work item.

Classify the selected work item as Medium risk because it may modify public-facing repository navigation and affect reviewer interpretation while remaining documentation-only.

Use two checkpoints: candidate implementation, then review and decision.

This v0.6.195 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.196 should create the Repository Landing and Demo Path Clarity candidate and tests. No landing/demo path clarity artifact is created by this v0.6.195 checkpoint.
