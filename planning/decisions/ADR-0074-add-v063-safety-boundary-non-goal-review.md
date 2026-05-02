# ADR-0074: Add v0.6.3 safety boundary and non-goal review

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.0 established work ordering, v0.6.1 inventoried capabilities, and
v0.6.2 defined evaluation criteria and acceptance gates.

Before deciding whether to build a local assessment lab, the project should
reconfirm which boundaries and non-goals remain hard constraints.

## Decision

Add a v0.6.3 safety boundary and non-goal review.

The checkpoint records:

- core safety statement,
- hard non-goals,
- intentionally blocked capabilities,
- safety boundary inventory,
- non-goal preservation rules,
- fail-closed requirements,
- local lab constraints,
- demo constraints,
- runtime gate hardening constraints,
- commercial PoC constraints,
- unsafe implication checklist,
- advancement conditions,
- runtime and scanning prohibitions.

## Consequences

Positive:

- Local lab decisioning can happen with clearer safety boundaries.
- Future demos and runtime gate work are less likely to overclaim.
- Non-goals remain visible before implementation expands.
- Public claim safety remains part of the development process.

Negative / deferred:

- This does not build the local lab.
- This does not enable runtime execution.
- This does not authorize scanning.
- This does not demonstrate production deployment.
