from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/133-v0656-public-validator-behavior-hardening-readiness-review.md"
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

REQUIRED_DOC_FLAGS = [
    "validator_behavior_hardening_readiness_review_completed = true",
    "validator_behavior_hardening_planning_may_be_considered = true",
    "validator_behavior_hardening_implementation_may_be_considered = false",
    "validator_behavior_hardening_scope_defined = false",
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
    "positive_control_must_remain_passing = true",
    "negative_fixtures_must_remain_fail_closed = true",
    "public_safe_static_fixture_set_must_remain = true",
    "metadata_contract_baseline_must_remain = true",
    "documentation_only_mapping_baseline_must_remain = true",
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
    require(V0655_DOC.exists(), "v0.6.55 consolidation review document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a readiness review only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not start validator behavior hardening implementation.",
            "v0.6.57 Public Validator Behavior Hardening Scope Planning",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.56 document missing readiness flag: {flag}")

    for category in EXPECTED_CATEGORIES:
        require(category in doc_text, f"v0.6.56 document missing hardening surface category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for phrase in [
        "Add validator JSON failure category output",
        "Add stable validator output contract",
        "Add metadata-level `expected_failure_category`",
        "Add JSON Schema for metadata or mapping",
        "Add new negative fixture categories",
        "Rewrite existing negative fixtures",
        "Reduce fixture duplication",
    ]:
        require(phrase in doc_text, f"v0.6.56 document missing implementation gate phrase: {phrase}")

    v0655_text = V0655_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_negative_fixture_track_consolidation_completed = true" in v0655_text,
        "v0.6.55 consolidation must be completed",
    )
    require(
        "negative_fixture_implementation_track_closed = true" in v0655_text,
        "v0.6.55 must close negative fixture implementation track",
    )
    require(
        "negative_fixture_metadata_contract_track_closed = true" in v0655_text,
        "v0.6.55 must close metadata contract track",
    )
    require(
        "failure_category_mapping_track_closed = true" in v0655_text,
        "v0.6.55 must close mapping track",
    )
    require("validator_behavior_modified = false" in v0655_text, "v0.6.55 must preserve validator behavior boundary")
    require(
        "validator_behavior_hardening_implementation_started = false" in v0655_text,
        "v0.6.55 must not start validator hardening implementation",
    )

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control")

    for category in EXPECTED_CATEGORIES:
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        require(metadata_path.exists(), f"metadata missing: {category}")
        metadata = load_json(metadata_path)

        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.56 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this hardening provides certification",
        "this hardening is legally sufficient",
        "this hardening provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this hardening",
        "runtime execution is authorized by this hardening",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.56 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.56 public validator behavior hardening readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
