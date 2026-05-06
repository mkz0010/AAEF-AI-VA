from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/98-v0621-static-fixture-validator-required-node-check-planning.md"


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
    validator = read_text("tools/validate_static_lab_fixtures.py")
    adr = read_text("planning/decisions/ADR-0092-add-v0621-static-fixture-validator-required-node-check-planning.md")
    issue = read_text("planning/issues/0091-add-v0621-static-fixture-validator-required-node-check-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.21 checkpoint")
    require("v0.6.21 Static Fixture Validator Required-node Check Planning" in doc, "v0.6.21 doc must exist")
    require("tools/validate_static_lab_fixtures.py" in doc, "doc must mention current scaffold")
    require("This checkpoint is required-node check planning only." in doc, "doc must record planning-only boundary")
    require("v0.6.22 Static Fixture Validator Required-node Check Minimal Implementation" in doc, "doc must name next checkpoint")

    sections = [
        "Public-safe design boundary",
        "Planning proposition",
        "Required-node planning posture",
        "Planned manifest expectation",
        "Required fixture node set",
        "Missing-node failure planning",
        "Review-only result planning",
        "Fail-closed behavior planning",
        "Read-only implementation boundary",
        "Relationship to current scaffold",
        "Future implementation sequence",
        "Negative test planning",
        "Registration readiness",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    phrases = [
        "This proposition is intentionally non-executing.",
        "Required-node planning is not validator behavior.",
        "This checkpoint does not implement manifest parsing.",
        "No runtime node type should be required.",
        "Missing-node failures should fail closed.",
        "Required-node check output must not authorize execution.",
        "Fail-closed behavior should prefer human review over permissive assumptions.",
        "Future required-node check implementation must remain read-only.",
        "v0.6.21 does not change the validator implementation.",
        "Positive fixture generation should not precede missing-node negative tests.",
        "Every negative case should be synthetic, local-only, non-executing, and blocking.",
        "Registration readiness is not runtime authorization.",
    ]
    for phrase in phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    required_nodes = [
        "`candidate_profile_fixture`",
        "`static_sketch_fixture`",
        "`diagnostic_context_fixture`",
        "`ai_request_fixture`",
        "`gate_decision_fixture`",
        "`expected_evidence_fixture`",
        "`reviewer_question_fixture`",
        "`non_proof_fixture`",
        "`scenario_trace_fixture`",
    ]
    for node in required_nodes:
        require(node in doc, f"doc must include required node: {node}")

    missing_categories = [
        "`missing_fixture_manifest`",
        "`missing_candidate_profile_fixture`",
        "`missing_static_sketch_fixture`",
        "`missing_diagnostic_context_fixture`",
        "`missing_ai_request_fixture`",
        "`missing_gate_decision_fixture`",
        "`missing_expected_evidence_fixture`",
        "`missing_reviewer_question_fixture`",
        "`missing_non_proof_fixture`",
        "`missing_scenario_trace_fixture`",
    ]
    for category in missing_categories:
        require(category in doc, f"doc must include missing-node category: {category}")

    false_markers = [
        "required_node_checks_implemented = false",
        "fixture_schema_complete = false",
        "fixture_validator_complete = false",
        "negative_tests_complete = false",
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
        "this checkpoint implements required-node checks",
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
    require("Add v0.6.21 static fixture validator required-node check planning" in adr, "ADR must record v0.6.21 decision")
    require("Completed by v0.6.21 candidate" in issue, "Issue must record v0.6.21 completion status")
    require("## v0.6.21 - Static fixture validator required-node check planning" in changelog, "CHANGELOG must include v0.6.21")
    require("## v0.6.21 Static fixture validator required-node check planning" in roadmap, "ROADMAP must include v0.6.21")
    require("test_v0621_static_fixture_validator_required_node_check_planning.py" in run_all, "run_all must include v0.6.21 test")

    print("v0.6.21 static fixture validator required-node check planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
