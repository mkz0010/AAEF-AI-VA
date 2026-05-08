from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/169-v0693-applied-evidence-handback-material-preparation-decision.md"
V0692_DOC = ROOT / "docs/168-v0692-narrow-public-safe-aaef-main-handback-drafting-candidate-review-close-readiness.md"
V0691_DOC = ROOT / "docs/167-v0691-narrow-public-safe-aaef-main-handback-drafting-candidate.md"
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
    "applied_evidence_handback_material_preparation_decision_completed = true",
    "applied_evidence_handback_material_preparation_decision_is_documentation_only = true",
    "applied_evidence_handback_material_preparation_decision_uses_v0692_close_readiness = true",
    "selected_next_step_after_handback_drafting_closeout = narrow_public_safe_aaef_main_handback_material_preparation_planning",
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_selected = true",
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_may_be_considered = true",
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_started = false",
    "narrow_public_safe_aaef_main_handback_material_preparation_planning_implemented = false",
    "narrow_public_safe_aaef_main_handback_material_candidate_may_be_considered = true",
    "narrow_public_safe_aaef_main_handback_material_candidate_generated = false",
    "narrow_public_safe_aaef_main_handback_material_package_generated = false",
    "aaef_main_handback_material_preparation_authorized_for_next_checkpoint = true",
    "aaef_main_handback_material_preparation_started = false",
    "aaef_main_handback_material_prepared = false",
    "aaef_main_handback_material_drafted = false",
    "aaef_main_handback_material_submitted = false",
    "aaef_main_handback_material_package_created = false",
    "aaef_main_handback_drafting_candidate_close_ready_retained = true",
    "aaef_main_handback_drafting_candidate_retained = true",
    "aaef_main_handback_drafting_candidate_internal_only = true",
    "aaef_main_handback_drafting_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
    "aaef_main_handback_drafting_authorized_for_next_checkpoint = false",
    "aaef_main_handback_drafting_started = false",
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
    "public_sample_relationship_to_validator_validator_changed = false",
    "public_sample_relationship_to_validator_output_changed = false",
    "public_sample_relationship_to_validator_contract_created = false",
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
    "handback_material_must_be_public_safe = true",
    "handback_material_must_be_evidence_interface_level = true",
    "handback_material_must_exclude_implementation_details = true",
    "handback_material_must_exclude_patent_sensitive_detail = true",
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
    require(V0692_DOC.exists(), "v0.6.92 handback drafting candidate closeout document must exist")
    require(V0691_DOC.exists(), "v0.6.91 handback drafting candidate document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: decision",
            "It is a material preparation decision checkpoint only.",
            "It does not prepare AAEF main handback material.",
            "It does not open an AAEF main issue.",
            "It does not open an AAEF main pull request.",
            "It does not draft AAEF main release notes.",
            "It does not draft AAEF main document changes.",
            "It does not write AAEF main handback text.",
            "It does not create a handback package.",
            "It does not create a handback draft.",
            "It does not create final handback text.",
            "v0.6.94 Narrow Public-Safe AAEF Main Handback Material Preparation Planning",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.93 document missing decision flag: {flag}")

    for option in [
        "Narrow public-safe AAEF main handback material preparation planning",
        "Prepare AAEF main handback material now",
        "Open AAEF main issue now",
        "Open AAEF main PR now",
        "Draft AAEF main release notes now",
        "Draft AAEF main document changes now",
        "Create a handback package now",
        "Move to static mock package refinement",
        "Move to validator implementation",
        "Runtime/scanner/Docker/credential/customer/delivery work",
        "Pause",
    ]:
        require(option in doc_text, f"v0.6.93 document missing option review row: {option}")

    for phrase in [
        "target material shape",
        "target audience",
        "permitted public-safe lesson wording families",
        "forbidden wording families",
        "exact source boundaries",
        "material packaging boundaries",
        "review gates before any final text or AAEF main workflow",
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
        require(phrase in doc_text, f"v0.6.93 document missing retained phrase: {phrase}")

    for phrase in [
        "the exact AAEF main handback text",
        "whether any AAEF main handback material should be drafted",
        "whether any AAEF main issue, pull request, release note, or document should be opened or drafted",
        "whether any lesson should be promoted to AAEF main",
        "whether to create a handback package",
        "whether to create a handback draft",
        "whether to create final handback text",
        "whether to prepare release notes",
        "whether to prepare document changes",
        "whether to create a material preparation candidate",
        "whether a material preparation candidate is close-ready",
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
        require(phrase in doc_text, f"v0.6.93 document missing unresolved decision phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(category in doc_text, f"v0.6.93 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.93 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.93 document missing retained false boundary flag: {flag}")

    v0692 = V0692_DOC.read_text(encoding="utf-8")
    for phrase in [
        "narrow_public_safe_aaef_main_handback_drafting_candidate_review_completed = true",
        "narrow_public_safe_aaef_main_handback_drafting_candidate_close_ready = true",
        "narrow_public_safe_aaef_main_handback_drafting_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
        "narrow_public_safe_aaef_main_handback_drafting_candidate_internal_only = true",
        "aaef_main_handback_material_preparation_may_be_considered = true",
        "aaef_main_handback_material_preparation_authorized_for_next_checkpoint = true",
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
        require(phrase in v0692, f"v0.6.92 baseline missing required phrase: {phrase}")

    v0691 = V0691_DOC.read_text(encoding="utf-8")
    require("narrow_public_safe_aaef_main_handback_drafting_candidate_added = true" in v0691, "v0.6.91 drafting candidate must exist")

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
        require("expected_failure_category" not in metadata, f"v0.6.93 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    for phrase in [
        "this project is certified compliant",
        "this decision provides certification",
        "this decision is legally sufficient",
        "this decision provides an audit opinion",
        "this decision prepares aaef main handback material",
        "this decision opens an aaef main issue",
        "scanner execution is authorized by this decision",
        "runtime execution is authorized by this decision",
    ]:
        require(phrase not in lower_doc, f"v0.6.93 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.93 applied evidence handback material preparation decision tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
