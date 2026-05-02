# ADR-0082: Add v0.6.11 local lab candidate profile and preflight evidence planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.10 defined a safe Docker lab roadmap and local target candidate
planning. The next step is to define candidate profile fields and preflight evidence
expectations without selecting a target for execution or starting any local lab.

## Decision

Add a v0.6.11 local lab candidate profile and preflight evidence planning checkpoint.

The checkpoint records:

- public-safe design boundary,
- planning proposition,
- candidate profile model,
- candidate profile examples,
- candidate comparison criteria,
- preflight evidence package model,
- preflight evidence status model,
- advancement gate model,
- candidate rejection criteria,
- human review requirements,
- network and target boundary,
- tool action taxonomy planning,
- generated artifact boundary,
- synthetic data requirement,
- non-proof statement,
- relationship to v0.6.10,
- runtime, scanning, Docker execution, and delivery prohibitions.

## Consequences

Positive:

- Future local lab work gets reviewable candidate profile fields.
- Preflight evidence can be planned before any lab execution is considered.
- Candidate comparison remains non-executing and gate-bound.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not select a target for execution.
- This does not install Docker.
- This does not run containers.
- This does not collect live preflight evidence.
- This does not create Docker Compose files.
- This does not enable scanner execution.
