# Controlled Local Runtime Readiness

## Purpose

This document defines the first controlled local runtime readiness gate for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.1.30 established a lifecycle integration checkpoint. v0.2.0 starts moving toward local runtime integration, but only through detection and readiness checks.

## Core Principle

Runtime detection is not execution authority.

The platform may detect that a local ZAP runtime appears to exist, but it must not start ZAP, spawn a process, perform network activity, inject credentials, capture raw artifacts, or scan a target in this phase.

## Current Scope

v0.2.0 introduces controlled local runtime readiness for:

~~~text
tool: zap
adapter: zap
runtime_profile_status: runtime_detection_only
~~~

## What Is Allowed

The current readiness gate may:

- define a local ZAP runtime profile,
- check for candidate binary names,
- record whether a runtime appears detectable,
- produce a readiness result,
- keep execution blocked,
- identify blockers and next actions.

## What Is Not Allowed

The current readiness gate must not:

- start ZAP,
- call the ZAP API,
- run any external process,
- perform network activity,
- scan localhost,
- scan Docker targets,
- inject credentials,
- capture raw runtime artifacts,
- create AI-visible raw output,
- treat runtime detection as execution permission.

## Safety Invariants

The readiness result must keep:

~~~text
runtime_detection_only: true
external_process_executed: false
network_activity_performed: false
real_execution_permitted: false
credential_injection_permitted: false
raw_artifact_capture_permitted: false
sanitizer_required_before_ai_visible: true
scope_registry_required: true
human_approval_required_for_execution_transition: true
~~~

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/runtime-readiness/demo/
~~~

Generated files:

- `runtime-profile.generated.json`
- `runtime-readiness-result.generated.json`

## Example Command

~~~bash
py tools/generate_runtime_readiness_demo.py
~~~

To test a simulated detected runtime without executing anything:

~~~bash
py tools/generate_runtime_readiness_demo.py detected
~~~

## Relationship to v0.1.30

v0.1.30 established the dry-run/review lifecycle checkpoint.

v0.2.0 starts the next phase by introducing local runtime detection only. It does not change the no-real-execution boundary.

## Future Work

Future v0.2.x work should add:

- local-only vulnerable target setup documentation,
- runtime destination binding in the scope registry,
- bounded execution mode transition design,
- ZAP runtime start/stop design without enabling it yet,
- sanitizer coverage expansion for ZAP artifacts,
- raw artifact capture boundary design,
- emergency stop and timeout readiness.

## Relationship to Local Target Lab Profile

Runtime readiness only describes whether a local tool runtime appears available.

The local target lab profile separately defines what a future bounded local execution may point toward. Neither grants execution authority.

See `docs/40-local-target-lab-profile.md`.
