# Report Packet Review Gate

## Purpose

This document defines the first report packet review gate for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.1.27 introduced report review and report packet candidate assembly. v0.1.28 adds packet review before delivery authorization.

## Core Principle

A report packet candidate is not customer-delivery-ready.

Packet review may allow a delivery authorization candidate to be assembled, but customer delivery still requires a separate delivery authorization gate.

## Terminology

This project avoids `final` as a lifecycle label for report artifacts.

The lifecycle uses reviewable terms:

- `report_finding`
- `report_review`
- `report_packet_candidate`
- `report_packet_review`
- `delivery_authorization_candidate`

## Review Decisions

The MVP supports:

- `approved_for_delivery_authorization`
- `needs_revision`
- `rejected`

## Current MVP Behavior

Only `approved_for_delivery_authorization` may create a delivery authorization candidate.

Even then, the delivery authorization candidate keeps:

~~~text
requires_delivery_authorization: true
customer_delivery_ready: false
report_ready: false
secret_exposed_to_ai: false
evidence_required: true
~~~

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/report-packet-reviews/demo/
~~~

Generated files for approved review:

- `raw-artifact.demo.json`
- `sanitized-artifact.generated.json`
- `finding-candidate.generated.json`
- `finding-review.generated.json`
- `report-finding.generated.json`
- `report-review.generated.json`
- `report-packet-candidate.generated.json`
- `report-packet-review.generated.json`
- `report-packet-review-gate-result.generated.json`
- `delivery-authorization-candidate.generated.json`
- `report-packet-review.generated.md`

## Example Command

~~~bash
py tools/generate_report_packet_review_demo.py
~~~

You can also test non-delivery outcomes:

~~~bash
py tools/generate_report_packet_review_demo.py needs_revision
py tools/generate_report_packet_review_demo.py rejected
~~~

## Fail-Closed Conditions

The packet review gate fails closed when:

- packet review decision is unsupported,
- packet review is not bound to the packet candidate,
- packet review scope does not match,
- customer_delivery_ready is true,
- report_ready is true,
- evidence_required is false,
- secret_exposed_to_ai is true,
- obvious sensitive literals appear in review content.

## Future Work

Future versions should add:

- delivery authorization gate,
- customer-delivery readiness checks,
- delivery approver identity policy,
- customer scope authorization linkage,
- export controls,
- report packet versioning,
- post-delivery evidence records.

## Relationship to Delivery Authorization Gate

A `delivery_authorization_candidate` must pass delivery authorization before a delivery package can be generated.

The current MVP may generate a package but still does not perform customer delivery.

See `docs/37-delivery-authorization-gate.md`.
