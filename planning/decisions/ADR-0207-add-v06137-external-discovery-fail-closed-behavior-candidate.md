# ADR-0207: Add v0.6.137 external discovery fail-closed behavior candidate

Status: Accepted
Date: 2026-05-10

## Context

v0.6.136 prepared readiness for the external_discovery=true fail-closed behavior work item selected in v0.6.135.

## Decision

Add a deterministic external discovery fail-closed helper and tests.

The helper evaluates `external_discovery=true` against explicit decision allowance, target-boundary compatibility, destination binding, scope support, and authorization validity. It fails closed on missing, malformed, ambiguous, local-only, local-lab-only, unsupported-scope, invalid-authorization, or unapproved external discovery cases and returns an evidence-safe result object.

## Consequences

v0.6.138 should review the candidate behavior and decide whether to close the work item.

No runtime execution, scanner execution, Docker execution, credential injection, customer target, delivery authorization, AAEF main issue, or AAEF main PR is authorized by this candidate.
