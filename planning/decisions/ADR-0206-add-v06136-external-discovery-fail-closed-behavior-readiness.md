# ADR-0206: Add v0.6.136 external discovery fail-closed behavior readiness

Status: Accepted
Date: 2026-05-10

## Context

v0.6.135 selected external_discovery=true fail-closed behavior as a High-risk gate-semantics work item and assigned three checkpoints.

## Decision

Add a readiness checkpoint for external discovery fail-closed behavior.

The readiness checkpoint identifies current semantics to inspect, target discovery, target-boundary inputs, expected behavior, fail-closed boundaries, tests to add or update, evidence boundaries, and non-goals.

## Consequences

v0.6.137 may implement candidate behavior and tests.

No external_discovery behavior, runtime behavior, validator behavior, schema, public sample, AAEF main handback state, or external submission state is changed by this readiness checkpoint.
