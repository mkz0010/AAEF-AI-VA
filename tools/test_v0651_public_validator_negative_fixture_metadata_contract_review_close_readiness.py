from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/128-v0651-public-validator-negative-fixture-metadata-contract-review-close-readiness.md"
V0650_DOC = ROOT / "docs/127-v0650-public-validator-negative-fixture-metadata-contract-candidate.md"
V0649_DOC = ROOT / "docs/126-v0649-public-validator-negative-fixture-metadata-contract-readiness-review.md"
V0650_TEST = ROOT / "tools/test_v0650_public_validator_negative_fixture_metadata_contract_candidate.py"
FIXTURE_ROOT = ROOT / "examples/applied-evidence/public-validator-negative-fixtures"
INDEX = FIXTURE_ROOT / "negative_fixture_index.example.json"
POSITIVE_CONTROL = ROOT / "examples/applied-evidence/sanitized-static-mock"

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
    "metadata_contract_candidate_review_completed = true",
    "metadata_contract_track_close_ready = true",
    "close_public_validator_negative_fixture_metadata_contract_track = true",
    "retain_metadata_contract_candidate = true",
    "retain_metadata_contract_test = true",
    "metadata_contract_applies_to_existing_v0646_fixture_set = true",
    "metadata_contract_schema_added = false",
    "metadata_contract_json_schema_added = false",
    "negative_fixture_metadata_rewritten = false",
    "negative_fixtures_added = false",
    "validator_behavior_modified = false",
    "validator_behavior_expansion_implemented = false",
    "validator_failure_category_mapping_started = false",
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
    require(V0650_DOC.exists(), "v0.6.50 metadata contract candidate document must exist")
    require(V0649_DOC.exists(), "v0.6.49 readiness review document must exist")
    require(V0650_TEST.exists(), "v0.6.50 contract test must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a review and close-readiness checkpoint.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not modify validator behavior.",
            "It does not start validator failure category mapping.",
            "v0.6.50 Public Validator Negative Fixture Metadata Contract Candidate",
            "v0.6.52 Public Validator Failure Category Mapping Readiness Review",
            "aaef_handback_category_applied_implementation = true",
            "aaef_core_promotion = false",
            "aaef_profile_promotion = false",
            "aaef_practical_package_promotion = false",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.51 document missing close-readiness flag: {flag}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.51 document must retain field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.51 document must retain false boundary flag: {flag}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.51 document must retain category: {category}")

    v0650_text = V0650_DOC.read_text(encoding="utf-8")
    require("metadata_contract_candidate_added = true" in v0650_text, "v0.6.50 must add metadata contract candidate")
    require("metadata_contract_test_added = true" in v0650_text, "v0.6.50 must add metadata contract test")
    require("metadata_contract_json_schema_added = false" in v0650_text, "v0.6.50 must avoid JSON Schema")
    require("validator_behavior_modified = false" in v0650_text, "v0.6.50 must not modify validator behavior")

    v0649_text = V0649_DOC.read_text(encoding="utf-8")
    require("metadata_contract_candidate_may_be_considered = true" in v0649_text, "v0.6.49 must allow candidate consideration")
    require("metadata_contract_implemented = false" in v0649_text, "v0.6.49 must be readiness-only")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control")

    for category in EXPECTED_CATEGORIES:
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        require(metadata_path.exists(), f"metadata missing: {category}")
        metadata = load_json(metadata_path)

        for field in REQUIRED_METADATA_FIELDS:
            require(field in metadata, f"required metadata field missing for {category}: {field}")

        require(metadata["negative_category"] == category, f"negative_category mismatch: {category}")
        require(metadata["expected_validator_result"] == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(isinstance(metadata["expected_blockers"], list) and metadata["expected_blockers"], f"expected blockers must remain non-empty: {category}")
        require(metadata["synthetic_public_safe_static_fixture"] is True, f"fixture must remain public-safe static: {category}")
        require(str(metadata["source_positive_control"]).endswith("sanitized-static-mock"), f"source positive control mismatch: {category}")

        boundary = metadata["runtime_boundary"]
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
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
        require(phrase not in lower_doc, f"v0.6.51 document must not include affirmative overclaim phrase: {phrase}")

    # Re-run the inherited read-only contract test so this close-readiness review is standalone.
    subprocess.run([sys.executable, V0650_TEST.as_posix()], cwd=ROOT, check=True)

    print("v0.6.51 public validator negative fixture metadata contract review and close-readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
