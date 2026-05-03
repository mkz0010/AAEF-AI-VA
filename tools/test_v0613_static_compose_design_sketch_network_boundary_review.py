from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/90-v0613-static-compose-design-sketch-and-network-boundary-review.md"


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
    adr = read_text("planning/decisions/ADR-0084-add-v0613-static-compose-design-sketch-network-boundary-review.md")
    issue = read_text("planning/issues/0083-add-v0613-static-compose-design-sketch-network-boundary-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.13 static Compose design sketch checkpoint")
    require("v0.6.13 Static Compose Design Sketch and Network Boundary Review" in doc, "v0.6.13 doc must exist")

    sections = [
        "Public-safe design boundary",
        "Planning proposition",
        "Static sketch prohibition",
        "Static sketch model",
        "Sketch status model",
        "Service role inventory",
        "Network boundary review",
        "Port binding intent review",
        "Outbound network posture",
        "Environment and secret posture",
        "Volume and persistence posture",
        "Reset and teardown posture",
        "Static sketch review questions",
        "Preflight evidence expectations",
        "Advancement gate model",
        "Human review requirements",
        "Generated artifact boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    phrases = [
        "This checkpoint is static design sketch and network boundary review only.",
        "This proposition is intentionally non-executing.",
        "The static sketch must not contain runnable Docker Compose syntax.",
        "The sketch should use descriptive fields, not runnable configuration.",
        "A static sketch is not a Compose file.",
        "A static sketch is not an execution plan.",
        "Service role inventory must not provide runnable service definitions.",
        "Port binding intent is not permission to bind ports.",
        "Outbound behavior must remain blocked unless later explicit work changes scope.",
        "The sketch must not include secret values.",
        "Reset and teardown posture is not execution.",
        "Preflight evidence planning is not preflight satisfaction.",
        "This checkpoint does not introduce an execution-approved state.",
        "Human review remains a gate.",
        "Public repository content should contain planning, not generated private static sketch outputs.",
        "v0.6.14 Static Lab Scenario Fixture Planning",
    ]
    for phrase in phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    required_terms = [
        "`static_sketch_id`",
        "`runnable_configuration_present`",
        "`service_role_inventory`",
        "`network_boundary_intent`",
        "`port_binding_intent`",
        "`outbound_network_intent`",
        "`blocked_runnable_syntax_present`",
        "`local_target_candidate`",
        "`tool_gateway_control_plane`",
        "`static_sketch_ref`",
        "`non_runnable_syntax_review`",
        "private-not-in-git/static-compose-sketches/",
        "private-not-in-git/static-compose-network-reviews/",
    ]
    for term in required_terms:
        require(term in doc, f"doc must include term: {term}")

    false_markers = [
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
    require("Add v0.6.13 static Compose design sketch and network boundary review" in adr, "ADR must record v0.6.13 decision")
    require("Completed by v0.6.13 candidate" in issue, "Issue must record v0.6.13 completion status")
    require("## v0.6.13 - Static Compose design sketch and network boundary review" in changelog, "CHANGELOG must include v0.6.13")
    require("## v0.6.13 Static Compose design sketch and network boundary review" in roadmap, "ROADMAP must include v0.6.13")
    require("test_v0613_static_compose_design_sketch_network_boundary_review.py" in run_all, "run_all must include v0.6.13 test")

    print("v0.6.13 static Compose design sketch and network boundary review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
