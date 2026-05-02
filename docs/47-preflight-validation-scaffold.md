# Preflight Validation Scaffold

## Purpose

This document defines the first preflight validation scaffold for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.2.7 introduced the execution authorization gate scaffold. v0.2.8 defines what must be checked immediately before any future local-only execution could ever be authorized.

## Core Principle

Preflight validation design is not preflight satisfaction.

This scaffold records the execution-before-checklist. It does not satisfy preflight, authorize execution, launch processes, perform network activity, scan targets, inject credentials, or capture raw artifacts.

## Current Flow

~~~text
execution authorization gate scaffold
  ↓
preflight validation scaffold
  ↓
future preflight check implementation
~~~

The current MVP stops at the preflight scaffold and gate.

## Required Preflight Checks

The scaffold records these required future checks:

- runtime readiness check,
- local target lab profile check,
- runtime destination binding check,
- bounded execution transition check,
- local-only execution plan check,
- runtime safety policy check,
- runtime enforcement design check,
- execution authorization check,
- human approval check,
- operator confirmation check,
- scope owner approval check,
- no-egress guard check,
- timeout watcher check,
- kill-switch controller check,
- evidence emitter check,
- sanitizer boundary check.

## Current MVP Behavior

The scaffold and gate keep:

~~~text
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

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/preflight-validation/demo/
~~~

Generated files:

- `execution-authorization.generated.json`
- `execution-authorization-gate-result.generated.json`
- `preflight-validation.generated.json`
- `preflight-validation-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_preflight_validation_demo.py
~~~

You can also test alternative review states:

~~~bash
py tools/generate_preflight_validation_demo.py needs_revision
py tools/generate_preflight_validation_demo.py rejected
~~~

## Relationship to Future Execution

The preflight validation scaffold is the checklist boundary immediately before any future execution authorization could be satisfied.

It still requires future implementation of concrete checks and evidence records.

## Future Work

Future v0.2.x work should add:

- concrete preflight check implementations,
- preflight evidence records,
- current runtime readiness verification,
- current scope registry binding verification,
- no-egress verification evidence,
- timeout and kill-switch verification evidence,
- human/operator/scope-owner approval binding,
- sanitizer boundary verification,
- execution authorization test fixtures.

## Relationship to Runtime Transition Checkpoint

The preflight validation scaffold becomes input to the runtime transition checkpoint.

The checkpoint confirms that the project is ready to design concrete preflight checks, not to execute.

See `docs/48-runtime-transition-checkpoint.md`.
