# 0023: Add evidence reconstruction report

## Status

In Progress

## Priority

P0

## Type

Evidence / Reconstruction

## Background

The project now has evidence chain linkage, but reviewers need a report that explains the chain.

## Decision Summary

Add an evidence reconstruction report generator.

The report summarizes the linked chain and explains why real execution is not permitted in the current MVP.

## Acceptance Criteria

- reconstruction report module is added
- reconstruction report generator is added
- generated JSON report is produced under ignored/private path
- generated Markdown report is produced under ignored/private path
- report includes key IDs
- report includes safety assertions
- report includes readiness blockers
- report includes next actions
- report includes chain nodes and links
- report states real execution is not permitted
- local checks pass

## Related Documents

- docs/30-evidence-reconstruction-report.md
- docs/29-evidence-chain-review-linkage.md
- planning/decisions/ADR-0024-add-evidence-reconstruction-report.md
