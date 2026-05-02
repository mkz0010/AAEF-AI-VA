# Report Finding Promotion Gate

## Purpose

This document defines the first report finding promotion gate for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.1.25 introduced finding candidate review. v0.1.26 adds a promotion gate that can create a report finding review object from a confirmed finding review.

## Core Principle

A confirmed finding review is not automatically customer-delivery-ready.

The promotion gate may create a report finding, but the result still requires report review.

## Terminology

This project does not use `final` as a lifecycle label for report artifacts.

Report artifacts remain reviewable and versioned. The current object is called:

~~~text
report_finding
~~~

It is not customer-delivery-ready in the current MVP.

## Current MVP Behavior

Only a confirmed finding review may be promoted.

The resulting report finding keeps:

~~~text
requires_report_review: true
customer_delivery_ready: false
report_ready: false
secret_exposed_to_ai: false
evidence_required: true
~~~

Non-confirmed reviews are not promoted.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/report-findings/demo/
~~~

Generated files for confirmed review:

- `raw-artifact.demo.json`
- `sanitized-artifact.generated.json`
- `finding-candidate.generated.json`
- `finding-review.generated.json`
- `report-finding-promotion-gate.generated.json`
- `report-finding.generated.json`
- `report-finding.generated.md`

## Example Command

~~~bash
py tools/generate_report_finding_promotion_demo.py
~~~

You can also test non-promoted outcomes:

~~~bash
py tools/generate_report_finding_promotion_demo.py rejected
py tools/generate_report_finding_promotion_demo.py needs_more_info
py tools/generate_report_finding_promotion_demo.py duplicate
py tools/generate_report_finding_promotion_demo.py false_positive
~~~

## Fail-Closed Conditions

The promotion gate fails closed when:

- finding review is not confirmed,
- report finding is not bound to candidate and review,
- report_ready is true,
- customer_delivery_ready is true,
- secret_exposed_to_ai is true,
- evidence_required is false,
- obvious sensitive literals appear in report finding content,
- raw artifact references are embedded.

## Future Work

Future versions should add:

- report review gate,
- report packet generation,
- customer-delivery readiness checks,
- severity review,
- impact review,
- remediation review,
- evidence attachment review,
- report versioning.

## Relationship to Report Review Gate

A promoted `report_finding` must pass report review before it can move into a report packet candidate.

See `docs/35-report-review-gate.md`.
