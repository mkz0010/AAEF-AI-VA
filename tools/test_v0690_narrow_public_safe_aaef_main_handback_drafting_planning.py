from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/166-v0690-narrow-public-safe-aaef-main-handback-drafting-planning.md"
V0689_DOC = ROOT / "docs/165-v0689-applied-evidence-handback-drafting-decision.md"
V0688_DOC = ROOT / "docs/164-v0688-narrow-public-safe-aaef-main-handback-preparation-review-close-readiness.md"
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
    "narrow_public_safe_aaef_main_handback_drafting_planning_completed = true",
    "narrow_public_safe_aaef_main_handback_drafting_planning_is_documentation_only = true",
    "narrow_public_safe_aaef_main_handback_drafting_planning_uses_v0689_decision = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_may_be_considered = true",
    "narrow_public_safe_aaef_main_handback_drafting_candidate_generated = false",
    "narrow_public_safe_aaef_main_handback_draft_generated = false",
    "aaef_main_handback_drafting_authorized_for_next_checkpoint = true",
    "aaef_main_handback_drafting_started = false",
    "aaef_main_handback_material_prepared = false",
    "aaef_main_handback_material_drafted = false",
    "aaef_main_handback_prepared = false",
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
    "evidence_interface_handback_readiness_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
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
    "public_sample_relationship_to_validator_close_ready_retained = true",
    "public_sample_relationship_to_validator_validator_changed = false",
    "public_sample_relationship_to_validator_output_changed = false",
    "public_sample_relationship_to_validator_contract_created = false",
    "public_sample_relationship_to_validator_public_sample_changed = false",
    "public_sample_relationship_to_validator_sample_refined = false",
    "public_sample_five_questions_clarity_close_ready_retained = true",
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
    "implementation_details = forbidden",
    "patent_sensitive_browser_state_or_diagnostic_reconstruction_detail = forbidden",
    "scanner_output = forbidden",
    "credential_material = forbidden",
    "private_generated_artifacts = forbidden",
    "private_review_records = forbidden",
    "runtime_authorization = forbidden",
    "delivery_authorization = forbidden",
    "diagnostic_completeness_claim = forbidden",
    "certification_claim = forbidden",
    "legal_advice_claim = forbidden",
    "audit_opinion_claim = forbidden",
    "compliance_claim = forbidden",
    "external_framework_equivalence_claim = forbidden",
    "public_negative_fixture_set_current = v0.6.46",
    "public_negative_fixture_count = 13",
    "public_negative_fixture_set_static = true",
    "public_negative_fixture_set_synthetic = true",
    "public_negative_fixture_set_public_safe = true",
    "public_negative_fixture_set_retained = true",
    "handback_drafting_candidate_must_be_public_safe = true",
    "handback_drafting_candidate_must_be_evidence_interface_level = true",
    "handback_drafting_candidate_must_exclude_implementation_details = true",
    "handback_drafting_candidate_must_exclude_patent_sensitive_detail = true",
    "handback_drafting_candidate_must_not_open_aaef_main_issue = true",
    "handback_drafting_candidate_must_not_open_aaef_main_pr = true",
    "handback_drafting_candidate_must_not_submit_to_aaef_main = true",
    "handback_drafting_candidate_must_not_prepare_release_notes = true",
    "handback_drafting_candidate_must_not_prepare_document_changes = true",
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
    require(V0689_DOC.exists(), "v0.6.89 handback drafting decision document must exist")
    require(V0688_DOC.exists(), "v0.6.88 handback preparation closeout document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: planning",
            "It is a drafting planning checkpoint only.",
            "It does not prepare AAEF main handback material.",
            "It does not open an AAEF main issue.",
            "It does not open an AAEF main pull request.",
            "It does not draft AAEF main release notes.",
            "It does not draft AAEF main document changes.",
            "It does not write AAEF main handback text.",
            "It does not create a handback package.",
            "It does not create a handback draft.",
            "It does not create a handback drafting candidate.",
            "v0.6.91 Narrow Public-Safe AAEF Main Handback Drafting Candidate",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.90 document missing planning flag: {flag}")

    for phrase in [
        "Target artifact shape for a future candidate",
        "Target audience planning",
        "Permitted wording families",
        "Forbidden wording families",
        "Drafting source boundaries",
        "Drafting review gates for a future candidate",
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
        "AAEF main maintainers",
        "AAEF reviewers",
        "AAEF framework readers",
        "AAEF-AI-VA maintainers",
    ]:
        require(phrase in doc_text, f"v0.6.90 document missing planning section, gate, or audience: {phrase}")

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
        "AAEF-AI-VA proves AAEF compliance",
        "AAEF-AI-VA certifies or validates AAEF",
        "AAEF-AI-VA is production-ready",
        "AAEF-AI-VA provides legal compliance",
        "AAEF-AI-VA provides audit opinion",
        "AAEF-AI-VA proves vulnerability detection completeness",
        "Public validator success authorizes execution",
        "Model output authorizes execution",
        "Public samples are live evidence",
        "Browser-state or diagnostic reconstruction detail",
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
        require(phrase in doc_text, f"v0.6.90 document missing wording/lesson/boundary phrase: {phrase}")

    for phrase in [
        "the exact AAEF main handback text",
        "whether any AAEF main handback material should be drafted",
        "whether any AAEF main issue, pull request, release note, or document should be opened or drafted",
        "whether any lesson should be promoted to AAEF main",
        "whether to create a handback package",
        "whether to create a handback draft",
        "whether to create a handback drafting candidate",
        "whether a handback drafting candidate is close-ready",
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
        require(phrase in doc_text, f"v0.6.90 document missing unresolved decision phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.90 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.90 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.90 document missing retained false boundary flag: {flag}")

    v0689 = V0689_DOC.read_text(encoding="utf-8")
    for phrase in [
        "applied_evidence_handback_drafting_decision_completed = true",
        "selected_next_step_after_handback_preparation_closeout = narrow_public_safe_aaef_main_handback_drafting_planning",
        "narrow_public_safe_aaef_main_handback_drafting_planning_selected = true",
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
        require(phrase in v0689, f"v0.6.89 baseline missing required phrase: {phrase}")

    v0688 = V0688_DOC.read_text(encoding="utf-8")
    require("narrow_public_safe_aaef_main_handback_preparation_close_ready = true" in v0688, "v0.6.88 preparation closeout must be close-ready")
    require("narrow_public_safe_aaef_main_handback_preparation_candidate_internal_only = true" in v0688, "v0.6.88 preparation candidate must remain internal")

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
        require("expected_failure_category" not in metadata, f"v0.6.90 must not add metadata-level failure category: {category}")
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
        require(phrase not in lower_doc, f"v0.6.90 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.90 narrow public-safe AAEF main handback drafting planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
