from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/108-v0631-static-mock-applied-evidence-package-private-review-record.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_cmd(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(REPO), text=True, capture_output=True, check=False)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    generator = read_text("tools/generate_static_mock_applied_evidence_private_review_record.py")
    adr = read_text("planning/decisions/ADR-0102-add-v0631-static-mock-applied-evidence-private-review-record.md")
    issue = read_text("planning/issues/0101-add-v0631-static-mock-applied-evidence-private-review-record.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.31 checkpoint")
    require("v0.6.31 Static/Mock Applied Evidence Package Private Review Record" in doc, "v0.6.31 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("private-not-in-git/applied-evidence-runs/static-mock-demo/" in doc, "doc must reference private package path")

    generator_terms = [
        "DEFAULT_PACKAGE_DIR",
        "DEFAULT_OUTPUT_DIR",
        "EXPECTED_SCENARIOS",
        "generate_review",
        "review_scenario",
        "promotion_status",
        "keep_private",
        "public_sample_promotion_authorized",
        "runtime_execution_authorized",
        "scanner_execution_authorized",
        "customer_target_authorized",
        "delivery_authorized",
    ]
    for term in generator_terms:
        require(term in generator, f"review generator must include: {term}")

    forbidden_runtime_terms = [
        "os.system(",
        "requests.",
        "urllib.request",
        "socket.",
        "docker run",
        "nmap -",
        "zap-cli",
        "nuclei -",
    ]
    generator_lower = generator.lower()
    for term in forbidden_runtime_terms:
        require(term.lower() not in generator_lower, f"review generator must not include runtime behavior: {term}")

    with tempfile.TemporaryDirectory() as tmp:
        package_dir = Path(tmp) / "package"
        review_dir = Path(tmp) / "review"

        package_proc = run_cmd([
            sys.executable,
            "tools/generate_static_mock_applied_evidence_package.py",
            "--output-dir",
            str(package_dir),
        ])
        require(package_proc.returncode == 0, package_proc.stderr or package_proc.stdout)

        review_proc = run_cmd([
            sys.executable,
            "tools/generate_static_mock_applied_evidence_private_review_record.py",
            "--package-dir",
            str(package_dir),
            "--output-dir",
            str(review_dir),
        ])
        require(review_proc.returncode == 0, review_proc.stderr or review_proc.stdout)
        payload = json.loads(review_proc.stdout)

        require(payload["status"] == "reviewed_keep_private", "review status must keep private")
        require(payload["promotion_status"] == "keep_private", "promotion status must keep private")
        require(payload["scenario_count"] == 4, "review must cover four scenarios")
        require(payload["runtime_boundary"]["public_sample_generated"] is False, "public sample must remain false")
        require(payload["runtime_boundary"]["scan_execution_allowed"] is False, "scan execution must remain false")
        require(payload["runtime_boundary"]["customer_target"] is False, "customer target must remain false")
        require(payload["runtime_boundary"]["delivery_authorized"] is False, "delivery authorization must remain false")

        record = load_json(review_dir / "private-review-record.generated.json")
        gate = load_json(review_dir / "promotion-gate-result.generated.json")
        record_md = (review_dir / "private-review-record.generated.md").read_text(encoding="utf-8")
        gate_md = (review_dir / "promotion-gate-result.generated.md").read_text(encoding="utf-8")

        require(record["review_status"] == "reviewed_keep_private", "record review status mismatch")
        require(record["promotion_status"] == "keep_private", "record promotion status mismatch")
        require(record["scenario_count"] == 4, "record scenario count mismatch")
        require(record["linkage_ok"] is True, "record linkage must be ok")
        require(record["runtime_delivery_boundaries_ok"] is True, "boundaries must be ok")
        require(gate["public_sample_promotion_authorized"] is False, "gate must not authorize public sample")
        require(gate["runtime_execution_authorized"] is False, "gate must not authorize runtime execution")
        require(gate["scanner_execution_authorized"] is False, "gate must not authorize scanner execution")
        require(gate["customer_target_authorized"] is False, "gate must not authorize customer target")
        require(gate["delivery_authorized"] is False, "gate must not authorize delivery")
        require("does not authorize public sample promotion" in record_md, "record markdown must preserve boundary")
        require("Promotion status: `keep_private`" in gate_md, "gate markdown must preserve keep_private")

    required_doc_phrases = [
        "This checkpoint is private review-record generation only.",
        "This proposition authorizes only private review-record generation under",
        "If the package is missing, the review generator should fail closed rather than assume success.",
        "Generated review outputs are not intended to be committed.",
        "The review is structural and boundary-oriented, not semantic assurance.",
        "The default safe successful status is `reviewed_keep_private`.",
        "This result does not authorize public sample publication.",
        "Any blocker keeps the package private.",
        "Do not expose private generated package contents if the review remains private.",
        "v0.6.32 Static/Mock Applied Evidence Package Public Sample Promotion Decision Record",
    ]
    for phrase in required_doc_phrases:
        require(phrase in doc, f"doc must include phrase: {phrase}")

    markers = [
        "private_package_review_record_generated = true",
        "promotion_gate_result_generated = true",
        "public_sample_promotion_authorized = false",
        "public_sample_generated = false",
        "public_artifact_generated = false",
        "structural_validator_implemented = false",
        "structural_validator_checks_execute = false",
        "tool_backed_diagnostic_capture_started = false",
        "local_lab_diagnostic_system_built = false",
        "validator_authorizes_execution = false",
        "validator_authorizes_scanning = false",
        "validator_authorizes_docker = false",
        "validator_authorizes_delivery = false",
        "docker_compose_file_created = false",
        "docker_compose_executed = false",
        "docker_image_pulled = false",
        "container_started = false",
        "port_bound = false",
        "docker_execution_authorized = false",
        "execution_authorized = false",
        "runtime_execution_authorized = false",
        "scanner_execution_authorized = false",
        "real_execution_permitted = false",
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "customer_target = false",
        "customer_target_authorized = false",
        "external_network_target = false",
        "delivery_authorized = false",
    ]
    for marker in markers:
        require(marker in doc, f"doc must preserve marker: {marker}")

    forbidden_claims = [
        "this checkpoint promotes public samples",
        "this checkpoint generates public sample artifacts",
        "this checkpoint implements structural validators",
        "this checkpoint executes validator checks",
        "this checkpoint builds the local-lab diagnostic system",
        "this checkpoint creates docker compose files",
        "this checkpoint pulls docker images",
        "this checkpoint starts containers",
        "this checkpoint binds ports",
        "this checkpoint enables runtime execution",
        "this checkpoint allows scan execution",
        "this checkpoint permits credential injection",
        "this checkpoint allows customer target operation",
        "this checkpoint authorizes delivery",
        "this checkpoint proves vulnerability detection accuracy",
        "this checkpoint is production ready",
        "this checkpoint provides implementation conformance",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
        "external framework equivalence is established",
    ]
    combined = "\n".join([readme, doc, generator, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("Add v0.6.31 static/mock applied evidence private review record" in adr, "ADR must record v0.6.31 decision")
    require("Completed by v0.6.31 candidate" in issue, "Issue must record v0.6.31 completion status")
    require("## v0.6.31 - Static/mock applied evidence package private review record" in changelog, "CHANGELOG must include v0.6.31")
    require("## v0.6.31 Static/mock applied evidence package private review record" in roadmap, "ROADMAP must include v0.6.31")
    require("test_v0631_static_mock_applied_evidence_private_review_record.py" in run_all, "run_all must include v0.6.31 test")

    print("v0.6.31 static/mock applied evidence private review record tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
