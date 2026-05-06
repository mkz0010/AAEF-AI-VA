from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/102-v0625-static-applied-evidence-fixture-planning.md"


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
    adr = read_text("planning/decisions/ADR-0096-add-v0625-static-applied-evidence-fixture-planning.md")
    issue = read_text("planning/issues/0095-add-v0625-static-applied-evidence-fixture-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.25 checkpoint")
    require("v0.6.25 Static Applied Evidence Fixture Planning" in doc, "v0.6.25 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")

    sections = [
        "Planned fixture root",
        "Common fixture artifact set",
        "Common identifier linkage",
        "`tool_action_request` fixture planning",
        "`gate_decision` fixture planning",
        "`dispatch_decision` fixture planning",
        "Result artifact fixture planning",
        "`evidence_event` fixture planning",
        "`review_summary` fixture planning",
        "`non_proof_statement` fixture planning",
        "Scenario fixture plan: permitted-safe-diagnostic",
        "Scenario fixture plan: denied-out-of-scope-request",
        "Scenario fixture plan: human-approval-required",
        "Scenario fixture plan: not-executed-expired",
        "Fixture-to-AAEF five questions planning",
        "Future static fixture generation readiness",
        "Future structural validator planning hooks",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    artifacts = [
        "`tool_action_request.example.json`",
        "`gate_decision.example.json`",
        "`dispatch_decision.example.json`",
        "`execution_result.example.json`",
        "`non_execution_result.example.json`",
        "`evidence_event.example.json`",
        "`review_summary.example.md`",
        "`non_proof_statement.example.md`",
    ]
    for artifact in artifacts:
        require(artifact in doc, f"doc must include artifact: {artifact}")

    scenarios = [
        "`permitted-safe-diagnostic`",
        "`denied-out-of-scope-request`",
        "`human-approval-required`",
        "`not-executed-expired`",
    ]
    for scenario in scenarios:
        require(scenario in doc, f"doc must include scenario: {scenario}")

    linkage_terms = [
        "`request_id`",
        "`linked_request_id`",
        "`decision_id`",
        "`linked_decision_id`",
        "`dispatch_decision_id`",
        "`linked_dispatch_decision_id`",
        "`result_id`",
        "`linked_result_id`",
        "`evidence_event_id`",
    ]
    for term in linkage_terms:
        require(term in doc, f"doc must include linkage term: {term}")

    required_phrases = [
        "This checkpoint is fixture planning only.",
        "This proposition is intentionally non-executing.",
        "The artifact set is planned, not generated.",
        "Identifier linkage should be structurally checkable later.",
        "The request must remain non-authoritative.",
        "Dispatch and non-dispatch must be explicit.",
        "Non-execution evidence is first-class evidence.",
        "The review summary is not a customer deliverable.",
        "Fixture generation should start as static/mock evidence, not live diagnostic evidence.",
        "v0.6.26 Reviewer Walkthrough and Five Questions Mapping",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    five_questions = [
        "Who or what acted?",
        "On whose behalf?",
        "With what authority?",
        "Was the action allowed at the point of execution?",
        "What evidence proves what happened?",
    ]
    for question in five_questions:
        require(question in doc, f"doc must include AAEF question: {question}")

    false_markers = [
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

    require("Add v0.6.25 static applied evidence fixture planning" in adr, "ADR must record v0.6.25 decision")
    require("Completed by v0.6.25 candidate" in issue, "Issue must record v0.6.25 completion status")
    require("## v0.6.25 - Static applied evidence fixture planning" in changelog, "CHANGELOG must include v0.6.25")
    require("## v0.6.25 Static applied evidence fixture planning" in roadmap, "ROADMAP must include v0.6.25")
    require("test_v0625_static_applied_evidence_fixture_planning.py" in run_all, "run_all must include v0.6.25 test")

    print("v0.6.25 static applied evidence fixture planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
