# 0044: Add generated preflight evidence record examples

## Status

In Progress

## Priority

P0

## Type

Preflight Evidence / Examples

## Background

v0.3.1 added the preflight evidence record model.

The project should now add representative generated examples to show how fail-closed preflight evidence should look before live preflight evidence generation is implemented.

## Decision Summary

Add generated preflight evidence record examples.

The examples are scaffold examples only. They do not satisfy checks, satisfy preflight, authorize execution, or permit runtime activity.

## Acceptance Criteria

- preflight evidence examples module is added
- preflight evidence examples generator is added
- representative examples are generated
- runtime readiness example is included
- runtime destination binding example is included
- execution authorization example is included
- no-egress guard example is included
- sanitizer boundary example is included
- examples fail closed
- example_record_generated is true
- live_evidence_record_generated remains false
- check_satisfied remains false
- preflight_satisfied remains false
- execution_authorized remains false
- ready_for_runtime_execution remains false
- ai_visible remains false
- raw_artifact_capture_permitted remains false
- sanitized_summary_required remains true
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

- docs/51-generated-preflight-evidence-record-examples.md
- docs/50-preflight-evidence-record-model.md
- planning/decisions/ADR-0045-add-generated-preflight-evidence-record-examples.md
