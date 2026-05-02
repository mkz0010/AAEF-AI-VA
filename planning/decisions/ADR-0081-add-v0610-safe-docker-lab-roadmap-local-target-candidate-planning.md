# ADR-0081: Add v0.6.10 safe Docker lab roadmap and local target candidate planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.8 and v0.6.9 defined public-safe demo, reviewer walkthrough,
evidence reconstruction, and sample report demonstration planning.

The next step is to plan a future safe local lab path without enabling Docker
execution, scanner execution, external network testing, or customer-target
operation.

## Decision

Add a v0.6.10 safe Docker lab roadmap and local target candidate planning
checkpoint.

The checkpoint records:

- public-safe design boundary,
- roadmap proposition,
- candidate local targets,
- candidate acceptance criteria,
- candidate exclusion criteria,
- phased safe Docker lab roadmap,
- required preflight evidence for future advancement,
- human review expectations,
- network boundary requirements,
- tool interaction boundary,
- generated artifact boundary,
- synthetic data requirement,
- non-proof statement,
- relationship to v0.6.5 through v0.6.9,
- runtime, scanning, Docker execution, and delivery prohibitions.

## Consequences

Positive:

- Future lab work can be discussed without jumping to execution.
- Local target candidates are named with explicit candidate-only boundaries.
- Docker, network, target, preflight, and review expectations are recorded early.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not install Docker.
- This does not run containers.
- This does not create Docker Compose files.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
