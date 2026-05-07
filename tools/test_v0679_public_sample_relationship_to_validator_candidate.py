from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/155-v0679-public-sample-relationship-to-validator-candidate.md"
V0678_DOC = ROOT / "docs/154-v0678-public-sample-relationship-to-validator-planning.md"
V0676_DOC = ROOT / "docs/153-v0676-applied-evidence-next-gap-selection-after-clarity-closeout.md"
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
    "public_sample_relationship_to_validator_candidate_added = true",
    "public_sample_relationship_to_validator_candidate_is_documentation_only = true",
    "public_sample_relationship_to_validator_candidate_uses_v0678_planning = true",
    "public_sample_relationship_to_validator_candidate_uses_v0676_selection = true",
    "public_sample_relationship_to_validator_selected_gap_retained = true",
    "public_sample_relationship_to_validator_reviewer_aid_generated = true",
    "public_sample_relationship_to_validator_candidate_close_readiness_may_be_considered = true",
    "public_sample_relationship_to_validator_started = true",
    "public_sample_relationship_to_validator_implemented = false",
    "public_sample_relationship_to_validator_validator_changed = false",
    "public_sample_relationship_to_validator_output_changed = false",
    "public_sample_relationship_to_validator_contract_created = false",
    "public_sample_relationship_to_validator_public_sample_changed = false",
    "public_sample_relationship_to_validator_sample_refined = false",
    "public_sample_relationship_to_validator_fixture_changed = false",
    "public_sample_relationship_to_validator_negative_fixture_changed = false",
    "public_sample_relationship_to_validator_json_schema_added = false",
    "public_sample_relationship_to_validator_new_walkthrough_created = false",
    "public_sample_relationship_to_validator_current_sample_content_retained = true",
    "public_sample_relationship_to_validator_current_validator_retained = true",
    "public_sample_relationship_to_validator_current_negative_fixtures_retained = true",
    "public_sample_relationship_to_validator_current_fixture_metadata_retained = true",
    "public_sample_relationship_to_validator_current_validator_output_retained = true",
    "evidence_interface_handback_readiness_started = false",
    "public_sample_five_questions_clarity_close_ready_retained = true",
    "public_sample_five_questions_clarity_reader_aid_retained = true",
    "public_sample_five_questions_clarity_candidate_revision_required = false",
    "public_sample_five_questions_clarity_implemented = false",
    "public_sample_five_questions_clarity_sample_refined = false",
    "public_sample_five_questions_clarity_public_sample_changed = false",
    "public_sample_five_questions_clarity_new_walkthrough_created = false",
    "applied_evidence_reviewer_current_state_summary_retained = true",
    "applied_evidence_reviewer_current_state_summary_close_ready_retained = true",
    "applied_evidence_reviewer_current_state_summary_revision_required = false",
    "applied_evidence_current_state_summary_generated = true",
    "applied_evidence_implementation_started = false",
    "applied_evidence_package_generated = false",
    "applied_evidence_private_review_record_generated = false",
    "applied_evidence_public_sample_promoted = false",
    "applied_evidence_sanitized_public_sample_refined = false",
    "applied_evidence_fixture_rewrite_approved = false",
    "applied_evidence_schema_change_approved = false",
    "applied_evidence_handback_prepared = false",
    "applied_evidence_static_mock_package_retained = true",
    "applied_evidence_sanitized_public_sample_retained = true",
    "applied_evidence_reviewer_walkthrough_history_retained = true",
    "applied_evidence_five_questions_mapping_history_retained = true",
    "applied_evidence_handback_boundary_retained = true",
    "public_validator_pause_closeout_retained = true",
    "public_validator_track_pause_state_retained = true",
    "public_validator_maintenance_continue_now = false",
    "validator_behavior_hardening_implementation_readiness_deferred = true",
    "public_validator_behavior_hardening_implementation_not_approved = true",
    "documentation_only_hardening_scope_retained = true",
    "documentation_only_failure_category_mapping_retained = true",
    "reviewer_navigation_note_retained = true",
    "public_negative_fixture_index_summary_retained = true",
    "v0678_relationship_planning_retained = true",
    "validator_behavior_hardening_implementation_may_be_considered = false",
    "validator_behavior_hardening_candidate_added = false",
    "validator_behavior_hardening_implemented = false",
    "validator_behavior_modified = false",
    "validator_behavior_expansion_implemented = false",
    "validator_failure_category_output_added = false",
    "validator_json_output_changed = false",
    "validator_output_contract_created = false",
    "metadata_level_expected_failure_category_added = false",
    "fixture_metadata_contract_changed = false",
    "negative_fixture_metadata_rewritten = false",
    "negative_fixtures_added = false",
    "json_schema_added = false",
    "validator_output_is_not_authority = true",
    "validator_success_is_not_execution_permission = true",
    "validator_failure_is_not_a_runtime_decision = true",
    "model_output_is_not_authority = true",
    "gate_decision_remains_authority_relevant = true",
    "execution_authorization_requires_separate_gate_and_evidence = true",
    "documentation_only_failure_category_mapping_is_not_validator_output = true",
    "documentation_only_failure_category_mapping_is_not_validator_output_contract = true",
    "documentation_only_failure_category_mapping_does_not_change_validator_behavior = true",
    "documentation_only_failure_category_mapping_does_not_change_fixture_metadata = true",
    "validator_does_not_authorize_execution = true",
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
    "positive_control_must_remain_passing = true",
    "negative_fixtures_must_remain_fail_closed = true",
    "public_safe_static_fixture_set_must_remain = true",
    "metadata_contract_baseline_must_remain = true",
    "documentation_only_mapping_baseline_must_remain = true",
    "documentation_only_hardening_scope_must_remain = true",
    "read_only_harnesses_must_remain = true",
    "validator_output_must_not_become_authority = true",
    "model_output_must_not_become_authority = true",
    "runtime_execution_must_remain_unauthorized = true",
    "scanner_execution_must_remain_unauthorized = true",
    "docker_execution_must_remain_unauthorized = true",
    "credential_injection_must_remain_unauthorized = true",
    "customer_target_operation_must_remain_unauthorized = true",
    "delivery_must_remain_unauthorized = true",
    "aaef_handback_category_applied_implementation = true",
    "aaef_core_promotion = false",
    "aaef_profile_promotion = false",
    "aaef_practical_package_promotion = false",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"malformed JSON: {path.relative_to(ROOT)}: {exc}") from exc


