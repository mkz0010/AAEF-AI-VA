# 0045: Add preflight evidence validation rules

## Status

In Progress

## Priority

P0

## Type

Preflight Evidence / Validation Rules

## Background

v0.3.2 added generated preflight evidence examples.

The project should define validation rules for those generated examples before moving to negative examples or live evidence validation.

## Decision Summary

Add preflight evidence validation rules.

The rules validate generated examples only. They do not validate live evidence, satisfy preflight, or authorize execution.

## Acceptance Criteria

- preflight evidence validation rules module is added
- preflight evidence validation rules generator is added
- generated examples are validated by rules
- live evidence records validated remains false
- all required evidence records validated remains false
- rules cover example boundary
- rules cover fail-closed behavior
- rules cover execution authorization boundary
- rules cover preflight boundary
- rules cover AI visibility boundary
- rules cover raw artifact boundary
- rules cover sanitizer summary requirement
- rules cover representative example coverage
- rules cover runtime execution boundary
- preflight_satisfied remains false
- execution_authorized remains false
- ready_for_runtime_execution remains false
- scan execution remains false
- network activity remains false
- real execution remains false
- external process execution remains false
- credential injection remains false
- raw artifact capture remains false
- customer target remains false
- external network target remains false
- local checks pass

## Related Documents

- docs/52-preflight-evidence-validation-rules.md
- docs/51-generated-preflight-evidence-record-examples.md
- planning/decisions/ADR-0046-add-preflight-evidence-validation-rules.md
