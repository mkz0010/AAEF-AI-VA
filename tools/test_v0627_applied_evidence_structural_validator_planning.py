from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/104-v0627-applied-evidence-structural-validator-planning.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains(text: str, phrase: str) -> bool:
    return re.sub(r"\s+", " ", phrase).strip() in re.sub(r"\s+", " ", text).strip()


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0098-add-v0627-applied-evidence-structural-validator-planning.md")
    issue = read_text("planning/issues/0097-add-v0627-applied-evidence-structural-validator-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.27 checkpoint")
    require("v0.6.27 Applied Evidence Structural Validator Planning" in doc, "v0.6.27 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")

    sections = [
        "Validator input boundary",
        "Validator output boundary",
        "Required artifact presence checks",
        "Required field checks",
        "Identifier linkage checks",
        "Scenario consistency checks",
        "Contradiction checks",
        "Non-execution evidence checks",
        "Reviewer walkthrough coverage checks",
        "Non-proof statement checks",
        "Overclaim prevention checks",
        "Failure category planning",
        "Validator review result planning",
        "Future implementation sequence",
        "Readiness for static/mock evidence generation",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    artifacts = [
        "`package_manifest.json`",
        "`tool_action_request.example.json`",
        "`gate_decision.example.json`",
        "`dispatch_decision.example.json`",
        "`execution_result.example.json`",
        "`non_execution_result.example.json`",
        "`evidence_event.example.json`",
        "`review_summary.example.md`",
        "`non_proof_statement.example.md`",
        "`reviewer_walkthrough.md`",
        "`aaef_five_questions_mapping.md`",
    ]
    for artifact in artifacts:
        require(artifact in doc, f"doc must include artifact: {artifact}")

    checks = [
        "missing_required_artifact",
        "missing_required_field",
        "broken_identifier_linkage",
        "scenario_consistency_failure",
        "dispatch_result_contradiction",
        "missing_non_execution_evidence",
        "missing_reviewer_walkthrough",
        "missing_five_questions_mapping",
        "missing_non_proof_statement",
        "overclaim_detected",
        "runtime_implication_detected",
        "customer_target_implication_detected",
        "delivery_authorization_implication_detected",
        "validator_uncertainty",
    ]
    for check in checks:
        require(f"`{check}`" in doc or check in doc, f"doc must include failure category: {check}")

    required_phrases = [
        "This checkpoint is structural validator planning only.",
        "This proposition is intentionally non-executing.",
        "Validator output must not authorize execution.",
        "Artifact absence should be blocking.",
        "Missing required fields should be blocking.",
        "Broken identifier linkage should be blocking.",
        "Scenario mismatch should be blocking.",
        "Contradiction checks are structural checks, not semantic assurance.",
        "Non-execution evidence is first-class evidence.",
        "Reviewer coverage checks should be blocking before public sample release.",
        "Overclaim prevention protects the public claim boundary.",
        "Every unsafe or uncertain failure should be blocking.",
        "Static/mock evidence generation should not precede structural validation planning.",
        "The earliest safe next step is not live diagnostic execution.",
        "v0.6.28 Static/Mock Applied Evidence Package Generation Readiness Review",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    false_markers = [
        "structural_validator_implemented = false",
        "structural_validator_checks_execute = false",
        "reviewer_walkthrough_generated = false",
        "five_questions_mapping_generated = false",
        "static_applied_evidence_fixtures_generated = false",
        "applied_evidence_scenarios_generated = false",
        "applied_evidence_package_generated = false",
        "static_mock_evidence_capture_started = false",
        "tool_backed_diagnostic_capture_started = false",
        "local_lab_diagnostic_system_built = false",
        "fixture_generated = false",
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
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "customer_target = false",
        "external_network_target = false",
        "delivery_authorized = false",
    ]
    for marker in false_markers:
        require(marker in doc, f"doc must preserve false marker: {marker}")

    forbidden_claims = [
        "this checkpoint implements structural validators",
        "this checkpoint executes validator checks",
        "this checkpoint generates fixtures",
        "this checkpoint generates evidence packages",
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
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("Add v0.6.27 applied evidence structural validator planning" in adr, "ADR must record v0.6.27 decision")
    require("Completed by v0.6.27 candidate" in issue, "Issue must record v0.6.27 completion status")
    require("## v0.6.27 - Applied evidence structural validator planning" in changelog, "CHANGELOG must include v0.6.27")
    require("## v0.6.27 Applied evidence structural validator planning" in roadmap, "ROADMAP must include v0.6.27")
    require("test_v0627_applied_evidence_structural_validator_planning.py" in run_all, "run_all must include v0.6.27 test")

    print("v0.6.27 applied evidence structural validator planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
