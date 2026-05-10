# ADR-0203: Add v0.6.133 request/decision constraint-diff enforcement candidate

Status: Accepted
Date: 2026-05-10

## Context

v0.6.132 prepared readiness for the request/decision constraint-diff enforcement work item selected in v0.6.131.

## Decision

Add a deterministic request/decision constraint-diff helper and tests.

The helper compares evidence-safe request constraints against authorization decision constraints, fails closed on material mismatches, missing required fields, malformed inputs, and external_discovery escalation, and returns an evidence-safe result object.

## Consequences

v0.6.134 should review the candidate behavior and decide whether to close the work item.

No runtime execution, scanner execution, Docker execution, credential injection, customer target, delivery authorization, AAEF main issue, or AAEF main PR is authorized by this candidate.
