from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/153-v0676-applied-evidence-next-gap-selection-after-clarity-closeout.md"
V0675_DOC = ROOT / "docs/152-v0675-public-sample-five-questions-clarity-review-close-readiness.md"
V0674_DOC = ROOT / "docs/151-v0674-public-sample-five-questions-clarity-candidate.md"
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
    "applied_evidence_next_gap_selection_after_clarity_closeout_completed = true",
    "applied_evidence_next_gap_selection_after_clarity_closeout_is_documentation_only = true",
    "applied_evidence_next_gap_selection_after_clarity_closeout_uses_v0675_clarity_closeout = true",
    "applied_evidence_next_gap_selected_after_clarity_closeout = public_sample_relationship_to_validator",
    "applied_evidence_next_gap_requires_separate_checkpoint = true",
    "public_sample_relationship_to_validator_may_be_considered = true",
    "public_sample_relationship_to_validator_planning_may_be_considered = true",
    "public_sample_relationship_to_validator_started = false",
    "public_sample_relationship_to_validator_implemented = false",
    "public_sample_relationship_to_validator_validator_changed = false",
    "public_sample_relationship_to_validator_output_changed = false",
    "public_sample_relationship_to_validator_contract_created = false",
    "public_sample_relationship_to_validator_public_sample_changed = false",
    "public_sample_relationship_to_validator_sample_refined = false",
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
    "reviewer_navigation_note_retained = true",
    "public_negative_fixture_index_summary_retained = true",
    "v0675_clarity_closeout_retained = true",
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
    "runtime_execution_authorized = false",
    "scanner_execution_authorized = false",
    "docker_execution_authorized = false",
    "credential_injection_permitted = false",
    "customer_target_authorized = false",
    "delivery_authorized = false",
    "public_sample_relationship_to_validator_planning_only = true",
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
    require(V0675_DOC.exists(), "v0.6.75 clarity closeout document must exist")
    require(V0674_DOC.exists(), "v0.6.74 clarity candidate document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a next-gap selection review only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not reorganize files.",
            "It does not edit `run_all_local_checks.py` beyond registering this read-only selection review test.",
            "It does not start Applied Evidence implementation work.",
            "It does not generate new Applied Evidence packages.",
            "It does not generate private review records.",
            "It does not promote new public samples.",
            "It does not refine sanitized public sample content.",
            "It does not change public example text.",
            "It does not create a new reviewer walkthrough.",
            "It does not prepare AAEF main handback material.",
            "It does not start public sample relationship-to-validator implementation work.",
            "v0.6.77 Public Sample Relationship-to-Validator Planning",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.76 document missing selection flag: {flag}")

    for option in [
        "Public sample relationship to validator",
        "Evidence-interface handback readiness",
        "Static mock package refinement",
        "New public sample promotion",
        "New package generation",
        "Validator behavior implementation readiness",
        "Runtime/scanner/Docker/credential/customer/delivery work",
        "Pause",
    ]:
        require(option in doc_text, f"v0.6.76 document missing gap option: {option}")

    for phrase in [
        "what the public sample is for",
        "what the public validator checks",
        "what the public validator does not check",
        "how negative fixtures relate to validator posture",
        "why validator output is not authority",
        "why documentation-only failure category mapping is not validator output",
        "why validator checks do not create runtime authorization",
        "why validator checks do not prove diagnostic completeness",
        "why validator checks do not create certification, compliance, legal, audit, or equivalence claims",
    ]:
        require(phrase in doc_text, f"v0.6.76 document missing selected gap rationale phrase: {phrase}")

    for phrase in [
        "What does the validator check?",
        "What does the validator not check?",
        "How do negative fixtures relate to the validator?",
        "Is validator output authority?",
        "Does validator success authorize execution?",
        "Does the documentation-only failure category mapping change validator output?",
    ]:
        require(phrase in doc_text, f"v0.6.76 document missing relationship question: {phrase}")

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
        "The documentation-only failure category mapping remains documentation-only.",
        "It is not validator output and not a validator output contract.",
    ]:
        require(phrase in doc_text, f"v0.6.76 document missing validator boundary phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.76 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.76 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.76 document missing retained false boundary flag: {flag}")

    for phrase in [
        "the exact public sample relationship-to-validator wording",
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
        require(phrase in doc_text, f"v0.6.76 document missing unresolved decision phrase: {phrase}")

    v0675_text = V0675_DOC.read_text(encoding="utf-8")
    require(
        "public_sample_five_questions_clarity_review_completed = true" in v0675_text,
        "v0.6.75 clarity review must be completed",
    )
    require(
        "public_sample_five_questions_clarity_close_ready = true" in v0675_text,
        "v0.6.75 clarity candidate must be close-ready",
    )
    require(
        "public_sample_relationship_to_validator_started = false" in v0675_text,
        "v0.6.75 must not start relationship-to-validator work",
    )
    require(
        "public_sample_five_questions_clarity_public_sample_changed = false" in v0675_text,
        "v0.6.75 must not change public sample",
    )
    require("validator_behavior_modified = false" in v0675_text, "v0.6.75 must preserve validator behavior boundary")

    v0674_text = V0674_DOC.read_text(encoding="utf-8")
    require(
        "public_sample_five_questions_clarity_candidate_added = true" in v0674_text,
        "v0.6.74 clarity candidate must be added",
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
        require("expected_failure_category" not in metadata, f"v0.6.76 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this next-gap selection provides certification",
        "this next-gap selection is legally sufficient",
        "this next-gap selection provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this next-gap selection",
        "runtime execution is authorized by this next-gap selection",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.76 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.76 applied evidence next gap selection after clarity closeout tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
