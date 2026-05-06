# ADR-0104: Add v0.6.33 sanitized public sample planning

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.32 recorded that the private static/mock applied evidence package
remains private, direct public sample generation remains unauthorized, and a later
sanitized public sample planning checkpoint may be considered. The next step is to
plan that sanitized public sample boundary without generating public artifacts.

## Decision

Add a v0.6.33 sanitized public sample planning checkpoint.

The checkpoint defines public sample scope, candidate public directory placement,
sanitized artifact naming, scenario coverage plan, private-to-public transformation
rules, synthetic-only requirements, publication hygiene checks, patent-sensitive detail
exclusion, non-proof visibility, overclaim prevention, human publication review, and
future generation gate conditions.

## Consequences

Positive:

- Public sample planning is separated from public sample generation.
- Private generated artifacts remain private.
- Sanitization, naming, placement, and publication hygiene expectations are explicit.
- Runtime execution, scanner execution, customer-target operation, and delivery remain
  blocked.

Negative / deferred:

- This does not create public samples.
- This does not implement the structural validator.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
