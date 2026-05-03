# ADR-0083: Add v0.6.12 non-running Docker Compose design review planning

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.10 defined a safe Docker lab roadmap. v0.6.11 defined local lab
candidate profiles and preflight evidence planning.

The next step is to define how a future Docker Compose design should be reviewed
before any Compose file is created, image is pulled, container is started, or scanner
is run.

## Decision

Add a v0.6.12 non-running Docker Compose design review planning checkpoint.

The checkpoint records:

- public-safe design boundary,
- planning proposition,
- non-running Compose design review model,
- candidate design posture,
- network boundary review,
- port exposure review,
- image provenance review,
- environment variable and secret review,
- volume and persistence review,
- reset and teardown review,
- resource limit review,
- image retrieval and assessment activity separation,
- preflight evidence expectations,
- advancement gate model,
- human review requirements,
- generated artifact boundary,
- non-proof statement,
- relationship to v0.6.10 and v0.6.11,
- runtime, scanning, Compose, image pull, Docker execution, and delivery prohibitions.

## Consequences

Positive:

- Future Compose work gets a design-review checkpoint before file creation.
- Image pull, network, port, secret, volume, and reset risks are considered early.
- Dependency setup is separated from assessment activity.
- Public materials remain separated from private advanced feature workstreams.

Negative / deferred:

- This does not create Docker Compose files.
- This does not pull images.
- This does not run containers.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
