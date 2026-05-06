# ADR-0109: Add v0.6.38 public example structural validation planning

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.35 generated sanitized public sample artifacts. v0.6.36 recorded
publication review. v0.6.37 reviewed close-readiness and recommended public example
structural validation planning. The next step is to plan validation before any
validator implementation is added.

## Decision

Add a v0.6.38 public example structural validation planning checkpoint.

The checkpoint defines future validator input scope, validation objectives,
required-artifact checks, scenario checks, naming checks, linkage checks, scenario
posture checks, non-proof checks, AAEF five-questions checks, publication hygiene
checks, runtime boundary checks, failure categories, validator output expectations,
AAEF-side reporting guidance, and runtime/scanning/customer/delivery boundaries.

## Consequences

Positive:

- Public example validation requirements are explicit before implementation.
- Future validator work can remain read-only and public-example scoped.
- Public sample maintainability improves without expanding claims.
- Runtime, scanner, customer-target, and delivery boundaries remain visible.

Negative / deferred:

- This does not implement a structural validator.
- This does not execute validator checks.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
