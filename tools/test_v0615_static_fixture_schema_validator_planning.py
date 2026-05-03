from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/92-v0615-static-fixture-schema-and-validator-planning.md"


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
    adr = read_text("planning/decisions/ADR-0086-add-v0615-static-fixture-schema-validator-planning.md")
    issue = read_text("planning/issues/0085-add-v0615-static-fixture-schema-validator-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.15 static fixture schema checkpoint")
    require("v0.6.15 Static Fixture Schema and Validator Planning" in doc, "v0.6.15 doc must exist")

    sections = [
        "Public-safe design boundary",
        "Planning proposition",
        "Fixture schema planning scope",
        "Fixture manifest schema planning",
        "Fixture node schema planning",
        "Required fixture node types",
        "AI request fixture schema planning",
        "Gate decision fixture schema planning",
        "Expected evidence fixture schema planning",
        "Scenario trace validation planning",
        "Synthetic data validation planning",
        "No-secret validation planning",
        "No-runtime validation planning",
        "No-runnable-configuration validation planning",
        "Validator failure categories",
        "Future validator registration planning",
        "Generated artifact boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    phrases = [
        "This checkpoint is schema and validator planning only.",
        "This proposition is intentionally non-executing.",
        "A fixture manifest is not an execution manifest.",
        "An AI request fixture is not execution authority.",
        "The gate decision fixture should keep execution authorization false.",
        "Expected evidence is not live evidence.",
        "The trace remains a review aid.",
        "No-secret validation should fail closed.",
        "No-runtime validation should block any fixture that implies execution.",
        "No-runnable-configuration validation prevents static fixtures from becoming execution instructions.",
        "Validator failures should block advancement.",
        "This checkpoint does not implement the future fixture validator.",
        "Public repository content should contain planning, not generated private fixture outputs.",
        "v0.6.16 Static Fixture Schema Draft and Negative Test Planning",
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
        "`fixture_node_id`",
        "`fixture_node_type`",
        "`source_checkpoint_ref`",
        "`execution_authorization_state`",
        "`gate_decision_id`",
        "`execution_authorization_result`",
        "`missing_required_node`",
        "`invalid_reference`",
        "`runtime_marker_not_false`",
        "`runnable_configuration_detected`",
        "`secret_like_content_detected`",
        "private-not-in-git/static-fixture-schema-reviews/",
        "private-not-in-git/static-fixture-validator-plans/",
    ]
    for term in terms:
        require(term in doc, f"doc must include term: {term}")

    false_markers = [
        "fixture_schema_implemented = false",
        "fixture_validator_implemented = false",
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
        "this checkpoint implements fixture schemas",
        "this checkpoint implements fixture validators",
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
    require("Add v0.6.15 static fixture schema and validator planning" in adr, "ADR must record v0.6.15 decision")
    require("Completed by v0.6.15 candidate" in issue, "Issue must record v0.6.15 completion status")
    require("## v0.6.15 - Static fixture schema and validator planning" in changelog, "CHANGELOG must include v0.6.15")
    require("## v0.6.15 Static fixture schema and validator planning" in roadmap, "ROADMAP must include v0.6.15")
    require("test_v0615_static_fixture_schema_validator_planning.py" in run_all, "run_all must include v0.6.15 test")

    print("v0.6.15 static fixture schema and validator planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
