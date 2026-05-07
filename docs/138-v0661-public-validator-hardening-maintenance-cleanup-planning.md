# v0.6.61 Public Validator Hardening Maintenance Cleanup Planning

Status: planning
Date: 2026-05-07

## Purpose

This checkpoint plans maintenance cleanup for the public validator hardening track after v0.6.60 established a conservative documentation-only maintenance baseline.

It is a maintenance cleanup planning checkpoint only.

It does not modify validator behavior.  
It does not add validator failure category output.  
It does not create a validator output contract.  
It does not add or change fixture metadata fields.  
It does not add a metadata-level `expected_failure_category` field.  
It does not add a JSON Schema file.  
It does not rewrite negative fixture metadata.  
It does not add new negative fixtures.  
It does not reorganize files in this checkpoint.  
It does not edit `run_all_local_checks.py` beyond registering this read-only planning test.  
It does not start validator behavior hardening implementation.  
It does not approve validator behavior hardening implementation readiness.  
It does not create runnable lab configuration.  
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

Previous maintenance baseline checkpoint:

~~~text
docs/137-v0660-public-validator-hardening-maintenance-baseline-review.md
~~~

Previous maintenance direction checkpoint:

~~~text
docs/136-v0659-public-validator-hardening-maintenance-direction-review.md
~~~

Previous scope close-readiness checkpoint:

~~~text
docs/135-v0658-public-validator-behavior-hardening-scope-review-close-readiness.md
~~~

Previous consolidation checkpoint:

~~~text
docs/132-v0655-public-validator-negative-fixture-track-consolidation-review.md
~~~

Retained public validator:

~~~text
tools/validate_public_example_structure.py
~~~

Retained positive control:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

Retained public negative fixture root:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

## Cleanup planning conclusion

The next safe public validator hardening work should be maintenance cleanup planning, not validator behavior implementation readiness.

The cleanup scope should improve reviewer navigation, ordering, readability, and non-implementation clarity while preserving all public-safe static fixture, metadata, mapping, hardening-scope, validator behavior, runtime, scanner, Docker, credential, customer-target, and delivery boundaries.

## Cleanup planning decision

~~~text
public_validator_hardening_maintenance_cleanup_planning_completed = true
public_validator_hardening_maintenance_cleanup_scope_defined = true
public_validator_hardening_maintenance_cleanup_is_documentation_only = true
public_validator_hardening_maintenance_cleanup_uses_v0660_baseline = true
public_validator_hardening_maintenance_cleanup_may_be_considered = true
public_validator_hardening_maintenance_cleanup_candidate_added = false
public_validator_hardening_maintenance_cleanup_implemented = false
public_validator_hardening_maintenance_cleanup_file_reorganization_approved = false
public_validator_hardening_maintenance_cleanup_fixture_rewrite_approved = false
public_validator_hardening_maintenance_cleanup_validator_change_approved = false
public_validator_behavior_hardening_implementation_readiness_deferred = true
public_validator_behavior_hardening_implementation_not_approved = true
documentation_only_hardening_scope_retained = true
v0655_consolidated_baselines_retained = true
v0656_readiness_boundary_retained = true
v0657_scope_plan_retained = true
v0658_scope_close_readiness_retained = true
v0659_maintenance_direction_retained = true
v0660_maintenance_baseline_retained = true
validator_behavior_hardening_implementation_may_be_considered = false
validator_behavior_hardening_candidate_added = false
validator_behavior_hardening_implemented = false
validator_behavior_modified = false
validator_behavior_expansion_implemented = false
validator_failure_category_output_added = false
validator_json_output_changed = false
validator_output_contract_created = false
metadata_level_expected_failure_category_added = false
fixture_metadata_contract_changed = false
negative_fixture_metadata_rewritten = false
negative_fixtures_added = false
json_schema_added = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
~~~

## Planned cleanup scope

The planned cleanup scope is intentionally narrow.

| Cleanup surface | Planned cleanup direction | Current decision |
| --- | --- | --- |
| public validator negative fixture index summary | add or improve reviewer-facing summary only | planning only |
| reviewer navigation note for v0.6.44-v0.6.61 | make the negative fixture and hardening track easier to follow | planning only |
| `run_all_local_checks.py` negative fixture test grouping comments | consider comment grouping without changing executed tests | planning only |
| fixture metadata explanations | improve explanation without metadata field changes | planning only |
| documentation-only failure category mapping layout | improve readability without validator output changes | planning only |
| hardening scope non-implementation wording | make it clearer that no behavior change is approved | planning only |
| public claim boundaries | keep non-authorization and non-proof boundaries visible | planning only |
| next-step clarity | make maintenance-first direction easier to understand | planning only |

This table is planning only.  
It does not approve cleanup implementation.

## Cleanup non-goals

The cleanup plan must not do any of the following.

~~~text
validator_code_change = false
validator_behavior_change = false
validator_json_output_change = false
validator_failure_category_output = false
validator_output_contract = false
metadata_level_expected_failure_category = false
fixture_metadata_rewrite = false
fixture_structure_rewrite = false
json_schema_creation = false
new_negative_fixture_category = false
runtime_execution = false
scanner_execution = false
docker_execution = false
credential_injection = false
customer_target_operation = false
delivery_authorization = false
~~~

