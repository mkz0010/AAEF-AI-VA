# ADR-0029: Add report review gate before report packet candidate assembly

## Status

Accepted

## Context

The platform can now promote confirmed finding reviews into report findings.

A report finding still should not become customer-delivery-ready. It needs a report review gate before packet assembly.

The project also avoids `final` as a lifecycle label and uses reviewable artifact names.

## Decision

Add a report review gate.

The gate supports `approved_for_report_packet`, `needs_revision`, and `rejected`.

Only approved report reviews may create a `report_packet_candidate`. Even then, customer delivery remains blocked.

## Consequences

- Report findings move through an explicit review gate.
- Packet assembly becomes a separate reviewable stage.
- Customer delivery remains unavailable in the MVP.
- The project continues avoiding misleading final lifecycle terminology.
