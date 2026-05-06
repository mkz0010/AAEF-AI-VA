from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/97-v0620-static-fixture-validator-read-only-implementation-scaffold.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_validator(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "tools/validate_static_lab_fixtures.py", *args],
        cwd=str(REPO),
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    validator = read_text("tools/validate_static_lab_fixtures.py")
    adr = read_text("planning/decisions/ADR-0091-add-v0620-static-fixture-validator-read-only-implementation-scaffold.md")
    issue = read_text("planning/issues/0090-add-v0620-static-fixture-validator-read-only-implementation-scaffold.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.20 checkpoint")
    require("v0.6.20 Static Fixture Validator Read-only Implementation Scaffold" in doc, "v0.6.20 doc must exist")
    require("tools/validate_static_lab_fixtures.py" in doc, "doc must mention validator scaffold")
    require("This checkpoint is read-only implementation scaffold only." in doc, "doc must record scaffold-only boundary")
    require("The scaffold does not authorize execution." in doc, "doc must state non-authorization")
    require("Validator output must not authorize execution." in doc, "doc must preserve output boundary")
    require("v0.6.21 Static Fixture Validator Required-node Check Planning" in doc, "doc must name next checkpoint")

    required_validator_terms = [
        "VALIDATOR_NAME",
        "VALIDATOR_VERSION",
        "NON_AUTHORIZATION_STATEMENT",
        "RUNTIME_BOUNDARY",
        "PLANNED_FAILURE_CATEGORIES",
        "ValidationFailure",
        "ValidationResult",
        "validate_fixture_dir",
        "result_to_dict",
        "build_parser",
        "missing_fixture_directory",
        "fixture_path_not_directory",
        "validator_uncertainty",
    ]
    for term in required_validator_terms:
        require(term in validator, f"validator scaffold must include: {term}")

    forbidden_runtime_terms = [
        "os.system(",
        "docker ",
        "nmap ",
        "zap ",
        "nuclei ",
        "requests.get(",
        "requests.post(",
        "urllib.request",
    ]
    validator_lower = validator.lower()
    for term in forbidden_runtime_terms:
        require(term.lower() not in validator_lower, f"validator scaffold must not include runtime behavior: {term}")

    false_markers = [
        "fixture_schema_complete",
        "fixture_validator_complete",
        "negative_tests_complete",
        "fixture_generated",
        "fixture_live_evidence",
        "validator_authorizes_execution",
        "validator_authorizes_scanning",
        "validator_authorizes_docker",
        "validator_authorizes_delivery",
        "docker_compose_file_created",
        "docker_compose_executed",
        "docker_image_pulled",
        "container_started",
        "port_bound",
        "docker_execution_authorized",
        "execution_authorized",
        "network_activity_allowed",
        "scan_execution_allowed",
        "credential_injection_permitted",
        "customer_target",
        "external_network_target",
        "delivery_authorized",
        "customer_deliverable",
    ]
    for marker in false_markers:
        require(marker in doc, f"doc must include runtime marker: {marker}")
        require(marker in validator, f"validator must include runtime marker: {marker}")

    with tempfile.TemporaryDirectory() as tmp:
        missing = Path(tmp) / "missing-fixtures"
        proc = run_validator("--fixture-dir", str(missing))
        require(proc.returncode == 1, "missing fixture dir must fail closed")
        payload = json.loads(proc.stdout)
        require(payload["validation_status"] == "blocked", "missing fixture dir must be blocked")
        require(payload["blocking"] is True, "missing fixture dir must be blocking")
        require("missing_fixture_directory" in payload["failure_categories"], "missing fixture dir category required")
        require(payload["runtime_boundary"]["validator_authorizes_execution"] is False, "validator must not authorize execution")
        require(payload["runtime_boundary"]["scan_execution_allowed"] is False, "validator must not allow scanning")
        require(payload["runtime_boundary"]["customer_target"] is False, "validator must not mark customer target")
        require(payload["runtime_boundary"]["delivery_authorized"] is False, "validator must not authorize delivery")

        fixture_dir = Path(tmp) / "fixtures"
        fixture_dir.mkdir()
        proc = run_validator("--fixture-dir", str(fixture_dir))
        require(proc.returncode == 0, "existing empty fixture dir should return review-only scaffold status")
        payload = json.loads(proc.stdout)
        require(payload["validation_status"] == "scaffold_review_only", "existing dir should be scaffold review only")
        require(payload["blocking"] is False, "existing empty dir should not be blocked by scaffold-only check")
        require(payload["non_authorization_statement"], "non-authorization statement required")

    forbidden_claims = [
        "this checkpoint implements complete fixture validation",
        "this checkpoint implements negative tests",
        "this checkpoint generates fixture files",
        "this checkpoint creates docker compose files",
        "this checkpoint pulls docker images",
        "this checkpoint starts containers",
        "this checkpoint binds ports",
        "this checkpoint enables runtime execution",
        "this checkpoint allows scan execution",
        "this checkpoint permits credential injection",
        "this checkpoint allows customer target operation",
        "this checkpoint authorizes delivery",
        "this checkpoint is production ready",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
    ]
    combined = "\n".join([readme, doc, validator, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("private advanced feature details" in doc, "public materials must keep advanced private workstream details abstract")
    require("Add v0.6.20 static fixture validator read-only implementation scaffold" in adr, "ADR must record v0.6.20 decision")
    require("Completed by v0.6.20 candidate" in issue, "Issue must record v0.6.20 completion status")
    require("## v0.6.20 - Static fixture validator read-only implementation scaffold" in changelog, "CHANGELOG must include v0.6.20")
    require("## v0.6.20 Static fixture validator read-only implementation scaffold" in roadmap, "ROADMAP must include v0.6.20")
    require("test_v0620_static_fixture_validator_read_only_implementation_scaffold.py" in run_all, "run_all must include v0.6.20 test")

    print("v0.6.20 static fixture validator read-only implementation scaffold tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
