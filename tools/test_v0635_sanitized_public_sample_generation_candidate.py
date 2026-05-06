from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/112-v0635-sanitized-public-sample-generation-candidate.md"
EXAMPLE_ROOT = REPO / "examples/applied-evidence/sanitized-static-mock"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_generator() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "tools/generate_sanitized_public_sample.py"],
        cwd=str(REPO),
        text=True,
        capture_output=True,
        check=False,
    )


def check_scenario(scenario_id: str, result_artifact: str, decision_result: str, dispatch_attempted: bool) -> None:
    scenario_dir = EXAMPLE_ROOT / "scenarios" / scenario_id
    require(scenario_dir.is_dir(), f"scenario dir missing: {scenario_id}")

    request = load_json(scenario_dir / "tool_action_request.example.json")
    decision = load_json(scenario_dir / "gate_decision.example.json")
    dispatch = load_json(scenario_dir / "dispatch_decision.example.json")
    result = load_json(scenario_dir / result_artifact)
    evidence = load_json(scenario_dir / "evidence_event.example.json")
    review = (scenario_dir / "review_summary.example.md").read_text(encoding="utf-8")
    non_proof = (scenario_dir / "non_proof_statement.example.md").read_text(encoding="utf-8")

    require(request["scenario_id"] == scenario_id, f"request scenario mismatch: {scenario_id}")
    require(decision["linked_request_id"] == request["request_id"], f"decision link mismatch: {scenario_id}")
    require(dispatch["linked_decision_id"] == decision["decision_id"], f"dispatch link mismatch: {scenario_id}")
    require(result["linked_dispatch_decision_id"] == dispatch["dispatch_decision_id"], f"result link mismatch: {scenario_id}")
    require(evidence["linked_request_id"] == request["request_id"], f"evidence request link mismatch: {scenario_id}")
    require(evidence["linked_decision_id"] == decision["decision_id"], f"evidence decision link mismatch: {scenario_id}")
    require(evidence["linked_dispatch_decision_id"] == dispatch["dispatch_decision_id"], f"evidence dispatch link mismatch: {scenario_id}")
    require(evidence["linked_result_id"] == result["result_id"], f"evidence result link mismatch: {scenario_id}")
    require(decision["decision_result"] == decision_result, f"decision result mismatch: {scenario_id}")
    require(dispatch["dispatch_attempted"] is dispatch_attempted, f"dispatch posture mismatch: {scenario_id}")
    require(result["real_execution_occurred"] is False, f"real execution must be false: {scenario_id}")
    require(result["runtime_boundary"]["scan_execution_allowed"] is False, f"scan execution must be false: {scenario_id}")
    require(result["runtime_boundary"]["customer_target"] is False, f"customer target must be false: {scenario_id}")
    require(result["runtime_boundary"]["delivery_authorized"] is False, f"delivery must be false: {scenario_id}")
    require("not authority" in review.lower(), f"review must state request is not authority: {scenario_id}")
    require("vulnerability detection accuracy" in non_proof, f"non-proof accuracy claim missing: {scenario_id}")
    require("delivery authorization" in non_proof, f"non-proof delivery claim missing: {scenario_id}")


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    generator = read_text("tools/generate_sanitized_public_sample.py")
    adr = read_text("planning/decisions/ADR-0106-add-v0635-sanitized-public-sample-generation-candidate.md")
    issue = read_text("planning/issues/0105-add-v0635-sanitized-public-sample-generation-candidate.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.35 checkpoint")
    require("v0.6.35 Sanitized Public Sample Generation Candidate" in doc, "v0.6.35 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must include public sample directory")

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

    proc = run_generator()
    require(proc.returncode == 0, proc.stderr or proc.stdout)
    payload = json.loads(proc.stdout)
    require(payload["status"] == "generated_sanitized_public_sample_candidate", "generator status mismatch")
    require(payload["scenario_count"] == 4, "scenario count mismatch")
    require(payload["hygiene_status"] == "passed", "hygiene must pass")
    require(payload["runtime_boundary"]["scan_execution_allowed"] is False, "scan execution must remain false")
    require(payload["runtime_boundary"]["delivery_authorized"] is False, "delivery must remain false")

    require((EXAMPLE_ROOT / "README.md").exists(), "example README missing")
    manifest = load_json(EXAMPLE_ROOT / "package_manifest.example.json")
    hygiene = load_json(EXAMPLE_ROOT / "publication_hygiene_report.example.json")
    mapping = (EXAMPLE_ROOT / "aaef_five_questions_mapping.example.md").read_text(encoding="utf-8")
    package_non_proof = (EXAMPLE_ROOT / "non_proof_statement.example.md").read_text(encoding="utf-8")

    require(manifest["package_status"] == "sanitized_public_sample_candidate", "manifest status mismatch")
    require(manifest["sample_type"] == "synthetic_non_executing_public_example", "sample type mismatch")
    require(hygiene["hygiene_status"] == "passed", "hygiene report must pass")
    require(hygiene["findings"] == [], "hygiene report must have no findings")
    require("Who or what acted?" in mapping, "AAEF mapping must include who/what question")
    require("delivery authorization" in package_non_proof, "package non-proof must reject delivery")

    check_scenario("permitted-safe-diagnostic", "execution_result.example.json", "permitted", True)
    check_scenario("denied-out-of-scope-request", "non_execution_result.example.json", "denied", False)
    check_scenario("human-approval-required", "non_execution_result.example.json", "held_requires_human_approval", False)
    check_scenario("not-executed-expired", "non_execution_result.example.json", "expired", False)

    public_files = [p for p in EXAMPLE_ROOT.rglob("*") if p.is_file()]
    require(public_files, "public example files must exist")
    for path in public_files:
        rel = path.relative_to(EXAMPLE_ROOT).as_posix()
        require(".generated." not in rel, f"public file must not use .generated. naming: {rel}")
        text = path.read_text(encoding="utf-8")
        forbidden_fragments = [
            "private-not-in-git",
            ".generated.",
            "BEGIN RSA PRIVATE KEY",
            "customer.example.com",
            "docker run",
            "127.0.0.1",
            "192.168.",
            "10.0.",
        ]
        for fragment in forbidden_fragments:
            require(fragment.lower() not in text.lower(), f"public file contains forbidden fragment {fragment}: {rel}")

    required_doc_phrases = [
        "This checkpoint is sanitized public sample candidate generation only.",
        "This proposition authorizes only sanitized public sample candidate generation.",
        "The sample demonstrates control-boundary evidence, not diagnostic accuracy.",
        "Hygiene uncertainty must fail closed.",
        "Non-proof statements are included at package and scenario levels.",
        "The sample is public-facing example material, not a customer deliverable.",
        "The next safe step is publication review or structural validation planning for public examples, not live diagnostic execution.",
        "v0.6.36 Sanitized Public Sample Publication Review Record",
    ]
    for phrase in required_doc_phrases:
        require(phrase in doc, f"doc must include phrase: {phrase}")

    markers = [
        "sanitized_public_sample_candidate_generated = true",
        "public_sample_publication_review_completed = false",
        "private_artifact_copied_to_public = false",
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
        "this checkpoint copies private generated artifacts into the public repository",
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

    require("Add v0.6.35 sanitized public sample generation candidate" in adr, "ADR must record v0.6.35 decision")
    require("Completed by v0.6.35 candidate" in issue, "Issue must record v0.6.35 completion status")
    require("## v0.6.35 - Sanitized public sample generation candidate" in changelog, "CHANGELOG must include v0.6.35")
    require("## v0.6.35 Sanitized public sample generation candidate" in roadmap, "ROADMAP must include v0.6.35")
    require("test_v0635_sanitized_public_sample_generation_candidate.py" in run_all, "run_all must include v0.6.35 test")

    print("v0.6.35 sanitized public sample generation candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
