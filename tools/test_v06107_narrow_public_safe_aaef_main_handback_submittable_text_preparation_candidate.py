from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/183-v06107-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate.md"
V06106_DOC = ROOT / "docs/182-v06106-narrow-public-safe-aaef-main-handback-submittable-text-preparation-planning.md"
V06105_DOC = ROOT / "docs/181-v06105-applied-evidence-handback-submittable-text-or-pause-decision.md"
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

REQUIRED_DOC_TEXT = [
    "Status: candidate",
    "It is a submittable text preparation candidate checkpoint only.",
    "It does not open an AAEF main issue.",
    "It does not open an AAEF main pull request.",
    "It does not submit anything to AAEF main.",
    "v0.6.108 Narrow Public-Safe AAEF Main Handback Submittable Text Preparation Candidate Review and Close-Readiness",
    "Internal submittable text candidate packet",
    "Internal submittable text candidate",
    "The following text is an internal submittable text candidate only.",
    "Proposed public-safe AAEF main handback text candidate",
    "AAEF-AI-VA provides a narrow Applied Implementation lesson",
    "The lesson is that evidence can preserve the distinction between AI-generated requests and execution authority.",
    "AI output is a request, not authority.",
    "Validator output can support structural review, but validator output is not authority.",
    "This lesson maps to the AAEF five questions",
    "Dispatch and non-dispatch both benefit from evidence.",
    "Static public samples are orientation artifacts",
    "This is ready for direct AAEF main submission.",
    "This opens the AAEF main issue.",
    "Non-submission gate",
    "AAEF main workflow gate",
    "public_safe_evidence_interface_boundary_lessons",
    "Evidence answers the AAEF five questions.",
    "Validator output is not authority.",
    "Static public samples are not live evidence.",
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

REQUIRED_FLAGS = [
    "narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate_added = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate_is_documentation_only = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate_uses_v06106_planning = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_generated = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_internal_only = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_submittable = false",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_submission_ready = false",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_not_submitted = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_close_readiness_may_be_considered = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
    "narrow_public_safe_aaef_main_handback_submittable_text_generated = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_internal_only = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_submittable = false",
    "narrow_public_safe_aaef_main_handback_submittable_text_submission_ready = false",
    "narrow_public_safe_aaef_main_handback_submission_selected = false",
    "narrow_public_safe_aaef_main_handback_submission_started = false",
    "aaef_main_issue_opened = false",
    "aaef_main_pull_request_opened = false",
    "aaef_main_release_note_drafted = false",
    "aaef_main_document_change_drafted = false",
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
    "metadata_level_expected_failure_category_added = false",
    "negative_fixtures_added = false",
    "json_schema_added = false",
    "runtime_execution_authorized = false",
    "scanner_execution_authorized = false",
    "docker_execution_authorized = false",
    "credential_injection_permitted = false",
    "customer_target_authorized = false",
    "delivery_authorized = false",
    "handback_text_must_be_public_safe = true",
    "handback_text_must_be_evidence_interface_level = true",
    "handback_text_must_exclude_implementation_details = true",
    "handback_text_must_exclude_patent_sensitive_detail = true",
    "handback_text_must_exclude_paid_or_nda_adoption_package = true",
    "handback_text_must_not_open_aaef_main_issue = true",
    "handback_text_must_not_open_aaef_main_pr = true",
    "handback_text_must_not_submit_to_aaef_main = true",
]

BASELINE_06106 = [
    "narrow_public_safe_aaef_main_handback_submittable_text_preparation_planning_completed = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_may_be_considered = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_generated = false",
    "aaef_main_handback_submittable_text_candidate_authorized_for_next_checkpoint = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_internal_only = true",
    "narrow_public_safe_aaef_main_handback_submittable_text_candidate_submittable = false",
    "narrow_public_safe_aaef_main_handback_submittable_text_generated = false",
    "narrow_public_safe_aaef_main_handback_submittable_text_submission_ready = false",
    "direct_submission_selected = false",
    "aaef_main_direct_submission_selected = false",
    "aaef_main_issue_direct_creation_selected = false",
    "aaef_main_pr_direct_creation_selected = false",
    "two_layer_public_private_boundary_retained = true",
    "aaef_main_handback_limited_to_evidence_interface_lessons = true",
    "validator_behavior_modified = false",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    for path in [DOC, V06106_DOC, V06105_DOC, V0655_DOC, INDEX, VALIDATOR]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED_DOC_TEXT + REQUIRED_FLAGS:
        require(phrase in doc_text, f"v0.6.107 document missing required text: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(category in doc_text, f"v0.6.107 document missing retained category: {category}")
        metadata = load_json(FIXTURE_ROOT / category / "negative_fixture_metadata.example.json")
        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.107 must not add metadata-level failure category: {category}")
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

    v06106 = V06106_DOC.read_text(encoding="utf-8")
    for phrase in BASELINE_06106:
        require(phrase in v06106, f"v0.6.106 baseline missing required phrase: {phrase}")

    v06105 = V06105_DOC.read_text(encoding="utf-8")
    require(
        "selected_next_step_after_final_text_candidate_closeout = narrow_public_safe_aaef_main_handback_submittable_text_preparation_planning" in v06105,
        "v0.6.105 must select submittable text preparation planning",
    )

    v0655 = V0655_DOC.read_text(encoding="utf-8")
    require("public_validator_negative_fixture_track_consolidation_completed = true" in v0655, "v0.6.55 consolidation must be completed")
    require("validator_behavior_modified = false" in v0655, "v0.6.55 must preserve validator behavior boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")

    lower_doc = doc_text.lower()
    for phrase in [
        "this project is certified compliant",
        "this candidate provides certification",
        "this candidate is legally sufficient",
        "this candidate provides an audit opinion",
        "this candidate is submitted to aaef main",
        "scanner execution is authorized by this candidate",
        "runtime execution is authorized by this candidate",
    ]:
        require(phrase not in lower_doc, f"v0.6.107 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.107 narrow public-safe AAEF main handback submittable text preparation candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
