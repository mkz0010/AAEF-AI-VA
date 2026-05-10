# ADR-0208: Add v0.6.138 external discovery fail-closed behavior review and decision

Status: Accepted
Date: 2026-05-10

## Context

v0.6.137 implemented the external_discovery=true fail-closed behavior candidate as checkpoint 2 of 3 for the High-risk gate-semantics work item selected in v0.6.135.

## Decision

Review and accept the v0.6.137 external discovery fail-closed behavior candidate.

The High-risk work item is closed. The accepted candidate provides a deterministic, evidence-safe helper and tests for evaluating external discovery against explicit decision allowance, target-boundary compatibility, destination binding, scope support, and authorization validity. It fail-closes missing, false, local-only, local-lab-only, missing/malformed destination binding, missing scope support, ambiguous target boundary, invalid authorization, and malformed external discovery flag cases.

## Consequences

Future work should select the next item using the v0.6.120 risk-tiered checkpoint granularity policy.

No runtime execution, scanner execution, Docker execution, credential injection, customer target, delivery authorization, AAEF main issue, or AAEF main PR is authorized by this review decision.
