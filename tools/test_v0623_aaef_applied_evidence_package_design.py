from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/100-v0623-aaef-applied-evidence-package-design.md"


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
    adr = read_text("planning/decisions/ADR-0094-add-v0623-aaef-applied-evidence-package-design.md")
    issue = read_text("planning/issues/0093-add-v0623-aaef-applied-evidence-package-design.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.23 checkpoint")
    require("v0.6.23 AAEF Applied Evidence Package Design" in doc, "v0.6.23 doc must exist")
    require("Short answer: when actual evidence capture begins" in doc, "doc must answer timing question")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")

    sections = [
        "Evidence package top-level structure",
        "Package manifest design",
        "Required artifact chain",
        "`tool_action_request` design",
        "`gate_decision` design",
        "`dispatch_decision` design",
        "Execution and non-execution result design",
        "Evidence event design",
        "Review summary design",
        "Minimum scenario package set",
        "Public and private artifact placement",
        "Diagnostic system build timing",
        "AAEF five questions package mapping",
        "Structural validator relationship",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    chain_terms = [
        "`tool_action_request`",
        "`gate_decision`",
        "`dispatch_decision`",
        "`execution_result`",
        "`non_execution_result`",
        "`evidence_event`",
        "`review_summary`",
    ]
    for term in chain_terms:
        require(term in doc, f"doc must include chain term: {term}")

    scenarios = [
        "`permitted-safe-diagnostic`",
        "`denied-out-of-scope-request`",
        "`human-approval-required`",
        "`not-executed-expired`",
    ]
    for scenario in scenarios:
        require(scenario in doc, f"doc must include scenario: {scenario}")

    timing_phrases = [
        "The project should start evidence capture with static/mock applied evidence, not with live diagnostic execution.",
        "Actual tool-backed diagnostic evidence should wait until the package structure, scenario definitions, reviewer walkthrough, structural validator, local lab target boundary, preflight checks, and execution authorization gates are all reviewable.",
        "Static/mock evidence package generation",
        "Real local-lab diagnostic system evidence capture",
        "v0.6.28 Static/Mock Applied Evidence Package Generation",
        "v0.7.x Local Lab Diagnostic Execution Gate",
    ]
    for phrase in timing_phrases:
        require(contains(doc, phrase), f"doc must include timing phrase: {phrase}")

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

    require("Add v0.6.23 AAEF applied evidence package design" in adr, "ADR must record v0.6.23 decision")
    require("Completed by v0.6.23 candidate" in issue, "Issue must record v0.6.23 completion status")
    require("## v0.6.23 - AAEF applied evidence package design" in changelog, "CHANGELOG must include v0.6.23")
    require("## v0.6.23 AAEF applied evidence package design" in roadmap, "ROADMAP must include v0.6.23")
    require("test_v0623_aaef_applied_evidence_package_design.py" in run_all, "run_all must include v0.6.23 test")

    print("v0.6.23 AAEF applied evidence package design tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
