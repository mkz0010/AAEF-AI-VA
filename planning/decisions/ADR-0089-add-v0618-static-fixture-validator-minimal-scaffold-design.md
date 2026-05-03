# ADR-0089: Add v0.6.18 static fixture validator minimal scaffold design

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.17 defined static fixture validator scaffold planning. The next step
is to define a minimal read-only validator scaffold design before writing validator
code, implementing CLI behavior, implementing checks, or generating fixtures.

## Decision

Add a v0.6.18 static fixture validator minimal scaffold design checkpoint.

The checkpoint records public-safe design boundary, design proposition, minimal
scaffold posture, planned module boundary, planned CLI boundary, planned input model,
planned output model, planned function boundaries, failure result model, fail-closed
behavior design, planned registration conditions, future implementation order,
generated artifact boundary, non-proof statement, relationship to v0.6.17, and
runtime, scanning, Compose, image pull, Docker execution, port binding, fixture
generation, validator implementation, negative test implementation, CLI
implementation, and delivery prohibitions.

## Consequences

Positive:

- Future validator implementation receives a minimal read-only design boundary.
- CLI, input, output, function, and failure-result boundaries are defined before code.
- Registration conditions preserve negative-test-first and fail-closed behavior.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not implement fixture schemas.
- This does not implement fixture validators.
- This does not implement CLI behavior.
- This does not implement negative tests.
- This does not generate fixture files.
- This does not enable scanner execution.
