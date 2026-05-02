# Negative Preflight Evidence Examples

Status: v0.3.4 scaffold

This document records representative invalid preflight evidence claims that must be rejected fail-closed.

These examples are not live evidence. They are intentionally unsafe, incomplete, stale, mismatched, or untrusted claims used to verify that the preflight path does not accidentally authorize runtime execution.

## Purpose

v0.3.3 added validation rules for generated preflight evidence examples.

v0.3.4 adds negative preflight evidence examples so the project can test that invalid claims fail closed before any runtime execution path is enabled.

The core assertion is:

~~~text
Invalid evidence claims must not satisfy preflight.
Invalid evidence claims must not authorize execution.
Invalid evidence claims must not permit runtime activity.
~~~

## Representative negative examples

The v0.3.4 negative example set covers:

- missing input evidence
- mismatched runtime-target binding
- stale runtime readiness state
- false `execution_authorized = true`
- false `preflight_satisfied = true`
- AI-visible raw evidence
- raw artifact capture permitted
- example/live evidence confusion
- no-egress verified spoofing
- sanitizer boundary verified spoofing

## Required outcome

Every negative example must result in:

~~~text
must_reject = true
fail_closed = true
evidence_record_accepted = false
check_satisfied = false
all_required_checks_satisfied = false
preflight_satisfied = false
execution_authorized = false
ready_for_runtime_execution = false
real_execution_permitted = false
external_process_execution_allowed = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
raw_artifact_capture_permitted = false
ai_visible_raw_evidence = false
live_evidence_records_generated = false
live_evidence_records_validated = false
all_required_evidence_records_validated = false
~~~

## Non-goals

v0.3.4 does not:

- generate live evidence records
- satisfy preflight
- authorize runtime execution
- start ZAP
- call the ZAP API
- run spidering
- run active scanning
- perform authenticated crawling
- allow network activity
- allow external process execution
- inject credentials
- capture raw artifacts

## Implementation artifacts

The negative examples are represented in:

- `prototypes/tool-gateway/preflight_evidence_negative_examples.py`
- `tools/generate_preflight_evidence_negative_examples_demo.py`
- `tools/test_preflight_evidence_negative_examples.py`

The local check suite includes the negative example validation test.

## Design boundary

The negative example layer exists to protect the future runtime path from false-positive evidence claims.

A claim that says an action is authorized is not authority.

A claim that says preflight is satisfied is not authority.

A claim that says a boundary was verified is not authority.

Only trusted, validated, policy-bound, scope-bound, and freshness-checked evidence can contribute to a future preflight decision. Even then, v0.3.4 does not enable execution.
