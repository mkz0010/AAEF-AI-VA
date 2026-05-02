# 0020: Add operator readiness review summary

## Status

In Progress

## Priority

P0

## Type

Operations / Review

## Background

The real execution readiness gate reports blockers, but operators need a reviewable summary.

The project should convert machine-readable readiness results into operator-facing review artifacts.

## Decision Summary

Add operator readiness review summary generation.

The summary categorizes blockers, recommends not executing by default, and produces private generated Markdown and JSON review artifacts.

## Acceptance Criteria

- operator readiness review module is added
- readiness blockers are categorized
- next actions are generated
- default recommendation is do_not_execute
- generated Markdown review is produced
- generated JSON review is produced
- generated review outputs remain under ignored/private paths
- local checks pass

## Related Documents

- docs/27-operator-readiness-review.md
- docs/26-real-execution-readiness-gate.md
- planning/decisions/ADR-0021-add-operator-readiness-review-summary.md
