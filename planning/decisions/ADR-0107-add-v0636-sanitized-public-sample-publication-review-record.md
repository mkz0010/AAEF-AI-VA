# ADR-0107: Add v0.6.36 sanitized public sample publication review record

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.35 generated a sanitized public sample candidate. The next step is to
record a publication review for that public example while preserving the limits that
the sample is synthetic, non-executing, non-diagnostic, not customer-deliverable, and
not a certification, legal, audit, compliance, production-readiness, or external
framework equivalence claim.

## Decision

Add a v0.6.36 sanitized public sample publication review record checkpoint.

The checkpoint adds `tools/generate_sanitized_public_sample_publication_review_record.py`,
generated publication review artifacts under `examples/applied-evidence/sanitized-static-mock/`,
and a local validation test.

## Consequences

Positive:

- The public sample candidate now has a publication review record.
- The sample status is explicit as a limited synthetic non-executing public example.
- Runtime, scanner, customer-target, and delivery boundaries remain visible.
- AAEF-side reporting can reference the public example without overclaiming.

Negative / deferred:

- This does not implement a structural validator.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
