# ADR-0088: Add v0.6.17 static fixture validator scaffold planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.16 defined static fixture schema draft and negative test planning.
The next step is to define the future validator scaffold responsibilities before
implementing validator code or generating fixtures.

## Decision

Add a v0.6.17 static fixture validator scaffold planning checkpoint.

The checkpoint records public-safe design boundary, planning proposition, validator scaffold posture, scaffold responsibility model, validator input boundary, validator output boundary, planned validation stages, fail-closed behavior planning, failure category model, negative-test handling planning, validator review record planning, future implementation order, registration gate planning, generated artifact boundary, non-proof statement, relationship to v0.6.16, and runtime, scanning, Compose, image pull, Docker execution, port binding, fixture generation, validator implementation, negative test implementation, and delivery prohibitions.

## Consequences

Positive:

- Validator scaffold responsibilities are clear before implementation.
- Future validation can remain read-only and fail-closed.
- Negative-test handling and failure categories are connected to scaffold planning.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not implement fixture schemas.
- This does not implement fixture validators.
- This does not implement negative tests.
- This does not generate fixture files.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
