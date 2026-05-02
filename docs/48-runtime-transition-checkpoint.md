# Runtime Transition Checkpoint

## Purpose

This document records the v0.2.9 runtime transition checkpoint for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.2.0 through v0.2.8 moved the platform close to the shape of controlled local execution. This checkpoint freezes the current boundary before concrete preflight implementation work begins.

## Core Principle

The platform is ready to design concrete preflight checks, not to execute.

This checkpoint confirms that the project has structured runtime readiness, target boundary, runtime-target binding, execution planning, safety policy, runtime enforcement design, execution authorization, and preflight validation. It also confirms that execution remains blocked.

## Current Runtime Transition Layers

~~~text
v0.2.0 controlled local runtime readiness
v0.2.1 local target lab profile
v0.2.2 scope registry runtime destination binding
v0.2.3 bounded execution transition candidate
v0.2.4 local-only execution plan review
v0.2.5 no-egress / timeout / kill-switch policy scaffold
v0.2.6 runtime enforcement design scaffold
v0.2.7 execution authorization gate scaffold
v0.2.8 preflight validation scaffold
v0.2.9 runtime transition checkpoint
~~~

## Checkpoint Safety Invariants

The checkpoint requires:

~~~text
local_only: true
preflight_satisfied: false
execution_authorized: false
execution_authorization_satisfied: false
runtime_enforcement_implemented: false
all_required_checks_satisfied: false
scan_execution_allowed: false
network_activity_allowed: false
real_execution_permitted: false
external_process_execution_allowed: false
credential_injection_permitted: false
raw_artifact_capture_permitted: false
customer_target: false
external_network_target: false
~~~

## What This Checkpoint Allows

This checkpoint allows the project to proceed toward:

- concrete preflight check implementation,
- preflight evidence records,
- runtime readiness verification,
- scope registry binding verification,
- no-egress verification evidence,
- timeout and kill-switch verification evidence,
- approval binding,
- sanitizer boundary verification.

## What This Checkpoint Does Not Allow

This checkpoint does not allow:

- starting ZAP,
- calling the ZAP API,
- spidering,
- active scanning,
- authenticated crawling,
- passive runtime collection,
- network activity,
- external process execution,
- credential injection,
- raw artifact capture,
- customer targets,
- external networks,
- satisfied preflight,
- execution authorization.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/runtime-transition-checkpoint/demo/
~~~

Generated files:

- `preflight-validation.generated.json`
- `preflight-validation-gate-result.generated.json`
- `runtime-transition-checkpoint.generated.json`
- `runtime-transition-checkpoint.generated.md`

## Example Command

~~~bash
py tools/generate_runtime_transition_checkpoint_demo.py
~~~

## Relationship to v0.3.0

v0.2.9 is a checkpoint before concrete preflight implementation.

A natural v0.3.0 direction is:

- concrete preflight check implementation scaffold,
- preflight evidence records,
- approval binding,
- no-egress/timeout/kill-switch verification artifacts,
- sanitizer boundary verification.

Even then, execution should remain disabled until an explicit future release changes the execution boundary.

## Relationship to Concrete Preflight Check Implementation

The runtime transition checkpoint becomes input to the concrete preflight check implementation scaffold.

v0.3.0 starts implementation scaffolding for preflight checks while keeping preflight unsatisfied and execution disabled.

See `docs/49-preflight-check-implementation-scaffold.md`.
