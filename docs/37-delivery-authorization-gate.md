# Delivery Authorization Gate

## Purpose

This document defines the first delivery authorization gate for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.1.28 introduced report packet review and delivery authorization candidates. v0.1.29 adds delivery authorization before delivery package generation.

## Core Principle

Delivery authorization does not mean customer delivery.

The current MVP may generate a delivery package for review workflow validation, but it must not dispatch, transmit, or deliver anything to a customer.

## Terminology

This project avoids `final` as a lifecycle label for report artifacts.

The lifecycle uses reviewable terms:

- `report_packet_candidate`
- `report_packet_review`
- `delivery_authorization_candidate`
- `delivery_authorization`
- `delivery_package`

## Authorization Decisions

The MVP supports:

- `authorized_for_delivery_package`
- `needs_revision`
- `rejected`

## Current MVP Behavior

Only `authorized_for_delivery_package` may create a delivery package.

Even then, the delivery package keeps:

~~~text
delivery_dispatched: false
customer_delivery_performed: false
customer_delivery_ready: false
report_ready: false
secret_exposed_to_ai: false
evidence_required: true
requires_export_control_review: true
~~~

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/delivery-authorizations/demo/
~~~

Generated files for authorized package generation:

- `raw-artifact.demo.json`
- `sanitized-artifact.generated.json`
- `finding-candidate.generated.json`
- `finding-review.generated.json`
- `report-finding.generated.json`
- `report-review.generated.json`
- `report-packet-candidate.generated.json`
- `report-packet-review.generated.json`
- `delivery-authorization-candidate.generated.json`
- `delivery-authorization.generated.json`
- `delivery-authorization-gate-result.generated.json`
- `delivery-package.generated.json`
- `delivery-authorization.generated.md`

## Example Command

~~~bash
py tools/generate_delivery_authorization_demo.py
~~~

You can also test non-package outcomes:

~~~bash
py tools/generate_delivery_authorization_demo.py needs_revision
py tools/generate_delivery_authorization_demo.py rejected
~~~

## Fail-Closed Conditions

The delivery authorization gate fails closed when:

- authorization decision is unsupported,
- authorization is not bound to the delivery candidate,
- authorization scope does not match,
- delivery_dispatched is true,
- customer_delivery_performed is true,
- customer_delivery_ready is true,
- report_ready is true,
- evidence_required is false,
- secret_exposed_to_ai is true,
- obvious sensitive literals appear in authorization content.

## Future Work

Future versions should add:

- export control review,
- actual delivery dispatch gate,
- customer delivery authorization linkage,
- report packet versioning,
- delivery evidence record,
- post-delivery audit trail,
- customer receipt acknowledgement.

## Relationship to Lifecycle Integration Checkpoint

The lifecycle integration checkpoint summarizes delivery authorization as part of the current v0.1.x control and review workflow.

It confirms that delivery packages are generated only for workflow validation and are not customer-delivery-ready.

See `docs/38-lifecycle-integration-checkpoint.md`.
