from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/168-v0692-narrow-public-safe-aaef-main-handback-drafting-candidate-review-close-readiness.md"
V0691_DOC = ROOT / "docs/167-v0691-narrow-public-safe-aaef-main-handback-drafting-candidate.md"
V0690_DOC = ROOT / "docs/166-v0690-narrow-public-safe-aaef-main-handback-drafting-planning.md"
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

REQUIRED_DOC_PHRASES = [
    "Status: review",
    "It is a review and close-readiness checkpoint only.",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_review_completed = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_close_ready = true",
    "close_narrow_public_safe_aaef_main_handback_drafting_candidate = true",
    "retain_v0691_narrow_public_safe_aaef_main_handback_drafting_candidate = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_retained = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_reviewed = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_scope_preserved = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_revision_required = false",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_replaced = false",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_uses_v0691_candidate = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_internal_only = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_reviewer_aid_retained = true",
    "narrow_public_safe_aaef_main_handback_draft_generated = false",
    "narrow_public_safe_aaef_main_handback_final_text_generated = false",
    "public_safe_evidence_interface_boundary_lessons_close_ready = true",
    "aaef_main_handback_material_preparation_may_be_considered = true",
    "aaef_main_handback_material_preparation_authorized_for_next_checkpoint = true",
    "aaef_main_handback_drafting_authorized_for_next_checkpoint = false",
    "aaef_main_handback_material_prepared = false",
    "aaef_main_handback_material_drafted = false",
    "aaef_main_handback_material_submitted = false",
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
    "public_sample_relationship_to_validator_public_sample_changed = false",
    "public_sample_relationship_to_validator_sample_refined = false",
    "public_sample_five_questions_clarity_sample_refined = false",
    "public_sample_five_questions_clarity_public_sample_changed = false",
    "applied_evidence_implementation_started = false",
    "applied_evidence_package_generated = false",
    "applied_evidence_private_review_record_generated = false",
    "applied_evidence_public_sample_promoted = false",
    "applied_evidence_sanitized_public_sample_refined = false",
    "applied_evidence_handback_prepared = false",
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
    "model_output_is_not_authority = true",
    "validator_output_is_not_authority = true",
    "validator_success_is_not_execution_permission = true",
    "gate_decision_remains_authority_relevant = true",
    "execution_authorization_requires_separate_gate_and_evidence = true",
    "handback_drafting_candidate_must_not_open_aaef_main_issue = true",
    "handback_drafting_candidate_must_not_open_aaef_main_pr = true",
    "handback_drafting_candidate_must_not_submit_to_aaef_main = true",
    "handback_drafting_candidate_must_not_prepare_release_notes = true",
    "handback_drafting_candidate_must_not_prepare_document_changes = true",
    "handback_drafting_candidate_must_not_write_final_text = true",
    "v0.6.93 Applied Evidence Handback Material Preparation Decision",
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
    require(DOC.exists(), "v0.6.92 document must exist")
    require(V0691_DOC.exists(), "v0.6.91 drafting candidate document must exist")
    require(V0690_DOC.exists(), "v0.6.90 drafting planning document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED_DOC_PHRASES:
        require(phrase in doc_text, f"v0.6.92 document missing expected phrase: {phrase}")

    for phrase in [
        "Internal drafting candidate packet",
        "Candidate target audience",
        "Candidate target artifact shape",
        "Candidate permitted wording families",
        "Candidate forbidden wording families",
        "Candidate source boundaries",
        "Candidate review gates",
        "Internal-only gate",
        "Public-safe source gate",
        "Evidence/interface scope gate",
        "AAEF five-questions gate",
        "Model-output-is-not-authority gate",
        "Validator-output-is-not-authority gate",
        "Non-execution evidence gate",
        "Static public sample gate",
        "Sensitive detail gate",
        "Private material gate",
        "Scanner/customer/credential gate",
        "Delivery gate",
        "Claim boundary gate",
        "Promotion gate",
        "AAEF main submission gate",
        "Final-text gate",
        "Candidate remains internal-only",
        "Candidate remains documentation-only",
        "Candidate does not prepare handback material",
        "Candidate does not open or draft AAEF main issue or PR content",
        "Candidate does not draft AAEF main release notes or document changes",
        "Candidate does not write final AAEF main handback text",
        "Candidate does not create handback package or draft",
        "Candidate does not promote AAEF Core/Profile/Practical Package content",
    ]:
        require(phrase in doc_text, f"v0.6.92 document missing close-readiness section or check: {phrase}")

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
        "They do not include live runtime evidence, scanner output, customer targets, credentials, private generated artifacts, delivery material, or diagnostic completeness claims.",
    ]:
        require(phrase in doc_text, f"v0.6.92 document missing retained lesson or boundary phrase: {phrase}")

    for phrase in [
        "the exact AAEF main handback text",
        "whether any AAEF main handback material should be drafted",
        "whether any AAEF main issue, pull request, release note, or document should be opened or drafted",
        "whether any lesson should be promoted to AAEF main",
        "whether to create a handback package",
        "whether to create a handback draft",
        "whether to create final handback text",
        "whether to draft release notes",
        "whether to draft document changes",
        "whether to change the public sample",
        "whether to change validator behavior",
        "whether to add validator failure category output",
        "whether to create a validator output contract",
        "whether to refine the sanitized public sample",
        "whether to create a new reviewer walkthrough",
        "whether to generate a new static/mock package",
        "whether to create a new private review record",
        "whether to promote a new public sample",
        "whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed",
    ]:
        require(phrase in doc_text, f"v0.6.92 document missing unresolved decision phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.92 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.92 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.92 document missing retained false boundary flag: {flag}")

    v0691 = V0691_DOC.read_text(encoding="utf-8")
    for phrase in [
        "narrow_public_safe_aaef_main_handback_drafting_candidate_added = true",
        "narrow_public_safe_aaef_main_handback_drafting_candidate_close_readiness_may_be_considered = true",
        "narrow_public_safe_aaef_main_handback_drafting_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
        "narrow_public_safe_aaef_main_handback_drafting_candidate_internal_only = true",
        "narrow_public_safe_aaef_main_handback_draft_generated = false",
        "narrow_public_safe_aaef_main_handback_final_text_generated = false",
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
        require(phrase in v0691, f"v0.6.91 baseline missing required phrase: {phrase}")

    v0690 = V0690_DOC.read_text(encoding="utf-8")
    require("narrow_public_safe_aaef_main_handback_drafting_planning_completed = true" in v0690, "v0.6.90 drafting planning must be completed")
    require("narrow_public_safe_aaef_main_handback_drafting_candidate_may_be_considered = true" in v0690, "v0.6.90 must allow drafting candidate consideration")

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
        require("expected_failure_category" not in metadata, f"v0.6.92 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    for phrase in [
        "this project is certified compliant",
        "this review provides certification",
        "this review is legally sufficient",
        "this review provides an audit opinion",
        "this review prepares aaef main handback material",
        "this review opens an aaef main issue",
        "scanner execution is authorized by this review",
        "runtime execution is authorized by this review",
    ]:
        require(phrase not in lower_doc, f"v0.6.92 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.92 narrow public-safe AAEF main handback drafting candidate review and close-readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
