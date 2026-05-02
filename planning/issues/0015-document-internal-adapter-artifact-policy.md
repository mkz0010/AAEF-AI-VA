# 0015: Document internal adapter artifact policy

## Status

In Progress

## Priority

P0

## Type

Design / Policy

## Background

v0.1.12 introduced Tool Gateway adapter stubs. v0.1.13 added generated output validation and removed internal adapter output from public generated results.

The project should now document how adapter output is handled before real tool integrations are introduced.

## Decision Summary

Adapter output is private internal artifact material by default.

It must not be embedded directly in:

- public/generated tool execution results,
- evidence records,
- AI-visible summaries,
- customer-facing reports.

Generated results may reference raw or sanitized artifacts through controlled artifact reference fields.

## Acceptance Criteria

- Internal adapter artifact policy is documented
- Public result object boundary is documented
- Evidence boundary is documented
- AI-visible boundary is documented
- Raw and sanitized artifact classes are distinguished
- Future real tool adapter guidance is recorded
- Local checks pass

## Related Documents

- docs/22-internal-adapter-artifact-policy.md
- docs/21-generated-output-validation.md
- docs/20-tool-gateway-adapter-stubs.md
- planning/decisions/ADR-0016-keep-adapter-output-as-private-internal-artifact.md
