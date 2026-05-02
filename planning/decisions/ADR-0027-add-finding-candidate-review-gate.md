# ADR-0027: Add finding candidate review gate

## Status

Accepted

## Context

The platform now creates sanitized finding candidates derived from sanitized artifacts.

A finding candidate must not become a confirmed vulnerability or report finding without human validation.

## Decision

Add a finding candidate review gate.

The gate records human review decisions and validates that the review is bound to the candidate and sanitized artifact.

Even confirmed candidates are not report-ready in the current MVP.

## Consequences

- Finding candidates become reviewable workflow objects.
- AI cannot make findings confirmed or report-ready by itself.
- Confirmed candidates can become eligible for a future report promotion gate.
- Rejected, duplicate, false positive, and needs-more-info outcomes are explicitly recorded.
