# ADR-0115: Add v0.6.44 public validator negative fixture planning

Status: Accepted  
Date: 2026-05-07

## Context

AAEF-AI-VA v0.6.40 implemented a read-only public example structural validator. v0.6.41 reviewed it. v0.6.42 and v0.6.43 prepared and reviewed AAEF Applied Implementation handback. The next safe hardening step is to plan negative fixtures before adding fixture files or harness behavior.

## Decision

Add a v0.6.44 public validator negative fixture planning checkpoint.

The checkpoint records planned fixture root, planned negative fixture categories, planned fixture behavior, expected blocker mapping, fixture construction rules, validation harness behavior, positive control expectations, AAEF handback relationship, readiness assessment, and runtime/scanning/customer/delivery boundaries.

## Consequences

Positive:

- Future negative fixture work is scoped before implementation.
- The validator hardening direction remains read-only and public-safe.
- Fail-closed behavior remains explicit.
- Runtime, scanner, customer-target, and delivery boundaries remain visible.

Negative / deferred:

- This does not implement negative fixtures.
- This does not modify validator behavior.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
