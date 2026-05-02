# Local Target Lab Profile

## Purpose

This document defines the first local target lab profile for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.2.0 introduced controlled local runtime readiness. v0.2.1 defines what the platform may point toward in a future local-only execution transition.

## Core Principle

Autonomous execution without a defined target is unsafe.

Before any future tool execution can be considered, the target boundary must be explicit, local, intentionally vulnerable, scope-bound, and non-customer.

## Current Scope

v0.2.1 supports target profiles for:

~~~text
localhost_only
docker_internal_only
intentionally_vulnerable_lab_only
~~~

## Allowed Future Target Types

The profile may describe:

- localhost lab target,
- Docker-internal vulnerable target,
- intentionally vulnerable local training app,
- OWASP Juice Shop style local lab,
- WebGoat/DVWA style local lab.

## Forbidden Target Types

The profile must not describe:

- customer targets,
- external network targets,
- public internet targets,
- production systems,
- unknown targets,
- targets not bound to scope registry,
- targets that require credentials in this phase.

## Current MVP Behavior

The local target lab gate may define a target boundary, but it still keeps:

~~~text
scan_execution_allowed: false
network_activity_allowed: false
credential_injection_allowed: false
raw_artifact_capture_allowed: false
scope_registry_binding_required: true
runtime_readiness_required: true
human_approval_required_for_execution_transition: true
~~~

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/local-target-lab/demo/
~~~

Generated files:

- `local-target-lab-profile.generated.json`
- `local-target-lab-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_local_target_lab_profile_demo.py
~~~

To generate a Docker-internal lab target profile:

~~~bash
py tools/generate_local_target_lab_profile_demo.py docker
~~~

## Relationship to Runtime Readiness

Runtime readiness defines whether a local runtime appears available.

The local target lab profile defines what a future bounded local execution may point toward.

Neither profile grants execution authority.

## Future Work

Future v0.2.x work should add:

- scope registry runtime destination records,
- local vulnerable target setup guide,
- Docker Compose lab target profile,
- bounded local execution transition gate,
- ZAP start/stop design,
- emergency stop and timeout controls,
- no-egress validation,
- raw artifact capture boundary.

## Relationship to Runtime Destination Binding

The local target lab profile defines the allowed local target boundary.

The runtime destination binding connects that target boundary to a runtime readiness profile without granting execution authority.

See `docs/41-scope-registry-runtime-destination-binding.md`.

## Relationship to Bounded Execution Transition

The local target lab profile is one prerequisite for a bounded execution transition candidate.

The candidate still requires no-egress, timeout, kill-switch, human approval, and execution plan review before any future local execution can be considered.

See `docs/42-bounded-execution-transition-candidate.md`.
