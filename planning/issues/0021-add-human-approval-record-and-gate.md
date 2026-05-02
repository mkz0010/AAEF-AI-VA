# 0021: Add human approval record and gate

## Status

In Progress

## Priority

P0

## Type

Approval / Review Control

## Background

The operator readiness review produces a reviewable summary, but the project needs a way to record human decisions.

Human approval must be explicit, bound, expiring, and non-bypassable.

## Decision Summary

Add a human approval record and approval gate.

The gate validates approval binding and keeps real execution disabled in the current MVP.

## Acceptance Criteria

- human approval module is added
- approval generator is added
- approval decisions support approved, rejected, needs_more_info, keep_blocked
- approval record binds command plan, tool, operation, target, and scope
- approval expiration is enforced
- evidence_required must be true
- real_execution_allowed must remain false in current MVP
- mismatched approval scope fails closed
- generated approval JSON and Markdown are produced under ignored/private paths
- local checks pass

## Related Documents

- docs/28-human-approval-record-gate.md
- docs/27-operator-readiness-review.md
- docs/26-real-execution-readiness-gate.md
- planning/decisions/ADR-0022-add-human-approval-record-and-gate.md
