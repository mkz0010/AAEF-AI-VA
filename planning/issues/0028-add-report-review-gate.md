# 0028: Add report review gate

## Status

In Progress

## Priority

P0

## Type

Report Review / Packet Candidate Control

## Background

Report findings can now be created from confirmed finding reviews, but they still need report review before they can be included in a report packet candidate.

## Decision Summary

Add report review gate.

Only approved report reviews can create a report packet candidate. The packet candidate remains not customer-delivery-ready.

## Acceptance Criteria

- report review module is added
- report review generator is added
- approved_for_report_packet / needs_revision / rejected decisions are supported
- only approved_for_report_packet creates report packet candidate
- report packet candidate requires packet review
- customer_delivery_ready remains false
- report_ready remains false
- secret_exposed_to_ai remains false
- evidence_required remains true
- mismatched review scope fails closed
- forbidden sensitive literals fail closed
- local checks pass

## Related Documents

- docs/35-report-review-gate.md
- docs/34-report-finding-promotion-gate.md
- planning/decisions/ADR-0029-add-report-review-gate.md
