# 0026: Add finding candidate review gate

## Status

In Progress

## Priority

P0

## Type

Finding Review / Promotion Control

## Background

Sanitized finding candidates exist, but there is no review gate that records whether a candidate is confirmed, rejected, needs more information, duplicate, or false positive.

## Decision Summary

Add finding candidate review gate.

The gate records human review decisions while keeping report_ready false in the current MVP.

## Acceptance Criteria

- finding review module is added
- finding review generator is added
- confirmed/rejected/needs_more_info/duplicate/false_positive decisions are supported
- review records bind to candidate ID, sanitized artifact ref, tool, operation, target, and scope
- confirmed candidate can become eligible for future report promotion review
- no review result is report-ready in current MVP
- secret_exposed_to_ai remains false
- evidence_required remains true
- mismatched review scope fails closed
- forbidden sensitive literals fail closed
- local checks pass

## Related Documents

- docs/33-finding-candidate-review-gate.md
- docs/32-sanitized-finding-candidate-model.md
- planning/decisions/ADR-0027-add-finding-candidate-review-gate.md
