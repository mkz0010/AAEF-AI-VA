from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/173-v0697-applied-evidence-handback-material-drafting-or-submission-decision.md"
V0696_DOC = ROOT / "docs/172-v0696-narrow-public-safe-aaef-main-handback-material-preparation-candidate-review-close-readiness.md"
V0695_DOC = ROOT / "docs/171-v0695-narrow-public-safe-aaef-main-handback-material-preparation-candidate.md"
V0655_DOC = ROOT / "docs/132-v0655-public-validator-negative-fixture-track-consolidation-review.md"
FIXTURE_ROOT = ROOT / "examples/applied-evidence/public-validator-negative-fixtures"
INDEX = FIXTURE_ROOT / "negative_fixture_index.example.json"
POSITIVE_CONTROL = ROOT / "examples/applied-evidence/sanitized-static-mock"
VALIDATOR = ROOT / "tools/validate_public_example_structure.py"

EXPECTED_CATEGORIES = [
    "missing-package-artifact", "missing-scenario-artifact", "missing-scenario-directory",
    "malformed-json", "broken-linkage", "scenario-posture-contradiction",
    "non-example-name", "missing-non-proof-statement", "missing-five-questions-mapping",
    "hygiene-not-passed", "forbidden-text-leakage", "overclaim-language",
    "boundary-flag-violation",
]

