# ADR-0080: Add v0.6.9 evidence reconstruction and sample report demonstration planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.8 defined a public-safe, non-executing demo scenario and reviewer
walkthrough.

The next step is to define how evidence reconstruction and sample report
demonstration can be planned without enabling execution, creating customer
deliverables, or exposing private advanced feature details.

## Decision

Add a v0.6.9 evidence reconstruction and sample report demonstration planning
checkpoint.

The checkpoint records:

- public-safe design boundary,
- demonstration proposition,
- evidence reconstruction scope,
- evidence reconstruction chain,
- sample evidence packet planning,
- sample report demonstration packet,
- report finding demonstration boundary,
- evidence-to-report transition,
- reviewer walkthrough questions,
- evidence sufficiency posture,
- human review and delivery boundary,
- private artifact boundary,
- synthetic data requirement,
- non-proof statement,
- relationship to v0.6.6, v0.6.7, and v0.6.8,
- runtime, scanning, and delivery prohibitions.

## Consequences

Positive:

- The project can explain evidence and report traceability before execution exists.
- Reviewers can inspect how requests, gates, evidence, findings, report packets,
  and delivery boundaries relate.
- Future sample artifacts have a safer planning boundary.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not create generated sample evidence artifacts.
- This does not create generated sample report artifacts.
- This does not enable dry-run behavior.
- This does not enable runtime execution.
- This does not create commercial PoC readiness.
