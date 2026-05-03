# ADR-0086: Add v0.6.15 static fixture schema and validator planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.14 defined static lab scenario fixture planning. The next step is to
define schema and validator planning before any fixture artifacts are generated or
committed.

## Decision

Add a v0.6.15 static fixture schema and validator planning checkpoint.

The checkpoint records public-safe design boundary, planning proposition, fixture
schema planning scope, fixture manifest schema planning, fixture node schema
planning, required fixture node types, AI request fixture schema planning, gate
decision fixture schema planning, expected evidence fixture schema planning,
scenario trace validation planning, synthetic data validation planning, no-secret
validation planning, no-runtime validation planning, no-runnable-configuration
validation planning, validator failure categories, future validator registration
planning, generated artifact boundary, non-proof statement, relationship to v0.6.14,
and runtime, scanning, Compose, image pull, Docker execution, port binding, fixture
generation, validator implementation, and delivery prohibitions.

## Consequences

Positive:

- Future static fixtures get schema and validator boundaries before generation.
- Reference integrity, trace integrity, synthetic data, no-secret, no-runtime, and
  no-runnable checks are planned early.
- Validator failure categories are defined before implementation.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not implement fixture schemas.
- This does not implement fixture validators.
- This does not generate fixture files.
- This does not create sample fixture artifacts.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
