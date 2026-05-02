# ADR-0060: Add commercial adoption preparation checkpoint

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA is now public, has a GitHub Release, and has recorded public launch and
release publication checkpoints.

The project should not be broadly promoted before there is a deliberate enterprise
adoption strategy. The immediate business value is more likely to come from targeted
conversations with vulnerability assessment companies, MSSPs, security consulting
firms, AI security teams, and security automation teams.

At the same time, the public repository should remain credible and technical, not
overly sales-oriented.

## Decision

Add a v0.5.0 commercial adoption preparation checkpoint.

The checkpoint records:

- public/private commercial-material boundary,
- commercial positioning,
- target customer profiles,
- differentiation from generic AI vulnerability assessment tools,
- suggested enterprise conversation flow,
- commercial inquiry wording,
- claim boundaries,
- continued runtime-execution prohibition.

A private local sales pack may be generated under `private-not-in-git/`, but it must
not be tracked.

## Consequences

Positive:

- The project can support targeted enterprise conversations without noisy public promotion.
- Public repository credibility is preserved.
- Sales material and customer-specific planning remain private.
- Commercial inquiry wording is separated from vulnerability reporting and runtime authorization.

Negative / deferred:

- This does not publish a contact channel.
- This does not define pricing.
- This does not create a commercial contract.
- This does not authorize runtime execution.
