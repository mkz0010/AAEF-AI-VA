# ADR-0092: Add v0.6.21 static fixture validator required-node check planning

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.20 added the first read-only validator scaffold. The next planned
validator behavior should be required-node presence checks, but implementation should
not begin until the required-node boundary is documented.

## Decision

Add a v0.6.21 static fixture validator required-node check planning checkpoint.

The checkpoint records public-safe design boundary, planning proposition,
required-node planning posture, planned manifest expectation, required fixture node
set, missing-node failure planning, review-only result planning, fail-closed behavior
planning, read-only implementation boundary, relationship to the current scaffold,
future implementation sequence, negative test planning, registration readiness,
non-proof statement, relationship to v0.6.20, and runtime, scanning, Compose, image
pull, Docker execution, port binding, fixture generation, required-node check
implementation, complete validator implementation, negative test implementation, and
delivery prohibitions.

## Consequences

Positive:

- The next validator behavior is scoped before implementation.
- Required fixture node expectations are explicit.
- Missing-node failures can be planned as blocking and fail-closed.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not implement required-node checks.
- This does not implement complete fixture validation.
- This does not implement negative tests.
- This does not generate fixture files.
- This does not enable scanner execution.
