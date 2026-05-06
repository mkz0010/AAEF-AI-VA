from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/106-v0629-static-mock-applied-evidence-package-private-generation-candidate.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_generator(output_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            "tools/generate_static_mock_applied_evidence_package.py",
            "--output-dir",
            str(output_dir),
        ],
        cwd=str(REPO),
        text=True,
        capture_output=True,
        check=False,
    )


def check_scenario(root: Path, scenario_id: str, expected_result_artifact: str, expected_decision: str, expected_dispatch: bool) -> None:
    scenario_dir = root / "scenarios" / scenario_id
    require(scenario_dir.is_dir(), f"scenario dir must exist: {scenario_id}")

    request = load_json(scenario_dir / "tool_action_request.generated.json")
    decision = load_json(scenario_dir / "gate_decision.generated.json")
    dispatch = load_json(scenario_dir / "dispatch_decision.generated.json")
    result = load_json(scenario_dir / expected_result_artifact)
    evidence = load_json(scenario_dir / "evidence_event.generated.json")
    review = (scenario_dir / "review_summary.generated.md").read_text(encoding="utf-8")
    non_proof = (scenario_dir / "non_proof_statement.generated.md").read_text(encoding="utf-8")

    require(request["scenario_id"] == scenario_id, f"request scenario id mismatch: {scenario_id}")
    require(decision["scenario_id"] == scenario_id, f"decision scenario id mismatch: {scenario_id}")
    require(dispatch["scenario_id"] == scenario_id, f"dispatch scenario id mismatch: {scenario_id}")
    require(result["scenario_id"] == scenario_id, f"result scenario id mismatch: {scenario_id}")
    require(evidence["scenario_id"] == scenario_id, f"evidence scenario id mismatch: {scenario_id}")

    require(decision["linked_request_id"] == request["request_id"], f"request to decision linkage failed: {scenario_id}")
    require(dispatch["linked_decision_id"] == decision["decision_id"], f"decision to dispatch linkage failed: {scenario_id}")
    require(result["linked_dispatch_decision_id"] == dispatch["dispatch_decision_id"], f"dispatch to result linkage failed: {scenario_id}")
    require(evidence["linked_request_id"] == request["request_id"], f"evidence to request linkage failed: {scenario_id}")
    require(evidence["linked_decision_id"] == decision["decision_id"], f"evidence to decision linkage failed: {scenario_id}")
    require(evidence["linked_dispatch_decision_id"] == dispatch["dispatch_decision_id"], f"evidence to dispatch linkage failed: {scenario_id}")
    require(evidence["linked_result_id"] == result["result_id"], f"evidence to result linkage failed: {scenario_id}")

    require(decision["decision_result"] == expected_decision, f"decision posture mismatch: {scenario_id}")
    require(dispatch["dispatch_attempted"] is expected_dispatch, f"dispatch posture mismatch: {scenario_id}")
    require(result["real_execution_occurred"] is False, f"real execution must remain false: {scenario_id}")
    require(result["runtime_boundary"]["scan_execution_allowed"] is False, f"scan execution must remain false: {scenario_id}")
    require(result["runtime_boundary"]["customer_target"] is False, f"customer target must remain false: {scenario_id}")
    require(result["runtime_boundary"]["delivery_authorized"] is False, f"delivery authorization must remain false: {scenario_id}")

    require("not authority" in review.lower(), f"review must mention non-authority: {scenario_id}")
    require("vulnerability detection accuracy" in non_proof, f"non-proof must reject accuracy claim: {scenario_id}")
    require("delivery authorization" in non_proof, f"non-proof must reject delivery claim: {scenario_id}")


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    generator = read_text("tools/generate_static_mock_applied_evidence_package.py")
    adr = read_text("planning/decisions/ADR-0100-add-v0629-static-mock-applied-evidence-package-private-generation-candidate.md")
    issue = read_text("planning/issues/0099-add-v0629-static-mock-applied-evidence-package-private-generation-candidate.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")
    gitignore = read_text(".gitignore") if (REPO / ".gitignore").exists() else ""

    require(DOC in readme, "README must link v0.6.29 checkpoint")
    require("v0.6.29 Static/Mock Applied Evidence Package Private Generation Candidate" in doc, "v0.6.29 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("private-not-in-git/" in gitignore or "private-not-in-git" in gitignore, ".gitignore must exclude private-not-in-git")

    generator_terms = [
        "DEFAULT_OUTPUT_DIR",
        "private-not-in-git/applied-evidence-runs/static-mock-demo",
        "SCENARIOS",
        "permitted-safe-diagnostic",
        "denied-out-of-scope-request",
        "human-approval-required",
        "not-executed-expired",
        "generate_package",
        "generate_scenario",
        "NON_AUTHORIZATION_STATEMENT",
        "RUNTIME_BOUNDARY",
        "real_execution_permitted",
        "scan_execution_allowed",
        "delivery_authorized",
    ]
    for term in generator_terms:
        require(term in generator, f"generator must include: {term}")

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
        require(term.lower() not in generator_lower, f"generator must not include runtime behavior: {term}")

    with tempfile.TemporaryDirectory() as tmp:
        output_dir = Path(tmp) / "static-mock-demo"
        proc = run_generator(output_dir)
        require(proc.returncode == 0, proc.stderr or proc.stdout)
        payload = json.loads(proc.stdout)
        require(payload["status"] == "generated_private_static_mock_package", "generator status mismatch")
        require(payload["scenario_count"] == 4, "generator must produce four scenarios")
        require(payload["runtime_boundary"]["scan_execution_allowed"] is False, "scan execution must remain false")
        require(payload["runtime_boundary"]["customer_target"] is False, "customer target must remain false")
        require(payload["runtime_boundary"]["delivery_authorized"] is False, "delivery authorization must remain false")

        manifest = load_json(output_dir / "package_manifest.generated.json")
        summary = load_json(output_dir / "package_summary.generated.json")
        walkthrough = (output_dir / "reviewer_walkthrough.generated.md").read_text(encoding="utf-8")
        mapping = (output_dir / "aaef_five_questions_mapping.generated.md").read_text(encoding="utf-8")
        package_non_proof = (output_dir / "non_proof_statement.generated.md").read_text(encoding="utf-8")

        require(manifest["package_status"] == "private_static_mock_generated", "manifest status mismatch")
        require(summary["scenario_count"] == 4, "summary scenario count mismatch")
        require("does not run scanners" in walkthrough.lower(), "walkthrough must preserve no-scanner boundary")
        require("Who or what acted?" in mapping, "five questions mapping must include who/what")
        require("delivery authorization" in package_non_proof, "package non-proof must reject delivery claim")

        check_scenario(output_dir, "permitted-safe-diagnostic", "execution_result.generated.json", "permitted", True)
        check_scenario(output_dir, "denied-out-of-scope-request", "non_execution_result.generated.json", "denied", False)
        check_scenario(output_dir, "human-approval-required", "non_execution_result.generated.json", "held_requires_human_approval", False)
        check_scenario(output_dir, "not-executed-expired", "non_execution_result.generated.json", "expired", False)

    required_doc_phrases = [
        "This checkpoint is private static/mock generation only.",
        "This proposition authorizes only private static/mock artifact generation under",
        "Generated outputs are not intended to be committed.",
        "Only the static/mock generator runs. No scanner runs.",
        "Generated private artifacts are not public samples.",
        "Public-safe promotion is not delivery authorization.",
        "v0.6.30 Static/Mock Applied Evidence Package Review and Promotion Gate Planning",
    ]
    for phrase in required_doc_phrases:
        require(phrase in doc, f"doc must include phrase: {phrase}")

    false_markers = [
        "static_mock_generation_authorized_for_public = false",
        "public_sample_generated = false",
        "structural_validator_implemented = false",
        "structural_validator_checks_execute = false",
        "tool_backed_diagnostic_capture_started = false",
        "local_lab_diagnostic_system_built = false",
        "fixture_live_evidence = false",
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
        "real_execution_permitted = false",
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "customer_target = false",
        "external_network_target = false",
        "delivery_authorized = false",
    ]
    for marker in false_markers:
        require(marker in doc, f"doc must preserve marker: {marker}")

    forbidden_claims = [
        "this checkpoint provides public samples",
        "this checkpoint provides real local-lab diagnostic evidence",
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

    require("Add v0.6.29 static/mock applied evidence package private generation candidate" in adr, "ADR must record v0.6.29 decision")
    require("Completed by v0.6.29 candidate" in issue, "Issue must record v0.6.29 completion status")
    require("## v0.6.29 - Static/mock applied evidence package private generation candidate" in changelog, "CHANGELOG must include v0.6.29")
    require("## v0.6.29 Static/mock applied evidence package private generation candidate" in roadmap, "ROADMAP must include v0.6.29")
    require("test_v0629_static_mock_applied_evidence_package_private_generation_candidate.py" in run_all, "run_all must include v0.6.29 test")

    print("v0.6.29 static/mock applied evidence package private generation candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
