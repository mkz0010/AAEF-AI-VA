from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/160-v0684-evidence-interface-handback-readiness-review-close-readiness.md"
V0683_DOC = ROOT / "docs/159-v0683-evidence-interface-handback-readiness-candidate.md"
V0682_DOC = ROOT / "docs/158-v0682-evidence-interface-handback-readiness-planning.md"
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
    "evidence_interface_handback_readiness_review_completed = true",
    "evidence_interface_handback_readiness_close_ready = true",
    "close_evidence_interface_handback_readiness_candidate = true",
    "retain_v0683_evidence_interface_handback_readiness_candidate = true",
    "evidence_interface_handback_readiness_candidate_retained = true",
    "evidence_interface_handback_readiness_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
    "public_safe_evidence_interface_boundary_lessons_close_ready = true",
    "evidence_interface_handback_material_prepared = false",
    "aaef_main_handback_prepared = false",
    "aaef_main_issue_opened = false",
    "aaef_main_pull_request_opened = false",
    "aaef_main_release_note_drafted = false",
    "aaef_main_document_change_drafted = false",
    "aaef_main_handback_text_written = false",
    "aaef_core_promotion = false",
    "aaef_profile_promotion = false",
    "aaef_practical_package_promotion = false",
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
    "public_sample_five_questions_clarity_close_ready_retained = true",
    "applied_evidence_implementation_started = false",
    "applied_evidence_package_generated = false",
    "applied_evidence_private_review_record_generated = false",
    "applied_evidence_public_sample_promoted = false",
    "applied_evidence_sanitized_public_sample_refined = false",
    "validator_behavior_modified = false",
    "validator_failure_category_output_added = false",
    "validator_output_contract_created = false",
    "metadata_level_expected_failure_category_added = false",
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
    "commercial_strategy = forbidden",
    "pricing_strategy = forbidden",
    "customer_material = forbidden",
    "customer_target_information = forbidden",
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
    "positive_control_must_remain_passing = true",
    "negative_fixtures_must_remain_fail_closed = true",
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


def require_text(path: Path, expected: list[str]) -> str:
    require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    for item in expected:
        require(item in text, f"{path.relative_to(ROOT)} missing expected text: {item}")
    return text


def main() -> int:
    require(V0683_DOC.exists(), "v0.6.83 handback readiness candidate document must exist")
    require(V0682_DOC.exists(), "v0.6.82 handback readiness planning document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a review and close-readiness checkpoint only.",
            "It does not prepare AAEF main handback material.",
            "It does not open an AAEF main issue.",
            "It does not open an AAEF main pull request.",
            "It does not write AAEF main handback text.",
            "It does not submit anything to AAEF main.",
            "v0.6.85 Applied Evidence Handback Preparation Decision",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.84 document missing close-readiness flag: {flag}")

    for phrase in [
        "Candidate remains readiness triage only",
        "Candidate does not prepare handback material",
        "Candidate does not open or draft AAEF main issue or PR content",
        "Candidate identifies only evidence/interface-level lessons",
        "Candidate evaluates the AAEF five questions",
        "Candidate preserves model-output-is-not-authority",
        "Candidate preserves validator-output-is-not-authority",
        "Candidate preserves non-execution evidence boundaries",
        "Candidate excludes implementation details",
        "Candidate excludes patent-sensitive detail",
        "Candidate excludes private artifacts and scanner output",
        "Candidate excludes credentials, customer material, and delivery material",
        "Candidate avoids certification, compliance, legal, audit, and equivalence claims",
        "Candidate preserves public sample, validator, fixture, package, and runtime boundaries",
        "Candidate remains documentation-only",
        "Evidence answers the AAEF five questions",
        "AI output as request, not authority",
        "Gate decision decides execution permission",
        "Dispatch and non-dispatch both need evidence",
        "Validator output is not authority",
        "Static public samples are not live evidence",
        "Reviewer traceability across request, decision, execution posture, and evidence",
        "Non-execution evidence remains meaningful",
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
        require(phrase in doc_text, f"v0.6.84 document missing required phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.84 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.84 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.84 document missing retained false boundary flag: {flag}")

    for phrase in [
        "whether any AAEF main handback material should be prepared",
        "whether any AAEF main issue, pull request, release note, or document should be opened or drafted",
        "whether any lesson should be promoted to AAEF main",
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
        require(phrase in doc_text, f"v0.6.84 document missing unresolved decision phrase: {phrase}")

    v0683 = V0683_DOC.read_text(encoding="utf-8")
    for phrase in [
        "evidence_interface_handback_readiness_candidate_added = true",
        "evidence_interface_handback_readiness_candidate_close_readiness_may_be_considered = true",
        "evidence_interface_handback_readiness_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons",
        "aaef_main_handback_prepared = false",
        "aaef_main_issue_opened = false",
        "aaef_main_pull_request_opened = false",
        "aaef_main_handback_text_written = false",
        "validator_behavior_modified = false",
    ]:
        require(phrase in v0683, f"v0.6.83 baseline missing required phrase: {phrase}")

    v0682 = V0682_DOC.read_text(encoding="utf-8")
    require("evidence_interface_handback_readiness_planning_completed = true" in v0682, "v0.6.82 planning must be completed")

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
        require("expected_failure_category" not in metadata, f"v0.6.84 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    for phrase in [
        "this project is certified compliant",
        "this close-readiness review provides certification",
        "this close-readiness review is legally sufficient",
        "this close-readiness review provides an audit opinion",
        "this close-readiness review prepares aaef main handback material",
        "this review opens an aaef main issue",
        "scanner execution is authorized by this close-readiness review",
        "runtime execution is authorized by this close-readiness review",
    ]:
        require(phrase not in lower_doc, f"v0.6.84 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.84 evidence-interface handback readiness review and close-readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
