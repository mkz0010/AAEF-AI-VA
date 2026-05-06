# ADR-0103: Add v0.6.32 static/mock applied evidence public sample promotion decision record

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.31 generated a private review record for the private static/mock
applied evidence package. The review status was `reviewed_keep_private`, promotion
status was `keep_private`, scenario count was four, blocker categories were empty, and
public sample / runtime / scanner / customer-target / delivery authorization remained
false.

## Decision

Add a v0.6.32 static/mock applied evidence package public sample promotion decision
record.

The decision keeps the private package private, does not authorize public sample
generation, and allows only a later sanitized public sample planning checkpoint to be
considered under separate review.

## Consequences

Positive:

- The v0.6.31 review result is translated into a clear promotion decision.
- Direct public generation remains blocked.
- A later sanitized public sample planning checkpoint can be considered without
  authorizing sample generation.
- Runtime execution, scanner execution, customer-target operation, and delivery remain
  separate blocked tracks.

Negative / deferred:

- This does not create public samples.
- This does not implement the structural validator.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
