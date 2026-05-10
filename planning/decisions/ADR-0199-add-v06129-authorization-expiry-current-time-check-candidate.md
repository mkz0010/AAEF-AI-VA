# ADR-0199: Add v0.6.129 authorization expiry current-time check candidate

Status: Accepted
Date: 2026-05-10

## Context

v0.6.128 prepared readiness for the authorization expiry current-time check selected in v0.6.127.

## Decision

Add a deterministic authorization expiry current-time helper and tests.

The helper evaluates expiry against an explicit current-time value, fails closed on expired, malformed, missing-required, timezone-naive, or ambiguous current-time inputs, and returns an evidence-safe decision object.

## Consequences

v0.6.130 should review the candidate behavior and decide whether to close the work item.

No runtime execution, scanner execution, Docker execution, credential injection, customer target, delivery authorization, AAEF main issue, or AAEF main PR is authorized by this candidate.
