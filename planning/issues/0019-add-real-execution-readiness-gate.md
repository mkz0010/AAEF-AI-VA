# 0019: Add real execution readiness gate

## Status

In Progress

## Priority

P0

## Type

Control / Readiness

## Background

The project now has adapter command plans and controlled executor dry-run policy.

Before any real tool execution is introduced, the project needs a readiness gate that makes the required prerequisites explicit and machine-checkable.

## Decision Summary

Add a real execution readiness gate.

The gate reports blockers and does not execute tools.

Default MVP behavior keeps real execution disabled.

## Acceptance Criteria

- real execution gate module is added
- default readiness config disables real execution
- valid dry-run command plan is evaluated
- gate reports real execution as not permitted by default
- gate identifies dry-run command plan as blocker
- gate fails closed when evidence emission is disabled
- gate fails closed when artifact paths are not private
- gate fails closed when human approval status is invalid
- gate fails closed when command plan fails controlled executor validation
- local checks pass

## Related Documents

- docs/26-real-execution-readiness-gate.md
- docs/24-controlled-executor-policy.md
- docs/25-scope-registry-target-alias-resolution.md
- planning/decisions/ADR-0020-add-real-execution-readiness-gate.md
