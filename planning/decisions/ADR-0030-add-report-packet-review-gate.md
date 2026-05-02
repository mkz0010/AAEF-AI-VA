# ADR-0030: Add report packet review gate before delivery authorization

## Status

Accepted

## Context

The platform can now create report packet candidates from approved report reviews.

A report packet candidate still should not be customer-delivery-ready. It needs packet review before any delivery authorization workflow.

The project avoids `final` lifecycle labels and uses reviewable artifact names.

## Decision

Add a report packet review gate.

The gate supports `approved_for_delivery_authorization`, `needs_revision`, and `rejected`.

Only approved packet reviews may create a `delivery_authorization_candidate`. Even then, customer delivery remains blocked.

## Consequences

- Report packet candidates move through an explicit packet review gate.
- Delivery authorization becomes a separate reviewable stage.
- Customer delivery remains unavailable in the MVP.
- The project continues to enforce staged review and avoids final lifecycle terminology.
