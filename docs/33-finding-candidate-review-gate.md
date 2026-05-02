# Finding Candidate Review Gate

## Purpose

This document defines the first finding candidate review gate for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.1.24 introduced sanitized finding candidates. v0.1.25 adds a human review gate for those candidates.

## Core Principle

A finding candidate is not a confirmed vulnerability.

A human review decision must be recorded before a candidate can move toward any future report promotion flow.

Even a confirmed review does not make the candidate report-ready in the current MVP.

## Review Decisions

The MVP supports:

- `confirmed`
- `rejected`
- `needs_more_info`
- `duplicate`
- `false_positive`

## Current MVP Behavior

The finding review gate can mark a candidate as eligible for a future report promotion review only when the review decision is:

~~~text
confirmed
~~~

However, it still keeps:

~~~text
report_ready: false
~~~

The report finding promotion gate is future work.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/finding-reviews/demo/
~~~

Generated files:

- `raw-artifact.demo.json`
- `sanitized-artifact.generated.json`
- `finding-candidate.generated.json`
- `finding-review.generated.json`
- `finding-review-gate-result.generated.json`
- `finding-review.generated.md`

## Example Command

~~~bash
py tools/generate_finding_review_demo.py
~~~

You can also generate a confirmed review for workflow testing:

~~~bash
py tools/generate_finding_review_demo.py confirmed
~~~

Even with `confirmed`, the review remains not report-ready in the current MVP.

## Fail-Closed Conditions

The review gate fails closed when:

- review decision is unsupported,
- review record is not bound to the candidate,
- review scope does not match,
- report_ready is true,
- evidence_required is false,
- secret_exposed_to_ai is true,
- review notes contain obvious sensitive literals.

## Relationship to Finding Candidates

The finding candidate model creates a safe review object from sanitized artifacts.

The review gate records what a human decided about that candidate.

## Future Work

Future versions should add:

- report finding promotion gate,
- CVSS/CWE/OWASP mapping review,
- duplicate linking,
- reviewer identity policy,
- customer impact review,
- remediation guidance review,
- report draft generation.

## Relationship to Report Finding Promotion Gate

Confirmed finding reviews may move to the report finding promotion gate.

The promoted object is a `report_finding`, but it still requires report review and is not customer-delivery-ready in the current MVP.

See `docs/34-report-finding-promotion-gate.md`.
