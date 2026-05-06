from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/103-v0626-reviewer-walkthrough-and-five-questions-mapping.md"


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
    adr = read_text("planning/decisions/ADR-0097-add-v0626-reviewer-walkthrough-five-questions-mapping.md")
    issue = read_text("planning/issues/0096-add-v0626-reviewer-walkthrough-five-questions-mapping.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.26 checkpoint")
    require("v0.6.26 Reviewer Walkthrough and Five Questions Mapping" in doc, "v0.6.26 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")

    sections = [
        "Reviewer walkthrough artifact plan",
        "Walkthrough reader model",
        "Common walkthrough sequence",
        "AAEF five questions",
        "Artifact-to-question mapping",
        "Scenario walkthrough: permitted-safe-diagnostic",
        "Scenario walkthrough: denied-out-of-scope-request",
        "Scenario walkthrough: human-approval-required",
        "Scenario walkthrough: not-executed-expired",
        "Scenario outcome explanation matrix",
        "Five questions mapping by scenario",
        "Non-proof walkthrough requirements",
        "Reviewer acceptance checklist",
        "Future walkthrough generation readiness",
        "Future structural validator planning hooks",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    scenarios = [
        "`permitted-safe-diagnostic`",
        "`denied-out-of-scope-request`",
        "`human-approval-required`",
        "`not-executed-expired`",
    ]
    for scenario in scenarios:
        require(scenario in doc, f"doc must include scenario: {scenario}")

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

    five_questions = [
        "Who or what acted?",
        "On whose behalf?",
        "With what authority?",
        "Was the action allowed at the point of execution?",
        "What evidence proves what happened?",
    ]
    for question in five_questions:
        require(question in doc, f"doc must include AAEF question: {question}")

    required_phrases = [
        "This checkpoint is reviewer walkthrough and mapping planning only.",
        "This proposition is intentionally non-executing.",
        "JSON files alone are not enough.",
        "The mapping should not imply audit or legal sufficiency.",
        "Non-execution evidence is first-class evidence.",
        "The mapping is reviewer guidance, not certification.",
        "This checklist is not an audit opinion.",
        "Walkthrough generation should describe static/mock evidence, not live diagnostic evidence.",
        "v0.6.27 Applied Evidence Structural Validator Planning",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    false_markers = [
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
        "this checkpoint generates walkthroughs",
        "this checkpoint generates mappings",
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

    require("Add v0.6.26 reviewer walkthrough and five questions mapping" in adr, "ADR must record v0.6.26 decision")
    require("Completed by v0.6.26 candidate" in issue, "Issue must record v0.6.26 completion status")
    require("## v0.6.26 - Reviewer walkthrough and five questions mapping" in changelog, "CHANGELOG must include v0.6.26")
    require("## v0.6.26 Reviewer walkthrough and five questions mapping" in roadmap, "ROADMAP must include v0.6.26")
    require("test_v0626_reviewer_walkthrough_five_questions_mapping.py" in run_all, "run_all must include v0.6.26 test")

    print("v0.6.26 reviewer walkthrough and five questions mapping tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
