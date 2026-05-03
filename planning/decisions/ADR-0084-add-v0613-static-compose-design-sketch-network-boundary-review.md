# ADR-0084: Add v0.6.13 static Compose design sketch and network boundary review

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.12 defined non-running Docker Compose design review planning. The next step is to define an even safer static design sketch layer that can record service roles, network boundary intent, and port binding intent without creating a runnable Compose file.

## Decision

Add a v0.6.13 static Compose design sketch and network boundary review checkpoint.

The checkpoint records public-safe design boundary, planning proposition, static sketch prohibition, static sketch model, sketch status model, service role inventory, network boundary review, port binding intent review, outbound network posture, environment and secret posture, volume and persistence posture, reset and teardown posture, static sketch review questions, preflight evidence expectations, advancement gate model, human review requirements, generated artifact boundary, non-proof statement, relationship to v0.6.12, and runtime, scanning, Compose, image pull, Docker execution, port binding, and delivery prohibitions.

## Consequences

Positive:

- Future lab design can be discussed without creating runnable Compose configuration.
- Network and port posture are reviewed before file creation.
- Runnable syntax is treated as a blocking condition at this checkpoint.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not create Docker Compose files.
- This does not pull images.
- This does not run containers.
- This does not bind ports.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
