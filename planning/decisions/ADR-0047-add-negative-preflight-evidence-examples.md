# ADR-0047: Add negative preflight evidence examples

Status: accepted

## Context

The project has reached the point where preflight evidence record models, generated examples, and validation rules exist.

The next risk is false-positive evidence interpretation. A malformed, stale, mismatched, incomplete, or unsafe evidence claim must not be accepted as sufficient to satisfy preflight or authorize execution.

## Decision

Add representative negative preflight evidence examples for v0.3.4.

These examples intentionally describe invalid evidence claims, including:

- missing input evidence
- mismatched runtime-target binding
- stale runtime readiness state
- false execution authorization claims
- false preflight satisfaction claims
- AI-visible raw evidence
- raw artifact capture permission claims
- example/live evidence confusion
- no-egress verification spoofing
- sanitizer boundary verification spoofing

Each example must be rejected fail-closed.

## Required invariants

~~~text
negative_examples_recorded = true
negative_examples_validated = true
live_evidence_records_validated = false
all_required_evidence_records_validated = false
all_required_checks_satisfied = false
preflight_satisfied = false
execution_authorized = false
ready_for_runtime_execution = false
real_execution_permitted = false
external_process_execution_allowed = false
network_activity_allowed = false
scan_execution_allowed = false
raw_artifact_capture_permitted = false
~~~

## Consequences

The project gains a testable negative evidence layer before any live evidence validation or runtime execution is enabled.

The change also clarifies that an evidence claim is not authority by itself. Preflight satisfaction and execution authorization remain separate controlled decisions.

## Non-goals

This ADR does not permit runtime execution, live evidence generation, ZAP startup, ZAP API calls, spidering, active scanning, credential injection, network activity, or raw artifact capture.
