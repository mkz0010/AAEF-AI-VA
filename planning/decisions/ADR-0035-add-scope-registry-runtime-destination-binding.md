# ADR-0035: Add scope registry runtime destination binding before bounded execution transition

## Status

Accepted

## Context

v0.2.0 added controlled local runtime readiness. v0.2.1 added local target lab profiles.

The next step is to bind a runtime readiness profile to a local target lab profile through a scope-registry-style destination record.

Autonomous execution without a bound target is unsafe. Runtime detection alone must not authorize execution, and target definition alone must not authorize execution.

## Decision

Add scope registry runtime destination binding.

The binding associates the ZAP runtime readiness profile with a local lab target profile, records a destination ID, and allows only a future bounded execution transition candidate.

The binding does not permit scan execution, network activity, process execution, credential injection, raw artifact capture, customer targets, or external network targets.

## Consequences

- Runtime and target boundaries are explicitly connected.
- Targetless autonomous execution is prevented.
- Future bounded execution work has a concrete binding object to reference.
- The no-execution boundary remains intact.
