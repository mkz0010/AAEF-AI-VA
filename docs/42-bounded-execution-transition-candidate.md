# Bounded Execution Transition Candidate

## Purpose

This document defines the first bounded execution transition candidate for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.2.2 introduced runtime destination binding. v0.2.3 structures the conditions required before any future local-only execution plan can be considered.

## Core Principle

A bounded execution transition candidate is not execution authority.

It only records that runtime, target, and destination binding are available as prerequisites for future design work.

## Current Flow

~~~text
runtime_destination_binding
  ↓
bounded_execution_transition_candidate
  ↓
local-only execution plan review
~~~

The current MVP stops at the candidate/gate layer.

## Current MVP Behavior

The transition candidate keeps:

~~~text
local_only: true
execution_plan_review_required: true
human_approval_required: true
no_egress_required: true
timeout_required: true
kill_switch_required: true
evidence_required: true
scan_execution_allowed: false
network_activity_allowed: false
real_execution_permitted: false
external_process_execution_allowed: false
credential_injection_permitted: false
raw_artifact_capture_permitted: false
customer_target: false
external_network_target: false
~~~

## Required Future Controls

Before any future local-only execution transition can be considered, the platform must define:

- local-only execution plan review,
- no-egress controls,
- timeout controls,
- kill-switch controls,
- operation allowlist,
- human approval for execution transition,
- raw artifact capture boundary,
- sanitizer binding,
- evidence generation requirement.

## What This Prevents

This candidate prevents:

- runtime-target binding from becoming execution authority,
- execution without an operation allowlist,
- execution without no-egress controls,
- execution without timeout and kill-switch behavior,
- raw artifact capture without sanitizer boundaries,
- credential injection without explicit authorization,
- targetless or external execution.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/bounded-execution-transition/demo/
~~~

Generated files:

- `runtime-destination-binding.generated.json`
- `runtime-destination-binding-gate-result.generated.json`
- `bounded-execution-transition-candidate.generated.json`
- `bounded-execution-transition-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_bounded_execution_transition_demo.py
~~~

You can also test alternative review states:

~~~bash
py tools/generate_bounded_execution_transition_demo.py needs_design
py tools/generate_bounded_execution_transition_demo.py rejected
~~~

## Relationship to Future Local Execution

The candidate is the bridge between static binding and a future local-only execution plan.

It does not start ZAP, scan localhost, perform network activity, capture raw output, or inject credentials.

## Future Work

Future v0.2.x work should add:

- local-only execution plan review,
- operation allowlist,
- no-egress validation profile,
- timeout and kill-switch policy,
- ZAP process lifecycle plan,
- raw artifact capture boundary,
- sanitizer policy binding to runtime output,
- execution transition human approval record.

## Relationship to Local-Only Execution Plan Review

The bounded execution transition candidate can become input to a local-only execution plan review.

The execution plan still does not grant execution authority.

See `docs/43-local-only-execution-plan-review.md`.
