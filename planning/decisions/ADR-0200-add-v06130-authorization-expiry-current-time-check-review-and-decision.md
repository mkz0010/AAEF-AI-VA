# ADR-0200: Add v0.6.130 authorization expiry current-time check review and decision

Status: Accepted
Date: 2026-05-10

## Context

v0.6.129 implemented the authorization expiry current-time check candidate as checkpoint 2 of 3 for the High-risk gate-semantics work item selected in v0.6.127.

## Decision

Review and accept the v0.6.129 authorization expiry current-time check candidate.

The High-risk work item is closed. The accepted candidate provides a deterministic, evidence-safe helper and tests for evaluating authorization expiry against an explicit current-time value, with fail-closed handling for expired, malformed, missing-required, timezone-naive, and ambiguous current-time inputs.

## Consequences

Future work should select the next item using the v0.6.120 risk-tiered checkpoint granularity policy.

No runtime execution, scanner execution, Docker execution, credential injection, customer target, delivery authorization, AAEF main issue, or AAEF main PR is authorized by this review decision.
