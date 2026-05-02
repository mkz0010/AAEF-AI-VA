# Scope Registry Runtime Destination Binding

## Purpose

This document defines the first scope registry runtime destination binding for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.2.0 introduced controlled local runtime readiness. v0.2.1 introduced local target lab profiles. v0.2.2 binds the two through a scope-registry-style runtime destination record.

## Core Principle

A runtime and a target must be explicitly bound before any future execution transition can be considered.

Runtime detection is not execution authority.

Target definition is not execution authority.

Binding runtime and target is still not execution authority.

## Current Binding

The MVP binding connects:

~~~text
runtime_readiness
  +
local_target_lab_profile
  ↓
scope_registry_runtime_destination_binding
  ↓
bounded_execution_transition_candidate_allowed
~~~

This means the binding may become input to a future bounded execution transition gate.

It does not permit execution.

## Current MVP Behavior

The binding keeps:

~~~text
scan_execution_allowed: false
network_activity_allowed: false
real_execution_permitted: false
credential_injection_permitted: false
raw_artifact_capture_permitted: false
external_process_execution_allowed: false
customer_target: false
external_network_target: false
~~~

## What This Prevents

The binding prevents:

- targetless autonomous execution,
- runtime-only execution decisions,
- target-only execution decisions,
- customer target binding,
- external network binding,
- scan enablement without a transition gate,
- credential injection without a transition gate,
- raw artifact capture without a transition gate.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/runtime-destination-bindings/demo/
~~~

Generated files:

- `runtime-profile.generated.json`
- `runtime-readiness-result.generated.json`
- `local-target-lab-profile.generated.json`
- `local-target-lab-gate-result.generated.json`
- `runtime-destination-binding.generated.json`
- `runtime-destination-binding-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_runtime_destination_binding_demo.py
~~~

To generate a Docker-internal binding demo:

~~~bash
py tools/generate_runtime_destination_binding_demo.py docker
~~~

## Relationship to Future Bounded Execution

This binding is a prerequisite for a future bounded execution transition candidate.

The future transition gate must still verify:

- runtime readiness,
- local lab target profile,
- scope registry binding,
- explicit operation,
- timeout,
- no-egress controls,
- human approval,
- raw artifact capture boundary,
- sanitizer requirement,
- evidence generation.

## Future Work

Future v0.2.x work should add:

- bounded execution transition candidate,
- no-egress validation profile,
- timeout and kill-switch requirements,
- ZAP start/stop dry-run plan,
- local-only operation allowlist,
- raw artifact capture design,
- sanitizer policy binding to runtime outputs.

## Relationship to Bounded Execution Transition Candidate

A runtime destination binding may become input to a bounded execution transition candidate.

The transition candidate still does not grant execution authority.

See `docs/42-bounded-execution-transition-candidate.md`.

## Relationship to Local Execution Planning

Runtime destination binding is an upstream prerequisite for local-only execution planning.

The local execution plan still keeps scans, process execution, network activity, credential injection, and raw artifact capture disabled.

See `docs/43-local-only-execution-plan-review.md`.
