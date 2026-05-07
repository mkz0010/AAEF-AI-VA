# v0.6.53 Public Validator Failure Category Mapping Candidate

Status: candidate
Date: 2026-05-07

## Purpose

This checkpoint adds a documentation-only candidate mapping between public negative fixture categories and public validator failure category names.

It follows the safest option identified in v0.6.52: a documentation-only mapping table.

It does not modify validator behavior.  
It does not add validator failure category output.  
It does not add or change fixture metadata fields.  
It does not add a JSON Schema file.  
It does not rewrite negative fixture metadata.  
It does not add new negative fixtures.  
It does not create runnable lab configuration.  
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

Previous checkpoints:

* v0.6.51 Public Validator Negative Fixture Metadata Contract Review and Close-Readiness
* v0.6.52 Public Validator Failure Category Mapping Readiness Review

Current readiness review:

~~~text
docs/129-v0652-public-validator-failure-category-mapping-readiness-review.md
~~~

Current metadata contract baseline:

~~~text
docs/127-v0650-public-validator-negative-fixture-metadata-contract-candidate.md
docs/128-v0651-public-validator-negative-fixture-metadata-contract-review-close-readiness.md
~~~

Current negative fixture root:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

Current validator:

~~~text
tools/validate_public_example_structure.py
~~~

## Candidate scope

This is a documentation-only mapping candidate.

~~~text
failure_category_mapping_candidate_added = true
failure_category_mapping_documentation_only = true
failure_category_mapping_table_added = true
failure_category_mapping_applies_to_existing_v0646_fixture_set = true
failure_category_mapping_uses_v0651_metadata_contract_baseline = true
failure_category_mapping_validator_output_added = false
failure_category_mapping_validator_behavior_modified = false
failure_category_mapping_metadata_field_added = false
failure_category_mapping_fixture_metadata_rewritten = false
failure_category_mapping_schema_added = false
negative_fixtures_added = false
validator_behavior_modified = false
validator_behavior_expansion_implemented = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
~~~

## Candidate mapping table

The candidate mapping covers the current v0.6.46 public negative fixture categories only.

| Negative fixture category | Candidate validator failure category name | Candidate status |
| --- | --- | --- |
| `missing-package-artifact` | `missing_required_package_artifact` | candidate |
| `missing-scenario-artifact` | `missing_required_scenario_artifact` | candidate |
| `missing-scenario-directory` | `missing_required_scenario_directory` | candidate |
| `malformed-json` | `malformed_json` | candidate |
| `broken-linkage` | `broken_evidence_linkage` | candidate |
| `scenario-posture-contradiction` | `scenario_posture_contradiction` | candidate |
| `non-example-name` | `non_example_or_unsafe_name` | candidate |
| `missing-non-proof-statement` | `missing_non_proof_statement` | candidate |
| `missing-five-questions-mapping` | `missing_five_questions_mapping` | candidate |
| `hygiene-not-passed` | `publication_hygiene_not_passed` | candidate |
| `forbidden-text-leakage` | `forbidden_text_leakage` | candidate |
| `overclaim-language` | `overclaim_language` | candidate |
| `boundary-flag-violation` | `boundary_flag_violation` | candidate |

## Interpretation

This mapping is reviewer-facing and evidence-interface-facing.

It means:

* each known negative fixture category has a candidate stable failure category name,
* reviewers can compare fixture intent with future validator failure category naming,
* future work can decide whether to keep the mapping documentation-only, add metadata-level fields, or add validator JSON output names after separate review.

It does not mean:

* validator output is authoritative,
* validator output is complete,
* validator behavior has changed,
* a new validator output contract exists,
* fixture metadata has changed,
* runtime execution is authorized,
* scanner execution is authorized,
* Docker execution is authorized,
* credential injection is authorized,
* customer-target operation is authorized,
* report delivery is authorized,
* certification, legal sufficiency, audit sufficiency, compliance, or external-framework equivalence is claimed.

## Candidate constraints

The mapping candidate must remain within these constraints:

~~~text
mapping_is_documentation_only = true
mapping_is_reviewer_facing = true
mapping_is_evidence_interface_facing = true
validator_output_contract_created = false
validator_json_output_changed = false
fixture_metadata_contract_changed = false
fixture_metadata_rewritten = false
new_fixture_category_added = false
runtime_or_scanner_authority_added = false
~~~

## Future implementation gates

A later checkpoint may consider one of these options only after separate review:

| Option | Requires separate review? | Notes |
| --- | --- | --- |
| Keep documentation-only mapping | yes | safest path |
| Add metadata-level `expected_failure_category` | yes | requires fixture metadata rewrite review |
| Add validator JSON output failure category names | yes | requires validator behavior implementation readiness review |
| Add JSON Schema for mapping | yes | requires schema design and compatibility review |

v0.6.53 chooses only the documentation-only candidate.

## Applied Implementation boundary

This remains AAEF-AI-VA Applied Implementation work.

~~~text
aaef_handback_category_applied_implementation = true
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

AAEF main handback, if any, should remain evidence/interface-level only:

> Public-safe Applied Implementations can define documentation-only mappings between static negative fixture categories and candidate validator failure category names without treating validator output as execution authority.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.54 Public Validator Failure Category Mapping Review and Close-Readiness
~~~

That checkpoint should review whether the documentation-only mapping candidate is sufficient to close the mapping track before any validator output or behavior work is considered.

## Out of scope

This checkpoint does not add validator failure category output, add a metadata-level failure category field, add a JSON Schema, rewrite fixture metadata, add negative fixtures, modify validator behavior, start validator behavior hardening implementation, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
