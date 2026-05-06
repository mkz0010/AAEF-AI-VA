from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
DOC = REPO / "docs/123-v0646-public-validator-negative-fixture-implementation-candidate.md"
ADR = REPO / "planning/decisions/ADR-0117-add-v0646-public-validator-negative-fixture-implementation-candidate.md"
ISSUE = REPO / "planning/issues/0116-add-v0646-public-validator-negative-fixture-implementation-candidate.md"
VALIDATOR = REPO / "tools/validate_public_example_structure.py"
POSITIVE_ROOT = REPO / "examples/applied-evidence/sanitized-static-mock"
NEGATIVE_ROOT = REPO / "examples/applied-evidence/public-validator-negative-fixtures"
INDEX = NEGATIVE_ROOT / "negative_fixture_index.example.json"

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

FORBIDDEN_RUNTIME_MARKERS = [
    "docker_compose_executed = true",
    "docker_image_pulled = true",
    "container_started = true",
    "port_bound = true",
    "docker_execution_authorized = true",
    "execution_authorized = true",
    "runtime_execution_authorized = true",
    "scanner_execution_authorized = true",
    "real_execution_permitted = true",
    "network_activity_allowed = true",
    "scan_execution_allowed = true",
    "credential_injection_permitted = true",
    "customer_target_authorized = true",
    "delivery_authorized = true",
    "customer_deliverable = true",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(root: Path) -> tuple[int, dict[str, Any], str, str]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), "--root", str(root), "--json"],
        cwd=REPO,
        check=False,
        capture_output=True,
        text=True,
    )
    try:
        data = json.loads(proc.stdout)
    except Exception as exc:
        raise AssertionError(
            f"Validator output for {root} was not parseable JSON. exit={proc.returncode}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        ) from exc
    return proc.returncode, data, proc.stdout, proc.stderr


def blocker_matches(observed: list[str], expected: str) -> bool:
    if expected.endswith(":*"):
        prefix = expected[:-1]
        return any(item.startswith(prefix) for item in observed)
    if expected.endswith("*"):
        prefix = expected[:-1]
        return any(item.startswith(prefix) for item in observed)
    return expected in observed


def assert_validator_runtime_boundary(result: dict[str, Any], label: str) -> None:
    boundary = result.get("runtime_boundary")
    require(isinstance(boundary, dict), f"{label} validator result must include runtime boundary")
    for flag in [
        "public_example_structural_validator_read_only",
        "public_example_structural_validator_public_example_scoped",
    ]:
        require(boundary.get(flag) is True, f"{label} validator boundary flag must be true: {flag}")
    for flag in [
        "public_example_structural_validator_authorizes_execution",
        "runtime_execution_authorized",
        "scanner_execution_authorized",
        "scan_execution_allowed",
        "credential_injection_permitted",
        "customer_target",
        "customer_target_authorized",
        "delivery_authorized",
        "customer_deliverable",
    ]:
        require(boundary.get(flag) is False, f"{label} validator boundary flag must be false: {flag}")


def main() -> int:
    doc = read_text(DOC)
    adr = read_text(ADR)
    issue = read_text(ISSUE)
    readme = read_text(REPO / "README.md")
    changelog = read_text(REPO / "CHANGELOG.md")
    roadmap = read_text(REPO / "ROADMAP.md")
    run_all = read_text(REPO / "tools/run_all_local_checks.py")

    require("v0.6.46 Public Validator Negative Fixture Implementation Candidate" in doc, "doc must include v0.6.46 title")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("docs/122-v0645-public-validator-negative-fixture-implementation-readiness-review.md" in doc, "doc must reference v0.6.45 readiness review")
    require("examples/applied-evidence/public-validator-negative-fixtures/" in doc, "doc must reference negative fixture root")
    require("tools/test_v0646_public_validator_negative_fixture_implementation_candidate.py" in doc, "doc must reference harness test")
    require("v0.6.47 Public Validator Negative Fixture Coverage Review" in doc, "doc must recommend v0.6.47 coverage review")

    required_markers = [
        "public_validator_negative_fixture_implementation_candidate = true",
        "negative_fixture_root_created = true",
        "negative_fixtures_implemented = true",
        "negative_fixture_count = 13",
        "negative_fixture_metadata_implemented = true",
        "negative_fixture_index_implemented = true",
        "negative_fixture_harness_implemented = true",
        "positive_control_preserved = true",
        "validator_behavior_modified = false",
        "public_example_structural_validator_read_only = true",
        "public_example_structural_validator_authorizes_execution = false",
        "fail_closed_expectation_validated_by_harness = true",
        "aaef_handback_category_applied_implementation = true",
        "aaef_core_promotion = false",
        "aaef_profile_promotion = false",
        "aaef_practical_package_promotion = false",
        "private_artifact_copied_to_public = false",
        "fixture_live_evidence = false",
        "validator_authorizes_execution = false",
        "validator_authorizes_scanning = false",
        "validator_authorizes_docker = false",
        "validator_authorizes_delivery = false",
        "runtime_execution_authorized = false",
        "scanner_execution_authorized = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "customer_target_authorized = false",
        "delivery_authorized = false",
    ]
    for marker in required_markers:
        require(marker in doc, f"doc must include marker: {marker}")

    combined = "\n".join([doc, adr, issue, readme, changelog, roadmap]).lower()
    for marker in FORBIDDEN_RUNTIME_MARKERS:
        require(marker.lower() not in combined, f"forbidden runtime marker found: {marker}")

    require(DOC.relative_to(REPO).as_posix() in readme, "README must link v0.6.46 doc")
    require("## v0.6.46 - Public validator negative fixture implementation candidate" in changelog, "CHANGELOG must include v0.6.46")
    require("## v0.6.46 Public validator negative fixture implementation candidate" in roadmap, "ROADMAP must include v0.6.46")
    require("test_v0646_public_validator_negative_fixture_implementation_candidate.py" in run_all, "run_all must include v0.6.46 test")
    require("ADR-0117" in read_text(ADR), "ADR must record v0.6.46 decision")
    require("Completed by v0.6.46 candidate" in read_text(ISSUE), "Issue must record v0.6.46 completion status")

    require(POSITIVE_ROOT.is_dir(), "positive control must exist")
    require(NEGATIVE_ROOT.is_dir(), "negative fixture root must exist")
    require(INDEX.is_file(), "negative fixture index must exist")
    index = read_json(INDEX)
    require(index.get("synthetic_public_safe_static_fixtures") is True, "fixture index must mark static synthetic fixtures")
    require(index.get("validator_behavior_modified") is False, "fixture index must not modify validator behavior")
    require(index.get("source_positive_control") == "examples/applied-evidence/sanitized-static-mock", "fixture index must reference positive control")

    fixtures = index.get("fixtures")
    require(isinstance(fixtures, list), "fixture index must include fixtures list")
    categories = sorted(item.get("negative_category") for item in fixtures)
    require(categories == sorted(EXPECTED_CATEGORIES), f"fixture categories mismatch: {categories}")

    positive_code, positive_result, _, _ = run_validator(POSITIVE_ROOT)
    require(positive_code == 0, "positive control must pass validator")
    require(positive_result.get("public_example_structural_validation_status") == "passed", "positive control must report passed")
    require(positive_result.get("blocker_categories") == [], "positive control must not have blockers")
    assert_validator_runtime_boundary(positive_result, "positive control")

    for fixture in fixtures:
        category = fixture["negative_category"]
        path = REPO / fixture["path"]
        require(path.is_dir(), f"fixture directory must exist: {category}")
        metadata_path = path / "negative_fixture_metadata.example.json"
        require(metadata_path.is_file(), f"fixture metadata must exist: {category}")
        metadata = read_json(metadata_path)
        require(metadata.get("fixture_id") == fixture.get("fixture_id"), f"fixture id mismatch: {category}")
        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must be fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must be marked synthetic/static: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"metadata boundary must exist: {category}")
        for flag in [
            "fixture_live_evidence",
            "validator_behavior_modified_by_fixture",
            "runtime_execution_authorized",
            "scanner_execution_authorized",
            "scan_execution_allowed",
            "credential_injection_permitted",
            "customer_target",
            "customer_target_authorized",
            "delivery_authorized",
            "customer_deliverable",
        ]:
            require(boundary.get(flag) is False, f"metadata boundary flag must remain false for {category}: {flag}")

        code, result, stdout, stderr = run_validator(path)
        require(code != 0, f"negative fixture must fail closed: {category}\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}")
        require(result.get("public_example_structural_validation_status") == "failed", f"negative fixture status must be failed: {category}")
        blockers = result.get("blocker_categories")
        require(isinstance(blockers, list) and blockers, f"negative fixture must include blockers: {category}")
        expected_blockers = metadata.get("expected_blockers")
        require(isinstance(expected_blockers, list) and expected_blockers, f"expected blockers must exist: {category}")
        for expected in expected_blockers:
            require(blocker_matches(blockers, expected), f"expected blocker not observed for {category}: {expected}; observed={blockers}")
        assert_validator_runtime_boundary(result, category)

    print("v0.6.46 public validator negative fixture implementation candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
