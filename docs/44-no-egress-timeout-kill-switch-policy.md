# No-Egress, Timeout, and Kill-Switch Policy Scaffold

## Purpose

This document defines the first no-egress, timeout, and kill-switch policy scaffold for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.2.4 introduced local-only execution plan review. v0.2.5 defines the safety controls that must exist before any future local runtime process launch can be considered.

## Core Principle

Safety policy is not execution authority.

A no-egress, timeout, and kill-switch policy may define future requirements, but it must not start tools, call ZAP APIs, perform network activity, run scans, inject credentials, or capture raw artifacts.

## Current Flow

~~~text
local-only execution plan
  ↓
no-egress / timeout / kill-switch policy scaffold
  ↓
future runtime enforcement design
~~~

The current MVP stops at the policy scaffold and gate.

## No-Egress Requirements

The policy scaffold requires future execution to remain local-only.

Allowed destination examples are limited to:

- `127.0.0.1`
- `localhost`
- `::1`
- approved Docker-internal lab hostnames

Denied destination categories include:

- public internet,
- customer network,
- production network,
- metadata service,
- cloud control plane,
- private corporate network,
- unknown external host.

## Timeout Requirements

The policy scaffold records:

~~~text
max_runtime_seconds: 60
idle_timeout_seconds: 15
~~~

These are policy values only. They are not runtime-enforced in the current MVP.

## Kill-Switch Requirements

The policy scaffold requires future support for:

- operator manual stop,
- timeout forced stop,
- policy violation stop,
- future process tree termination.

These are policy requirements only. They are not runtime-enforced in the current MVP.

## Current MVP Behavior

The policy and gate keep:

~~~text
no_egress_required: true
no_egress_policy_defined: true
timeout_required: true
timeout_policy_defined: true
kill_switch_required: true
kill_switch_policy_defined: true
process_tree_termination_required: true
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

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/runtime-safety-policy/demo/
~~~

Generated files:

- `local-execution-plan.generated.json`
- `local-execution-plan-review-gate-result.generated.json`
- `runtime-safety-policy.generated.json`
- `runtime-safety-policy-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_runtime_safety_policy_demo.py
~~~

You can also test alternative review states:

~~~bash
py tools/generate_runtime_safety_policy_demo.py needs_revision
py tools/generate_runtime_safety_policy_demo.py rejected
~~~

## Relationship to Future Execution

This policy scaffold is a prerequisite for future runtime enforcement design.

It does not enable execution. Future work must still implement and test actual runtime enforcement before any ZAP process launch can be considered.

## Future Work

Future v0.2.x work should add:

- runtime enforcement design,
- process launch wrapper design,
- no-egress validation checks,
- timeout enforcement implementation,
- kill-switch implementation,
- process tree termination behavior,
- raw artifact capture boundary,
- sanitizer policy binding to runtime output,
- human approval for execution transition.

## Relationship to Runtime Enforcement Design

The no-egress, timeout, and kill-switch policy scaffold becomes input to the runtime enforcement design scaffold.

The enforcement design still does not implement or authorize runtime execution.

See `docs/45-runtime-enforcement-design-scaffold.md`.
