# ADR-0026: Add sanitized finding candidate model

## Status

Accepted

## Context

The platform now has a sanitizer/redaction policy scaffold.

After raw adapter artifacts are sanitized, the platform needs a safe intermediate object for AI-assisted analysis and human review.

The object should not be a confirmed vulnerability or customer-facing report item.

## Decision

Add a sanitized finding candidate model.

Finding candidates are derived from sanitized artifacts, require human review, are not report-ready, and keep severity/confidence conservative by default.

## Consequences

- AI can receive a safer candidate object rather than raw tool output.
- Human review remains mandatory.
- The platform avoids treating tool output or AI analysis as confirmed vulnerability findings.
- Future report generation can promote only reviewed candidates.
