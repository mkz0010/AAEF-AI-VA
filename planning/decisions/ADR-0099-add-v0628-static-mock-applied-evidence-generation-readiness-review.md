# ADR-0099: Add v0.6.28 static/mock applied evidence package generation readiness review

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.27 defined applied evidence structural validator planning. The next
question is whether the project is ready to generate a static/mock applied evidence
package. Before generation starts, the project should record readiness criteria,
blocker categories, private-first generation posture, public-safe promotion criteria,
and runtime/scanning boundaries.

## Decision

Add a v0.6.28 static/mock applied evidence package generation readiness review
checkpoint.

The checkpoint defines readiness summary, required readiness inputs, static/mock
generation readiness criteria, private-first generation posture, public-safe promotion
criteria, blocker categories, minimum generated package candidate, generation sequence,
structural validator readiness relationship, reviewer review requirement, diagnostic
system timing, completion signal for AAEF side, and runtime/scanning boundaries.

## Consequences

Positive:

- The project can decide whether static/mock generation is safe before writing
  generated artifacts.
- Private-first generation is preferred over public sample generation.
- Blocker categories and public-safe promotion criteria are explicit.
- Live diagnostic execution remains separate from static/mock evidence generation.

Negative / deferred:

- This does not generate evidence packages.
- This does not implement the structural validator.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
