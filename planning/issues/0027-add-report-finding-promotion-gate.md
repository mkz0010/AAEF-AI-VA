# 0027: Add report finding promotion gate

## Status

In Progress

## Priority

P0

## Type

Report Finding / Promotion Control

## Background

Finding candidates can now be reviewed, but confirmed finding reviews need a controlled path into report finding review objects.

The project should not use `final` lifecycle terminology.

## Decision Summary

Add report finding promotion gate.

Confirmed finding reviews may create a `report_finding`, but the report finding remains not report-ready and not customer-delivery-ready.

## Acceptance Criteria

- report promotion module is added
- report finding generator is added
- only confirmed finding reviews can be promoted
- rejected/needs_more_info/duplicate/false_positive are not promoted
- report finding binds to candidate and finding review
- report finding requires report review
- report finding is not customer-delivery-ready
- report finding keeps report_ready false
- secret_exposed_to_ai remains false
- forbidden sensitive literals fail closed
- local checks pass

## Related Documents

- docs/34-report-finding-promotion-gate.md
- docs/33-finding-candidate-review-gate.md
- planning/decisions/ADR-0028-add-report-finding-promotion-gate.md
