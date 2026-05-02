# Concrete Preflight Check Implementation Scaffold

## Purpose

This document defines the v0.3.0 concrete preflight check implementation scaffold for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.2.9 recorded that the runtime transition path is ready for preflight implementation work while execution remains blocked. v0.3.0 starts the next phase by defining implementation scaffolds for each required preflight check.

## Core Principle

A preflight check implementation scaffold is not a satisfied preflight check.

This scaffold defines the implementation responsibility, input sources, evidence type, and fail-closed behavior for each required preflight check. It does not implement the checks, satisfy preflight, authorize execution, launch processes, perform network activity, scan targets, inject credentials, or capture raw artifacts.

## Current Flow

~~~text
runtime transition checkpoint
  ↓
concrete preflight check implementation scaffold
  ↓
future preflight evidence records
~~~

## Required Check Implementation Scaffolds

The scaffold covers:

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

## Common Check Requirements

Every check scaffold requires:

~~~text
implemented: false
satisfied: false
required: true
evidence_record_required: true
evidence_record_generated: false
fail_closed_on_missing_input: true
fail_closed_on_mismatch: true
fail_closed_on_stale_state: true
~~~

## Current MVP Behavior

The implementation scaffold and gate keep:

~~~text
concrete_checks_implemented: false
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

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/preflight-check-implementation/demo/
~~~

Generated files:

- `runtime-transition-checkpoint.generated.json`
- `runtime-transition-checkpoint.generated.md`
- `preflight-check-implementation.generated.json`
- `preflight-check-implementation-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_preflight_check_implementation_demo.py
~~~

You can also test alternative review states:

~~~bash
py tools/generate_preflight_check_implementation_demo.py needs_revision
py tools/generate_preflight_check_implementation_demo.py rejected
~~~

## Relationship to Future Evidence Records

This scaffold prepares the structure for preflight evidence records.

The next natural step is to define the evidence record shape emitted by each preflight check result.

## Future Work

Future v0.3.x work should add:

- preflight evidence record model,
- concrete pure validation functions,
- negative tests for missing inputs,
- negative tests for mismatched bindings,
- stale-state detection,
- approval binding checks,
- no-egress verification records,
- timeout and kill-switch verification records,
- sanitizer boundary verification records.

## Relationship to Preflight Evidence Record Model

The concrete preflight check implementation scaffold becomes input to the preflight evidence record model.

The evidence model defines record shapes for future generated evidence without satisfying checks or authorizing execution.

See `docs/50-preflight-evidence-record-model.md`.

## Relationship to Generated Preflight Evidence Examples

Generated preflight evidence examples show how future fail-closed check outputs should be represented.

They do not implement checks or authorize execution.

See `docs/51-generated-preflight-evidence-record-examples.md`.
