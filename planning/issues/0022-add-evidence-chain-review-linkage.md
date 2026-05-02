# 0022: Add evidence chain review linkage

## Status

In Progress

## Priority

P0

## Type

Evidence / Review Linkage

## Background

The project now has separate records for execution, evidence, readiness review, human approval, and approval gate results.

The next step is to link these records so that a diagnostic action can be reconstructed.

## Decision Summary

Add evidence chain linkage and generator.

The evidence chain validates ID and field consistency across the full review path and produces generated private JSON/Markdown artifacts.

## Acceptance Criteria

- evidence chain module is added
- evidence chain generator is added
- request/auth/result/evidence IDs are validated
- target/scope/tool/operation consistency is validated
- operator review and human approval are linked
- human approval gate result is linked
- real execution remains false
- secret exposure remains false
- generated chain JSON and Markdown are produced under ignored/private paths
- local checks pass

## Related Documents

- docs/29-evidence-chain-review-linkage.md
- docs/28-human-approval-record-gate.md
- docs/27-operator-readiness-review.md
- planning/decisions/ADR-0023-add-evidence-chain-review-decision-linkage.md