## Retained category set

The current 13 public negative fixture categories remain retained.

| Negative fixture category | Cleanup planning status |
| --- | --- |
| `missing-package-artifact` | retained |
| `missing-scenario-artifact` | retained |
| `missing-scenario-directory` | retained |
| `malformed-json` | retained |
| `broken-linkage` | retained |
| `scenario-posture-contradiction` | retained |
| `non-example-name` | retained |
| `missing-non-proof-statement` | retained |
| `missing-five-questions-mapping` | retained |
| `hygiene-not-passed` | retained |
| `forbidden-text-leakage` | retained |
| `overclaim-language` | retained |
| `boundary-flag-violation` | retained |

Later categories should not be added without a separate negative fixture planning and readiness review.

## Retained artifacts and baselines

The cleanup plan retains the v0.6.60 maintenance baseline.

~~~text
retain_public_safe_static_negative_fixtures = true
retain_negative_fixture_index = true
retain_read_only_negative_fixture_harness = true
retain_metadata_contract_candidate = true
retain_metadata_contract_test = true
retain_documentation_only_mapping_candidate = true
retain_mapping_candidate_test = true
retain_documentation_only_hardening_scope = true
retain_positive_control = true
retain_public_example_structural_validator = true
~~~

## Maintained compatibility requirements

The cleanup plan keeps these compatibility requirements active.

~~~text
positive_control_must_remain_passing = true
negative_fixtures_must_remain_fail_closed = true
public_safe_static_fixture_set_must_remain = true
metadata_contract_baseline_must_remain = true
documentation_only_mapping_baseline_must_remain = true
documentation_only_hardening_scope_must_remain = true
read_only_harnesses_must_remain = true
validator_output_must_not_become_authority = true
model_output_must_not_become_authority = true
runtime_execution_must_remain_unauthorized = true
scanner_execution_must_remain_unauthorized = true
docker_execution_must_remain_unauthorized = true
credential_injection_must_remain_unauthorized = true
customer_target_operation_must_remain_unauthorized = true
delivery_must_remain_unauthorized = true
~~~

## Candidate cleanup order for later review

A later cleanup candidate should use this order unless a reviewer records a reason to change it.

| Priority | Cleanup candidate | Reason |
| --- | --- | --- |
| 1 | reviewer navigation note for v0.6.44-v0.6.61 | improves track comprehension without touching fixtures or validator |
| 2 | public validator negative fixture index summary | makes current retained fixture set easier to review |
| 3 | hardening scope non-implementation wording | reduces risk of accidental implementation interpretation |
| 4 | public claim boundary reminders | preserves non-proof and non-authorization clarity |
| 5 | `run_all_local_checks.py` grouping comments | improves local check readability without changing commands |
| 6 | mapping documentation layout | improves reviewer readability without output contract changes |
| 7 | fixture metadata explanations without field changes | improves readability without metadata contract change |
| 8 | duplicate prose reduction across review documents | should be considered only after navigation and boundary clarity are stable |

This ordering is not an implementation approval.

## Explicitly deferred implementation paths

The following remain deferred and are not approved by v0.6.61:

| Deferred path | Required gate before consideration |
| --- | --- |
| Validator behavior implementation | validator behavior implementation readiness review |
| Add validator JSON failure category output | validator output contract readiness review |
| Metadata-level `expected_failure_category` | fixture metadata rewrite readiness review |
| JSON Schema for metadata or mapping | schema design and compatibility review |
| New negative fixture categories | negative fixture planning and readiness review |
| Fixture rewrite or reduction | fixture maintenance planning and compatibility review |
| Runtime, scanner, Docker, or credential execution | runtime authorization, preflight, and safety gate review |

## Maintenance cleanup risks to avoid

The maintenance cleanup plan should avoid:

* making the documentation appear to implement validator behavior,
* hiding that validator behavior is unchanged,
* turning documentation-only mapping into a validator output contract,
* silently introducing metadata fields,
* silently rewriting fixtures,
* changing local check execution semantics through comments,
* treating examples as live evidence,
* treating validator output as proof of diagnostic completeness,
* implying certification, compliance, legal sufficiency, audit sufficiency, or external-framework equivalence,
* weakening public/private artifact boundaries,
* leaking patent-sensitive implementation detail.

## Applied Implementation boundary

This remains AAEF-AI-VA Applied Implementation work.

~~~text
aaef_handback_category_applied_implementation = true
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

AAEF main handback, if any, should remain evidence/interface-level only:

> Public-safe Applied Implementations can plan maintenance cleanup for validator hardening artifacts while preserving documentation-only status, public-safe static fixtures, and non-execution boundaries.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.62 Public Validator Hardening Maintenance Cleanup Candidate
~~~

That checkpoint may implement a narrow maintenance cleanup candidate, preferably starting with reviewer navigation and summary improvements only.

It should not modify validator behavior, validator output, fixture metadata fields, JSON Schema, or runtime/scanner/Docker/credential/customer/delivery boundaries.

## Out of scope

This checkpoint does not modify validator behavior, add validator failure category output, create a validator output contract, add metadata-level failure category fields, add JSON Schema, rewrite fixture metadata, add negative fixtures, reorganize files, start validator behavior hardening implementation, approve validator behavior hardening implementation readiness, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
