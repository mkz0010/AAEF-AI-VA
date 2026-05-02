# Local-Only Execution Plan Review

## Purpose

This document defines the first local-only execution plan review for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.2.3 introduced the bounded execution transition candidate. v0.2.4 defines the next review object: a local-only execution plan that still does not execute anything.

## Core Principle

An execution plan is not execution authority.

A local-only execution plan can describe future-safe operation categories, but it must not start ZAP, call ZAP APIs, scan targets, perform network activity, inject credentials, or capture raw artifacts.

## Current Flow

~~~text
bounded_execution_transition_candidate
  ↓
local-only execution plan
  ↓
execution plan review gate
~~~

The current MVP stops at the plan review gate.

## Allowed Plan Operations

The current plan may only include:

~~~text
runtime_detection
health_check_plan_only
~~~

These are plan-level operations. They do not authorize process launch or network calls.

## Prohibited Runtime Operations

The current plan explicitly prohibits:

- `zap_start`
- `zap_stop`
- `zap_api_call`
- `spider`
- `ajax_spider`
- `active_scan`
- `passive_scan_runtime_collection`
- `authenticated_crawl`
- `credential_injection`
- `raw_artifact_capture`
- `external_network_access`
- `customer_target_access`

## Current MVP Behavior

The plan and review gate keep:

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

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/local-execution-plan-review/demo/
~~~

Generated files:

- `bounded-execution-transition-candidate.generated.json`
- `bounded-execution-transition-gate-result.generated.json`
- `local-execution-plan.generated.json`
- `local-execution-plan-review-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_local_execution_plan_review_demo.py
~~~

You can also test alternative review states:

~~~bash
py tools/generate_local_execution_plan_review_demo.py needs_revision
py tools/generate_local_execution_plan_review_demo.py rejected
~~~

## Relationship to Future Execution

This plan is the first place where future execution behavior is described.

It does not enable execution. Instead, it narrows the future path by stating that only plan-level detection and health-check design may be recorded in the current MVP.

## Future Work

Future v0.2.x work should add:

- no-egress validation profile,
- timeout and kill-switch policy,
- ZAP process lifecycle plan,
- local-only runtime health-check design,
- execution transition human approval record,
- runtime output artifact boundary,
- sanitizer policy binding to runtime output.

## Relationship to Runtime Safety Policy

The local-only execution plan becomes input to the no-egress, timeout, and kill-switch policy scaffold.

The safety policy still does not grant execution authority.

See `docs/44-no-egress-timeout-kill-switch-policy.md`.

## Relationship to Runtime Enforcement Design

The local-only execution plan is upstream of runtime safety policy and runtime enforcement design.

The enforcement design records future components but still does not permit process launch, network activity, scans, credential injection, or raw artifact capture.

See `docs/45-runtime-enforcement-design-scaffold.md`.
