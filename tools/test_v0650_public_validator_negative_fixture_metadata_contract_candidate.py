from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/127-v0650-public-validator-negative-fixture-metadata-contract-candidate.md"
V0649_DOC = ROOT / "docs/126-v0649-public-validator-negative-fixture-metadata-contract-readiness-review.md"
V0648_DOC = ROOT / "docs/125-v0648-public-validator-negative-fixture-coverage-hardening-planning.md"
V0646_DOC = ROOT / "docs/123-v0646-public-validator-negative-fixture-implementation-candidate.md"
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

NON_AUTHORIZATION_FRAGMENTS = [
    "does not authorize runtime execution",
    "scanner execution",
    "Docker execution",
    "credential injection",
    "customer-target operation",
    "delivery",
]

REQUIRED_DOC_FLAGS = [
    "metadata_contract_candidate_added = true",
    "metadata_contract_documented = true",
    "metadata_contract_test_added = true",
    "metadata_contract_applies_to_public_negative_fixtures = true",
    "metadata_contract_applies_to_existing_v0646_fixture_set = true",
    "metadata_contract_schema_added = false",
    "metadata_contract_json_schema_added = false",
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
    require(V0649_DOC.exists(), "v0.6.49 readiness review document must exist before v0.6.50")
    require(V0648_DOC.exists(), "v0.6.48 hardening planning document must exist before v0.6.50")
    require(V0646_DOC.exists(), "v0.6.46 implementation candidate document must exist before v0.6.50")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(VALIDATOR.exists(), "public example validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: candidate",
            "This document is a candidate contract.",
            "This checkpoint does not modify validator behavior.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not add a JSON Schema file.",
            "v0.6.49 Public Validator Negative Fixture Metadata Contract Readiness Review",
            "v0.6.51 Public Validator Negative Fixture Metadata Contract Review and Close-Readiness",
            "aaef_handback_category_applied_implementation = true",
            "aaef_core_promotion = false",
            "aaef_profile_promotion = false",
            "aaef_practical_package_promotion = false",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"contract candidate document missing flag: {flag}")

    for field in REQUIRED_METADATA_FIELDS:
        require(f"`{field}`" in doc_text, f"contract candidate must document required field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"contract candidate must document false boundary flag: {flag}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"contract candidate must document expected category: {category}")

    v0649_text = V0649_DOC.read_text(encoding="utf-8")
    require(
        "metadata_contract_candidate_may_be_considered = true" in v0649_text,
        "v0.6.49 must authorize consideration of a contract candidate",
    )
    require("metadata_contract_implemented = false" in v0649_text, "v0.6.49 must not already implement the contract")
    require("validator_behavior_modified = false" in v0649_text, "v0.6.49 must preserve validator behavior boundary")

    v0648_text = V0648_DOC.read_text(encoding="utf-8")
    require(
        "expected_blocker_metadata_contract_planned = true" in v0648_text,
        "v0.6.48 must plan expected blocker metadata contract",
    )

    v0646_text = V0646_DOC.read_text(encoding="utf-8")
    require("negative_fixture_count = 13" in v0646_text, "v0.6.46 must retain 13 negative fixtures")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control")

    observed_categories = set()
    for category in EXPECTED_CATEGORIES:
        fixture_dir = FIXTURE_ROOT / category
        metadata_path = fixture_dir / "negative_fixture_metadata.example.json"

        require(fixture_dir.exists(), f"fixture directory missing: {category}")
        require(metadata_path.exists(), f"metadata missing: {category}")

        metadata = load_json(metadata_path)
        observed_categories.add(metadata.get("negative_category"))

        for field in REQUIRED_METADATA_FIELDS:
            require(field in metadata, f"required metadata field missing for {category}: {field}")

        require(metadata["negative_category"] == category, f"negative_category mismatch: {category}")
        require(metadata["expected_validator_result"] == "fail_closed", f"expected_validator_result must be fail_closed: {category}")
        require(isinstance(metadata["expected_blockers"], list) and metadata["expected_blockers"], f"expected_blockers must be non-empty list: {category}")
        require(metadata["synthetic_public_safe_static_fixture"] is True, f"synthetic_public_safe_static_fixture must be true: {category}")
        require(str(metadata["source_positive_control"]).endswith("sanitized-static-mock"), f"source_positive_control must point to positive control: {category}")

        statement = metadata["non_authorization_statement"]
        require(isinstance(statement, str) and statement.strip(), f"non_authorization_statement must be non-empty: {category}")
        for fragment in NON_AUTHORIZATION_FRAGMENTS:
            require(fragment in statement, f"non_authorization_statement missing fragment for {category}: {fragment}")

        boundary = metadata["runtime_boundary"]
        require(isinstance(boundary, dict), f"runtime_boundary must be object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(flag in boundary, f"runtime_boundary missing flag for {category}: {flag}")
            require(boundary[flag] is False, f"runtime_boundary flag must be false for {category}: {flag}")

    require(set(EXPECTED_CATEGORIES).issubset(observed_categories), "all expected categories must be represented in metadata")

    lower_doc = doc_text.lower()
    # Check only unambiguous affirmative overclaim phrasings. The document is
    # allowed to mention certification, legal sufficiency, audit sufficiency,
    # production readiness, and delivery in explicit non-claim / denial contexts.
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this contract provides certification",
        "this contract is legally sufficient",
        "this contract provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this contract",
        "runtime execution is authorized by this contract",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"contract candidate must not include affirmative overclaim phrase: {phrase}")

    required_denial_phrases = [
        "the project is production ready",
        "the project provides certification",
    ]
    for phrase in required_denial_phrases:
        require(phrase in lower_doc, f"contract candidate should retain explicit non-claim context for: {phrase}")

    print("v0.6.50 public validator negative fixture metadata contract candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
