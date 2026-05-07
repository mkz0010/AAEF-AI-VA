from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/131-v0654-public-validator-failure-category-mapping-review-close-readiness.md"
V0653_DOC = ROOT / "docs/130-v0653-public-validator-failure-category-mapping-candidate.md"
V0652_DOC = ROOT / "docs/129-v0652-public-validator-failure-category-mapping-readiness-review.md"
V0653_TEST = ROOT / "tools/test_v0653_public_validator_failure_category_mapping_candidate.py"
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
    "failure_category_mapping_candidate_review_completed = true",
    "failure_category_mapping_track_close_ready = true",
    "close_public_validator_failure_category_mapping_track = true",
    "retain_documentation_only_mapping_candidate = true",
    "retain_mapping_candidate_test = true",
    "failure_category_mapping_applies_to_existing_v0646_fixture_set = true",
    "failure_category_mapping_uses_v0651_metadata_contract_baseline = true",
    "failure_category_mapping_documentation_only = true",
    "failure_category_mapping_validator_output_added = false",
    "failure_category_mapping_validator_behavior_modified = false",
    "failure_category_mapping_metadata_field_added = false",
    "failure_category_mapping_fixture_metadata_rewritten = false",
    "failure_category_mapping_schema_added = false",
    "validator_json_output_changed = false",
    "validator_output_contract_created = false",
    "fixture_metadata_contract_changed = false",
    "fixture_metadata_rewritten = false",
    "new_fixture_category_added = false",
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
    require(V0653_DOC.exists(), "v0.6.53 mapping candidate document must exist")
    require(V0652_DOC.exists(), "v0.6.52 mapping readiness review document must exist")
    require(V0653_TEST.exists(), "v0.6.53 mapping candidate test must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a review and close-readiness checkpoint.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not rewrite negative fixture metadata.",
            "v0.6.53 Public Validator Failure Category Mapping Candidate",
            "v0.6.55 Public Validator Negative Fixture Track Consolidation Review",
            "aaef_handback_category_applied_implementation = true",
            "aaef_core_promotion = false",
            "aaef_profile_promotion = false",
            "aaef_practical_package_promotion = false",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.54 document missing close-readiness flag: {flag}")

    for category, failure_category in CATEGORY_TO_FAILURE.items():
        require(f"`{category}`" in doc_text, f"v0.6.54 document missing negative category: {category}")
        require(f"`{failure_category}`" in doc_text, f"v0.6.54 document missing failure category: {failure_category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for phrase in [
        "Keep mapping documentation-only",
        "Add metadata-level `expected_failure_category`",
        "Add validator JSON output category names",
        "Add JSON Schema for mapping",
        "Add new negative fixture categories",
    ]:
        require(phrase in doc_text, f"v0.6.54 document missing future guardrail phrase: {phrase}")

    v0653_text = V0653_DOC.read_text(encoding="utf-8")
    require(
        "failure_category_mapping_candidate_added = true" in v0653_text,
        "v0.6.53 must add mapping candidate",
    )
    require(
        "failure_category_mapping_documentation_only = true" in v0653_text,
        "v0.6.53 mapping must be documentation-only",
    )
    require(
        "failure_category_mapping_validator_output_added = false" in v0653_text,
        "v0.6.53 must not add validator output",
    )
    require(
        "failure_category_mapping_metadata_field_added = false" in v0653_text,
        "v0.6.53 must not add metadata field",
    )
    require("validator_behavior_modified = false" in v0653_text, "v0.6.53 must preserve validator behavior boundary")

    v0652_text = V0652_DOC.read_text(encoding="utf-8")
    require(
        "failure_category_mapping_candidate_may_be_considered = true" in v0652_text,
        "v0.6.52 must allow mapping candidate consideration",
    )
    require(
        "failure_category_mapping_implemented = false" in v0652_text,
        "v0.6.52 must not implement mapping",
    )

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")

    for category in CATEGORY_TO_FAILURE:
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        require(metadata_path.exists(), f"metadata missing: {category}")
        metadata = load_json(metadata_path)

        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.54 must not add metadata-level failure category: {category}")
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
        require(phrase not in lower_doc, f"v0.6.54 document must not include affirmative overclaim phrase: {phrase}")

    # Re-run the inherited documentation-only mapping candidate test so this close-readiness review is standalone.
    subprocess.run([sys.executable, V0653_TEST.as_posix()], cwd=ROOT, check=True)

    print("v0.6.54 public validator failure category mapping review and close-readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
