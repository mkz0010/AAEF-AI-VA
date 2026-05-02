# ADR-0031: Add delivery authorization gate before delivery package generation

## Status

Accepted

## Context

The platform can now create delivery authorization candidates from approved report packet reviews.

A delivery authorization candidate still should not imply customer delivery. The project needs a gate that can authorize package generation while keeping dispatch and customer delivery disabled.

The project avoids `final` lifecycle labels and uses reviewable artifact names.

## Decision

Add a delivery authorization gate.

The gate supports `authorized_for_delivery_package`, `needs_revision`, and `rejected`.

Only authorized delivery candidates may create a `delivery_package`. Even then, customer delivery, dispatch, and report-ready status remain false.

## Consequences

- Delivery package generation becomes an explicit gated action.
- Customer delivery remains unavailable in the MVP.
- The project separates package generation from delivery dispatch.
- The project continues to enforce staged review and avoids final lifecycle terminology.
