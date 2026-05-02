from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/77-v060-implementation-and-evaluation-work-ordering.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0071-add-v060-implementation-evaluation-work-ordering.md")
    issue = read_text("planning/issues/0070-add-v060-implementation-evaluation-work-ordering.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.0 implementation/evaluation work-ordering checkpoint")
    require("v0.6.0 Implementation and Evaluation Work Ordering" in readme, "README must mention v0.6.0 work ordering")
    require("v0.6.0 Implementation and Evaluation Work Ordering" in doc, "v0.6.0 work-ordering doc must exist")

    required_sections = [
        "Current baseline",
        "Core sequencing rule",
        "Workstream map",
        "Recommended order",
        "Why not start with the local lab immediately?",
        "Decision gates",
        "Priority rules",
        "Capability maturity levels",
        "Local lab decision options",
        "Minimum safe path before any local execution",
        "Commercial PoC readiness path",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.0 work-ordering doc must include section: {section}")

    required_phrases = [
        "This checkpoint is planning and sequencing only.",
        "Plan before implementation.",
        "Evaluate before demonstration.",
        "Gate before execution.",
        "Local-only before customer-facing.",
        "Evidence before claims.",
        "Human review before delivery.",
        "Commercial boundary before commercial PoC.",
        "Starting with ordering and evaluation prevents these mistakes",
        "The default recommended option is documentation-only or dry-run until evaluation",
        "Commercial PoC readiness should not be the immediate next step.",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"v0.6.0 work-ordering doc must include phrase: {phrase}")

    recommended_order = [
        "v0.6.1 capability inventory and maturity map",
        "v0.6.2 evaluation criteria and acceptance model",
        "v0.6.3 safety boundary and non-goal review",
        "v0.6.4 local assessment lab decision record",
        "v0.6.5 demo scenario and reviewer walkthrough planning",
        "v0.6.6 runtime gate hardening plan",
        "v0.6.7 evidence and report UX improvement plan",
        "v0.6.8 controlled local lab profile expansion",
        "v0.6.9 commercial PoC readiness boundary",
    ]
    for item in recommended_order:
        require(item in doc, f"recommended order must include: {item}")

    decision_gates = [
        "Capability gate",
        "Evidence gate",
        "Safety gate",
        "Scope gate",
        "Claim gate",
        "Rework gate",
        "Commercial gate",
    ]
    for gate in decision_gates:
        require(gate in doc, f"decision gates must include: {gate}")

    maturity_levels = [
        "L0 | Concept recorded",
        "L1 | Static example",
        "L2 | Local validation",
        "L3 | Dry-run behavior",
        "L4 | Local-only controlled behavior",
        "L5 | Reviewed PoC candidate",
        "L6 | Commercial deployment candidate",
    ]
    for level in maturity_levels:
        require(level in doc, f"maturity levels must include: {level}")

    local_lab_options = [
        "No local lab yet",
        "Documentation-only local lab",
        "Static fixture local lab",
        "Dry-run local lab",
        "Localhost-only controlled lab",
        "Deferred commercial PoC lab",
    ]
    for option in local_lab_options:
        require(option in doc, f"local lab options must include: {option}")

    required_false_markers = [
        "execution_authorized = false",
        "preflight_satisfied = false",
        "ready_for_runtime_execution = false",
        "real_execution_permitted = false",
        "external_process_execution_allowed = false",
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "raw_artifact_capture_permitted = false",
        "customer_target = false",
        "external_network_target = false",
    ]
    for marker in required_false_markers:
        require(marker in doc, f"v0.6.0 work-ordering doc must preserve marker: {marker}")

    claims_section = doc.split("## Claims to avoid", 1)[1].split("## Required local checks", 1)[0].lower()
    claims_to_avoid = [
        "production deployment approval",
        "runtime execution readiness",
        "scan authorization",
        "customer-target authorization",
        "compliance certification",
        "legal approval",
        "audit opinion",
        "completed legal review",
        "completed dependency audit",
        "managed service approval",
        "commercial license grant",
        "safety guarantee",
        "external framework equivalence",
        "audit sufficiency",
    ]
    for claim in claims_to_avoid:
        require(claim in claims_section, f"v0.6.0 claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "runtime execution enabled",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
        "is certified compliant",
        "legal approval is granted",
        "audit opinion is issued",
        "commercial license is granted automatically",
        "safety is guaranteed",
        "production deployment approved",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden v0.6.0 work-ordering claim found: {claim}")

    require("Add v0.6.0 implementation and evaluation work ordering" in adr, "ADR must record v0.6.0 work-ordering decision")
    require("Completed by v0.6.0 candidate" in issue, "Issue must record v0.6.0 completion status")
    require("## v0.6.0 - Implementation and evaluation work ordering" in changelog, "CHANGELOG must include v0.6.0")
    require("## v0.6.0 Implementation and evaluation work ordering" in roadmap, "ROADMAP must include v0.6.0")
    require("test_v060_implementation_evaluation_work_ordering.py" in run_all, "run_all must include v0.6.0 work-ordering test")

    print("v0.6.0 implementation and evaluation work-ordering tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
