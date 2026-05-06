# ADR-0117: Add v0.6.46 public validator negative fixture implementation candidate

Status: Accepted
Date: 2026-05-07

## Context

AAEF-AI-VA v0.6.44 planned negative fixtures for the read-only public example structural validator.
v0.6.45 reviewed implementation readiness without creating fixtures or changing validator behavior.
The next safe step is to add a synthetic, public-safe, static negative fixture set and a read-only harness test.

## Decision

Add a v0.6.46 public validator negative fixture implementation candidate.

The checkpoint adds static negative fixtures under `examples/applied-evidence/public-validator-negative-fixtures/`, fixture metadata, a fixture index, a local read-only harness test, and documentation.
The harness runs the existing public example structural validator against the positive control and each negative fixture root, expecting positive pass and negative fail-closed results.

## Consequences

Positive:
- The public validator now has synthetic negative fixture coverage.
- Expected blocker metadata makes fixture intent reviewable.
- Positive control preservation is tested explicitly.
- Validator behavior remains unchanged.
- Runtime/scanning/customer/delivery boundaries remain blocked.

Negative / deferred:
- This does not modify validator behavior.
- This does not prove diagnostic accuracy or completeness.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
