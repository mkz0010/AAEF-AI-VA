# ADR-0106: Add v0.6.35 sanitized public sample generation candidate

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.34 reviewed readiness for a sanitized public sample generation
candidate. The next step is to generate synthetic, non-executing `.example.` artifacts
under the planned public examples directory while preserving runtime, scanner,
customer-target, delivery, certification, legal, and audit boundaries.

## Decision

Add a v0.6.35 sanitized public sample generation candidate.

The checkpoint adds `tools/generate_sanitized_public_sample.py`, generated public
example artifacts under `examples/applied-evidence/sanitized-static-mock/`, and a
local validation test.

## Consequences

Positive:

- Reviewers can inspect a public-safe applied evidence sample.
- The sample demonstrates request-to-evidence linkage and non-execution evidence.
- Non-proof statements are visible in public example artifacts.
- The sample remains separate from runtime execution and customer delivery.

Negative / deferred:

- This does not implement a structural validator.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
