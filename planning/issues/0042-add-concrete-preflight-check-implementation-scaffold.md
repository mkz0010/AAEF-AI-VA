# 0042: Add concrete preflight check implementation scaffold

## Status

In Progress

## Priority

P0

## Type

Preflight Implementation / Scaffold

## Background

v0.2.9 added a runtime transition checkpoint confirming readiness for preflight implementation work while keeping execution disabled.

The next step is to define how each required preflight check will be implemented and evidenced.

## Decision Summary

Add concrete preflight check implementation scaffold.

The scaffold records input sources, evidence types, fail-closed behavior, and responsibilities for each required preflight check while keeping all checks unimplemented and unsatisfied.

## Acceptance Criteria

- preflight check implementation module is added
- preflight check implementation generator is added
- all required preflight checks receive implementation scaffolds
- every check has input sources
- every check has evidence type
- every check requires evidence record
- every check fails closed on missing input
- every check fails closed on mismatch
- every check fails closed on stale state
- concrete_checks_implemented remains false
- all_required_checks_satisfied remains false
- preflight_satisfied remains false
- execution_authorized remains false
- runtime_enforcement_implemented remains false
- ready_for_runtime_execution remains false
- scan execution remains false
- network activity remains false
- real execution remains false
- external process execution remains false
- credential injection remains false
- raw artifact capture remains false
- customer target remains false
- external network target remains false
- local checks pass

## Related Documents

- docs/49-preflight-check-implementation-scaffold.md
- docs/48-runtime-transition-checkpoint.md
- planning/decisions/ADR-0043-add-concrete-preflight-check-implementation-scaffold.md