REQUIRED_FLAGS = [
    "applied_evidence_handback_material_drafting_or_submission_decision_completed = true",
    "applied_evidence_handback_material_drafting_or_submission_decision_is_documentation_only = true",
    "applied_evidence_handback_material_drafting_or_submission_decision_uses_v0696_close_readiness = true",
    "selected_next_step_after_material_preparation_closeout = narrow_public_safe_aaef_main_handback_text_drafting_planning",
    "narrow_public_safe_aaef_main_handback_text_drafting_planning_selected = true",
    "narrow_public_safe_aaef_main_handback_text_drafting_planning_started = false",
    "narrow_public_safe_aaef_main_handback_text_candidate_generated = false",
    "narrow_public_safe_aaef_main_handback_submittable_text_generated = false",
    "narrow_public_safe_aaef_main_handback_submission_selected = false",
    "aaef_main_direct_submission_selected = false",
    "aaef_main_issue_direct_creation_selected = false",
    "aaef_main_pr_direct_creation_selected = false",
    "aaef_main_release_note_direct_drafting_selected = false",
    "aaef_main_document_change_direct_drafting_selected = false",
    "aaef_main_handback_package_direct_creation_selected = false",
    "aaef_main_handback_material_preparation_close_ready_retained = true",
    "aaef_main_handback_material_preparation_candidate_internal_only = true",
    "aaef_main_handback_material_preparation_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
    "aaef_main_handback_material_prepared = false",
    "aaef_main_handback_material_drafted = false",
    "aaef_main_handback_material_submitted = false",
    "aaef_main_handback_material_package_created = false",
    "two_layer_public_private_boundary_retained = true",
    "public_repository_as_trust_proof_retained = true",
    "paid_or_nda_implementation_package_protected = true",
    "aaef_main_handback_limited_to_evidence_interface_lessons = true",
    "aaef_main_handback_excludes_adoption_package = true",
    "aaef_main_handback_excludes_enterprise_runbooks = true",
    "aaef_main_handback_excludes_customer_templates = true",
    "aaef_main_handback_excludes_poc_detail_templates = true",
    "aaef_main_handback_excludes_commercial_tool_gateway_detail = true",
    "aaef_main_handback_excludes_pricing_contract_material = true",
    "aaef_main_handback_excludes_delivery_authorization_material = true",
    "aaef_main_handback_excludes_credential_handling_detail = true",
    "aaef_main_handback_excludes_scanner_output = true",
    "aaef_main_handback_excludes_private_artifacts = true",
    "aaef_main_handback_excludes_patent_sensitive_detail = true",
    "aaef_main_issue_opened = false",
    "aaef_main_pull_request_opened = false",
    "aaef_main_release_note_drafted = false",
    "aaef_main_document_change_drafted = false",
    "aaef_main_handback_text_written = false",
    "aaef_main_handback_package_created = false",
    "aaef_core_promotion = false",
    "aaef_profile_promotion = false",
    "aaef_practical_package_promotion = false",
    "lesson_promotion_to_aaef_main_decided = false",
    "candidate_identifies_only_evidence_interface_lessons = true",
    "candidate_evaluates_aaef_five_questions = true",
    "candidate_preserves_model_output_not_authority = true",
    "candidate_preserves_validator_output_not_authority = true",
    "candidate_preserves_non_execution_evidence_boundary = true",
    "candidate_excludes_implementation_details = true",
    "candidate_excludes_patent_sensitive_detail = true",
    "candidate_excludes_private_artifacts = true",
    "candidate_excludes_scanner_output = true",
    "candidate_excludes_credentials = true",
    "candidate_excludes_customer_material = true",
    "candidate_excludes_delivery_material = true",
    "candidate_excludes_runtime_authorization = true",
    "candidate_excludes_overclaims = true",
    "validator_behavior_modified = false",
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
    "enterprise_review_guide_created = false",
    "technical_due_diligence_summary_created = false",
    "safe_poc_boundary_template_created = false",
    "control_matrix_created = false",
    "reviewer_walkthrough_created = false",
    "readme_current_baseline_updated = false",
    "security_reporting_channel_updated = false",
    "authorization_expiry_now_check_added = false",
    "constraint_diff_enforcement_added = false",
    "external_discovery_fail_closed_added = false",
    "mock_completed_status_renamed = false",
    "handback_text_must_be_public_safe = true",
    "handback_text_must_be_evidence_interface_level = true",
    "handback_text_must_exclude_paid_or_nda_adoption_package = true",
    "handback_text_must_not_open_aaef_main_issue = true",
    "handback_text_must_not_open_aaef_main_pr = true",
    "handback_text_must_not_submit_to_aaef_main = true",
    "handback_text_must_not_write_final_text = true",
    "handback_text_must_not_create_submittable_text = true",
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
    for path in [DOC, V0696_DOC, V0695_DOC, V0655_DOC, INDEX, VALIDATOR]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")

    doc_text = DOC.read_text(encoding="utf-8")
    required_phrases = [
        "Status: decision",
        "It is a drafting or submission decision checkpoint only.",
        "It does not prepare AAEF main handback material.",
        "It does not open an AAEF main issue.",
        "It does not open an AAEF main pull request.",
        "It does not draft AAEF main issue text.",
        "It does not draft AAEF main pull request text.",
        "It does not write AAEF main handback text.",
        "It does not write final AAEF main handback text.",
        "It does not create submittable handback text.",
        "v0.6.98 Narrow Public-Safe AAEF Main Handback Text Drafting Planning",
        "Direct submission to AAEF main is not selected.",
        "Direct AAEF main issue creation is not selected.",
        "Direct AAEF main pull request creation is not selected.",
        "Narrow public-safe AAEF main handback text drafting planning",
        "Direct AAEF main submission now",
        "Open AAEF main issue now",
        "Open AAEF main PR now",
        "target text shape",
        "permitted public-safe text families",
        "forbidden text families",
        "Retained two-layer publication boundary",
        "public_safe_evidence_interface_boundary_lessons",
        "Evidence answers the AAEF five questions",
        "AI output as request, not authority",
        "Gate decision decides execution permission",
        "Validator output is not authority",
        "Static public samples are not live evidence",
        "Who or what acted?",
        "On whose behalf?",
        "With what authority?",
        "Was the action allowed at execution?",
        "What evidence proves what happened?",
        "README current/latest baseline clarity",
        "SECURITY.md reporting-channel consistency",
        "Authorization expiry checked against current time",
        "Request/decision constraint-diff enforcement",
        "Fail-closed handling for external_discovery=true",
        "Mock/dry-run status terminology such as avoiding ambiguous `completed`",
        "Enterprise Review Guide",
        "Technical due diligence summary",
        "Safe PoC boundary template",
        "Control matrix",
        "Reviewer walkthrough",
    ]
    for phrase in required_phrases + REQUIRED_FLAGS:
        require(phrase in doc_text, f"v0.6.97 document missing required text: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(category in doc_text, f"v0.6.97 document missing retained category: {category}")
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        metadata = load_json(metadata_path)
        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.97 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in [
            "runtime_execution_authorized", "scanner_execution_authorized", "scan_execution_allowed",
            "credential_injection_permitted", "customer_target", "customer_target_authorized",
            "delivery_authorized", "customer_deliverable", "fixture_live_evidence",
            "validator_behavior_modified_by_fixture",
        ]:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    v0696 = V0696_DOC.read_text(encoding="utf-8")
    for phrase in [
        "narrow_public_safe_aaef_main_handback_material_preparation_candidate_review_completed = true",
        "narrow_public_safe_aaef_main_handback_material_preparation_candidate_close_ready = true",
        "aaef_main_handback_material_drafting_or_submission_decision_may_be_considered = true",
        "two_layer_public_private_boundary_retained = true",
        "aaef_main_handback_limited_to_evidence_interface_lessons = true",
        "aaef_main_handback_material_prepared = false",
        "aaef_main_issue_opened = false",
        "aaef_main_pull_request_opened = false",
        "aaef_main_handback_text_written = false",
        "aaef_main_handback_package_created = false",
        "validator_behavior_modified = false",
    ]:
        require(phrase in v0696, f"v0.6.96 baseline missing required phrase: {phrase}")

    v0695 = V0695_DOC.read_text(encoding="utf-8")
    require("narrow_public_safe_aaef_main_handback_material_preparation_candidate_added = true" in v0695, "v0.6.95 material preparation candidate must exist")

    v0655 = V0655_DOC.read_text(encoding="utf-8")
    require("public_validator_negative_fixture_track_consolidation_completed = true" in v0655, "v0.6.55 consolidation must be completed")
    require("validator_behavior_modified = false" in v0655, "v0.6.55 must preserve validator behavior boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")

    lower_doc = doc_text.lower()
    for phrase in [
        "this project is certified compliant",
        "this decision provides certification",
        "this decision is legally sufficient",
        "this decision provides an audit opinion",
        "this decision prepares aaef main handback material",
        "this decision opens an aaef main issue",
        "this decision writes final aaef main handback text",
        "this decision creates submittable text",
        "scanner execution is authorized by this decision",
        "runtime execution is authorized by this decision",
    ]:
        require(phrase not in lower_doc, f"v0.6.97 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.97 applied evidence handback material drafting or submission decision tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
