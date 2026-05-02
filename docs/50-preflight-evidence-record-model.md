# Preflight Evidence Record Model

## Purpose

This document defines the v0.3.1 preflight evidence record model for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.3.0 defined concrete preflight check implementation scaffolds. v0.3.1 defines the evidence record model each check will eventually generate.

## Core Principle

An evidence record model is not generated evidence.

This model defines the evidence record shape, status, required inputs, fail-closed behavior, and AI visibility boundary for each preflight check. It does not generate records, satisfy checks, satisfy preflight, authorize execution, launch processes, perform network activity, scan targets, inject credentials, or capture raw artifacts.

## Current Flow

~~~text
concrete preflight check implementation scaffold
  ↓
preflight evidence record model
  ↓
future generated preflight evidence records
~~~

## Evidence Record Model

Each required preflight check gets a record model with:

~~~text
evidence_record_required: true
evidence_record_generated: false
check_implemented: false
check_satisfied: false
validation_result: not_evaluated
failure_mode: not_evaluated
fail_closed: true
ai_visible: false
raw_artifact_capture_permitted: false
sanitized_summary_required: true
~~~

## Required Record Coverage

The model covers:

- `runtime_readiness_check`
- `local_target_lab_profile_check`
- `runtime_destination_binding_check`
- `bounded_execution_transition_check`
- `local_execution_plan_check`
- `runtime_safety_policy_check`
- `runtime_enforcement_design_check`
- `execution_authorization_check`
- `human_approval_check`
- `operator_confirmation_check`
- `scope_owner_approval_check`
- `no_egress_guard_check`
- `timeout_watcher_check`
- `kill_switch_controller_check`
- `evidence_emitter_check`
- `sanitizer_boundary_check`

## Current MVP Behavior

The evidence model and gate keep:

~~~text
evidence_records_defined: true
evidence_records_generated: false
all_required_evidence_records_defined: true
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

Preflight evidence records may eventually contain raw runtime, target, approval, or policy state.

Therefore, model records are:

~~~text
ai_visible: false
raw_artifact_capture_permitted: false
sanitized_summary_required: true
~~~

Future work must define sanitized summaries before any preflight evidence can become AI-visible.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/preflight-evidence-record-model/demo/
~~~

Generated files:

- `preflight-check-implementation.generated.json`
- `preflight-check-implementation-gate-result.generated.json`
- `preflight-evidence-record-model.generated.json`
- `preflight-evidence-record-model-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_preflight_evidence_record_model_demo.py
~~~

You can also test alternative review states:

~~~bash
py tools/generate_preflight_evidence_record_model_demo.py needs_revision
py tools/generate_preflight_evidence_record_model_demo.py rejected
~~~

## Future Work

Future v0.3.x work should add:

- generated evidence record examples,
- evidence record validation rules,
- evidence integrity fields,
- preflight reconstruction tests,
- sanitized evidence summaries,
- negative tests for unsafe evidence claims,
- missing-input and mismatch evidence cases.

## Relationship to Generated Preflight Evidence Examples

The preflight evidence record model becomes input to representative generated preflight evidence examples.

The examples are not live evidence and do not satisfy preflight.

See `docs/51-generated-preflight-evidence-record-examples.md`.

## Relationship to Preflight Evidence Validation Rules

The preflight evidence record model remains the upstream shape for generated examples and validation rules.

Validation rules for generated examples do not satisfy live preflight evidence requirements.

See `docs/52-preflight-evidence-validation-rules.md`.
