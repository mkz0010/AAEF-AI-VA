# ZAP Adapter Command Plan

## Purpose

This document records the v0.1.15 update that moves the ZAP adapter stub closer to real tool integration without executing ZAP.

The project still does not invoke ZAP, external processes, local browsers, network tools, or customer targets.

Instead, the ZAP adapter now builds a structured dry-run command plan.

## Decision

The ZAP adapter may build a command plan, but it must not execute it.

The command plan describes:

- approved tool,
- approved operation,
- target_id,
- scope_id,
- credential_ref,
- credential resolution component,
- approved constraints,
- planned execution steps,
- raw and sanitized artifact references,
- blocked behaviors.

The command plan must not contain:

- raw username,
- raw password,
- API key,
- session cookie,
- bearer token,
- Authorization header,
- ZAP API key,
- arbitrary shell command generated from AI text.

## Why This Matters

Real tool integration should not start by letting AI build shell commands.

The safe path is:

~~~text
AI tool_action_request
  ↓
AAEF authorization_decision
  ↓
Tool Gateway binding checks
  ↓
adapter command plan
  ↓
future controlled executor
~~~

This preserves the AAEF principle:

Model output is not authority.

## Dry-run-only Behavior

The current ZAP adapter uses:

~~~text
execution_mode: dry_run_plan_only
external_process_execution: false
secret_material_included: false
~~~

This makes the command plan suitable for review and testing before real execution is added.

## Future Integration Path

Before ZAP is actually executed, the project should define:

- target alias resolution,
- ZAP runtime location,
- ZAP API access model,
- ZAP API key handling,
- ZAP context creation behavior,
- authentication profile injection,
- raw artifact path,
- sanitization behavior,
- stop conditions,
- timeout behavior,
- network egress controls,
- human approval requirements for higher-risk operations.

## Relationship to Internal Adapter Artifact Policy

The adapter may return command plan details when called directly in tests.

Tool Gateway generated public outputs must still not embed adapter output.

Adapter command plans are internal implementation artifacts unless explicitly sanitized and exposed.
