# v0.6.48 Public Validator Negative Fixture Coverage Hardening Planning

Status: planning
Date: 2026-05-07

## Purpose

This checkpoint plans how to harden public validator negative fixture coverage after the first negative fixture track was closed in v0.6.47.

It is a planning checkpoint only.

It does not modify validator behavior.  
It does not add new negative fixtures.  
It does not rewrite the v0.6.46 fixture set.  
It does not create runnable lab configuration.  
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

Previous checkpoints:

* v0.6.44 Public Validator Negative Fixture Planning
* v0.6.45 Public Validator Negative Fixture Implementation Readiness Review
* v0.6.46 Public Validator Negative Fixture Implementation Candidate
* v0.6.47 Public Validator Negative Fixture Coverage Review and Close-Readiness

Current public fixture root:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

Current positive control:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

Current read-only harness:

~~~text
tools/test_v0646_public_validator_negative_fixture_implementation_candidate.py
tools/test_v0647_public_validator_negative_fixture_coverage_review_close_readiness.py
~~~

Current validator:

~~~text
tools/validate_public_example_structure.py
~~~

## Planning conclusion

The first negative fixture track is closed, but later hardening should be planned before any validator behavior expansion.

v0.6.48 defines a conservative hardening plan that can be used to decide whether a later checkpoint should modify the public example structural validator, refine expected blocker metadata, reduce fixture duplication, or improve maintainability.

This checkpoint does not implement those changes.

## Reviewed negative fixture categories

* `missing-package-artifact`
* `missing-scenario-artifact`
* `missing-scenario-directory`
* `malformed-json`
* `broken-linkage`
* `scenario-posture-contradiction`
* `non-example-name`
* `missing-non-proof-statement`
* `missing-five-questions-mapping`
* `hygiene-not-passed`
* `forbidden-text-leakage`
* `overclaim-language`
* `boundary-flag-violation`

## Candidate hardening map

| Negative fixture category | Planned hardening surface |
| --- | --- |
| `missing-package-artifact` | required package artifact coverage |
| `missing-scenario-artifact` | required scenario artifact coverage |
| `missing-scenario-directory` | scenario coverage completeness |
| `malformed-json` | JSON parse failure coverage |
| `broken-linkage` | request / gate / dispatch / evidence linkage coverage |
| `scenario-posture-contradiction` | scenario posture consistency coverage |
| `non-example-name` | public example naming coverage |
| `missing-non-proof-statement` | non-proof statement coverage |
| `missing-five-questions-mapping` | AAEF five-questions mapping coverage |
| `hygiene-not-passed` | publication hygiene coverage |
| `forbidden-text-leakage` | forbidden text leakage coverage |
| `overclaim-language` | overclaim language coverage |
| `boundary-flag-violation` | runtime/scanner/customer/delivery boundary coverage |

## Candidate hardening workstreams

### Workstream A: Expected blocker metadata contract

Plan a lightweight contract for expected blocker metadata.

Candidate fields:

~~~text
negative_category
expected_validator_result
expected_blockers
expected_failure_surface
expected_error_keywords
non_authorization_statement
runtime_boundary
source_positive_control
synthetic_public_safe_static_fixture
~~~

### Workstream B: Validator failure category alignment

Plan a mapping between negative fixture categories and validator blocker categories.

The mapping is planning only and does not require validator code changes in this checkpoint.

### Workstream C: Fixture maintainability and size review

The v0.6.46 fixture set is intentionally complete but large.

A later checkpoint may consider whether fully materialized fixtures, shared fixture templates, generated fixture material, fixture summaries, or a compact manifest would be easier to maintain.

No restructuring is performed in v0.6.48.

### Workstream D: Positive control guardrail

Plan to keep the positive control separate and unmutated.

~~~text
positive_control_preserved = true
positive_control_must_remain_unmutated = true
positive_control_expected_result = pass
negative_fixtures_expected_result = fail_closed
~~~

### Workstream E: Public-safety and publication hygiene guardrail

Plan to preserve publication hygiene and public-safety boundaries before and after any later validator hardening.

~~~text
private_artifact_copied_to_public = false
credential_material_present = false
customer_material_present = false
scanner_output_present = false
runtime_execution_authorized = false
docker_execution_authorized = false
network_activity_allowed = false
delivery_authorized = false
~~~

### Workstream F: Applied Implementation handback boundary

Plan to keep any AAEF main handback at evidence/interface level only.

Potential AAEF main handback lesson:

> Public-safe Applied Implementations can use static negative fixtures with explicit expected blocker metadata to test whether evidence packages fail closed without turning validator output into authority.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, or private generated artifacts.

## Recommended sequencing

A safe later sequence would be:

1. v0.6.49: Public Validator Negative Fixture Metadata Contract Readiness Review
2. v0.6.50: Public Validator Negative Fixture Metadata Contract Candidate
3. v0.6.51: Public Validator Failure Category Mapping Planning
4. v0.6.52: Public Validator Failure Category Mapping Candidate
5. Later: validator behavior hardening implementation readiness review

This sequencing deliberately separates planning, metadata contract, mapping, and validator behavior.

## Planning decision flags

~~~text
public_validator_negative_fixture_hardening_planning_completed = true
negative_fixture_track_closed_before_hardening = true
negative_fixture_hardening_goals_defined = true
expected_blocker_metadata_contract_planned = true
validator_failure_category_alignment_planned = true
fixture_maintainability_review_planned = true
positive_control_guardrail_planned = true
publication_hygiene_guardrail_planned = true
applied_implementation_handback_boundary_planned = true
new_negative_fixtures_added = false
existing_negative_fixtures_rewritten = false
validator_behavior_modified = false
validator_behavior_expansion_implemented = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
~~~

## Safety boundary assessment

~~~text
public_safe_static_fixture_set = true
synthetic_only = true
fixture_live_evidence = false
private_artifact_copied_to_public = false
tool_backed_diagnostic_capture_started = false
local_lab_diagnostic_system_built = false
docker_compose_file_created = false
docker_compose_executed = false
docker_image_pulled = false
container_started = false
port_bound = false
runtime_execution_authorized = false
scanner_execution_authorized = false
scan_execution_allowed = false
network_activity_allowed = false
credential_injection_permitted = false
customer_target = false
customer_target_authorized = false
external_network_target = false
delivery_authorized = false
customer_deliverable = false
~~~

## Applied Implementation boundary

This remains AAEF-AI-VA Applied Implementation work.

~~~text
aaef_handback_category_applied_implementation = true
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

## Out of scope

This checkpoint does not modify validator behavior, add negative fixtures, rewrite existing negative fixtures, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
