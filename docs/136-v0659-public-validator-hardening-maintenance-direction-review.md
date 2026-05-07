# v0.6.59 Public Validator Hardening Maintenance Direction Review

Status: review
Date: 2026-05-07

## Purpose

This checkpoint chooses the conservative post-v0.6.58 direction for public validator hardening.

It selects maintenance direction review rather than immediate validator behavior hardening implementation readiness.

It is a direction review only.

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

## Direction conclusion

The project should not move directly into validator behavior hardening implementation readiness.

The conservative next direction is maintenance-oriented:

* keep the current public validator behavior unchanged,
* keep validator output unchanged,
* keep the documentation-only hardening scope,
* keep the current public-safe static negative fixture set,
* reduce future complexity before implementation is considered,
* review maintainability of the current public validator negative fixture and documentation track.

## Direction decision

~~~text
public_validator_hardening_maintenance_direction_review_completed = true
public_validator_hardening_direction_selected = maintenance_first
public_validator_behavior_hardening_implementation_readiness_deferred = true
public_validator_behavior_hardening_implementation_not_approved = true
documentation_only_hardening_scope_retained = true
v0655_consolidated_baselines_retained = true
v0656_readiness_boundary_retained = true
v0657_scope_plan_retained = true
v0658_scope_close_readiness_retained = true
maintenance_review_may_continue = true
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

## Maintenance rationale

Maintenance-first is preferred because the current public validator track already has several retained documentation and test baselines:

* public-safe static negative fixtures,
* negative fixture index,
* metadata contract candidate,
* metadata contract test,
* documentation-only failure category mapping,
* mapping candidate test,
* documentation-only hardening scope,
* read-only local checks.

This is valuable, but it also increases maintenance surface area.  
Before implementation hardening, the project should decide whether the current public track is easy enough to review, explain, and maintain.

## Maintenance review surfaces

A later maintenance checkpoint may review these surfaces.

| Maintenance surface | Review question | Current decision |
| --- | --- | --- |
| documentation ordering | Are v0.6.44-v0.6.58 docs easy to navigate? | review may continue |
| test ordering | Are negative fixture tests easy to understand in `run_all_local_checks.py`? | review may continue |
| fixture duplication | Are public negative fixtures too repetitive to maintain safely? | review may continue |
| metadata readability | Are `negative_fixture_metadata.example.json` files understandable enough? | review may continue |
| mapping readability | Is the documentation-only failure category mapping easy to review? | review may continue |
| hardening scope readability | Is the documentation-only hardening scope easy to distinguish from implementation? | review may continue |
| public claim boundaries | Are non-authorization and non-proof boundaries still obvious? | review may continue |
| next-step clarity | Is it clear why implementation readiness is deferred? | review may continue |

This table does not approve any implementation changes.

## Retained category set

The current 13 public negative fixture categories remain retained.

| Negative fixture category | Direction status |
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

## Maintained compatibility requirements

The v0.6.57 and v0.6.58 compatibility requirements remain retained.

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

## Explicitly deferred implementation paths

The following remain deferred and are not approved by v0.6.59:

| Deferred path | Required gate before consideration |
| --- | --- |
| Validator behavior implementation | validator behavior implementation readiness review |
| Validator JSON failure category output | validator output contract readiness review |
| Metadata-level `expected_failure_category` | fixture metadata rewrite readiness review |
| JSON Schema for metadata or mapping | schema design and compatibility review |
| New negative fixture categories | negative fixture planning and readiness review |
| Fixture rewrite or reduction | fixture maintenance planning and compatibility review |
| Runtime, scanner, Docker, or credential execution | runtime authorization, preflight, and safety gate review |

## Maintenance-first risks to avoid

A maintenance-first path should avoid:

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

> Public-safe Applied Implementations can choose a maintenance-first path after closing a documentation-only validator hardening scope, preserving reviewability and claim boundaries before considering validator behavior implementation.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.60 Public Validator Hardening Maintenance Baseline Review
~~~

That checkpoint should review the maintainability of the retained public validator hardening baselines before any validator behavior implementation readiness review is considered.

It should not implement validator behavior changes.

## Out of scope

This checkpoint does not modify validator behavior, add validator failure category output, create a validator output contract, add metadata-level failure category fields, add JSON Schema, rewrite fixture metadata, add negative fixtures, start validator behavior hardening implementation, approve validator behavior hardening implementation readiness, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
