# ADR-0096: Add v0.6.25 static applied evidence fixture planning

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.24 defined the four minimum applied evidence scenarios. The next step
is to define the static fixture artifact plan for each scenario before generating
fixtures or evidence packages.

## Decision

Add a v0.6.25 static applied evidence fixture planning checkpoint.

The checkpoint defines planned fixture root, common fixture artifact set, common
identifier linkage, per-artifact fixture planning, per-scenario fixture plans, AAEF
five-questions fixture mapping, future static fixture generation readiness,
structural validator planning hooks, and runtime/scanning boundaries.

## Consequences

Positive:

- Each future scenario has a planned artifact set.
- Identifier linkage and non-execution evidence are planned before generation.
- Reviewer-facing summaries and non-proof statements are included in the fixture plan.
- Static/mock evidence remains separate from tool-backed local-lab diagnostic capture.

Negative / deferred:

- This does not generate fixtures.
- This does not generate evidence packages.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
