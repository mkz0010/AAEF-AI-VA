# v0.6.52 Public Validator Failure Category Mapping Readiness Review

Status: review
Date: 2026-05-07

## Purpose

This checkpoint reviews whether the project is ready to define a future mapping between public negative fixture categories and public validator failure categories.

It is a readiness review only.

It does not implement a failure category mapping.  
It does not modify validator behavior.  
It does not add validator failure category output.  
It does not add a JSON Schema file.  
It does not rewrite negative fixture metadata.  
It does not add new negative fixtures.  
It does not create runnable lab configuration.  
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

Previous checkpoints:

* v0.6.48 Public Validator Negative Fixture Coverage Hardening Planning
* v0.6.49 Public Validator Negative Fixture Metadata Contract Readiness Review
* v0.6.50 Public Validator Negative Fixture Metadata Contract Candidate
* v0.6.51 Public Validator Negative Fixture Metadata Contract Review and Close-Readiness

Current negative fixture root:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

Current metadata contract:

~~~text
docs/127-v0650-public-validator-negative-fixture-metadata-contract-candidate.md
~~~

Current metadata contract close-readiness review:

~~~text
docs/128-v0651-public-validator-negative-fixture-metadata-contract-review-close-readiness.md
~~~

Current validator:

~~~text
tools/validate_public_example_structure.py
~~~

## Readiness conclusion

The project is ready to consider a future public validator failure category mapping candidate.

This readiness conclusion is intentionally narrow:

* It supports defining a future mapping between negative fixture categories and validator failure category names.
* It supports using the closed v0.6.50 metadata contract as the mapping input.
* It supports keeping the mapping reviewer-facing and evidence-interface-facing.
* It does not implement the mapping.
* It does not change validator output.
* It does not modify validator behavior.
* It does not rewrite fixture metadata.
* It does not add fixtures.

## Candidate mapping scope

A future failure category mapping may align the current v0.6.46 negative fixture categories with stable validator failure category names.

| Negative fixture category | Candidate failure category name | Readiness status |
| --- | --- | --- |
| `missing-package-artifact` | `missing_required_package_artifact` | ready for candidate consideration |
| `missing-scenario-artifact` | `missing_required_scenario_artifact` | ready for candidate consideration |
| `missing-scenario-directory` | `missing_required_scenario_directory` | ready for candidate consideration |
| `malformed-json` | `malformed_json` | ready for candidate consideration |
| `broken-linkage` | `broken_evidence_linkage` | ready for candidate consideration |
| `scenario-posture-contradiction` | `scenario_posture_contradiction` | ready for candidate consideration |
| `non-example-name` | `non_example_or_unsafe_name` | ready for candidate consideration |
| `missing-non-proof-statement` | `missing_non_proof_statement` | ready for candidate consideration |
| `missing-five-questions-mapping` | `missing_five_questions_mapping` | ready for candidate consideration |
| `hygiene-not-passed` | `publication_hygiene_not_passed` | ready for candidate consideration |
| `forbidden-text-leakage` | `forbidden_text_leakage` | ready for candidate consideration |
| `overclaim-language` | `overclaim_language` | ready for candidate consideration |
| `boundary-flag-violation` | `boundary_flag_violation` | ready for candidate consideration |

This table is readiness guidance for a later mapping candidate.  
It is not itself an implemented validator output contract.

## Mapping readiness criteria

The project is ready to move to a mapping candidate only if all of the following remain true:

~~~text
failure_category_mapping_readiness_review_completed = true
failure_category_mapping_candidate_may_be_considered = true
failure_category_mapping_scope_defined = true
failure_category_mapping_input_metadata_contract_closed = true
failure_category_mapping_expected_categories_identified = true
failure_category_mapping_candidate_names_identified = true
failure_category_mapping_reviewer_facing_only = true
failure_category_mapping_implementation_ready_for_later_checkpoint = true
failure_category_mapping_implemented = false
failure_category_mapping_validator_output_added = false
failure_category_mapping_validator_behavior_modified = false
failure_category_mapping_schema_added = false
negative_fixture_metadata_rewritten = false
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

## Candidate mapping principles

A future mapping candidate should follow these principles:

1. Keep mapping names stable and machine-readable.
2. Avoid treating a failure category as proof of diagnostic completeness.
3. Avoid treating validator output as execution authority.
4. Preserve positive-control separation.
5. Preserve the v0.6.50 metadata contract.
6. Preserve synthetic, public-safe, static fixture boundaries.
7. Preserve non-authorization statements.
8. Preserve runtime/scanner/Docker/credential/customer/delivery prohibitions.
9. Avoid private artifacts, live evidence, scanner output, customer material, delivery material, or patent-sensitive implementation detail.
10. Keep AAEF handback at evidence/interface level only.

## Future candidate options

A later v0.6.53 mapping candidate may choose one of these shapes:

### Option A: Documentation-only mapping table

Add a documented table that maps negative fixture categories to candidate validator failure category names.

This is the lowest-risk option.

### Option B: Metadata-level mapping field

Add a new optional metadata field such as:

~~~text
expected_failure_category
~~~

This would require a separate fixture metadata update review because it would rewrite public fixture metadata.

### Option C: Validator JSON output category names

Add stable failure category names to validator JSON output.

This would require a validator behavior implementation readiness review before implementation.

v0.6.52 does not choose among these options.  
It only confirms that a future mapping candidate may be considered.

## Risks to avoid

A future mapping should avoid:

* making validator output authoritative,
* creating an implied assurance or conformance claim,
* implying certification, legal sufficiency, audit sufficiency, compliance, or external-framework equivalence,
* implying vulnerability detection completeness,
* creating live execution requirements,
* adding scanner, Docker, runtime, credential, customer-target, or delivery authority,
* leaking private artifacts or patent-sensitive implementation detail,
* silently expanding the closed metadata contract track.

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

AAEF main handback, if any, should remain evidence/interface-level only:

> Public-safe Applied Implementations can plan a reviewer-facing mapping between static negative fixture categories and validator failure categories without treating validator output as execution authority.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.53 Public Validator Failure Category Mapping Candidate
~~~

That checkpoint may add a documentation-only mapping candidate or another explicitly scoped candidate shape.

It should not modify validator behavior unless a separate validator behavior implementation readiness review is completed first.

## Out of scope

This checkpoint does not implement a failure category mapping, add validator failure category output, add a JSON Schema, rewrite fixture metadata, add negative fixtures, modify validator behavior, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
