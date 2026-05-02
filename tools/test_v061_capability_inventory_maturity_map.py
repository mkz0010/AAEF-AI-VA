from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/78-v061-capability-inventory-and-maturity-map.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0072-add-v061-capability-inventory-maturity-map.md")
    issue = read_text("planning/issues/0071-add-v061-capability-inventory-maturity-map.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.1 capability inventory checkpoint")
    require("v0.6.1 Capability Inventory and Maturity Map" in readme, "README must mention v0.6.1 capability inventory")
    require("v0.6.1 Capability Inventory and Maturity Map" in doc, "v0.6.1 capability inventory doc must exist")

    required_sections = [
        "Maturity model",
        "Current maturity summary",
        "Capability inventory",
        "Capability gaps",
        "Readiness by future path",
        "Recommended next checkpoint",
        "Local lab implication",
        "Commercial PoC implication",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.1 capability inventory doc must include section: {section}")

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
        require(level in doc, f"maturity model must include: {level}")

    current_summary_terms = [
        "Public repository and release governance",
        "Licensing and commercial-use boundary",
        "Reviewer navigation and FAQ",
        "Tool Gateway behavior",
        "Evidence linkage and reconstruction",
        "Runtime readiness boundary",
        "Preflight scaffolding",
        "Local assessment lab",
        "Commercial PoC readiness",
        "Production deployment",
    ]
    for term in current_summary_terms:
        require(term in doc, f"current maturity summary must include: {term}")

    required_capabilities = [
        "Scope registry",
        "Tool Gateway runner",
        "Tool Gateway adapters",
        "Controlled executor policy",
        "Real execution readiness gate",
        "Operator readiness review",
        "Human approval gate",
        "Evidence chain linkage",
        "Evidence reconstruction report",
        "Sanitizer redaction policy",
        "Finding candidate model",
        "Report finding promotion gate",
        "Delivery authorization gate",
        "Runtime readiness gate",
        "Local target lab profile",
        "Runtime destination binding",
        "Execution authorization gate scaffold",
        "Preflight validation scaffold",
        "Preflight evidence examples",
        "Negative preflight evidence examples",
        "Public FAQ and reviewer objections",
        "v0.6.0 work ordering",
    ]
    for capability in required_capabilities:
        require(capability in doc, f"capability inventory must include: {capability}")

    required_test_paths = [
        "tools/test_tool_gateway_runner.py",
        "tools/test_human_approval_gate.py",
        "tools/test_evidence_chain_linkage.py",
        "tools/test_report_finding_promotion_gate.py",
        "tools/test_delivery_authorization_gate.py",
        "tools/test_runtime_readiness_gate.py",
        "tools/test_preflight_evidence_negative_examples.py",
        "tools/test_public_faq_reviewer_objections.py",
        "tools/test_v060_implementation_evaluation_work_ordering.py",
    ]
    for path in required_test_paths:
        require(path in doc, f"capability inventory must include test path: {path}")

    required_gaps = [
        "Evaluation criteria and acceptance model",
        "Capability scoring model",
        "Local assessment lab decision record",
        "Allowed and denied action taxonomy",
        "Preflight concrete checks",
        "Runtime enforcement implementation",
        "Evidence/report UX improvement",
        "Demo scenario walkthrough",
        "Commercial PoC readiness boundary",
    ]
    for gap in required_gaps:
        require(gap in doc, f"capability gaps must include: {gap}")

    readiness_terms = [
        "Continue documentation and evaluation planning",
        "Build evaluation criteria",
        "Improve generated evidence UX",
        "Build dry-run demo walkthrough",
        "Build local assessment lab",
        "Enable controlled local execution",
        "Prepare commercial PoC",
        "Production deployment",
    ]
    for term in readiness_terms:
        require(term in doc, f"readiness by future path must include: {term}")

    required_phrases = [
        "v0.6.2 Evaluation Criteria and Acceptance Model",
        "Do not build a localhost-only controlled lab yet.",
        "First define evaluation criteria and acceptance model.",
        "Commercial PoC readiness remains later work.",
        "This checkpoint is inventory and planning only.",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"v0.6.1 capability inventory doc must include phrase: {phrase}")

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
        require(marker in doc, f"v0.6.1 capability inventory doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"v0.6.1 claims-to-avoid section must include: {claim}")

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
        require(claim not in combined, f"Forbidden v0.6.1 capability inventory claim found: {claim}")

    require("Add v0.6.1 capability inventory and maturity map" in adr, "ADR must record v0.6.1 capability inventory decision")
    require("Completed by v0.6.1 candidate" in issue, "Issue must record v0.6.1 completion status")
    require("## v0.6.1 - Capability inventory and maturity map" in changelog, "CHANGELOG must include v0.6.1")
    require("## v0.6.1 Capability inventory and maturity map" in roadmap, "ROADMAP must include v0.6.1")
    require("test_v061_capability_inventory_maturity_map.py" in run_all, "run_all must include v0.6.1 capability inventory test")

    print("v0.6.1 capability inventory and maturity map tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
