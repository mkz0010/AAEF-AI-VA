# Lifecycle Integration Checkpoint

## Purpose

This document records the v0.1.30 lifecycle integration checkpoint for the AAEF-controlled AI Vulnerability Assessment Platform.

The project has accumulated many control and review layers. Before moving toward controlled local tool runtime integration, the current lifecycle should be summarized and validated as a stable checkpoint.

## Core Principle

The v0.1.x line establishes control, review, evidence, sanitization, finding, report, packet, and delivery-package lifecycle boundaries.

It does not perform real vulnerability assessment execution or customer delivery.

## Current Stable Lifecycle

The current lifecycle covers:

~~~text
tool_action_request
  ↓
authorization_decision
  ↓
Tool Gateway
  ↓
controlled executor / readiness gate
  ↓
evidence chain / reconstruction report
  ↓
sanitizer / redaction policy
  ↓
finding candidate
  ↓
finding review gate
  ↓
report finding promotion gate
  ↓
report_finding
  ↓
report review gate
  ↓
report_packet_candidate
  ↓
report packet review gate
  ↓
delivery_authorization_candidate
  ↓
delivery authorization gate
  ↓
delivery_package
~~~

## Stable Capabilities

v0.1.30 summarizes the following stable local capabilities:

- Tool Gateway mock execution and generated evidence records,
- credential_ref and mock Vault metadata validation,
- scope registry target alias resolution,
- controlled executor dry-run policy,
- real execution readiness gate,
- operator readiness review,
- human approval record and approval gate,
- evidence chain and reconstruction report,
- sanitizer and redaction policy scaffold,
- sanitized finding candidate model,
- finding candidate review gate,
- report finding promotion gate,
- report review gate,
- report packet review gate,
- delivery authorization gate.

## Explicit Non-Goals

The checkpoint explicitly keeps these out of scope:

- real ZAP/Burp/Nmap/nuclei execution,
- external process execution,
- network activity,
- raw adapter artifact exposure to AI,
- customer delivery,
- delivery dispatch,
- final lifecycle terminology,
- report-ready artifacts,
- customer-delivery-ready artifacts.

## Safety Invariants

The checkpoint validates that:

~~~text
real_execution_permitted: false
external_process_executed: false
network_activity_performed: false
secret_exposed_to_ai: false
report_ready: false
customer_delivery_ready: false
delivery_dispatched: false
customer_delivery_performed: false
evidence_required: true
~~~

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/lifecycle-checkpoints/demo/
~~~

Generated files:

- `lifecycle-checkpoint.generated.json`
- `lifecycle-checkpoint.generated.md`

## Example Command

~~~bash
py tools/generate_lifecycle_checkpoint.py
~~~

## Relationship to v0.2.x

The v0.1.x line should be treated as a control and review workflow scaffold.

The next natural phase is v0.2.x, focused on controlled local runtime readiness, likely including:

- controlled local ZAP runtime readiness,
- local-only vulnerable target setup,
- runtime detection without execution,
- sanitizer coverage expansion,
- scope registry runtime destination storage design,
- bounded execution mode transition design.

## Terminology Note

This project avoids `final` as a lifecycle label for report artifacts.

Artifacts remain reviewable, versioned, and subject to separate authorization gates.

## Relationship to Controlled Local Runtime Readiness

The lifecycle checkpoint is the baseline before controlled local runtime work.

v0.2.0 starts with runtime detection only and keeps real execution, external process execution, and network activity disabled.

See `docs/39-controlled-local-runtime-readiness.md`.
