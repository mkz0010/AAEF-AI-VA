# 0030: Add delivery authorization gate

## Status

In Progress

## Priority

P0

## Type

Delivery Authorization / Package Control

## Background

Delivery authorization candidates can now be created, but there is no gate that authorizes package generation while keeping customer delivery disabled.

## Decision Summary

Add delivery authorization gate.

Only authorized delivery candidates can create a delivery package. The delivery package remains not customer-delivery-ready and is not dispatched.

## Acceptance Criteria

- delivery authorization module is added
- delivery authorization generator is added
- authorized_for_delivery_package / needs_revision / rejected decisions are supported
- only authorized_for_delivery_package creates delivery package
- delivery package is generated but not dispatched
- customer_delivery_performed remains false
- customer_delivery_ready remains false
- report_ready remains false
- secret_exposed_to_ai remains false
- evidence_required remains true
- mismatched authorization scope fails closed
- forbidden sensitive literals fail closed
- local checks pass

## Related Documents

- docs/37-delivery-authorization-gate.md
- docs/36-report-packet-review-gate.md
- planning/decisions/ADR-0031-add-delivery-authorization-gate.md
