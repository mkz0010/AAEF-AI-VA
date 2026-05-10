# ADR-0204: Add v0.6.134 request/decision constraint-diff enforcement review and decision

Status: Accepted
Date: 2026-05-10

## Context

v0.6.133 implemented the request/decision constraint-diff enforcement candidate as checkpoint 2 of 3 for the High-risk gate-semantics work item selected in v0.6.131.

## Decision

Review and accept the v0.6.133 request/decision constraint-diff enforcement candidate.

The High-risk work item is closed. The accepted candidate provides a deterministic, evidence-safe helper and tests for comparing request constraints with authorization decision constraints, with fail-closed handling for material mismatches, missing required fields, malformed inputs, and external_discovery escalation.

## Consequences

Future work should select the next item using the v0.6.120 risk-tiered checkpoint granularity policy.

No runtime execution, scanner execution, Docker execution, credential injection, customer target, delivery authorization, AAEF main issue, or AAEF main PR is authorized by this review decision.
