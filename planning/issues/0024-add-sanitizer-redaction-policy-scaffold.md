# 0024: Add sanitizer and redaction policy scaffold

## Status

In Progress

## Priority

P0

## Type

Sanitization / Data Boundary

## Background

Before real ZAP, Burp, Nmap, nuclei, or browser artifacts are processed by AI, raw tool output must be sanitized.

The project needs a sanitizer/redaction policy scaffold.

## Decision Summary

Add sanitizer module, redaction policy, demo generator, and tests.

The sanitizer redacts obvious sensitive values and marks sanitized artifacts as AI-visible only after completion.

## Acceptance Criteria

- sanitizer module is added
- redaction policy JSON is added
- demo sanitized artifact generator is added
- authorization headers are redacted
- cookie headers are redacted
- bearer tokens are redacted
- API keys are redacted
- CSRF/session/password values are redacted
- private IP values are redacted
- raw artifact path must be private/ignored
- sanitized output keeps secret_exposed_to_ai false
- local checks pass

## Related Documents

- docs/31-sanitizer-redaction-policy.md
- docs/30-evidence-reconstruction-report.md
- planning/decisions/ADR-0025-add-sanitizer-redaction-policy-scaffold.md
