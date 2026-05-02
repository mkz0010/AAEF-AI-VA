# Generated Preflight Evidence Record Examples

## Purpose

This document defines the v0.3.2 generated preflight evidence record examples for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.3.1 defined the preflight evidence record model. v0.3.2 adds representative generated examples that demonstrate how fail-closed preflight evidence should look before any live preflight evidence generation exists.

## Core Principle

Generated examples are not live evidence.

These examples are generated scaffold artifacts. They do not prove a live check ran, do not satisfy checks, do not satisfy preflight, do not authorize execution, and do not permit runtime activity.

## Current Flow

~~~text
preflight evidence record model
  ↓
generated preflight evidence record examples
  ↓
future live preflight evidence generation
~~~

## Representative Examples

The current example set covers:

- `runtime_readiness_check`
- `runtime_destination_binding_check`
- `execution_authorization_check`
- `no_egress_guard_check`
- `sanitizer_boundary_check`

Each example records a fail-closed outcome.

## Example Record Invariants

Each representative example keeps:

~~~text
example_record_generated: true
live_evidence_record_generated: false
check_implemented: false
check_satisfied: false
preflight_satisfied: false
execution_authorized: false
validation_result: failed_closed
fail_closed: true
ai_visible: false
raw_artifact_capture_permitted: false
sanitized_summary_required: true
~~~

## Example Set Invariants

The example set keeps:

~~~text
examples_recorded: true
example_records_generated: true
live_evidence_records_generated: false
all_required_evidence_records_generated: false
all_required_checks_satisfied: false
preflight_satisfied: false
execution_authorized: false
execution_authorization_satisfied: false
runtime_enforcement_implemented: false
ready_for_runtime_execution: false
ready_for_customer_target: false
ready_for_external_network: false

scan_execution_allowed: false
network_activity_allowed: false
real_execution_permitted: false
external_process_execution_allowed: false
credential_injection_permitted: false
raw_artifact_capture_permitted: false
customer_target: false
external_network_target: false
~~~

## AI Visibility Boundary

The examples include sanitized summaries, but the example records themselves remain:

~~~text
ai_visible: false
raw_artifact_capture_permitted: false
sanitized_summary_required: true
~~~

This keeps the future distinction between raw evidence and sanitized summaries explicit.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/preflight-evidence-examples/demo/
~~~

Generated files:

- `preflight-evidence-record-model.generated.json`
- `preflight-evidence-record-model-gate-result.generated.json`
- `preflight-evidence-example-set.generated.json`
- `preflight-evidence-example-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_preflight_evidence_examples_demo.py
~~~

You can also test alternative review states:

~~~bash
py tools/generate_preflight_evidence_examples_demo.py needs_revision
py tools/generate_preflight_evidence_examples_demo.py rejected
~~~

## Future Work

Future v0.3.x work should add:

- generated examples for all required preflight checks,
- negative examples for missing inputs,
- negative examples for mismatched bindings,
- negative examples for stale state,
- evidence integrity fields,
- preflight reconstruction examples,
- live evidence generation separated from scaffold examples.

## Relationship to Preflight Evidence Validation Rules

Generated preflight evidence examples become input to the preflight evidence validation rules.

Passing validation rules for generated examples does not validate live evidence or authorize execution.

See `docs/52-preflight-evidence-validation-rules.md`.
