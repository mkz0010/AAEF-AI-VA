# ADR-0093: Add v0.6.22 AAEF applied evidence work intake and current-state review

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.21 completed static fixture validator required-node check planning.
A new AAEF-side request asks AAEF-AI-VA to prioritize a safe, minimal applied
evidence record for AI-assisted vulnerability assessment workflows.

The request changes the immediate priority: the next step should not be required-node
minimal implementation. The next step should be intake, current-state inventory, and
work ordering for an applied evidence package.

## Decision

Add a v0.6.22 AAEF applied evidence work intake and current-state review checkpoint.

The checkpoint records current repository state, public/private boundaries, safe local
lab scope, required applied evidence chain, minimum scenarios, reviewer walkthrough
requirement, AAEF five questions mapping requirement, structural validator posture,
optimal work ordering, completion signal expectations, and runtime/scanning boundary
markers.

## Consequences

Positive:

- AAEF-AI-VA responds to the AAEF-side applied evidence request before continuing
  validator implementation.
- The next work is ordered around reviewable evidence rather than scanner strength.
- Public/private and patent-sensitive abstraction boundaries are kept explicit.
- Required-node implementation is deferred until applied evidence package design is
  anchored.

Negative / deferred:

- This does not implement required-node checks.
- This does not generate fixture files.
- This does not create the applied evidence package yet.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