def require_text(path: Path, expected: list[str]) -> str:
    require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    for item in expected:
        require(item in text, f"{path.relative_to(ROOT)} missing expected text: {item}")
    return text


def main() -> int:
    require(V0678_DOC.exists(), "v0.6.78 relationship planning document must exist")
    require(V0676_DOC.exists(), "v0.6.76 next-gap selection document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: candidate",
            "It is a relationship candidate checkpoint only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not reorganize files.",
            "It does not edit `run_all_local_checks.py` beyond registering this read-only candidate test.",
            "It does not start Applied Evidence implementation work.",
            "It does not generate new Applied Evidence packages.",
            "It does not generate private review records.",
            "It does not promote new public samples.",
            "It does not refine sanitized public sample content.",
            "It does not change public example text.",
            "It does not create a new reviewer walkthrough.",
            "It does not prepare AAEF main handback material.",
            "v0.6.80 Public Sample Relationship-to-Validator Review and Close-Readiness",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.79 document missing candidate flag: {flag}")

    for section in [
        "## 1. Scope and non-goals",
        "## 2. Public sample purpose",
        "## 3. Public validator purpose",
        "## 4. What the public validator checks and does not check",
        "## 5. Public negative fixture relationship",
        "## 6. Validator output is not authority",
        "## 7. Documentation-only mapping boundary",
        "## 8. Non-execution and non-delivery boundary",
        "## 9. Relationship matrix",
        "## 10. Candidate acceptance checks",
    ]:
        require(section in doc_text, f"v0.6.79 document missing relationship section: {section}")

    for phrase in [
        "The public sample is a sanitized, static, public-safe evidence-interface example.",
        "The public validator is a structural validator for public examples.",
        "Validator success means the public example passed the current structural checks.",
        "Validator success does not mean execution is authorized.",
        "Public negative fixtures are synthetic, static, public-safe fail-closed examples.",
        "Negative fixture categories can help organize reviewer understanding, but the mapping remains documentation-only",
        "It does not add `expected_failure_category`.",
        "It does not create JSON Schema.",
        "A validator result can support structural review.",
        "It does not authorize a tool, scanner, runtime, Docker container, credential, target, customer operation, or report delivery.",
    ]:
        require(phrase in doc_text, f"v0.6.79 document missing relationship phrase: {phrase}")

    for phrase in [
        "What is the public sample for?",
        "What does the public validator check?",
        "What does the public validator not check?",
        "How do negative fixtures relate?",
        "Is validator output authority?",
        "Does validator success authorize execution?",
        "Does documentation-only mapping change validator output?",
    ]:
        require(phrase in doc_text, f"v0.6.79 document missing relationship matrix question: {phrase}")

    for phrase in [
        "Candidate preserves the current public sample content",
        "Candidate preserves current validator behavior",
        "Candidate explains what the public sample is for",
        "Candidate explains what the public validator checks",
        "Candidate explains what the public validator does not check",
        "Candidate explains how negative fixtures relate to validator posture",
        "Candidate states validator output is not authority",
        "Candidate states validator success does not authorize execution",
        "Candidate states documentation-only failure category mapping is not validator output",
        "Candidate states documentation-only failure category mapping is not a validator output contract",
        "Candidate preserves runtime/scanner/Docker/credential/customer/delivery prohibitions",
        "Candidate avoids certification, compliance, legal, audit, and equivalence claims",
        "Candidate does not prepare AAEF main handback material",
        "Candidate remains documentation-only",
    ]:
        require(phrase in doc_text, f"v0.6.79 document missing candidate acceptance check: {phrase}")

    for phrase in [
        "vulnerability detection",
        "diagnostic completeness",
        "live execution evidence",
        "runtime authorization",
        "scanner authorization",
        "credential authorization",
        "customer-target authorization",
        "delivery authorization",
        "certification",
        "legal advice",
        "audit opinion",
        "compliance claim",
        "external-framework equivalence",
    ]:
        require(phrase in doc_text, f"v0.6.79 document missing validator boundary phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.79 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.79 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.79 document missing retained false boundary flag: {flag}")

    for phrase in [
        "whether this relationship candidate is close-ready",
        "whether to change the public sample",
        "whether to change validator behavior",
        "whether to add validator failure category output",
        "whether to create a validator output contract",
        "whether to refine the sanitized public sample",
        "whether to create a new reviewer walkthrough",
        "whether to prepare an AAEF main handback",
        "whether to generate a new static/mock package",
        "whether to create a new private review record",
        "whether to promote a new public sample",
        "whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed",
    ]:
        require(phrase in doc_text, f"v0.6.79 document missing unresolved decision phrase: {phrase}")

    v0678_text = V0678_DOC.read_text(encoding="utf-8")
    require(
        "public_sample_relationship_to_validator_planning_completed = true" in v0678_text,
        "v0.6.78 relationship planning must be completed",
    )
    require(
        "public_sample_relationship_to_validator_candidate_may_be_considered = true" in v0678_text,
        "v0.6.78 must allow relationship candidate consideration",
    )
    require(
        "public_sample_relationship_to_validator_validator_changed = false" in v0678_text,
        "v0.6.78 must not change validator",
    )
    require(
        "public_sample_relationship_to_validator_output_changed = false" in v0678_text,
        "v0.6.78 must not change validator output",
    )
    require(
        "public_sample_relationship_to_validator_contract_created = false" in v0678_text,
        "v0.6.78 must not create validator output contract",
    )
    require("validator_behavior_modified = false" in v0678_text, "v0.6.78 must preserve validator behavior boundary")

    v0676_text = V0676_DOC.read_text(encoding="utf-8")
    require(
        "applied_evidence_next_gap_selected_after_clarity_closeout = public_sample_relationship_to_validator" in v0676_text,
        "v0.6.76 must select public sample relationship to validator",
    )

    v0655_text = V0655_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_negative_fixture_track_consolidation_completed = true" in v0655_text,
        "v0.6.55 consolidation must be completed",
    )
    require("validator_behavior_modified = false" in v0655_text, "v0.6.55 must preserve validator behavior boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control")

    for category in EXPECTED_CATEGORIES:
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        require(metadata_path.exists(), f"metadata missing: {category}")
        metadata = load_json(metadata_path)

        for field in REQUIRED_METADATA_FIELDS:
            require(field in metadata, f"metadata field missing for {category}: {field}")

        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.79 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this relationship candidate provides certification",
        "this relationship candidate is legally sufficient",
        "this relationship candidate provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this relationship candidate",
        "runtime execution is authorized by this relationship candidate",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.79 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.79 public sample relationship-to-validator candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
