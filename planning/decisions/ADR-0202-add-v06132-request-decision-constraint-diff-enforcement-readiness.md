# ADR-0202: Add v0.6.132 request/decision constraint-diff enforcement readiness

Status: Accepted
Date: 2026-05-10

## Context

v0.6.131 selected request/decision constraint-diff enforcement as a High-risk gate-semantics work item and assigned three checkpoints.

## Decision

Add a readiness checkpoint for request/decision constraint-diff enforcement.

The readiness checkpoint identifies comparison inputs, target discovery, expected behavior, diff categories, fail-closed boundaries, tests to add or update, evidence boundaries, and non-goals.

## Consequences

v0.6.133 may implement candidate behavior and tests.

No constraint-diff behavior, runtime behavior, validator behavior, schema, public sample, AAEF main handback state, or external submission state is changed by this readiness checkpoint.
