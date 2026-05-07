from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/143-v0666-applied-evidence-next-direction-intake.md"
V0665_DOC = ROOT / "docs/142-v0665-public-validator-pause-review-closeout.md"
V0664_DOC = ROOT / "docs/141-v0664-public-validator-maintenance-pause-next-direction-review.md"
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
    "applied_evidence_next_direction_intake_completed = true",
    "applied_evidence_next_direction_selected = applied_evidence_current_state_review",
    "applied_evidence_next_direction_requires_separate_checkpoint = true",
    "applied_evidence_current_state_review_may_be_considered = true",
    "applied_evidence_current_state_review_started = false",
    "applied_evidence_implementation_started = false",
    "applied_evidence_package_generated = false",
    "applied_evidence_private_review_record_generated = false",
    "applied_evidence_public_sample_promoted = false",
    "applied_evidence_fixture_rewrite_approved = false",
    "applied_evidence_schema_change_approved = false",
    "public_validator_pause_closeout_retained = true",
    "public_validator_track_pause_state_retained = true",
    "public_validator_maintenance_continue_now = false",
    "validator_behavior_hardening_implementation_readiness_deferred = true",
    "public_validator_behavior_hardening_implementation_not_approved = true",
    "documentation_only_hardening_scope_retained = true",
    "reviewer_navigation_note_retained = true",
    "public_negative_fixture_index_summary_retained = true",
    "v0665_pause_closeout_retained = true",
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
    "public_validator_pause_review_closeout_completed = true",
    "public_validator_pause_state_closed = true",
    "public_validator_next_direction_selected = applied_evidence_next_direction_intake",
    "public_validator_next_direction_requires_separate_checkpoint = true",
    "continue_public_validator_maintenance_now = false",
    "prepare_validator_behavior_implementation_readiness_now = false",
    "public_negative_fixture_set_current = v0.6.46",
    "public_negative_fixture_count = 13",
    "public_negative_fixture_set_static = true",
    "public_negative_fixture_set_synthetic = true",
    "public_negative_fixture_set_public_safe = true",
    "public_negative_fixture_set_retained = true",
    "applied_evidence_private_artifact_copied_to_public = false",
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
    require(V0665_DOC.exists(), "v0.6.65 pause closeout document must exist")
    require(V0664_DOC.exists(), "v0.6.64 pause direction document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: intake",
            "It is an intake checkpoint only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not reorganize files.",
            "It does not edit `run_all_local_checks.py` beyond registering this read-only intake test.",
            "It does not start Applied Evidence implementation work.",
            "It does not generate new Applied Evidence packages.",
            "It does not generate private review records.",
            "It does not promote new public samples.",
            "v0.6.67 Applied Evidence Current-State Review",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.66 document missing intake flag: {flag}")

    for option in [
        "Applied Evidence current-state review",
        "Static applied evidence package refinement",
        "Public reviewer walkthrough refinement",
        "Evidence-interface handback to AAEF main",
        "Public validator maintenance continuation",
        "Validator behavior implementation readiness",
        "Runtime, scanner, Docker, credential, customer-target, or delivery work",
    ]:
        require(option in doc_text, f"v0.6.66 document missing intake option: {option}")

    for surface in [
        "sanitized public sample baseline",
        "static mock applied evidence package",
        "five questions mapping",
        "reviewer walkthrough",
        "evidence-interface handback",
        "validator relationship",
        "non-execution boundary",
        "next candidate work",
    ]:
        require(surface in doc_text, f"v0.6.66 document missing review surface: {surface}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.66 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.66 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.66 document missing retained false boundary flag: {flag}")

    for phrase in [
        "what Applied Evidence package should be refined",
        "whether a new public sample should be promoted",
        "whether an evidence-interface handback to AAEF main should be prepared",
        "whether static mock package structure should be changed",
        "whether public reviewer walkthrough should be rewritten",
        "whether validator behavior should eventually be hardened",
        "whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed",
    ]:
        require(phrase in doc_text, f"v0.6.66 document missing unresolved decision phrase: {phrase}")

    v0665_text = V0665_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_pause_review_closeout_completed = true" in v0665_text,
        "v0.6.65 pause closeout must be completed",
    )
    require(
        "public_validator_next_direction_selected = applied_evidence_next_direction_intake" in v0665_text,
        "v0.6.65 must select Applied Evidence next-direction intake",
    )
    require(
        "It does not start Applied Evidence implementation work." in v0665_text,
        "v0.6.65 must not start Applied Evidence implementation work",
    )
    require("validator_behavior_modified = false" in v0665_text, "v0.6.65 must preserve validator behavior boundary")

    v0664_text = V0664_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_next_direction_selected = pause_and_reassess" in v0664_text,
        "v0.6.64 must select pause and reassess",
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
        require("expected_failure_category" not in metadata, f"v0.6.66 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this intake provides certification",
        "this intake is legally sufficient",
        "this intake provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this intake",
        "runtime execution is authorized by this intake",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.66 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.66 applied evidence next-direction intake tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
