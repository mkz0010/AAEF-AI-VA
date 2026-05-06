from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/124-v0647-public-validator-negative-fixture-coverage-review-close-readiness.md"
PREVIOUS_DOC = ROOT / "docs/123-v0646-public-validator-negative-fixture-implementation-candidate.md"
FIXTURE_ROOT = ROOT / "examples/applied-evidence/public-validator-negative-fixtures"
POSITIVE_CONTROL = ROOT / "examples/applied-evidence/sanitized-static-mock"
INDEX = FIXTURE_ROOT / "negative_fixture_index.example.json"
V0646_HARNESS = ROOT / "tools/test_v0646_public_validator_negative_fixture_implementation_candidate.py"
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

REQUIRED_FALSE_BOUNDARY_FLAGS = [
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
        raise AssertionError(f"malformed JSON: {path}: {exc}") from exc


def require_text(path: Path, expected: list[str]) -> str:
    require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    for item in expected:
        require(item in text, f"{path.relative_to(ROOT)} missing expected text: {item}")
    return text


def find_list_with_categories(index: dict) -> list[dict]:
    candidates: list[list] = []

    def walk(value):
        if isinstance(value, list):
            candidates.append(value)
            for item in value:
                walk(item)
        elif isinstance(value, dict):
            for nested in value.values():
                walk(nested)

    walk(index)

    expected = set(EXPECTED_CATEGORIES)
    for candidate in candidates:
        if not candidate or not all(isinstance(item, dict) for item in candidate):
            continue
        observed = set()
        for item in candidate:
            category = (
                item.get("negative_category")
                or item.get("category")
                or item.get("fixture_category")
                or item.get("fixture_id", "").replace("v0646-", "")
            )
            if category:
                observed.add(category)
        if expected.issubset(observed):
            return candidate
    raise AssertionError("negative fixture index does not enumerate all expected categories")


def main() -> int:
    require(PREVIOUS_DOC.exists(), "v0.6.46 implementation candidate document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(V0646_HARNESS.exists(), "v0.6.46 read-only harness must exist")
    require(VALIDATOR.exists(), "public example structural validator must exist")

    doc_text = require_text(
        DOC,
        [
            "public_validator_negative_fixture_coverage_review_completed = true",
            "public_validator_negative_fixture_track_close_ready = true",
            "close_public_validator_negative_fixture_track = true",
            "retain_public_safe_static_negative_fixtures = true",
            "negative_fixture_count = 13",
            "positive_control_preserved = true",
            "validator_behavior_modified = false",
            "runtime_execution_authorized = false",
            "scanner_execution_authorized = false",
            "credential_injection_permitted = false",
            "customer_target_authorized = false",
            "delivery_authorized = false",
            "aaef_handback_category_applied_implementation = true",
            "aaef_core_promotion = false",
            "aaef_profile_promotion = false",
            "aaef_practical_package_promotion = false",
            "v0.6.48 Public Validator Negative Fixture Coverage Hardening Planning",
        ],
    )

    require(
        "does not modify validator behavior" in doc_text
        or "validator behavior is not modified" in doc_text,
        "v0.6.47 document must explicitly avoid validator behavior modification",
    )

    previous_text = PREVIOUS_DOC.read_text(encoding="utf-8")
    require("negative_fixture_count = 13" in previous_text, "v0.6.46 must record 13 negative fixtures")
    require("validator_behavior_modified = false" in previous_text, "v0.6.46 must preserve validator behavior boundary")

    index = load_json(INDEX)
    fixture_set_id = str(index.get("fixture_set_id", ""))
    require(fixture_set_id.startswith("v0646"), "fixture index must identify the v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "fixture index must mark fixtures as public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "fixture index must identify the positive control")
    validator_ref = str(index.get("validator_path") or index.get("validator") or "")
    require(validator_ref.endswith("validate_public_example_structure.py"), "fixture index must identify validator path")

    runtime_boundary = index.get("runtime_boundary", {})
    require(isinstance(runtime_boundary, dict), "fixture index must include runtime_boundary")
    for flag in REQUIRED_FALSE_BOUNDARY_FLAGS:
        if flag in runtime_boundary:
            require(runtime_boundary[flag] is False, f"index runtime boundary flag must be false: {flag}")

    index_entries = find_list_with_categories(index)
    require(len(index_entries) >= 13, "fixture index must enumerate at least the expected 13 fixtures")

    observed_dirs = sorted(p.name for p in FIXTURE_ROOT.iterdir() if p.is_dir())
    require(set(EXPECTED_CATEGORIES).issubset(set(observed_dirs)), "fixture root must contain all expected fixture categories")

    for category in EXPECTED_CATEGORIES:
        fixture_dir = FIXTURE_ROOT / category
        require(fixture_dir.exists(), f"missing fixture directory: {category}")

        metadata_path = fixture_dir / "negative_fixture_metadata.example.json"
        require(metadata_path.exists(), f"missing metadata for fixture: {category}")
        metadata = load_json(metadata_path)

        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"fixture must expect fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must be public-safe static: {category}")
        require(
            str(metadata.get("source_positive_control", "")).endswith("sanitized-static-mock"),
            f"fixture must identify positive control: {category}",
        )

        expected_blockers = metadata.get("expected_blockers")
        require(isinstance(expected_blockers, list) and expected_blockers, f"fixture must declare expected blockers: {category}")

        statement = metadata.get("non_authorization_statement", "")
        for fragment in [
            "does not authorize runtime execution",
            "scanner execution",
            "Docker execution",
            "credential injection",
            "customer-target operation",
            "delivery",
        ]:
            require(fragment in statement, f"fixture non-authorization statement incomplete for {category}: {fragment}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"fixture must include runtime_boundary: {category}")
        for flag in REQUIRED_FALSE_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"fixture boundary flag must be false for {category}: {flag}")

        readme = fixture_dir / "README.md"
        require(readme.exists(), f"fixture README missing: {category}")

    non_example_sentinel = FIXTURE_ROOT / "non-example-name/not_public_safe_name.txt"
    require(non_example_sentinel.exists(), "non-example-name fixture must retain intentional non-example sentinel")

    forbidden_roots = [
        FIXTURE_ROOT / "private-not-in-git",
        FIXTURE_ROOT / ".git",
        FIXTURE_ROOT / "__pycache__",
    ]
    for forbidden in forbidden_roots:
        require(not forbidden.exists(), f"forbidden fixture path exists: {forbidden.relative_to(ROOT)}")

    subprocess.run([sys.executable, V0646_HARNESS.as_posix()], cwd=ROOT, check=True)

    print("v0.6.47 public validator negative fixture coverage review and close-readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
