# ADR-0034: Add local target lab profile before bounded execution work

## Status

Accepted

## Context

v0.2.0 introduced controlled local runtime readiness.

Before any future local execution transition, the target boundary must be defined. Autonomous execution without a target is unsafe.

The project needs a local target lab profile that permits only local or Docker-internal intentionally vulnerable lab targets and keeps execution blocked.

## Decision

Add local target lab profile and gate.

The profile supports localhost-only, docker-internal-only, and intentionally-vulnerable-lab-only target modes.

Customer targets, external network targets, scan execution, network activity, credential injection, and raw artifact capture remain forbidden.

## Consequences

- Future bounded execution has a target boundary to reference.
- Customer and external targets are explicitly out of scope.
- The project separates target definition from execution authority.
- The no-scan/no-network boundary remains intact.
