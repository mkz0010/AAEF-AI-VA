# ADR-0071: Add v0.6.0 implementation and evaluation work ordering

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA has completed a strong v0.5.x public foundation through v0.5.10.

The next phase may include a local assessment lab, evaluation criteria, runtime gate
hardening, evidence UX improvements, demo scenarios, or commercial PoC planning.
Starting directly with a local lab may be useful, but it risks pulling the project
toward execution before capability boundaries and evaluation criteria are clear.

## Decision

Add a v0.6.0 implementation and evaluation work-ordering checkpoint.

The checkpoint records:

- current baseline,
- core sequencing rule,
- workstream map,
- recommended order,
- local lab decision options,
- capability maturity levels,
- decision gates,
- minimum safe path before local execution,
- commercial PoC readiness path,
- runtime and scanning prohibitions.

## Consequences

Positive:

- v0.6.x starts with sequencing rather than premature implementation.
- Local lab work becomes a decision, not an assumption.
- Evaluation and evidence can guide implementation order.
- Commercial PoC readiness remains separated from public repository claims.

Negative / deferred:

- This does not build the local lab.
- This does not enable runtime execution.
- This does not define a commercial contract.
- This does not demonstrate production deployment.
