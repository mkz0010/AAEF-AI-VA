# Real Execution Readiness Gate

## Purpose

This document defines the first real execution readiness gate for the AAEF-controlled AI Vulnerability Assessment Platform.

The project now has:

- AI-visible tool action requests,
- AAEF authorization decisions,
- Tool Gateway binding checks,
- credential_ref validation,
- scope registry target binding,
- adapter command plans,
- controlled executor dry-run policy.

The next required boundary is a readiness gate that decides whether the system is even eligible to move toward real tool execution.

## Core Principle

Real execution is not permitted merely because a command plan exists.

A command plan must pass:

1. Tool Gateway binding checks,
2. credential_ref checks,
3. scope registry target binding,
4. controlled executor policy,
5. real execution readiness gate.

Even then, current MVP behavior remains dry-run-only.

## Current MVP Decision

In the current MVP:

~~~text
real_execution_enabled: false
real_execution_permitted: false
external_process_executed: false
network_activity_performed: false
~~~

The readiness gate evaluates conditions but does not execute tools.

## Required Readiness Conditions

Before future real execution can be considered, all of the following must be true:

- real execution is explicitly enabled,
- real tool runtime is configured,
- network egress profile is configured,
- artifact paths are private/ignored,
- sanitizer is configured,
- stop and timeout controls are configured,
- evidence emission is required,
- target binding is approved,
- credential injection policy is configured,
- human approval is either approved or not required.

The current MVP still blocks execution because command plans are dry-run-only.

## Blockers

The readiness gate reports blockers such as:

- `real_execution_disabled`
- `runtime_configured_not_ready`
- `egress_profile_configured_not_ready`
- `sanitizer_configured_not_ready`
- `stop_timeout_configured_not_ready`
- `target_binding_approved_not_ready`
- `credential_injection_policy_configured_not_ready`
- `human_approval_not_satisfied`
- `command_plan_is_dry_run_only`

## Fail-Closed Conditions

The readiness gate fails closed when:

- evidence emission is disabled,
- artifact paths are not private,
- human approval status is unsupported,
- controlled executor validation fails,
- command plan contains shell command or forbidden fields,
- command plan includes unsafe target or artifact behavior.

## Why This Matters

This gate prevents a future implementation from accidentally turning command plans into real execution authority.

The safe chain is:

~~~text
AI request
  ↓
AAEF authorization
  ↓
Tool Gateway checks
  ↓
scope registry target binding
  ↓
adapter command plan
  ↓
controlled executor policy
  ↓
real execution readiness gate
  ↓
future bounded execution
~~~

## Relationship to Future Real Tool Execution

Future real ZAP execution must not be added by simply calling a subprocess from the adapter.

It should be added only after the readiness gate is extended and tested for:

- runtime identity,
- egress restrictions,
- target destination resolution,
- secret injection,
- artifact capture,
- sanitizer handoff,
- stop conditions,
- timeout behavior,
- human approval,
- evidence emission.

## Relationship to Operator Readiness Review

The readiness gate produces machine-readable blockers.

The operator readiness review converts those blockers into categorized next actions and a reviewable Markdown/JSON artifact.

See `docs/27-operator-readiness-review.md`.

## Relationship to Human Approval Gate

Human approval is one readiness condition, but it is not sufficient authority by itself.

The current MVP validates approval records while keeping real execution disabled.

See `docs/28-human-approval-record-gate.md`.
