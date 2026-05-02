# ADR-0072: Add v0.6.1 capability inventory and maturity map

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.0 established implementation and evaluation work ordering.

Before choosing whether to build a local assessment lab or harden runtime gates, the
project needs a capability inventory and maturity map. This reduces the risk of
building new features before understanding existing evidence and gaps.

## Decision

Add a v0.6.1 capability inventory and maturity map.

The checkpoint records:

- maturity model,
- current maturity summary,
- capability inventory,
- capability gaps,
- readiness by future path,
- recommended next checkpoint,
- local lab implication,
- commercial PoC implication,
- runtime and scanning prohibitions.

## Consequences

Positive:

- Existing capabilities are easier to reason about.
- Future work can be prioritized by maturity gaps.
- Local lab work remains a decision path rather than an assumption.
- Evaluation criteria can be designed from the actual inventory.

Negative / deferred:

- This does not build the local lab.
- This does not enable runtime execution.
- This does not provide a scoring model.
- This does not demonstrate production deployment.
