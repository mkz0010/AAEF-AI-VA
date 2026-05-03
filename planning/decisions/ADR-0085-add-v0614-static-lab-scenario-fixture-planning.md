# ADR-0085: Add v0.6.14 static lab scenario fixture planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.13 defined static Compose design sketch and network boundary review.
The next step is to define how a future non-executing static fixture set could link
candidate profile, static sketch, AI request, gate decision, expected evidence, and
reviewer walkthrough without creating runtime artifacts.

## Decision

Add a v0.6.14 static lab scenario fixture planning checkpoint.

The checkpoint records public-safe design boundary, planning proposition, static
fixture set model, fixture manifest model, fixture node status model,
candidate-to-sketch linkage, diagnostic context fixture boundary, AI request fixture
boundary, gate decision fixture boundary, expected evidence fixture boundary,
scenario trace model, reviewer walkthrough linkage, fixture validation expectations,
generated artifact boundary, non-proof statement, relationship to v0.6.13, and
runtime, scanning, Compose, image pull, Docker execution, port binding, fixture
generation, and delivery prohibitions.

## Consequences

Positive:

- Future demo fixtures can be planned without creating runtime artifacts.
- Candidate profile, static sketch, AI request, gate decision, and evidence expectation
  become reviewably connected.
- Fixture validation expectations are defined before fixture generation.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not generate fixture files.
- This does not create sample fixture artifacts.
- This does not create runnable Compose configuration.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
