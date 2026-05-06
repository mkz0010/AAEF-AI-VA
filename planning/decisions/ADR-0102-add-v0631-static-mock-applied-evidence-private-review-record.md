# ADR-0102: Add v0.6.31 static/mock applied evidence private review record

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.29 generated a private-first static/mock applied evidence package.
v0.6.30 planned the review and promotion gate. The next step is to generate a private
review record for the generated package while keeping public sample promotion,
diagnostic execution, customer-target operation, and delivery authorization blocked.

## Decision

Add a v0.6.31 static/mock applied evidence package private review record checkpoint.

The checkpoint adds `tools/generate_static_mock_applied_evidence_private_review_record.py`
and a local test that generates and validates private review outputs. The review
outputs summarize scenario coverage, artifact coverage, representative linkage,
non-proof visibility, runtime/scanning/customer/delivery boundaries, blocker
categories, and promotion gate result.

## Consequences

Positive:

- The generated private package now has a private review record.
- The review record supports AAEF-side reporting without exposing private contents.
- Promotion remains blocked unless a later public-safe decision explicitly changes it.
- Diagnostic execution remains separate from private static/mock review.

Negative / deferred:

- This does not create public samples.
- This does not implement the structural validator.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
