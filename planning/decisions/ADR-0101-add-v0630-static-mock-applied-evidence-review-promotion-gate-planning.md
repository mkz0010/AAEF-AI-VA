# ADR-0101: Add v0.6.30 static/mock applied evidence package review and promotion gate planning

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.29 generated a private-first static/mock applied evidence package.
Before any public sanitized sample promotion is considered, the project needs a
review and promotion gate plan.

## Decision

Add a v0.6.30 static/mock applied evidence package review and promotion gate planning
checkpoint.

The checkpoint defines review input package, review objectives, private package
review criteria, promotion gate criteria, promotion blocker categories, promotion
outcomes, public sample planning boundary, AAEF-side reporting boundary, runtime and
diagnostic execution separation, structural validator relationship, rollback posture,
and runtime/scanning boundaries.

## Consequences

Positive:

- The private generated package is not automatically promoted to public sample status.
- Public promotion criteria and blockers are explicit.
- AAEF-side reporting can reference private package existence without exposing content.
- Real local-lab diagnostic execution remains separate from static/mock promotion.

Negative / deferred:

- This does not create public samples.
- This does not generate a private review record.
- This does not implement the structural validator.
- This does not run diagnostic tools.
- This does not enable scanner execution.
