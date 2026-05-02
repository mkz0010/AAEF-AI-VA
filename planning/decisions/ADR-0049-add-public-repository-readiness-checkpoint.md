# ADR-0049: Add public repository readiness checkpoint

Status: Accepted  
Date: 2026-05-02

## Context

AAEF-AI-VA has reached a point where it has:

- runtime execution prohibition boundaries,
- preflight evidence examples and negative examples,
- AGPL-3.0 licensing boundary,
- AAEF / CC BY 4.0 attribution boundary,
- commercial-use boundary documentation.

Before creating or pushing a public repository, the project needs a checkpoint that
separates public repository readiness from runtime execution readiness.

## Decision

Add a public repository readiness checkpoint for v0.3.6.

The checkpoint records that public review readiness requires visible repository
metadata and publication boundaries, but does not authorize runtime execution.

The checkpoint is supported by a local test that verifies expected repository
publication markers.

## Consequences

Positive:

- Public publication can be prepared without weakening execution controls.
- License, attribution, private artifact, and commercial-use boundaries are easier to review.
- The repository gains a pre-publication checklist suitable for local validation.

Negative / deferred:

- This does not create a remote repository.
- This does not review third-party dependencies deeply.
- This does not define final commercial contract terms.
- This does not replace legal review.
