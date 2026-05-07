from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/157-v0681-applied-evidence-next-gap-selection-after-relationship-closeout.md"
V0680_DOC = ROOT / "docs/156-v0680-public-sample-relationship-to-validator-review-close-readiness.md"
V0679_DOC = ROOT / "docs/155-v0679-public-sample-relationship-to-validator-candidate.md"
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
    "applied_evidence_next_gap_selection_after_relationship_closeout_completed = true",
    "applied_evidence_next_gap_selection_after_relationship_closeout_is_documentation_only = true",
    "applied_evidence_next_gap_selection_after_relationship_closeout_uses_v0680_relationship_closeout = true",
    "applied_evidence_next_gap_selected_after_relationship_closeout = evidence_interface_handback_readiness",
    "applied_evidence_next_gap_requires_separate_checkpoint = true",
    "evidence_interface_handback_readiness_may_be_considered = true",
    "evidence_interface_handback_readiness_planning_may_be_considered = true",
    "evidence_interface_handback_readiness_planning_only = true",
    "evidence_interface_handback_readiness_started = false",
    "evidence_interface_handback_readiness_implemented = false",
    "evidence_interface_handback_material_prepared = false",
    "aaef_main_handback_prepared = false",
    "aaef_main_handback_started = false",
    "aaef_main_handback_submitted = false",
    "aaef_core_promotion = false",
    "aaef_profile_promotion = false",
    "aaef_practical_package_promotion = false",
    "applied_evidence_implementation_started = false",
    "applied_evidence_package_generated = false",
    "applied_evidence_private_review_record_generated = false",
    "applied_evidence_public_sample_promoted = false",
    "applied_evidence_sanitized_public_sample_refined = false",
    "validator_behavior_modified = false",
    "validator_failure_category_output_added = false",
    "validator_json_output_changed = false",
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
    require(V0680_DOC.exists(), "v0.6.80 relationship closeout document must exist")
    require(V0679_DOC.exists(), "v0.6.79 relationship candidate document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a next-gap selection review only.",
            "It does not modify validator behavior.",
            "It does not create a validator output contract.",
            "It does not prepare AAEF main handback material.",
            "It does not start evidence-interface handback readiness planning.",
            "v0.6.82 Evidence-Interface Handback Readiness Planning",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.81 document missing selection flag: {flag}")

    for option in [
        "Evidence-interface handback readiness",
        "Static mock package refinement",
        "New public sample promotion",
        "New package generation",
        "Validator behavior implementation readiness",
        "Public validator behavior hardening implementation",
        "Runtime/scanner/Docker/credential/customer/delivery work",
        "Pause",
    ]:
        require(option in doc_text, f"v0.6.81 document missing gap option: {option}")

    for phrase in [
        "which lesson is evidence/interface-level only",
        "whether the lesson answers the AAEF five questions",
        "whether the lesson reinforces model-output-is-not-authority",
        "whether the lesson reinforces validator-output-is-not-authority",
        "whether the lesson preserves non-execution evidence",
        "whether the lesson avoids implementation details",
        "whether the lesson avoids patent-sensitive detail",
        "whether the lesson avoids private artifacts, scanner output, credentials, customer material, and delivery material",
        "whether the lesson avoids certification, compliance, legal, audit, or equivalence claims",
    ]:
        require(phrase in doc_text, f"v0.6.81 document missing selected gap rationale phrase: {phrase}")

    for phrase in [
        "Is there an evidence/interface-level lesson?",
        "Does the lesson answer the AAEF five questions?",
        "Does the lesson reinforce model-output-is-not-authority?",
        "Does the lesson reinforce validator-output-is-not-authority?",
        "Does the lesson preserve non-execution evidence?",
        "Does the lesson avoid sensitive material?",
        "Does the lesson avoid overclaims?",
    ]:
        require(phrase in doc_text, f"v0.6.81 document missing handback readiness question: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.81 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.81 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.81 document missing retained false boundary flag: {flag}")

    v0680_text = V0680_DOC.read_text(encoding="utf-8")
    require("public_sample_relationship_to_validator_review_completed = true" in v0680_text, "v0.6.80 relationship review must be completed")
    require("public_sample_relationship_to_validator_close_ready = true" in v0680_text, "v0.6.80 relationship candidate must be close-ready")
    require("evidence_interface_handback_readiness_started = false" in v0680_text, "v0.6.80 must not start evidence-interface handback readiness")
    require("applied_evidence_handback_prepared = false" in v0680_text, "v0.6.80 must not prepare handback material")
    require("validator_behavior_modified = false" in v0680_text, "v0.6.80 must preserve validator behavior boundary")

    v0679_text = V0679_DOC.read_text(encoding="utf-8")
    require("public_sample_relationship_to_validator_candidate_added = true" in v0679_text, "v0.6.79 relationship candidate must be added")

    v0655_text = V0655_DOC.read_text(encoding="utf-8")
    require("public_validator_negative_fixture_track_consolidation_completed = true" in v0655_text, "v0.6.55 consolidation must be completed")
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
        require("expected_failure_category" not in metadata, f"v0.6.81 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this next-gap selection provides certification",
        "this next-gap selection is legally sufficient",
        "this next-gap selection provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this next-gap selection",
        "runtime execution is authorized by this next-gap selection",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.81 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.81 applied evidence next gap selection after relationship closeout tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
