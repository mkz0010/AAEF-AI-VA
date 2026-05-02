# 0029: Add report packet review gate

## Status

In Progress

## Priority

P0

## Type

Report Packet / Delivery Authorization Control

## Background

Report packet candidates can now be created, but they still need packet review before delivery authorization can be considered.

## Decision Summary

Add report packet review gate.

Only approved packet reviews can create a delivery authorization candidate. The delivery candidate remains not customer-delivery-ready.

## Acceptance Criteria

- report packet review module is added
- report packet review generator is added
- approved_for_delivery_authorization / needs_revision / rejected decisions are supported
- only approved_for_delivery_authorization creates delivery authorization candidate
- delivery authorization candidate requires delivery authorization
- customer_delivery_ready remains false
- report_ready remains false
- secret_exposed_to_ai remains false
- evidence_required remains true
- mismatched review scope fails closed
- forbidden sensitive literals fail closed
- local checks pass

## Related Documents

- docs/36-report-packet-review-gate.md
- docs/35-report-review-gate.md
- planning/decisions/ADR-0030-add-report-packet-review-gate.md
