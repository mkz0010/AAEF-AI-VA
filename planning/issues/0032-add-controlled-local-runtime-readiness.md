# 0032: Add controlled local runtime readiness

## Status

In Progress

## Priority

P0

## Type

Runtime Readiness / Execution Boundary

## Background

The project has a stable v0.1.30 lifecycle checkpoint. The next phase should move toward execution, but only by adding runtime readiness checks first.

The project should detect local runtime availability without starting tools or performing network activity.

## Decision Summary

Add controlled local ZAP runtime readiness.

Runtime detection is allowed. Execution remains blocked.

## Acceptance Criteria

- runtime readiness module is added
- runtime readiness generator is added
- ZAP runtime profile is added
- runtime detection can be simulated in tests
- runtime detection does not execute external processes
- external_process_executed remains false
- network_activity_performed remains false
- real_execution_permitted remains false
- credential_injection_permitted remains false
- raw_artifact_capture_permitted remains false
- sanitizer requirement remains true
- scope registry requirement remains true
- human approval requirement remains true for future execution transition
- local checks pass

## Related Documents

- docs/39-controlled-local-runtime-readiness.md
- docs/38-lifecycle-integration-checkpoint.md
- planning/decisions/ADR-0033-add-controlled-local-runtime-readiness.md
