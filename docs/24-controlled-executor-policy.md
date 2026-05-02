# Controlled Executor Policy

## Purpose

This document defines the first controlled executor policy for the AAEF-controlled AI Vulnerability Assessment Platform.

The controlled executor is the future component that will eventually receive adapter command plans and decide whether they may be executed.

In v0.1.16, the executor remains dry-run-only. It does not execute external processes, does not invoke ZAP, does not make network connections, and does not access customer targets.

## Core Principle

A command plan is not authority.

A command plan is a structured internal artifact that still requires executor policy validation before any future execution.

This preserves the core AAEF principle:

Model output is not authority.

## Current MVP Behavior

The current controlled executor accepts only command plans that satisfy all of the following:

- `execution_mode` is `dry_run_plan_only`
- `external_process_execution` is `false`
- `secret_material_included` is `false`
- no shell command field is present
- no argv or arbitrary command field is present
- destructive tests are not allowed
- external discovery is not allowed
- raw and sanitized artifact refs point to ignored private paths

If the plan passes, the executor returns a dry-run acceptance result.

It still does not execute the tool.

## Denied Conditions

The controlled executor fails closed when:

- the plan is missing required fields,
- execution mode is not dry-run,
- external process execution is requested,
- secret material is included,
- destructive tests are enabled,
- external discovery is enabled,
- shell command or argv fields are present,
- raw artifact paths point to tracked or public locations,
- sanitized artifact paths point to tracked or public locations.

## Why This Matters

Tool integration must not become a backdoor where structured control is bypassed by a command string.

The safe execution chain is:

~~~text
AI tool_action_request
  ↓
AAEF authorization_decision
  ↓
Tool Gateway binding checks
  ↓
adapter command plan
  ↓
controlled executor policy
  ↓
future bounded execution
~~~

v0.1.16 implements the executor policy as dry-run-only validation.

## Future Real Execution Requirements

Before any real ZAP, Nmap, nuclei, Burp, or Nessus execution is allowed, the project should define:

- approved executor runtime,
- approved tool binary/API location,
- allowed subprocess or API invocation model,
- timeout behavior,
- kill/stop conditions,
- egress controls,
- target alias resolution,
- artifact capture path,
- sanitizer handoff,
- credential injection boundary,
- human approval requirements,
- evidence emission requirements.

## Relationship to ZAP Command Plan

v0.1.15 introduced a dry-run ZAP adapter command plan.

v0.1.16 adds the executor-side policy that evaluates such plans while still preventing actual execution.

This means the project now has both:

- adapter-side planning, and
- executor-side acceptance/refusal logic.

Both are required before real tool integration.

## Scope Registry Validation

The controlled executor validates target binding in command plans.

In the current MVP, target binding must use a scope registry destination reference and must not include raw destinations or allow network execution.
