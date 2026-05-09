from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/193-v06117-narrow-public-safe-aaef-main-handback-human-submission-checklist-review-close-readiness.md"
V06116_DOC = ROOT / "docs/192-v06116-narrow-public-safe-aaef-main-handback-human-submission-checklist-preparation.md"
V06115_DOC = ROOT / "docs/191-v06115-narrow-public-safe-aaef-main-handback-exact-issue-submission-or-pause-decision.md"
V0655_DOC = ROOT / "docs/132-v0655-public-validator-negative-fixture-track-consolidation-review.md"
FIXTURE_ROOT = ROOT / "examples/applied-evidence/public-validator-negative-fixtures"
INDEX = FIXTURE_ROOT / "negative_fixture_index.example.json"
POSITIVE_CONTROL = ROOT / "examples/applied-evidence/sanitized-static-mock"
VALIDATOR = ROOT / "tools/validate_public_example_structure.py"

EXPECTED_CATEGORIES = ['missing-package-artifact', 'missing-scenario-artifact', 'missing-scenario-directory', 'malformed-json', 'broken-linkage', 'scenario-posture-contradiction', 'non-example-name', 'missing-non-proof-statement', 'missing-five-questions-mapping', 'hygiene-not-passed', 'forbidden-text-leakage', 'overclaim-language', 'boundary-flag-violation']
REQUIRED_FLAGS = ['narrow_public_safe_aaef_main_handback_human_submission_checklist_review_close_readiness_completed = true', 'narrow_public_safe_aaef_main_handback_human_submission_checklist_review_close_readiness_is_documentation_only = true', 'narrow_public_safe_aaef_main_handback_human_submission_checklist_review_close_readiness_uses_v06116_checklist = true', 'human_submission_checklist_review_completed = true', 'human_submission_checklist_close_ready = true', 'human_submission_checklist_internal_only = true', 'human_submission_checklist_public_safe = true', 'human_submission_checklist_submission_ready = false', 'human_submission_checklist_not_submitted = true', 'human_submission_checklist_not_issue_command = true', 'human_submission_checklist_not_issue_url = true', 'human_submission_checklist_not_handback_package = true', 'human_submission_checklist_requires_final_human_approval = true', 'human_submission_checklist_target_repo_confirmation_required = true', 'human_submission_checklist_exact_title_body_review_required = true', 'human_submission_checklist_label_milestone_manual_only = true', 'human_submission_checklist_public_safe_source_confirmation_required = true', 'human_submission_checklist_no_private_material_confirmation_required = true', 'human_submission_checklist_no_patent_sensitive_material_confirmation_required = true', 'human_submission_checklist_no_commercial_material_confirmation_required = true', 'human_submission_checklist_no_overclaim_confirmation_required = true', 'human_submission_checklist_aaef_five_questions_confirmation_required = true', 'human_submission_checklist_authority_boundary_confirmation_required = true', 'human_submission_checklist_non_execution_evidence_confirmation_required = true', 'human_submission_checklist_static_sample_boundary_confirmation_required = true', 'selected_next_step_after_human_submission_checklist_close_readiness = narrow_public_safe_aaef_main_handback_human_maintainer_final_submission_decision_or_pause', 'narrow_public_safe_aaef_main_handback_human_maintainer_final_submission_decision_or_pause_selected = true', 'narrow_public_safe_aaef_main_handback_human_maintainer_final_submission_decision_or_pause_authorized_for_next_checkpoint = true', 'narrow_public_safe_aaef_main_handback_exact_issue_submission_authorized_for_next_checkpoint = false', 'narrow_public_safe_aaef_main_handback_exact_issue_text_submitted = false', 'narrow_public_safe_aaef_main_handback_exact_issue_text_submission_ready = false', 'narrow_public_safe_aaef_main_handback_exact_issue_text_generated = true', 'narrow_public_safe_aaef_main_handback_exact_issue_text_internal_only = true', 'narrow_public_safe_aaef_main_handback_exact_pr_text_generated = false', 'narrow_public_safe_aaef_main_handback_pr_text_submission_ready = false', 'narrow_public_safe_aaef_main_handback_submission_ready = false', 'narrow_public_safe_aaef_main_handback_submission_selected = false', 'narrow_public_safe_aaef_main_handback_submission_started = false', 'narrow_public_safe_aaef_main_handback_submission_completed = false', 'exact_issue_text_candidate_close_ready = true', 'exact_issue_text_candidate_internal_only = true', 'exact_issue_text_candidate_submission_ready = false', 'exact_issue_text_candidate_submittable = false', 'exact_issue_text_candidate_not_submitted = true', 'exact_issue_text_candidate_not_opened_as_issue = true', 'human_approval_gate_required_before_issue_opening = true', 'human_maintainer_execution_required = true', 'ai_output_is_checklist_review_support_not_execution_authority = true', 'validator_output_is_not_authority = true', 'direct_submission_selected = false', 'direct_aaef_main_workflow_selected = false', 'aaef_main_direct_submission_selected = false', 'aaef_main_issue_direct_creation_selected = false', 'aaef_main_pr_direct_creation_selected = false', 'aaef_main_release_note_direct_drafting_selected = false', 'aaef_main_document_change_direct_drafting_selected = false', 'aaef_main_handback_package_direct_creation_selected = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_release_note_drafted = false', 'aaef_main_document_change_drafted = false', 'aaef_main_handback_package_created = false', 'aaef_main_issue_submission_executed = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'public_evaluation_package_boundary_retained = true', 'paid_or_nda_adoption_package_boundary_retained = true', 'two_layer_public_private_boundary_retained = true', 'aaef_main_handback_limited_to_evidence_interface_lessons = true', 'aaef_main_handback_excludes_adoption_package = true', 'aaef_main_handback_excludes_enterprise_runbooks = true', 'aaef_main_handback_excludes_customer_templates = true', 'aaef_main_handback_excludes_poc_detail_templates = true', 'aaef_main_handback_excludes_commercial_tool_gateway_detail = true', 'aaef_main_handback_excludes_pricing_contract_material = true', 'aaef_main_handback_excludes_delivery_authorization_material = true', 'aaef_main_handback_excludes_credential_handling_detail = true', 'aaef_main_handback_excludes_scanner_output = true', 'aaef_main_handback_excludes_private_artifacts = true', 'aaef_main_handback_excludes_patent_sensitive_detail = true', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'lesson_promotion_to_aaef_main_decided = false', 'candidate_identifies_only_evidence_interface_lessons = true', 'candidate_evaluates_aaef_five_questions = true', 'candidate_preserves_model_output_not_authority = true', 'candidate_preserves_validator_output_not_authority = true', 'candidate_preserves_non_execution_evidence_boundary = true', 'candidate_excludes_implementation_details = true', 'candidate_excludes_patent_sensitive_detail = true', 'candidate_excludes_private_artifacts = true', 'candidate_excludes_scanner_output = true', 'candidate_excludes_credentials = true', 'candidate_excludes_customer_material = true', 'candidate_excludes_delivery_material = true', 'candidate_excludes_runtime_authorization = true', 'candidate_excludes_overclaims = true', 'validator_behavior_modified = false', 'validator_failure_category_output_added = false', 'validator_json_output_changed = false', 'validator_output_contract_created = false', 'metadata_level_expected_failure_category_added = false', 'fixture_metadata_contract_changed = false', 'negative_fixture_metadata_rewritten = false', 'negative_fixtures_added = false', 'json_schema_added = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'readme_current_baseline_updated = false', 'security_reporting_channel_updated = false', 'authorization_expiry_now_check_added = false', 'constraint_diff_enforcement_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'handback_text_must_be_public_safe = true', 'handback_text_must_be_evidence_interface_level = true', 'handback_text_must_exclude_paid_or_nda_adoption_package = true', 'handback_text_must_not_open_aaef_main_issue = true', 'handback_text_must_not_open_aaef_main_pr = true', 'handback_text_must_not_submit_to_aaef_main = true']
REQUIRED_PHRASES = ['Status: review', 'It is a human submission checklist review and close-readiness checkpoint only.', 'This checkpoint reviews the human submission checklist and marks it close-ready.', 'It does not open an AAEF main issue.', 'It does not open an AAEF main pull request.', 'It does not submit anything to AAEF main.', 'It does not generate an issue creation command.', 'It does not create an issue URL.', 'The checklist remains internal-only.', 'The checklist remains not submission-ready.', 'Human submission checklist close-ready = true.', 'selected_next_step_after_human_submission_checklist_close_readiness = narrow_public_safe_aaef_main_handback_human_maintainer_final_submission_decision_or_pause', 'v0.6.118 Narrow Public-Safe AAEF Main Handback Human-Maintainer Final Submission Decision or Pause', 'Checklist review conclusion', 'Close-readiness review checklist', 'Close-ready checklist boundary', 'Only the human maintainer may open an AAEF main issue.', 'AI output is checklist review support, not execution authority.', 'Validator output may support structural review, but validator output is not authority.', 'No issue creation command is generated.', 'No issue URL is generated.', 'Submission remains unauthorized', 'Target repository confirmation reviewed', 'Exact issue title/body confirmation reviewed', 'Label and milestone handling confirmation reviewed', 'Public-safe source confirmation reviewed', 'Private and patent-sensitive material exclusion reviewed', 'Commercial and paid/NDA adoption package exclusion reviewed', 'Overclaim exclusion reviewed', 'AAEF five-questions confirmation reviewed', 'Authority boundary confirmation reviewed', 'Non-execution evidence confirmation reviewed', 'Static public sample boundary confirmation reviewed', 'Final human-only action boundary reviewed', 'public_safe_evidence_interface_boundary_lessons', 'Evidence answers the AAEF five questions.', 'AI output as request, not authority.', 'Validator output is not authority.', 'Static public samples are not live evidence.', 'README current/latest baseline clarity', 'SECURITY.md reporting-channel consistency', 'Authorization expiry checked against current time', 'Request/decision constraint-diff enforcement', 'Fail-closed handling for external_discovery=true', 'Mock/dry-run status terminology such as avoiding ambiguous `completed`', 'Enterprise Review Guide', 'Technical due diligence summary', 'Safe PoC boundary template', 'Control matrix', 'Reviewer walkthrough']


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    for path in [DOC, V06116_DOC, V06115_DOC, V0655_DOC, INDEX, VALIDATOR]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED_PHRASES + REQUIRED_FLAGS:
        require(phrase in doc_text, f"v0.6.117 document missing required text: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(category in doc_text, f"v0.6.117 document missing retained category: {category}")
        metadata = load_json(FIXTURE_ROOT / category / "negative_fixture_metadata.example.json")
        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.117 must not add metadata-level failure category: {category}")
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

    v06116 = V06116_DOC.read_text(encoding="utf-8")
    for phrase in [
        "narrow_public_safe_aaef_main_handback_human_submission_checklist_preparation_completed = true",
        "human_submission_checklist_prepared = true",
        "human_submission_checklist_internal_only = true",
        "human_submission_checklist_submission_ready = false",
        "human_submission_checklist_not_submitted = true",
        "human_submission_checklist_not_issue_command = true",
        "human_submission_checklist_not_issue_url = true",
        "human_submission_checklist_requires_final_human_approval = true",
        "selected_next_step_after_human_submission_checklist_preparation = narrow_public_safe_aaef_main_handback_human_submission_checklist_review_close_readiness",
        "narrow_public_safe_aaef_main_handback_human_submission_checklist_review_close_readiness_authorized_for_next_checkpoint = true",
        "narrow_public_safe_aaef_main_handback_exact_issue_submission_authorized_for_next_checkpoint = false",
        "aaef_main_issue_opened = false",
        "aaef_main_pull_request_opened = false",
        "aaef_main_issue_submission_command_generated = false",
        "aaef_main_issue_url_generated = false",
        "two_layer_public_private_boundary_retained = true",
        "aaef_main_handback_limited_to_evidence_interface_lessons = true",
        "validator_behavior_modified = false",
    ]:
        require(phrase in v06116, f"v0.6.116 baseline missing required phrase: {phrase}")

    v06115 = V06115_DOC.read_text(encoding="utf-8")
    require(
        "human_maintainer_only_submission_checklist_preparation_selected = true" in v06115,
        "v0.6.115 must select human-maintainer-only checklist preparation",
    )

    v0655 = V0655_DOC.read_text(encoding="utf-8")
    require("public_validator_negative_fixture_track_consolidation_completed = true" in v0655, "v0.6.55 consolidation must be completed")
    require("validator_behavior_modified = false" in v0655, "v0.6.55 must preserve validator behavior boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")

    lower_doc = doc_text.lower()
    for phrase in [
        "this checklist provides certification",
        "this checklist is legally sufficient",
        "this checklist provides an audit opinion",
        "this checklist submits to aaef main",
        "this checklist opens an aaef main issue",
        "scanner execution is authorized by this checklist",
        "runtime execution is authorized by this checklist",
    ]:
        require(phrase not in lower_doc, f"v0.6.117 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.117 narrow public-safe AAEF main handback human submission checklist review close-readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
