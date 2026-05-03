from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/91-v0614-static-lab-scenario-fixture-planning.md"


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
    adr = read_text("planning/decisions/ADR-0085-add-v0614-static-lab-scenario-fixture-planning.md")
    issue = read_text("planning/issues/0084-add-v0614-static-lab-scenario-fixture-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.14 static lab scenario fixture checkpoint")
    require("v0.6.14 Static Lab Scenario Fixture Planning" in doc, "v0.6.14 doc must exist")

    sections = [
        "Public-safe design boundary",
        "Planning proposition",
        "Static fixture set model",
        "Fixture manifest model",
        "Fixture node status model",
        "Candidate-to-sketch linkage",
        "Diagnostic context fixture boundary",
        "AI request fixture boundary",
        "Gate decision fixture boundary",
        "Expected evidence fixture boundary",
        "Scenario trace model",
        "Reviewer walkthrough linkage",
        "Fixture validation expectations",
        "Generated artifact boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    phrases = [
        "This checkpoint is static scenario fixture planning only.",
        "This proposition is intentionally non-executing.",
        "These fixtures are planning concepts at this checkpoint.",
        "They are not generated artifacts yet.",
        "A fixture manifest is not an execution manifest.",
        "Candidate-to-sketch linkage is not target selection.",
        "The AI request fixture does not authorize execution.",
        "The gate decision fixture should keep execution authorization false.",
        "Expected evidence is not live evidence.",
        "The trace is not proof of live execution.",
        "Validation should not convert fixtures into execution artifacts.",
        "Public repository content should contain planning, not generated private fixture outputs.",
        "v0.6.15 Static Fixture Schema and Validator Planning",
    ]
    for phrase in phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    terms = [
        "`fixture_manifest`",
        "`candidate_profile_fixture`",
        "`static_sketch_fixture`",
        "`diagnostic_context_fixture`",
        "`ai_request_fixture`",
        "`gate_decision_fixture`",
        "`expected_evidence_fixture`",
        "`scenario_trace_fixture`",
        "`scenario_fixture_id`",
        "`synthetic_data_statement`",
        "`execution_boundary_statement`",
        "`blocked_by_runtime_implication`",
        "`blocked_by_sensitive_content`",
        "candidate_profile_fixture",
        "static_sketch_fixture",
        "diagnostic_context_fixture",
        "ai_request_fixture",
        "gate_decision_fixture",
        "expected_evidence_fixture",
        "private-not-in-git/static-lab-scenario-fixtures/",
        "private-not-in-git/static-lab-scenario-traces/",
    ]
    for term in terms:
        require(term in doc, f"doc must include term: {term}")

    false_markers = [
        "fixture_generated = false",
        "fixture_live_evidence = false",
        "static_sketch_runnable = false",
        "docker_compose_file_created = false",
        "docker_compose_executed = false",
        "docker_image_pulled = false",
        "container_started = false",
        "port_bound = false",
        "docker_execution_authorized = false",
        "preflight_satisfied = false",
        "execution_authorized = false",
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
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("private advanced feature details" in doc, "public materials must keep advanced private workstream details abstract")
    require("Add v0.6.14 static lab scenario fixture planning" in adr, "ADR must record v0.6.14 decision")
    require("Completed by v0.6.14 candidate" in issue, "Issue must record v0.6.14 completion status")
    require("## v0.6.14 - Static lab scenario fixture planning" in changelog, "CHANGELOG must include v0.6.14")
    require("## v0.6.14 Static lab scenario fixture planning" in roadmap, "ROADMAP must include v0.6.14")
    require("test_v0614_static_lab_scenario_fixture_planning.py" in run_all, "run_all must include v0.6.14 test")

    print("v0.6.14 static lab scenario fixture planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
