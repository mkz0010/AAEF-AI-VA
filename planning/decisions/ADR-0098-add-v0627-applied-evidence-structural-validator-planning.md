# ADR-0098: Add v0.6.27 applied evidence structural validator planning

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.26 defined reviewer walkthrough and AAEF five questions mapping. The
next step is to define structural validation checks before generating static/mock
applied evidence packages or implementing validators.

## Decision

Add a v0.6.27 applied evidence structural validator planning checkpoint.

The checkpoint defines validator input/output boundaries, required artifact presence
checks, required field checks, identifier linkage checks, scenario consistency checks,
contradiction checks, non-execution evidence checks, reviewer walkthrough coverage
checks, non-proof statement checks, overclaim prevention checks, failure category
planning, validator review result planning, future implementation sequence, readiness
for static/mock evidence generation, and runtime/scanning boundaries.

## Consequences

Positive:

- Future static/mock evidence packages will have a planned structural quality gate.
- Non-execution evidence and non-proof boundaries are checkable.
- Identifier linkage and scenario consistency are planned before generation.
- Public overclaim prevention remains explicit.

Negative / deferred:

- This does not implement the validator.
- This does not generate static/mock evidence packages.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
