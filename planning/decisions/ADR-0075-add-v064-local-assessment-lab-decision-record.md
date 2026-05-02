# ADR-0075: Add v0.6.4 local assessment lab decision record

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.0 established implementation ordering, v0.6.1 inventoried
capabilities, v0.6.2 defined evaluation criteria, and v0.6.3 reconfirmed safety
boundaries and non-goals.

The project now needs to decide whether the local assessment lab path should begin,
and if so, which maturity level should be allowed first.

## Decision

Proceed with a documentation-only local lab profile and dry-run planning.

Do not build localhost-only controlled execution yet.

The checkpoint records:

- selected local lab option,
- rejected options,
- selected maturity level,
- local lab profile scope,
- local-only assumptions,
- allowed artifacts,
- prohibited behavior,
- dry-run entry criteria,
- localhost-only controlled behavior entry criteria,
- exit criteria,
- v0.6.x sequence impact,
- runtime and scanning prohibitions.

## Consequences

Positive:

- The project can move toward a model environment without enabling execution.
- The next artifacts become clearer.
- The local lab remains explicitly separate from customer-target operation.
- Future demos and dry-runs have entry criteria.

Negative / deferred:

- This does not build the local lab.
- This does not enable dry-run behavior.
- This does not enable localhost-only controlled execution.
- This does not create commercial PoC readiness.
