from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/170-v0694-narrow-public-safe-aaef-main-handback-material-preparation-planning.md"
V0693_DOC = ROOT / "docs/169-v0693-applied-evidence-handback-material-preparation-decision.md"
V0692_DOC = ROOT / "docs/168-v0692-narrow-public-safe-aaef-main-handback-drafting-candidate-review-close-readiness.md"
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
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_completed = true",
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_is_documentation_only = true",
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_uses_v0693_decision = true",
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_started = true",
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_implemented = false",
    "narrow_public_safe_aaef_main_handback_material_candidate_may_be_considered = true",
    "narrow_public_safe_aaef_main_handback_material_candidate_generated = false",
    "narrow_public_safe_aaef_main_handback_material_candidate_close_readiness_may_be_considered = true",
    "narrow_public_safe_aaef_main_handback_material_package_generated = false",
    "narrow_public_safe_aaef_main_handback_material_final_text_generated = false",
    "aaef_main_handback_material_preparation_authorized_for_next_checkpoint = true",
    "aaef_main_handback_material_preparation_started = false",
    "aaef_main_handback_material_prepared = false",
    "aaef_main_handback_material_drafted = false",
    "aaef_main_handback_material_submitted = false",
    "aaef_main_handback_material_package_created = false",
    "public_evaluation_package_boundary_retained = true",
    "paid_or_nda_adoption_package_boundary_retained = true",
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
    "aaef_main_handback_drafting_candidate_close_ready_retained = true",
    "aaef_main_handback_drafting_candidate_internal_only = true",
    "aaef_main_handback_drafting_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
    "narrow_public_safe_aaef_main_handback_draft_generated = false",
    "narrow_public_safe_aaef_main_handback_final_text_generated = false",
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
    "public_safe_evidence_interface_boundary_lessons_close_ready = true",
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
    "model_output_is_not_authority = true",
    "validator_output_is_not_authority = true",
    "validator_success_is_not_execution_permission = true",
    "gate_decision_remains_authority_relevant = true",
    "execution_authorization_requires_separate_gate_and_evidence = true",
    "handback_material_must_be_public_safe = true",
    "handback_material_must_be_evidence_interface_level = true",
    "handback_material_must_exclude_implementation_details = true",
    "handback_material_must_exclude_patent_sensitive_detail = true",
    "handback_material_must_exclude_paid_or_nda_adoption_package = true",
    "handback_material_must_not_open_aaef_main_issue = true",
    "handback_material_must_not_open_aaef_main_pr = true",
    "handback_material_must_not_submit_to_aaef_main = true",
    "handback_material_must_not_prepare_release_notes = true",
    "handback_material_must_not_prepare_document_changes = true",
    "handback_material_must_not_write_final_text = true",
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
    require(V0693_DOC.exists(), "v0.6.93 handback material preparation decision document must exist")
    require(V0692_DOC.exists(), "v0.6.92 drafting candidate closeout document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: planning",
            "It is a material preparation planning checkpoint only.",
            "It does not prepare AAEF main handback material.",
            "It does not start AAEF main handback work.",
            "It does not open an AAEF main issue.",
            "It does not open an AAEF main pull request.",
            "It does not draft AAEF main release notes.",
            "It does not draft AAEF main document changes.",
            "It does not write AAEF main handback text.",
            "It does not submit anything to AAEF main.",
            "It does not create a handback package.",
            "It does not create a handback draft.",
            "It does not create final handback text.",
            "It does not create a handback material preparation candidate.",
            "v0.6.95 Narrow Public-Safe AAEF Main Handback Material Preparation Candidate",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.94 document missing planning flag: {flag}")

    for phrase in [
        "Two-layer publication boundary",
        "Target material shape for a future candidate",
        "Material source boundaries",
        "Material preparation review gates for a future candidate",
        "public_evaluation_package = allowed",
        "paid_or_nda_adoption_package = protected",
        "aaef_main_handback = evidence_interface_lessons_only",
        "implementation_adoption_know_how = excluded",
        "Safe executable demo",
        "Boundary design",
        "Simplified control matrix",
        "Simplified enterprise overview",
        "Not-production-scanner boundary",
        "Diagnostic-company PoC plan details",
        "Customer explanation templates",
        "Deployment decision checklists",
        "Integration workflow details",
        "Human review runbooks",
        "Commercial Tool Gateway implementation details",
        "Pricing, contracts, and responsibility boundary material",
        "Commercial license terms",
        "Two-layer boundary gate",
        "Commercial/adoption know-how gate",
    ]:
        require(phrase in doc_text, f"v0.6.94 document missing two-layer or planning phrase: {phrase}")

    for phrase in [
        "Evidence answers the AAEF five questions",
        "AI output as request, not authority",
        "Gate decision decides execution permission",
        "Dispatch and non-dispatch both need evidence",
        "Validator output is not authority",
        "Static public samples are not live evidence",
        "Reviewer traceability across request, decision, execution posture, and evidence",
        "Non-execution evidence remains meaningful",
        "AAEF-AI-VA is an Applied Implementation example",
        "Who or what acted?",
        "On whose behalf?",
        "With what authority?",
        "Was the action allowed at execution?",
        "What evidence proves what happened?",
        "blocked action evidence",
        "denied action evidence",
        "human-review-required evidence",
        "non-dispatched action evidence",
        "reviewer traceability evidence",
        "evidence that a request did not become an authorized execution",
    ]:
        require(phrase in doc_text, f"v0.6.94 document missing retained lesson or boundary phrase: {phrase}")

    for phrase in [
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
    ]:
        require(phrase in doc_text, f"v0.6.94 document missing deferred external review item: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(category in doc_text, f"v0.6.94 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.94 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.94 document missing retained false boundary flag: {flag}")

    v0693 = V0693_DOC.read_text(encoding="utf-8")
    for phrase in [
        "applied_evidence_handback_material_preparation_decision_completed = true",
        "selected_next_step_after_handback_drafting_closeout = narrow_public_safe_aaef_main_handback_material_preparation_planning",
        "narrow_public_safe_aaef_main_handback_material_preparation_planning_selected = true",
        "aaef_main_handback_material_prepared = false",
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
        "validator_behavior_modified = false",
    ]:
        require(phrase in v0693, f"v0.6.93 baseline missing required phrase: {phrase}")

    v0692 = V0692_DOC.read_text(encoding="utf-8")
    require("narrow_public_safe_aaef_main_handback_drafting_candidate_close_ready = true" in v0692, "v0.6.92 drafting candidate must be close-ready")
    require("aaef_main_handback_material_preparation_authorized_for_next_checkpoint = true" in v0692, "v0.6.92 must allow material preparation consideration")

    v0655 = V0655_DOC.read_text(encoding="utf-8")
    require("public_validator_negative_fixture_track_consolidation_completed = true" in v0655, "v0.6.55 consolidation must be completed")
    require("validator_behavior_modified = false" in v0655, "v0.6.55 must preserve validator behavior boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control")

    for category in EXPECTED_CATEGORIES:
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        metadata = load_json(metadata_path)
        for field in REQUIRED_METADATA_FIELDS:
            require(field in metadata, f"metadata field missing for {category}: {field}")
        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.94 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    for phrase in [
        "this project is certified compliant",
        "this planning provides certification",
        "this planning is legally sufficient",
        "this planning provides an audit opinion",
        "this planning prepares aaef main handback material",
        "this planning opens an aaef main issue",
        "scanner execution is authorized by this planning",
        "runtime execution is authorized by this planning",
    ]:
        require(phrase not in lower_doc, f"v0.6.94 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.94 narrow public-safe AAEF main handback material preparation planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
