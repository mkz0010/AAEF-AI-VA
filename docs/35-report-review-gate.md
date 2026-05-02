# Report Review Gate

## Purpose

This document defines the first report review gate for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.1.26 introduced report finding promotion. v0.1.27 adds a report review gate that decides whether a report finding may move into a report packet candidate.

## Core Principle

A report finding is not customer-delivery-ready.

A report review may allow report packet candidate assembly, but customer delivery still requires a separate packet review gate.

## Terminology

This project avoids `final` as a lifecycle label for report artifacts.

The lifecycle uses reviewable terms:

- `report_finding`
- `report_review`
- `report_packet_candidate`

## Review Decisions

The MVP supports:

- `approved_for_report_packet`
- `needs_revision`
- `rejected`

## Current MVP Behavior

Only `approved_for_report_packet` may create a report packet candidate.

Even then, the report packet candidate keeps:

~~~text
requires_packet_review: true
customer_delivery_ready: false
report_ready: false
secret_exposed_to_ai: false
evidence_required: true
~~~

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/report-reviews/demo/
~~~

Generated files for approved review:

- `raw-artifact.demo.json`
- `sanitized-artifact.generated.json`
- `finding-candidate.generated.json`
- `finding-review.generated.json`
- `report-finding.generated.json`
- `report-review.generated.json`
- `report-review-gate-result.generated.json`
- `report-packet-candidate.generated.json`
- `report-review.generated.md`

## Example Command

~~~bash
py tools/generate_report_review_demo.py
~~~

You can also test non-packet outcomes:

~~~bash
py tools/generate_report_review_demo.py needs_revision
py tools/generate_report_review_demo.py rejected
~~~

## Fail-Closed Conditions

The report review gate fails closed when:

- report review decision is unsupported,
- report review is not bound to the report finding,
- report review scope does not match,
- customer_delivery_ready is true,
- report_ready is true,
- evidence_required is false,
- secret_exposed_to_ai is true,
- obvious sensitive literals appear in review content.

## Future Work

Future versions should add:

- report packet review gate,
- customer-delivery readiness checks,
- packet-level evidence review,
- report versioning,
- reviewer identity policy,
- customer approval linkage,
- report export controls.

## Relationship to Report Packet Review Gate

A `report_packet_candidate` must pass packet review before it can move toward delivery authorization.

See `docs/36-report-packet-review-gate.md`.
