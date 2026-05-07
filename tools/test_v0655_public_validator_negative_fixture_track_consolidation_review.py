from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/132-v0655-public-validator-negative-fixture-track-consolidation-review.md"
PRIOR_DOCS = [
    ROOT / "docs/121-v0644-public-validator-negative-fixture-planning.md",
    ROOT / "docs/122-v0645-public-validator-negative-fixture-implementation-readiness-review.md",
    ROOT / "docs/123-v0646-public-validator-negative-fixture-implementation-candidate.md",
    ROOT / "docs/124-v0647-public-validator-negative-fixture-coverage-review-close-readiness.md",
    ROOT / "docs/125-v0648-public-validator-negative-fixture-coverage-hardening-planning.md",
    ROOT / "docs/126-v0649-public-validator-negative-fixture-metadata-contract-readiness-review.md",
    ROOT / "docs/127-v0650-public-validator-negative-fixture-metadata-contract-candidate.md",
    ROOT / "docs/128-v0651-public-validator-negative-fixture-metadata-contract-review-close-readiness.md",
    ROOT / "docs/129-v0652-public-validator-failure-category-mapping-readiness-review.md",
    ROOT / "docs/130-v0653-public-validator-failure-category-mapping-candidate.md",
    ROOT / "docs/131-v0654-public-validator-failure-category-mapping-review-close-readiness.md",
]

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

REQUIRED_DOC_FLAGS = [
    "public_negative_fixture_set_current = v0.6.46",
    "public_negative_fixture_count = 13",
    "public_negative_fixture_set_retained = true",
    "public_negative_fixture_set_static = true",
    "public_negative_fixture_set_synthetic = true",
    "public_negative_fixture_set_public_safe = true",
    "negative_fixture_implementation_track_closed = true",
    "negative_fixture_metadata_contract_track_closed = true",
    "failure_category_mapping_track_closed = true",
    "public_validator_negative_fixture_track_consolidation_completed = true",
    "retain_public_safe_static_negative_fixtures = true",
    "retain_negative_fixture_index = true",
    "retain_read_only_negative_fixture_harness = true",
    "retain_metadata_contract_candidate = true",
    "retain_metadata_contract_test = true",
    "retain_documentation_only_mapping_candidate = true",
    "retain_mapping_candidate_test = true",
    "retain_positive_control = true",
    "retain_public_example_structural_validator = true",
    "new_negative_fixtures_added = false",
    "existing_negative_fixtures_rewritten = false",
    "negative_fixture_metadata_rewritten = false",
    "metadata_contract_json_schema_added = false",
    "failure_category_mapping_schema_added = false",
    "metadata_level_expected_failure_category_added = false",
    "validator_failure_category_output_added = false",
    "validator_json_output_changed = false",
    "validator_output_contract_created = false",
    "validator_behavior_modified = false",
    "validator_behavior_expansion_implemented = false",
    "validator_behavior_hardening_implementation_started = false",
    "runtime_execution_authorized = false",
    "scanner_execution_authorized = false",
    "docker_execution_authorized = false",
    "credential_injection_permitted = false",
    "customer_target_authorized = false",
    "delivery_authorized = false",
    "aaef_handback_category_applied_implementation = true",
    "aaef_core_promotion = false",
    "aaef_profile_promotion = false",
    "aaef_practical_package_promotion = false",
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
    for path in PRIOR_DOCS:
        require(path.exists(), f"prior track document missing: {path.relative_to(ROOT)}")

    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "This checkpoint consolidates the public validator negative fixture track from v0.6.44 through v0.6.54.",
            "It is a consolidation review.",
            "It does not add new negative fixtures.",
            "It does not rewrite negative fixture metadata.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "v0.6.56 Public Validator Behavior Hardening Readiness Review",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.55 document missing consolidation flag: {flag}")

    for version in ["v0.6.44", "v0.6.45", "v0.6.46", "v0.6.47", "v0.6.48", "v0.6.49", "v0.6.50", "v0.6.51", "v0.6.52", "v0.6.53", "v0.6.54"]:
        require(version in doc_text, f"v0.6.55 document must mention consolidated version: {version}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.55 document missing category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for phrase in [
        "Add metadata-level `expected_failure_category`",
        "Add validator JSON output failure category names",
        "Add JSON Schema for metadata or mapping",
        "Add additional negative fixture categories",
        "Reduce fixture duplication or improve maintainability",
    ]:
        require(phrase in doc_text, f"v0.6.55 document missing future direction phrase: {phrase}")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control")

    for category in EXPECTED_CATEGORIES:
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        require(metadata_path.exists(), f"metadata missing: {category}")
        metadata = load_json(metadata_path)

        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.55 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this consolidation provides certification",
        "this consolidation is legally sufficient",
        "this consolidation provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this consolidation",
        "runtime execution is authorized by this consolidation",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.55 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.55 public validator negative fixture track consolidation review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
