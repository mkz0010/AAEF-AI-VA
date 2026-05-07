from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/125-v0648-public-validator-negative-fixture-coverage-hardening-planning.md"
V0647_DOC = ROOT / "docs/124-v0647-public-validator-negative-fixture-coverage-review-close-readiness.md"
V0646_DOC = ROOT / "docs/123-v0646-public-validator-negative-fixture-implementation-candidate.md"
FIXTURE_ROOT = ROOT / "examples/applied-evidence/public-validator-negative-fixtures"
POSITIVE_CONTROL = ROOT / "examples/applied-evidence/sanitized-static-mock"
INDEX = FIXTURE_ROOT / "negative_fixture_index.example.json"
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

REQUIRED_FLAGS = [
    "public_validator_negative_fixture_hardening_planning_completed = true",
    "negative_fixture_track_closed_before_hardening = true",
    "expected_blocker_metadata_contract_planned = true",
    "validator_failure_category_alignment_planned = true",
    "fixture_maintainability_review_planned = true",
    "positive_control_guardrail_planned = true",
    "publication_hygiene_guardrail_planned = true",
    "applied_implementation_handback_boundary_planned = true",
    "new_negative_fixtures_added = false",
    "existing_negative_fixtures_rewritten = false",
    "validator_behavior_modified = false",
    "validator_behavior_expansion_implemented = false",
    "runtime_execution_authorized = false",
    "scanner_execution_authorized = false",
    "docker_execution_authorized = false",
    "credential_injection_permitted = false",
    "customer_target_authorized = false",
    "delivery_authorized = false",
    "fixture_live_evidence = false",
    "docker_compose_executed = false",
    "container_started = false",
    "network_activity_allowed = false",
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


def find_index_category_entries(index: dict) -> list[dict]:
    lists: list[list] = []

    def walk(value):
        if isinstance(value, list):
            lists.append(value)
            for item in value:
                walk(item)
        elif isinstance(value, dict):
            for nested in value.values():
                walk(nested)

    walk(index)
    expected = set(EXPECTED_CATEGORIES)
    for values in lists:
        if not values or not all(isinstance(item, dict) for item in values):
            continue
        observed = set()
        for item in values:
            category = item.get("negative_category") or item.get("category") or item.get("fixture_category")
            if not category:
                category = str(item.get("fixture_id", "")).replace("v0646-", "")
            if category:
                observed.add(category)
        if expected.issubset(observed):
            return values
    raise AssertionError("negative fixture index must enumerate all expected categories")


def main() -> int:
    for path, label in [
        (DOC, "v0.6.48 planning document"),
        (V0647_DOC, "v0.6.47 close-readiness document"),
        (V0646_DOC, "v0.6.46 implementation candidate document"),
        (FIXTURE_ROOT, "negative fixture root"),
        (POSITIVE_CONTROL, "positive control"),
        (INDEX, "negative fixture index"),
        (VALIDATOR, "public example validator"),
    ]:
        require(path.exists(), f"missing {label}: {path.relative_to(ROOT)}")

    doc = DOC.read_text(encoding="utf-8")
    for marker in [
        "Status: planning",
        "It is a planning checkpoint only.",
        "It does not modify validator behavior.",
        "It does not add new negative fixtures.",
        "Expected blocker metadata contract",
        "Validator failure category alignment",
        "Fixture maintainability and size review",
        "Positive control guardrail",
        "Public-safety and publication hygiene guardrail",
        "Applied Implementation handback boundary",
        "v0.6.49: Public Validator Negative Fixture Metadata Contract Readiness Review",
    ] + REQUIRED_FLAGS:
        require(marker in doc, f"v0.6.48 document missing marker: {marker}")

    for category in EXPECTED_CATEGORIES:
        require(category in doc, f"v0.6.48 document must preserve category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    v0647 = V0647_DOC.read_text(encoding="utf-8")
    require("public_validator_negative_fixture_track_close_ready = true" in v0647, "v0.6.47 must be close-ready")
    require("close_public_validator_negative_fixture_track = true" in v0647, "v0.6.47 must close the first negative fixture track")
    require("validator_behavior_modified = false" in v0647, "v0.6.47 must preserve validator boundary")

    v0646 = V0646_DOC.read_text(encoding="utf-8")
    require("negative_fixture_count = 13" in v0646, "v0.6.46 must record 13 fixture count")
    require("validator_behavior_modified = false" in v0646, "v0.6.46 must preserve validator boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain the v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain synthetic public-safe static")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control pointer")
    validator_ref = str(index.get("validator_path") or index.get("validator") or "")
    require(validator_ref.endswith("validate_public_example_structure.py"), "index must preserve validator reference")
    require(len(find_index_category_entries(index)) >= 13, "index must still enumerate expected negative fixtures")

    for category in EXPECTED_CATEGORIES:
        metadata = load_json(FIXTURE_ROOT / category / "negative_fixture_metadata.example.json")
        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"fixture must still expect fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")
        require(isinstance(metadata.get("expected_blockers"), list) and metadata["expected_blockers"], f"fixture must retain expected blockers: {category}")
        boundary = metadata.get("runtime_boundary", {})
        require(isinstance(boundary, dict), f"fixture metadata must include runtime_boundary: {category}")
        for flag in [
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
        ]:
            require(boundary.get(flag) is False, f"fixture boundary flag must remain false for {category}: {flag}")

    forbidden = [
        "certified compliant",
        "legally sufficient",
        "production ready",
        "authorized for customer delivery",
        "scanner execution authorized",
        "runtime execution authorized",
    ]
    lower_doc = doc.lower()
    for phrase in forbidden:
        require(phrase not in lower_doc, f"v0.6.48 planning doc must not include overclaim phrase: {phrase}")

    print("v0.6.48 public validator negative fixture coverage hardening planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
