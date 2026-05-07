from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/145-v0668-applied-evidence-gap-prioritization-review.md"
V0667_DOC = ROOT / "docs/144-v0667-applied-evidence-current-state-review.md"
V0666_DOC = ROOT / "docs/143-v0666-applied-evidence-next-direction-intake.md"
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
    "applied_evidence_gap_prioritization_review_completed = true",
    "applied_evidence_gap_prioritization_is_documentation_only = true",
    "applied_evidence_gap_prioritization_uses_v0667_current_state_review = true",
    "applied_evidence_first_gap_selected = applied_evidence_reviewer_current_state_summary",
    "applied_evidence_second_gap_candidate = public_sample_five_questions_clarity",
    "applied_evidence_gap_prioritization_requires_separate_checkpoint = true",
    "applied_evidence_reviewer_current_state_summary_may_be_considered = true",
    "applied_evidence_reviewer_current_state_summary_started = false",
    "applied_evidence_public_sample_five_questions_clarity_started = false",
    "applied_evidence_current_state_summary_generated = false",
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
    "v0667_current_state_review_retained = true",
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
    "applied_evidence_reviewer_current_state_summary_planning_only = true",
    "applied_evidence_reviewer_current_state_summary_generated = false",
    "applied_evidence_public_sample_refined = false",
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
    require(V0667_DOC.exists(), "v0.6.67 current-state review document must exist")
    require(V0666_DOC.exists(), "v0.6.66 intake document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a gap prioritization review only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not reorganize files.",
            "It does not edit `run_all_local_checks.py` beyond registering this read-only prioritization test.",
            "It does not start Applied Evidence implementation work.",
            "It does not generate new Applied Evidence packages.",
            "It does not generate private review records.",
            "It does not promote new public samples.",
            "It does not refine sanitized public sample content.",
            "v0.6.69 Applied Evidence Reviewer Current-State Summary Planning",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.68 document missing prioritization flag: {flag}")

    for item in [
        "Applied Evidence reviewer current-state summary",
        "Public sample five-questions clarity",
        "Public sample relationship to validator",
        "Evidence-interface handback readiness",
        "Static mock package refinement",
        "New public sample promotion",
        "New package generation",
        "Runtime/scanner/Docker/credential/customer/delivery work",
        "what Applied Evidence artifacts exist today",
        "what is public-safe versus private history",
        "what the public sample is intended to demonstrate",
        "what the public validator checks",
        "what the public validator does not check",
    ]:
        require(item in doc_text, f"v0.6.68 document missing gap/prioritization phrase: {item}")

    for question in [
        "Who or what acted?",
        "On whose behalf?",
        "With what authority?",
        "Was the action allowed at execution?",
        "What evidence proves what happened?",
    ]:
        require(question in doc_text, f"v0.6.68 document missing AAEF question: {question}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.68 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.68 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.68 document missing retained false boundary flag: {flag}")

    for phrase in [
        "the exact content of an Applied Evidence reviewer current-state summary",
        "whether to refine the sanitized public sample",
        "whether to generate a new static/mock package",
        "whether to create a new private review record",
        "whether to promote a new public sample",
        "whether to prepare an AAEF main handback",
        "whether validator behavior should eventually be hardened",
        "whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed",
    ]:
        require(phrase in doc_text, f"v0.6.68 document missing unresolved decision phrase: {phrase}")

    v0667_text = V0667_DOC.read_text(encoding="utf-8")
    require(
        "applied_evidence_current_state_review_completed = true" in v0667_text,
        "v0.6.67 current-state review must be completed",
    )
    require(
        "applied_evidence_gap_review_may_be_considered = true" in v0667_text,
        "v0.6.67 must allow gap review consideration",
    )
    require(
        "applied_evidence_implementation_started = false" in v0667_text,
        "v0.6.67 must not start Applied Evidence implementation",
    )
    require("validator_behavior_modified = false" in v0667_text, "v0.6.67 must preserve validator behavior boundary")

    v0666_text = V0666_DOC.read_text(encoding="utf-8")
    require(
        "applied_evidence_next_direction_selected = applied_evidence_current_state_review" in v0666_text,
        "v0.6.66 must select current-state review",
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
        require("expected_failure_category" not in metadata, f"v0.6.68 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this prioritization review provides certification",
        "this prioritization review is legally sufficient",
        "this prioritization review provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this prioritization review",
        "runtime execution is authorized by this prioritization review",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.68 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.68 applied evidence gap prioritization review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
