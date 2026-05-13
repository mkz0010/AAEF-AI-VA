# ADR-0268: Add v0.6.198 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-13

## Context

v0.6.197 reviewed and accepted Repository Landing and Demo Path Clarity after the static, mock, non-execution fixture set was accepted in v0.6.194.

The repository now exposes a Safe Demo Fixture Review Path, but the next public-facing question is whether it should be called a public demo or described more conservatively.

## Decision

Select Public Demo Readiness Review as the next work item.

Classify the selected work item as Medium risk because it is documentation-only but may affect public interpretation of demo readiness, scanner capability, executable demo availability, PoC readiness, and third-party-testing authorization.

Use two checkpoints: candidate review, then review and decision.

This v0.6.198 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.199 should create the Public Demo Readiness Review candidate and tests. No public demo readiness candidate is created by this v0.6.198 checkpoint.
