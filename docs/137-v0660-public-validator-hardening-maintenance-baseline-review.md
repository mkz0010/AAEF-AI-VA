# v0.6.60 Public Validator Hardening Maintenance Baseline Review

Status: review
Date: 2026-05-07

## Purpose

This checkpoint reviews the maintenance baseline for the public validator hardening track after v0.6.59 selected the conservative maintenance-first direction.

It is a maintenance baseline review only.

It does not modify validator behavior.  
It does not add validator failure category output.  
It does not create a validator output contract.  
It does not add or change fixture metadata fields.  
It does not add a metadata-level `expected_failure_category` field.  
It does not add a JSON Schema file.  
It does not rewrite negative fixture metadata.  
It does not add new negative fixtures.  
It does not start validator behavior hardening implementation.  
It does not approve validator behavior hardening implementation readiness.  
It does not create runnable lab configuration.  
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

Previous maintenance direction checkpoint:

~~~text
docs/136-v0659-public-validator-hardening-maintenance-direction-review.md
~~~

Previous scope close-readiness checkpoint:

~~~text
docs/135-v0658-public-validator-behavior-hardening-scope-review-close-readiness.md
~~~

Previous scope planning checkpoint:

~~~text
docs/134-v0657-public-validator-behavior-hardening-scope-planning.md
~~~

Previous readiness checkpoint:

~~~text
docs/133-v0656-public-validator-behavior-hardening-readiness-review.md
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

## Maintenance baseline conclusion

The public validator hardening track has a maintainable documentation-only baseline for the current fixture set.

The baseline is acceptable for continued maintenance, but it should not be treated as approval to implement validator behavior hardening.

The next safe direction is to improve maintenance clarity before any validator behavior implementation readiness review is considered.

## Maintenance baseline decision

~~~text
public_validator_hardening_maintenance_baseline_review_completed = true
public_validator_hardening_maintenance_baseline_established = true
public_validator_hardening_maintenance_baseline_is_documentation_only = true
public_validator_hardening_maintenance_direction_retained = true
public_validator_behavior_hardening_implementation_readiness_deferred = true
public_validator_behavior_hardening_implementation_not_approved = true
documentation_only_hardening_scope_retained = true
v0655_consolidated_baselines_retained = true
v0656_readiness_boundary_retained = true
v0657_scope_plan_retained = true
v0658_scope_close_readiness_retained = true
v0659_maintenance_direction_retained = true
maintenance_baseline_may_continue = true
maintenance_cleanup_may_be_considered = true
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

## Maintenance baseline surfaces

The maintenance baseline retains these review surfaces.

| Maintenance surface | Baseline result | Follow-up direction |
| --- | --- | --- |
| documentation ordering | acceptable baseline | may improve reviewer navigation |
| test ordering | acceptable baseline | may group maintenance tests more clearly |
| fixture duplication | acceptable baseline | may review repetition before future fixture changes |
| metadata readability | acceptable baseline | may improve reviewer-facing explanations |
| mapping readability | acceptable baseline | may keep documentation-only mapping prominent |
| hardening scope readability | acceptable baseline | may clarify non-implementation posture |
| public claim boundaries | acceptable baseline | must retain non-authorization and non-proof boundaries |
| next-step clarity | acceptable baseline | should favor maintenance cleanup before implementation readiness |

This table is a maintenance baseline.  
It is not a validator behavior change, validator output contract, metadata rewrite, fixture rewrite, or schema addition.

## Retained category set

The current 13 public negative fixture categories remain retained.

| Negative fixture category | Maintenance baseline status |
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

The maintenance baseline retains:

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

The retained public validator remains:

~~~text
tools/validate_public_example_structure.py
~~~

The retained positive control remains:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

The retained public negative fixture root remains:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

## Maintained compatibility requirements

The following compatibility requirements remain active.

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

## Maintenance cleanup candidates for later review

A later checkpoint may consider maintenance cleanup only if it preserves the current public safety boundaries.

| Cleanup candidate | Current decision | Required gate |
| --- | --- | --- |
| Add a public validator negative fixture index summary | may be considered | maintenance cleanup planning review |
| Add a reviewer navigation note for v0.6.44-v0.6.60 | may be considered | maintenance cleanup planning review |
| Group negative fixture tests in `run_all_local_checks.py` comments | may be considered | maintenance cleanup planning review |
| Improve fixture metadata explanations without field changes | may be considered | fixture maintenance review |
| Improve mapping documentation layout | may be considered | documentation maintenance review |
| Clarify hardening scope non-implementation wording | may be considered | documentation maintenance review |
| Reduce duplicate prose across review documents | may be considered | documentation maintenance review |

These cleanup candidates do not approve validator behavior changes.

## Explicitly deferred implementation paths

The following remain deferred and are not approved by v0.6.60:

| Deferred path | Required gate before consideration |
| --- | --- |
| Validator behavior implementation | validator behavior implementation readiness review |
| Validator JSON failure category output | validator output contract readiness review |
| Metadata-level `expected_failure_category` | fixture metadata rewrite readiness review |
| JSON Schema for metadata or mapping | schema design and compatibility review |
| New negative fixture categories | negative fixture planning and readiness review |
| Fixture rewrite or reduction | fixture maintenance planning and compatibility review |
| Runtime, scanner, Docker, or credential execution | runtime authorization, preflight, and safety gate review |

## Maintenance risks to avoid

The maintenance baseline should avoid:

* hiding the fact that validator behavior is unchanged,
* allowing documentation to imply execution authority,
* turning documentation-only mapping into a validator output contract,
* silently introducing metadata fields,
* silently rewriting fixtures,
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

> Public-safe Applied Implementations can establish a documentation-only maintenance baseline for validator hardening before considering validator behavior implementation, preserving reviewability and claim boundaries.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.61 Public Validator Hardening Maintenance Cleanup Planning
~~~

That checkpoint should plan maintenance cleanup only, such as navigation, ordering, readability, or non-implementation clarity.

It should not implement validator behavior changes.

## Out of scope

This checkpoint does not modify validator behavior, add validator failure category output, create a validator output contract, add metadata-level failure category fields, add JSON Schema, rewrite fixture metadata, add negative fixtures, start validator behavior hardening implementation, approve validator behavior hardening implementation readiness, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
