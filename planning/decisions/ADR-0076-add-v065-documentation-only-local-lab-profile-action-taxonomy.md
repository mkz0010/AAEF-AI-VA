# ADR-0076: Add v0.6.5 documentation-only local lab profile and action taxonomy

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.4 decided to proceed with a documentation-only local lab profile
and dry-run planning while deferring localhost-only controlled execution.

The next step is to define the profile and action taxonomy before adding fixtures,
dry-run behavior, demo walkthroughs, or runtime hardening work.

## Decision

Add a v0.6.5 documentation-only local lab profile and action taxonomy.

The checkpoint records:

- v0.6.4 decision carried forward,
- documentation-only local lab profile,
- local-only assumptions,
- allowed action taxonomy,
- denied action taxonomy,
- preflight evidence requirements,
- human review requirements,
- generated output policy,
- what this lab does not prove,
- dry-run planning readiness,
- deferred localhost-only controlled behavior,
- runtime and scanning prohibitions.

## Consequences

Positive:

- The local lab path becomes more concrete without enabling execution.
- Allowed and denied action categories are visible before fixture or dry-run work.
- Dry-run planning can proceed from a safer profile.
- Public claims remain bounded by a clear non-proof section.

Negative / deferred:

- This does not build the local lab.
- This does not add static fixtures.
- This does not enable dry-run behavior.
- This does not enable localhost-only controlled execution.
- This does not create commercial PoC readiness.
