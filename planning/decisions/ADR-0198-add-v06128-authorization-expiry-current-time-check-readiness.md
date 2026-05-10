# ADR-0198: Add v0.6.128 authorization expiry current-time check readiness

Status: Accepted
Date: 2026-05-10

## Context

v0.6.127 selected authorization expiry checked against current time as a High-risk gate-semantics work item and assigned three checkpoints.

## Decision

Add a readiness checkpoint for authorization expiry current-time checking.

The readiness checkpoint identifies expected behavior, target discovery, tests to add or update, fail-closed boundaries, current-time source boundaries, and non-goals.

## Consequences

v0.6.129 may implement candidate behavior and tests.

No authorization behavior, runtime behavior, validator behavior, schema, public sample, AAEF main handback state, or external submission state is changed by this readiness checkpoint.
