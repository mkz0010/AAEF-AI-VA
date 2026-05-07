from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/154-v0678-public-sample-relationship-to-validator-planning.md"
V0676_DOC = ROOT / "docs/153-v0676-applied-evidence-next-gap-selection-after-clarity-closeout.md"
V0675_DOC = ROOT / "docs/152-v0675-public-sample-five-questions-clarity-review-close-readiness.md"
V0655_DOC = ROOT / "docs/132-v0655-public-validator-negative-fixture-track-consolidation-review.md"
FIXTURE_ROOT = ROOT / "examples/applied-evidence/public-validator-negative-fixtures"
INDEX = FIXTURE_ROOT / "negative_fixture_index.example.json"
POSITIVE_CONTROL = ROOT / "examples/applied-evidence/sanitized-static-mock"
VALIDATOR = ROOT / "tools/validate_public_example_structure.py"

EXPECTED_CATEGORIES = [
    "missing-package-artifact",
    "missing-scenario-artifact",
    "missing-scenario-directory",
    "malformed-json",
    "broken-linkage",
    "scenario-posture-contradiction",
    "non-example-name",
    "missing-non-proof-statement",
    "missing-five-questions-mapping",
    "hygiene-not-passed",
    "forbidden-text-leakage",
    "overclaim-language",
    "boundary-flag-violation",
]

REQUIRED_METADATA_FIELDS = [
    "negative_category",
    "expected_validator_result",
    "expected_blockers",
    "synthetic_public_safe_static_fixture",
    "source_positive_control",
    "non_authorization_statement",
    "runtime_boundary",
]

REQUIRED_BOUNDARY_FLAGS = [
    "runtime_execution_authorized",
    "scanner_execution_authorized",
    "scan_execution_allowed",
    "credential_injection_permitted",
    "customer_target",
    "customer_target_authorized",
    "delivery_authorized",
    "customer_deliverable",
    "fixture_live_evidence",
    "validator_behavior_modified_by_fixture",
]

REQUIRED_DOC_FLAGS = [
    "public_sample_relationship_to_validator_planning_completed = true",
    "public_sample_relationship_to_validator_planning_is_documentation_only = true",
    "public_sample_relationship_to_validator_planning_uses_v0676_selection = true",
    "public_sample_relationship_to_validator_selected_gap_retained = true",
    "public_sample_relationship_to_validator_candidate_may_be_considered = true",
    "public_sample_relationship_to_validator_planning_only = true",
    "public_sample_relationship_to_validator_started = false",
    "public_sample_relationship_to_validator_implemented = false",
    "public_sample_relationship_to_validator_reviewer_aid_generated = false",
    "public_sample_relationship_to_validator_validator_changed = false",
    "public_sample_relationship_to_validator_output_changed = false",
    "public_sample_relationship_to_validator_contract_created = false",
    "public_sample_relationship_to_validator_public_sample_changed = false",
    "public_sample_relationship_to_validator_sample_refined = false",
    "public_sample_relationship_to_validator_fixture_changed = false",
    "public_sample_relationship_to_validator_negative_fixture_changed = false",
    "public_sample_relationship_to_validator_json_schema_added = false",
    "public_sample_relationship_to_validator_new_walkthrough_created = false",
    "evidence_interface_handback_readiness_started = false",
    "public_sample_five_questions_clarity_close_ready_retained = true",
    "public_sample_five_questions_clarity_reader_aid_retained = true",
    "applied_evidence_implementation_started = false",
    "applied_evidence_package_generated = false",
    "applied_evidence_private_review_record_generated = false",
    "applied_evidence_public_sample_promoted = false",
    "applied_evidence_sanitized_public_sample_refined = false",
    "applied_evidence_handback_prepared = false",
    "public_validator_pause_closeout_retained = true",
    "documentation_only_failure_category_mapping_retained = true",
    "validator_behavior_modified = false",
    "validator_failure_category_output_added = false",
    "validator_json_output_changed = false",
    "validator_output_contract_created = false",
    "metadata_level_expected_failure_category_added = false",
    "fixture_metadata_contract_changed = false",
    "negative_fixture_metadata_rewritten = false",
    "negative_fixtures_added = false",
    "json_schema_added = false",
    "validator_output_is_not_authority = true",
    "validator_success_is_not_runtime_authorization = true",
    "validator_success_is_not_scanner_authorization = true",
    "validator_success_is_not_credential_authorization = true",
    "validator_success_is_not_customer_target_authorization = true",
    "validator_success_is_not_delivery_authorization = true",
    "validator_success_is_not_diagnostic_completeness_proof = true",
    "validator_success_is_not_certification = true",
    "validator_success_is_not_compliance_claim = true",
    "validator_success_is_not_legal_advice = true",
    "validator_success_is_not_audit_opinion = true",
    "validator_success_is_not_external_framework_equivalence = true",
    "documentation_only_failure_category_mapping_is_not_validator_output = true",
    "documentation_only_failure_category_mapping_is_not_validator_output_contract = true",
    "runtime_execution_authorized = false",
    "scanner_execution_authorized = false",
    "docker_execution_authorized = false",
    "credential_injection_permitted = false",
    "customer_target_authorized = false",
    "delivery_authorized = false",
    "public_negative_fixture_set_current = v0.6.46",
    "public_negative_fixture_count = 13",
    "public_negative_fixture_set_static = true",
    "public_negative_fixture_set_synthetic = true",
    "public_negative_fixture_set_public_safe = true",
    "public_negative_fixture_set_retained = true",
    "validator_output_must_not_become_authority = true",
    "model_output_must_not_become_authority = true",
    "runtime_execution_must_remain_unauthorized = true",
    "scanner_execution_must_remain_unauthorized = true",
    "docker_execution_must_remain_unauthorized = true",
    "credential_injection_must_remain_unauthorized = true",
    "customer_target_operation_must_remain_unauthorized = true",
    "delivery_must_remain_unauthorized = true",
    "aaef_handback_category_applied_implementation = true",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"malformed JSON: {path.relative_to(ROOT)}: {exc}") from exc


