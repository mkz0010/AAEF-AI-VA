# 0043: Add preflight evidence record model

## Status

In Progress

## Priority

P0

## Type

Preflight Evidence / Record Model

## Background

v0.3.0 added concrete preflight check implementation scaffolds.

Each required check now needs an evidence record model so that future check results can be captured, validated, reconstructed, and sanitized before any AI-visible use.

## Decision Summary

Add preflight evidence record model.

The model defines a non-generated evidence record shape for each required preflight check while keeping checks unsatisfied and execution disabled.

## Acceptance Criteria

- preflight evidence record module is added
- preflight evidence record generator is added
- every required preflight check has an evidence record model
- every record has evidence_type
- every record has input_sources
- every record has evidence_record_required=true
- every record has evidence_record_generated=false
- every record has check_satisfied=false
- every record has fail_closed=true
- every record has ai_visible=false
- every record has raw_artifact_capture_permitted=false
- every record has sanitized_summary_required=true
- evidence_records_generated remains false
- all_required_evidence_records_generated remains false
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

- docs/50-preflight-evidence-record-model.md
- docs/49-preflight-check-implementation-scaffold.md
- planning/decisions/ADR-0044-add-preflight-evidence-record-model.md
