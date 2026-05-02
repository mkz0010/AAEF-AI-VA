# 0017: Add controlled executor policy

## Status

In Progress

## Priority

P0

## Type

Prototype / Control

## Background

v0.1.15 added a ZAP adapter dry-run command plan.

The next step is to define the executor-side control layer that evaluates command plans before any future real tool execution.

## Decision Summary

Add a dry-run-only controlled executor policy.

The executor validates command plans and returns an acceptance result without executing external processes or performing network activity.

## Acceptance Criteria

- controlled executor module is added
- executor accepts valid dry-run command plan
- executor rejects non-dry-run mode
- executor rejects external process execution
- executor rejects secret material
- executor rejects destructive tests
- executor rejects external discovery
- executor rejects shell command or argv fields
- executor rejects tracked/public artifact paths
- local checks pass

## Related Documents

- docs/24-controlled-executor-policy.md
- docs/23-zap-adapter-command-plan.md
- docs/22-internal-adapter-artifact-policy.md
- planning/decisions/ADR-0018-add-controlled-executor-policy-before-real-tool-execution.md
