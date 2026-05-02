# Scope Registry and Target Alias Resolution

## Purpose

This document defines the first scope registry and target alias resolution model for the AAEF-controlled AI Vulnerability Assessment Platform.

Before real tool execution is introduced, the project must define how `target_id` values are resolved and constrained.

## Core Principle

A `target_id` is not a raw destination.

A `target_id` is an alias that must be resolved by Tool Gateway-controlled scope registry logic.

AI may reference `target_id`, but AI does not decide what URL, host, IP range, or network destination it represents.

## Why This Matters

Real diagnostic tools eventually need concrete destinations.

However, exposing or allowing AI to construct those destinations introduces risk:

- scope expansion,
- external discovery,
- scanning the wrong system,
- leaking customer target details to AI,
- embedding raw URLs/IP ranges into generated outputs,
- bypassing contract scope.

The scope registry provides the control point between AI-visible aliases and future executor-visible destinations.

## MVP Registry

The MVP registry lives at:

~~~text
prototypes/tool-gateway/scope_registry/registry.json
~~~

It contains only fictitious demo targets.

No real customer URL, IP address, domain, or network range should be committed to Git.

## Initial Target Entries

The initial registry includes:

- `webapp-demo-001`
- `net-demo-001`
- `external-demo-001`

Only approved targets may be resolved into command plans.

Denied or external candidate targets must fail closed.

## Target Binding

A resolved target binding includes:

- `target_id`
- `scope_id`
- `target_type`
- `environment`
- `approval_status`
- `approved_for_tool`
- `approved_operation`
- `network_destination_ref`
- `raw_destination_included`
- `network_execution_allowed`
- `egress_profile`

The current MVP requires:

~~~text
raw_destination_included: false
network_execution_allowed: false
network_destination_ref: scope-registry://...
~~~

## Command Plan Integration

The ZAP command plan now includes `target_binding`.

The controlled executor validates that:

- target binding matches the command plan target_id,
- target binding matches the scope_id,
- target binding is approved for the requested tool,
- raw destination is not included,
- destination is a scope registry reference,
- network execution is still disabled in the dry-run MVP.

## AI-visible Boundary

AI may see:

- `target_id`
- `scope_id`
- target type labels where appropriate
- approved operation labels

AI should not receive:

- raw production URLs,
- raw internal hostnames,
- raw IP addresses,
- raw network ranges,
- customer-sensitive routing or environment details.

## Future Real Execution

Before real execution, the project must define:

- where raw destination values are stored,
- who can resolve them,
- how egress is restricted,
- how target aliases map to runtime destinations,
- how customer scope approvals are represented,
- how target changes are reviewed and logged,
- how stale or revoked targets are handled.

## Relationship to Controlled Executor

The controlled executor remains dry-run-only.

Even if a target binding is valid, the current executor still performs no external process execution and no network activity.

Target binding is necessary but not sufficient for execution.

## Relationship to Real Execution Readiness Gate

Target binding is necessary but not sufficient for real execution.

The real execution readiness gate still requires runtime, egress, sanitizer, timeout, evidence, credential injection, and approval prerequisites before future execution can be considered.
