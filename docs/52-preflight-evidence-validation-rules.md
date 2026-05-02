# Preflight Evidence Validation Rules

## Purpose

This document defines the v0.3.3 preflight evidence validation rules for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.3.2 introduced generated preflight evidence examples. v0.3.3 defines rules that validate those generated examples while keeping them separate from live evidence, preflight satisfaction, and execution authorization.

## Core Principle

Validation of generated examples is not validation of live evidence.

The validation rules may pass for generated examples, but this does not mean live preflight evidence exists, checks are satisfied, preflight is satisfied, or execution is authorized.

## Current Flow

~~~text
generated preflight evidence record examples
  ↓
preflight evidence validation rules
  ↓
future live evidence validation rules
~~~

## Validation Rule Categories

The current rule set covers:

- example boundary,
- check satisfaction boundary,
- fail-closed behavior,
- authorization boundary,
- preflight boundary,
- AI visibility boundary,
- raw artifact boundary,
- sanitization boundary,
- representative example coverage,
- runtime execution boundary.

## Current Rule Behavior

The rule set keeps:

~~~text
validation_rules_defined: true
validation_rules_executed_against_examples: true
generated_examples_validated: true
live_evidence_records_validated: false
all_required_evidence_records_validated: false
all_required_checks_satisfied: false
preflight_satisfied: false
execution_authorized: false
execution_authorization_satisfied: false
runtime_enforcement_implemented: false
ready_for_runtime_execution: false
ready_for_customer_target: false
ready_for_external_network: false
~~~

## Non-Execution Invariants

The rule set and gate keep:

~~~text
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
private-not-in-git/preflight-evidence-validation-rules/demo/
~~~

Generated files:

- `preflight-evidence-example-set.generated.json`
- `preflight-evidence-example-gate-result.generated.json`
- `preflight-evidence-validation-rule-set.generated.json`
- `preflight-evidence-validation-rule-gate-result.generated.json`

## Example Command

~~~bash
py tools/generate_preflight_evidence_validation_rules_demo.py
~~~

You can also test alternative review states:

~~~bash
py tools/generate_preflight_evidence_validation_rules_demo.py needs_revision
py tools/generate_preflight_evidence_validation_rules_demo.py rejected
~~~

## Future Work

Future v0.3.x work should add:

- validation rules for all generated evidence examples,
- negative examples for missing inputs,
- negative examples for mismatched bindings,
- negative examples for stale state,
- negative examples for unsafe state,
- evidence integrity fields,
- reconstruction validation rules,
- separate live evidence validation rules.
