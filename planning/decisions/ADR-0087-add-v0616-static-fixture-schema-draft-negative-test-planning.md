# ADR-0087: Add v0.6.16 static fixture schema draft and negative test planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.15 defined static fixture schema and validator planning. The next
step is to define schema draft fields and negative test expectations before any
fixture schemas or validators are implemented.

## Decision

Add a v0.6.16 static fixture schema draft and negative test planning checkpoint.

The checkpoint records public-safe design boundary, planning proposition, schema
draft posture, fixture manifest draft fields, node envelope draft fields, required
node draft fields, AI request fixture draft fields, gate decision fixture draft
fields, expected evidence fixture draft fields, scenario trace draft rules, negative
test planning scope, missing-node negative test planning, broken-reference negative
test planning, runtime-implication negative test planning, runnable-configuration
negative test planning, secret-like content negative test planning, customer-like
content negative test planning, delivery and overclaiming negative test planning,
validator failure expectation model, future validator registration planning,
generated artifact boundary, non-proof statement, relationship to v0.6.15, and
runtime, scanning, Compose, image pull, Docker execution, port binding, fixture
generation, validator implementation, negative test implementation, and delivery
prohibitions.

## Consequences

Positive:

- Schema draft fields are clarified before schema implementation.
- Negative test expectations are defined before validator implementation.
- Unsafe fixture categories can be reviewed before sample fixture generation.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not implement fixture schemas.
- This does not implement fixture validators.
- This does not implement negative tests.
- This does not generate fixture files.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
