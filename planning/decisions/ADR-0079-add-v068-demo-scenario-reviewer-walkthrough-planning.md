# ADR-0079: Add v0.6.8 demo scenario and reviewer walkthrough planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.6 defined the AI request decision boundary and tool selection
criteria. v0.6.7 defined observation normalization and Diagnostic Fidelity Risk.

The next step is to define a public-safe demo scenario and reviewer walkthrough
that can explain the model without enabling execution or exposing private advanced
feature details.

## Decision

Add a v0.6.8 demo scenario and reviewer walkthrough planning checkpoint.

The checkpoint records:

- public-safe design boundary,
- core walkthrough proposition,
- walkthrough audience,
- demo scenario shape,
- reviewer walkthrough sequence,
- walkthrough artifacts,
- AI-visible information boundary,
- what AI may do in the walkthrough,
- what gates should show in the walkthrough,
- outcome model,
- non-proof statement,
- reviewer questions,
- demo success criteria,
- private workstream separation,
- relationship to v0.6.6 and v0.6.7,
- runtime and scanning prohibitions.

## Consequences

Positive:

- Reviewers can understand the control model before dry-run or lab work expands.
- The project can explain AI request generation without implying execution authority.
- Private advanced feature details remain separated from public demo planning.
- Future evidence and report demonstration planning has a safer foundation.

Negative / deferred:

- This does not add demo fixtures.
- This does not implement dry-run behavior.
- This does not enable runtime execution.
- This does not create commercial PoC readiness.
