# ADR-0064: Add dependency and repository governance readiness checkpoint

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA has public launch, commercial adoption, README compatibility, and
licensing/trademark/authorship protection checkpoints.

Before spending more effort on private sales material, the repository foundation
should be strengthened further. The project benefits from clear governance posture
around dependencies, license inventory expectations, branch protection planning,
release/tag governance, security disclosure, and private artifact boundaries.

## Decision

Add a v0.5.4 dependency and repository governance readiness checkpoint.

The checkpoint records:

- dependency/license inventory expectations,
- branch protection and ruleset planning,
- release and tag governance,
- security and disclosure governance,
- commercial-readiness relationship,
- runtime and scanning prohibitions.

## Consequences

Positive:

- The repository appears more mature to future technical and business reviewers.
- Future commercial discussions can point to governance readiness.
- Dependency and branch protection work is scoped without overclaiming completed legal or GitHub administration work.
- Runtime execution remains blocked.

Negative / deferred:

- This does not configure GitHub branch protection.
- This does not generate a full SBOM.
- This does not complete legal dependency review.
- This does not create a commercial contract.
- This does not authorize runtime execution.
