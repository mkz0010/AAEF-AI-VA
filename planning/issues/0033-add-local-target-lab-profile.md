# 0033: Add local target lab profile

## Status

In Progress

## Priority

P0

## Type

Target Boundary / Lab Profile

## Background

Runtime readiness now exists, but a future execution transition also needs an explicit target boundary.

Autonomous execution without a defined target is unsafe.

## Decision Summary

Add local target lab profile and gate.

Only local, Docker-internal, intentionally vulnerable lab targets are allowed for future runtime transition consideration. Scanning remains disabled.

## Acceptance Criteria

- local target lab module is added
- local target lab generator is added
- localhost-only target mode is supported
- docker-internal target mode is supported
- intentionally vulnerable lab mode is supported
- customer targets are forbidden
- external network targets are forbidden
- scan execution remains false
- network activity remains false
- credential injection remains false
- raw artifact capture remains false
- scope registry binding remains required
- runtime readiness remains required
- local checks pass

## Related Documents

- docs/40-local-target-lab-profile.md
- docs/39-controlled-local-runtime-readiness.md
- planning/decisions/ADR-0034-add-local-target-lab-profile.md
