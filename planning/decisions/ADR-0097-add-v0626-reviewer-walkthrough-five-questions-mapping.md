# ADR-0097: Add v0.6.26 reviewer walkthrough and five questions mapping

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.25 defined static applied evidence fixture planning. The next step is
to ensure those future fixtures are understandable to external reviewers and directly
mapped to AAEF's five practical questions.

## Decision

Add a v0.6.26 reviewer walkthrough and five questions mapping checkpoint.

The checkpoint defines reviewer walkthrough artifact planning, reader model, common
walkthrough sequence, AAEF five questions, artifact-to-question mapping, per-scenario
walkthroughs, scenario outcome explanation matrix, five questions mapping by scenario,
non-proof walkthrough requirements, reviewer acceptance checklist, future walkthrough
generation readiness, structural validator planning hooks, and runtime/scanning
boundaries.

## Consequences

Positive:

- Future evidence artifacts will be reviewer-facing, not just JSON-shaped.
- The AAEF five questions are explicitly mapped for all four scenarios.
- Non-execution evidence and non-proof boundaries remain visible to reviewers.
- Static/mock evidence remains separate from tool-backed local-lab diagnostic capture.

Negative / deferred:

- This does not generate walkthrough files.
- This does not generate evidence packages.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
