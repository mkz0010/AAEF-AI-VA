# v0.6.50 Public Validator Negative Fixture Metadata Contract Candidate

Status: candidate
Date: 2026-05-07

## Purpose

This checkpoint adds a candidate metadata contract for public validator negative fixtures.

The contract is intentionally narrow. It defines the metadata fields and boundary requirements that already exist in the v0.6.46 negative fixture set and makes them reviewable as a candidate contract.

This checkpoint does not modify validator behavior.  
It does not rewrite negative fixture metadata.  
It does not add new negative fixtures.  
It does not add a JSON Schema file.  
It does not create runnable lab configuration.  
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

Previous checkpoints:

* v0.6.46 Public Validator Negative Fixture Implementation Candidate
* v0.6.47 Public Validator Negative Fixture Coverage Review and Close-Readiness
* v0.6.48 Public Validator Negative Fixture Coverage Hardening Planning
* v0.6.49 Public Validator Negative Fixture Metadata Contract Readiness Review

Current public fixture root:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

Current metadata files:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/*/negative_fixture_metadata.example.json
~~~

Current positive control:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

Current validator:

~~~text
tools/validate_public_example_structure.py
~~~

## Candidate contract status

This document is a candidate contract.

~~~text
metadata_contract_candidate_added = true
metadata_contract_documented = true
metadata_contract_test_added = true
metadata_contract_applies_to_public_negative_fixtures = true
metadata_contract_applies_to_existing_v0646_fixture_set = true
metadata_contract_schema_added = false
metadata_contract_json_schema_added = false
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

## Contract subject

The contract applies to each file matching:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/*/negative_fixture_metadata.example.json
~~~

The contract does not apply to:

* positive control metadata,
* private generated artifacts,
* scanner output,
* live runtime evidence,
* customer materials,
* delivery packages,
* commercial material,
* patent-sensitive diagnostic reconstruction details.

## Required metadata fields

Each negative fixture metadata file must contain the following required fields.

| Field | Required value or type | Meaning |
| --- | --- | --- |
| `negative_category` | non-empty string | identifies the negative fixture category |
| `expected_validator_result` | `fail_closed` | records that the fixture is expected to fail closed |
| `expected_blockers` | non-empty list | records expected blocker categories or descriptions |
| `synthetic_public_safe_static_fixture` | `true` | confirms the fixture is synthetic, public-safe, and static |
| `source_positive_control` | path ending in `sanitized-static-mock` | links the fixture to the positive control |
| `non_authorization_statement` | non-empty string | states that the fixture authorizes no runtime/scanner/customer/delivery activity |
| `runtime_boundary` | object | records prohibited runtime and delivery boundary flags |

## Required runtime boundary flags

Each `runtime_boundary` object must contain these flags, and each must be `false`.

~~~text
runtime_execution_authorized = false
scanner_execution_authorized = false
scan_execution_allowed = false
credential_injection_permitted = false
customer_target = false
customer_target_authorized = false
delivery_authorized = false
customer_deliverable = false
fixture_live_evidence = false
validator_behavior_modified_by_fixture = false
~~~

## Required non-authorization statement fragments

Each `non_authorization_statement` must be explicit that the fixture does not authorize:

* runtime execution,
* scanner execution,
* Docker execution,
* credential injection,
* customer-target operation,
* delivery.

The exact wording may vary, but the statement must preserve all six boundaries.

## Expected categories covered by this candidate

The current contract candidate covers the v0.6.46 fixture categories:

| Category | Expected result |
| --- | --- |
| `missing-package-artifact` | fail closed |
| `missing-scenario-artifact` | fail closed |
| `missing-scenario-directory` | fail closed |
| `malformed-json` | fail closed |
| `broken-linkage` | fail closed |
| `scenario-posture-contradiction` | fail closed |
| `non-example-name` | fail closed |
| `missing-non-proof-statement` | fail closed |
| `missing-five-questions-mapping` | fail closed |
| `hygiene-not-passed` | fail closed |
| `forbidden-text-leakage` | fail closed |
| `overclaim-language` | fail closed |
| `boundary-flag-violation` | fail closed |

A later checkpoint may add categories only after a separate planning or readiness review.

## Contract interpretation

The contract is a reviewer-facing metadata contract.

It means:

* each negative fixture declares why it is expected to fail closed,
* each negative fixture links back to the positive control,
* each negative fixture preserves public-safe static posture,
* each negative fixture explicitly denies runtime/scanner/Docker/credential/customer/delivery authorization,
* reviewers can compare expected blockers against validator or harness behavior.

It does not mean:

* the validator is complete,
* the fixture proves diagnostic completeness,
* the fixture is live evidence,
* the fixture authorizes execution,
* the project is production ready,
* the project provides certification, compliance, legal sufficiency, audit sufficiency, or external-framework equivalence.

## Contract candidate test

The candidate contract is checked by:

~~~text
tools/test_v0650_public_validator_negative_fixture_metadata_contract_candidate.py
~~~

The test is read-only.

It checks the existing public negative fixture metadata and does not rewrite fixture files, modify validator behavior, add fixtures, run Docker, run scanners, inject credentials, contact customer targets, or authorize delivery.

## Applied Implementation boundary

This remains AAEF-AI-VA Applied Implementation work.

~~~text
aaef_handback_category_applied_implementation = true
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

AAEF main handback, if any, should remain evidence/interface-level only:

> A public-safe Applied Implementation can use a metadata contract for static negative fixtures to make expected fail-closed behavior reviewable without treating validator output as execution authority.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.51 Public Validator Negative Fixture Metadata Contract Review and Close-Readiness
~~~

That checkpoint should review whether the candidate contract is sufficient to close the metadata contract track before moving to validator failure category mapping.

## Out of scope

This checkpoint does not add a JSON Schema, rewrite fixture metadata, add negative fixtures, modify validator behavior, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
