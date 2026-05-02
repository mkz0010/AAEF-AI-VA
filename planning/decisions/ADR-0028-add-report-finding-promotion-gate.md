# ADR-0028: Add report finding promotion gate without using final lifecycle labels

## Status

Accepted

## Context

The platform can now create sanitized finding candidates and record finding review decisions.

Confirmed finding reviews need a controlled path into report finding review objects.

The project should avoid using `final` as a lifecycle label because report artifacts remain reviewable and versioned.

## Decision

Add a report finding promotion gate.

Only confirmed finding reviews can be promoted. The promoted object is `report_finding`.

In the current MVP, report findings require report review and are not customer-delivery-ready.

## Consequences

- Confirmed findings can enter a report review workflow.
- Non-confirmed findings cannot be promoted.
- AI cannot make findings customer-delivery-ready.
- The project avoids misleading `final` terminology.
