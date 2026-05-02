# 0016: Add ZAP adapter command plan

## Status

In Progress

## Priority

P0

## Type

Prototype / Design

## Background

Tool Gateway has adapter stubs, but the ZAP adapter should move closer to real integration in a controlled way.

The next step is a dry-run command plan that describes a future ZAP execution without actually running ZAP.

## Decision Summary

Add `build_command_plan()` to the ZAP adapter.

The command plan must be dry-run-only and must not include secrets or execute external processes.

## Acceptance Criteria

- ZAP adapter can build a dry-run command plan
- command plan includes tool, operation, target_id, scope_id, credential_ref, constraints, and artifact refs
- command plan marks external process execution as false
- command plan marks secret material as not included
- adapter tests verify command plan behavior
- Tool Gateway public generated outputs still exclude adapter output
- local checks pass

## Related Documents

- docs/23-zap-adapter-command-plan.md
- docs/22-internal-adapter-artifact-policy.md
- docs/20-tool-gateway-adapter-stubs.md
- planning/decisions/ADR-0017-add-zap-adapter-dry-run-command-plan.md