def main() -> int:
    for path, label in [
        (DOC, "v0.6.78 relationship planning document"),
        (V0676_DOC, "v0.6.76 next-gap selection document"),
        (V0675_DOC, "v0.6.75 clarity closeout document"),
        (V0655_DOC, "v0.6.55 consolidation document"),
        (INDEX, "negative fixture index"),
        (POSITIVE_CONTROL, "sanitized public sample baseline"),
        (VALIDATOR, "public validator"),
    ]:
        require(path.exists(), f"missing required {label}: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in [
        "Status: planning",
        "Tag `v0.6.77` was used for the repository hygiene cleanup",
        "It is a planning checkpoint only.",
        "It does not modify validator behavior.",
        "It does not add validator failure category output.",
        "It does not create a validator output contract.",
        "It does not add or change fixture metadata fields.",
        "It does not add a metadata-level `expected_failure_category` field.",
        "It does not add a JSON Schema file.",
        "It does not rewrite negative fixture metadata.",
        "It does not add new negative fixtures.",
        "It does not refine sanitized public sample content.",
        "It does not change public example text.",
        "It does not prepare AAEF main handback material.",
        "v0.6.79 Public Sample Relationship-to-Validator Candidate",
    ]:
        require(phrase in doc_text, f"v0.6.78 document missing expected text: {phrase}")

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.78 document missing planning flag: {flag}")

    for phrase in [
        "what the public sample is for",
        "what the public validator checks",
        "what the public validator does not check",
        "how public negative fixtures relate to fail-closed validator posture",
        "why validator output is not authority",
        "why validator success does not authorize execution",
        "why documentation-only failure category mapping is not validator output",
        "why documentation-only failure category mapping is not a validator output contract",
        "why validator checks do not prove diagnostic completeness",
        "why validator checks do not create certification, compliance, legal, audit, or equivalence claims",
        "What is the public sample for?",
        "What does the public validator check?",
        "What does the public validator not check?",
        "How do negative fixtures relate?",
        "Is validator output authority?",
        "Does validator success authorize execution?",
        "Does documentation-only mapping change validator output?",
        "Candidate preserves the current public sample content",
        "Candidate preserves current validator behavior",
        "Candidate states validator output is not authority",
        "Candidate states validator success does not authorize execution",
        "Candidate states documentation-only failure category mapping is not validator output",
        "Candidate states documentation-only failure category mapping is not a validator output contract",
        "Candidate remains documentation-only",
        "The documentation-only failure category mapping remains documentation-only.",
        "It is not validator output and not a validator output contract.",
    ]:
        require(phrase in doc_text, f"v0.6.78 document missing relationship phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.78 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.78 document missing retained metadata field: {field}")
    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.78 document missing retained false boundary flag: {flag}")

    v0676_text = V0676_DOC.read_text(encoding="utf-8")
    require("applied_evidence_next_gap_selected_after_clarity_closeout = public_sample_relationship_to_validator" in v0676_text, "v0.6.76 must select public sample relationship to validator")
    require("public_sample_relationship_to_validator_started = false" in v0676_text, "v0.6.76 must not start relationship-to-validator work")
    require("public_sample_relationship_to_validator_validator_changed = false" in v0676_text, "v0.6.76 must not change validator")
    require("public_sample_relationship_to_validator_contract_created = false" in v0676_text, "v0.6.76 must not create validator output contract")
    require("validator_behavior_modified = false" in v0676_text, "v0.6.76 must preserve validator behavior boundary")

    v0675_text = V0675_DOC.read_text(encoding="utf-8")
    require("public_sample_five_questions_clarity_close_ready = true" in v0675_text, "v0.6.75 clarity closeout must be completed")

    v0655_text = V0655_DOC.read_text(encoding="utf-8")
    require("public_validator_negative_fixture_track_consolidation_completed = true" in v0655_text, "v0.6.55 consolidation must be completed")
    require("validator_behavior_modified = false" in v0655_text, "v0.6.55 must preserve validator behavior boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")

    for category in EXPECTED_CATEGORIES:
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        require(metadata_path.exists(), f"metadata missing: {category}")
        metadata = load_json(metadata_path)
        for field in REQUIRED_METADATA_FIELDS:
            require(field in metadata, f"metadata field missing for {category}: {field}")
        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.78 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    for phrase in [
        "this project is certified compliant",
        "this relationship planning provides certification",
        "this relationship planning is legally sufficient",
        "this relationship planning provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this relationship planning",
        "runtime execution is authorized by this relationship planning",
    ]:
        require(phrase not in doc_text.lower(), f"v0.6.78 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.78 public sample relationship-to-validator planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
