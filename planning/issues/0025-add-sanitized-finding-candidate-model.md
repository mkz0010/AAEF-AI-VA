# 0025: Add sanitized finding candidate model

## Status

In Progress

## Priority

P0

## Type

Finding Candidate / Review Control

## Background

Sanitized artifacts are now available, but they need to become reviewable finding candidates before any AI-assisted analysis or report draft workflow.

## Decision Summary

Add sanitized finding candidate model and generator.

Candidates are AI-visible-safe but not confirmed vulnerabilities. They must require human review and must not be report-ready.

## Acceptance Criteria

- finding candidate module is added
- demo generator is added
- candidate is built from sanitized artifact
- candidate includes sanitized artifact ref
- candidate includes redaction summary metadata
- candidate requires human review
- candidate is not report-ready
- candidate keeps severity/confidence conservative
- candidate must not include raw artifact ref
- candidate fails closed on forbidden sensitive literals
- local checks pass

## Related Documents

- docs/32-sanitized-finding-candidate-model.md
- docs/31-sanitizer-redaction-policy.md
- planning/decisions/ADR-0026-add-sanitized-finding-candidate-model.md
