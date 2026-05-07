from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/129-v0652-public-validator-failure-category-mapping-readiness-review.md"
V0651_DOC = ROOT / "docs/128-v0651-public-validator-negative-fixture-metadata-contract-review-close-readiness.md"
V0650_DOC = ROOT / "docs/127-v0650-public-validator-negative-fixture-metadata-contract-candidate.md"
FIXTURE_ROOT = ROOT / "examples/applied-evidence/public-validator-negative-fixtures"
INDEX = FIXTURE_ROOT / "negative_fixture_index.example.json"
VALIDATOR = ROOT / "tools/validate_public_example_structure.py"

CATEGORY_TO_FAILURE = {
    "missing-package-artifact": "missing_required_package_artifact",
    "missing-scenario-artifact": "missing_required_scenario_artifact",
    "missing-scenario-directory": "missing_required_scenario_directory",
    "malformed-json": "malformed_json",
    "broken-linkage": "broken_evidence_linkage",
    "scenario-posture-contradiction": "scenario_posture_contradiction",
    "non-example-name": "non_example_or_unsafe_name",
    "missing-non-proof-statement": "missing_non_proof_statement",
    "missing-five-questions-mapping": "missing_five_questions_mapping",
    "hygiene-not-passed": "publication_hygiene_not_passed",
    "forbidden-text-leakage": "forbidden_text_leakage",
    "overclaim-language": "overclaim_language",
    "boundary-flag-violation": "boundary_flag_violation",
}

REQUIRED_DOC_FLAGS = [
    "failure_category_mapping_readiness_review_completed = true",
    "failure_category_mapping_candidate_may_be_considered = true",
    "failure_category_mapping_scope_defined = true",
    "failure_category_mapping_input_metadata_contract_closed = true",
    "failure_category_mapping_expected_categories_identified = true",
    "failure_category_mapping_candidate_names_identified = true",
    "failure_category_mapping_reviewer_facing_only = true",
    "failure_category_mapping_implementation_ready_for_later_checkpoint = true",
    "failure_category_mapping_implemented = false",
    "failure_category_mapping_validator_output_added = false",
    "failure_category_mapping_validator_behavior_modified = false",
    "failure_category_mapping_schema_added = false",
    "negative_fixture_metadata_rewritten = false",
    "negative_fixtures_added = false",
    "validator_behavior_modified = false",
    "validator_behavior_expansion_implemented = false",
    "runtime_execution_authorized = false",
    "scanner_execution_authorized = false",
    "docker_execution_authorized = false",
    "credential_injection_permitted = false",
    "customer_target_authorized = false",
    "delivery_authorized = false",
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
    require(V0651_DOC.exists(), "v0.6.51 metadata contract close-readiness document must exist")
    require(V0650_DOC.exists(), "v0.6.50 metadata contract candidate document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a readiness review only.",
            "It does not implement a failure category mapping.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not rewrite negative fixture metadata.",
            "v0.6.51 Public Validator Negative Fixture Metadata Contract Review and Close-Readiness",
            "v0.6.53 Public Validator Failure Category Mapping Candidate",
            "aaef_handback_category_applied_implementation = true",
            "aaef_core_promotion = false",
            "aaef_profile_promotion = false",
            "aaef_practical_package_promotion = false",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.52 document missing readiness flag: {flag}")

    for category, failure_category in CATEGORY_TO_FAILURE.items():
        require(f"`{category}`" in doc_text, f"v0.6.52 document missing negative category: {category}")
        require(f"`{failure_category}`" in doc_text, f"v0.6.52 document missing candidate failure category: {failure_category}")

    for option in [
        "Option A: Documentation-only mapping table",
        "Option B: Metadata-level mapping field",
        "Option C: Validator JSON output category names",
    ]:
        require(option in doc_text, f"v0.6.52 document missing future candidate option: {option}")

    v0651_text = V0651_DOC.read_text(encoding="utf-8")
    require("metadata_contract_track_close_ready = true" in v0651_text, "v0.6.51 must close metadata contract track before mapping readiness")
    require("close_public_validator_negative_fixture_metadata_contract_track = true" in v0651_text, "v0.6.51 must explicitly close the metadata contract track")
    require("validator_failure_category_mapping_started = false" in v0651_text, "v0.6.51 must not have started failure category mapping")
    require("validator_behavior_modified = false" in v0651_text, "v0.6.51 must preserve validator behavior boundary")

    v0650_text = V0650_DOC.read_text(encoding="utf-8")
    require("metadata_contract_candidate_added = true" in v0650_text, "v0.6.50 must add metadata contract candidate")
    require("metadata_contract_json_schema_added = false" in v0650_text, "v0.6.50 must avoid JSON Schema")
    require("validator_behavior_modified = false" in v0650_text, "v0.6.50 must preserve validator behavior boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")

    for category in CATEGORY_TO_FAILURE:
        fixture_dir = FIXTURE_ROOT / category
        metadata_path = fixture_dir / "negative_fixture_metadata.example.json"
        require(fixture_dir.exists(), f"fixture directory missing: {category}")
        require(metadata_path.exists(), f"metadata missing: {category}")
        metadata = load_json(metadata_path)
        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this mapping provides certification",
        "this mapping is legally sufficient",
        "this mapping provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this mapping",
        "runtime execution is authorized by this mapping",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.52 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.52 public validator failure category mapping readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
