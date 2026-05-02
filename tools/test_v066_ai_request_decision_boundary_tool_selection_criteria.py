from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/83-v066-ai-request-decision-boundary-and-tool-selection-criteria.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0077-add-v066-ai-request-decision-boundary-tool-selection-criteria.md")
    issue = read_text("planning/issues/0076-add-v066-ai-request-decision-boundary-tool-selection-criteria.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.6 AI request boundary checkpoint")
    require("v0.6.6 AI Request Decision Boundary and Tool Selection Criteria" in readme, "README must mention v0.6.6 AI request boundary")
    require("v0.6.6 AI Request Decision Boundary and Tool Selection Criteria" in doc, "v0.6.6 AI request boundary doc must exist")

    required_sections = [
        "Core proposition",
        "Decision boundary",
        "What AI may do",
        "What AI must not do",
        "Tool selection is not execution authority",
        "Tool action request fields",
        "Request generation context",
        "Current MVP tool criteria",
        "Future tool candidate tiers",
        "Tool-selection criteria",
        "Request outcome model",
        "Request quality criteria",
        "Rejection criteria",
        "Human review escalation",
        "Relationship to action taxonomy",
        "Relationship to observation fidelity",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.6 AI request boundary doc must include section: {section}")

    required_phrases = [
        "AI generates tool_action_request.",
        "Gates decide execution.",
        "AI must not authorize execution.",
        "Execution authority remains with authorization, scope, preflight, Tool Gateway, human review, and delivery gates.",
        "These are request-generation activities, not execution authorization.",
        "Tool selection does not mean:",
        "Every proposed tool action remains a `tool_action_request`.",
        "Every `tool_action_request` must be evaluated by gates.",
        "The field `execution_authority_claimed` must remain false.",
        "Context informs request generation only.",
        "They do not authorize execution.",
        "This checkpoint does not introduce an `executed` outcome.",
        "Tool-selection criteria are advisory criteria for request generation.",
        "They are not permission to run the tool.",
        "Human review remains a gate, not a rubber stamp.",
        "v0.6.7 Observation Normalization and Diagnostic Fidelity Risk Review",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"v0.6.6 AI request boundary doc must include phrase: {phrase}")

    allowed_ai_actions = [
        "read approved diagnostic context packages",
        "identify missing observations",
        "recommend candidate next observations",
        "choose a candidate method at request-generation level",
        "generate `tool_action_request`",
        "compare candidate tools",
        "state confidence and uncertainty",
        "request human review",
        "request additional preflight evidence",
    ]
    for item in allowed_ai_actions:
        require(item in doc, f"what AI may do must include: {item}")

    prohibited_ai_actions = [
        "authorize execution",
        "bypass authorization gates",
        "bypass scope gates",
        "bypass preflight gates",
        "bypass Tool Gateway enforcement",
        "bypass human review",
        "treat tool selection as permission",
        "treat confidence as authorization",
        "request real credentials",
        "decide customer-target operation",
        "decide external network testing",
    ]
    for item in prohibited_ai_actions:
        require(item in doc, f"what AI must not do must include: {item}")

    request_fields = [
        "`request_id`",
        "`requested_by`",
        "`request_generation_context_ref`",
        "`candidate_tool`",
        "`candidate_action_type`",
        "`target_binding_ref`",
        "`scope_binding_ref`",
        "`reason_for_request`",
        "`observations_used`",
        "`missing_information`",
        "`confidence`",
        "`expected_evidence`",
        "`safety_notes`",
        "`requires_human_review`",
        "`execution_authority_claimed`",
    ]
    for field in request_fields:
        require(field in doc, f"tool action request fields must include: {field}")

    current_tools = [
        "ZAP",
        "Nmap",
        "nuclei",
        "browser / safe_login_check",
    ]
    for tool in current_tools:
        require(tool in doc, f"current MVP tool criteria must include: {tool}")

    future_tools = [
        "testssl.sh or sslyze",
        "nikto",
        "ffuf or feroxbuster",
        "constrained sqlmap",
        "wapiti or arachni",
        "Burp Suite Pro CLI/API",
        "Nessus Essentials or OpenVAS",
    ]
    for tool in future_tools:
        require(tool in doc, f"future tool candidate tiers must include: {tool}")

    outcomes = [
        "`blocked`",
        "`requires_human_review`",
        "`requires_more_observation`",
        "`requires_preflight_evidence`",
        "`documentation_recorded`",
        "`future_dry_run_candidate`",
        "`execution_not_authorized`",
    ]
    for outcome in outcomes:
        require(outcome in doc, f"request outcome model must include: {outcome}")

    rejection_criteria = [
        "claims execution authority",
        "lacks target binding",
        "lacks scope binding",
        "requests an action in the denied taxonomy",
        "requests live scanning",
        "requests external network testing",
        "requests customer-target operation",
        "requests real credential injection",
        "requests raw sensitive artifact capture",
        "attempts to bypass preflight",
        "attempts to bypass human review",
        "treats confidence as permission",
        "treats tool choice as authorization",
        "relies on unapproved raw artifacts",
    ]
    for item in rejection_criteria:
        require(item in doc, f"rejection criteria must include: {item}")

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
        require(marker in doc, f"v0.6.6 AI request boundary doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"v0.6.6 claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
        "this checkpoint permits credential injection",
        "this repository permits credential injection",
        "this checkpoint allows customer target operation",
        "this repository allows customer target operation",
        "this checkpoint says ai authorizes execution",
        "this repository says ai authorizes execution",
        "this checkpoint says ai runs tools autonomously",
        "this repository says ai runs tools autonomously",
        "this checkpoint treats tool choice as permission",
        "this repository treats tool choice as permission",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
        "commercial license is granted automatically by this repository",
        "safety is guaranteed by this checkpoint",
        "production deployment is approved by this checkpoint",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden v0.6.6 AI request boundary claim found: {claim}")

    require("Add v0.6.6 AI request decision boundary and tool selection criteria" in adr, "ADR must record v0.6.6 AI request boundary decision")
    require("Completed by v0.6.6 candidate" in issue, "Issue must record v0.6.6 completion status")
    require("## v0.6.6 - AI request decision boundary and tool selection criteria" in changelog, "CHANGELOG must include v0.6.6")
    require("## v0.6.6 AI request decision boundary and tool selection criteria" in roadmap, "ROADMAP must include v0.6.6")
    require("test_v066_ai_request_decision_boundary_tool_selection_criteria.py" in run_all, "run_all must include v0.6.6 AI request boundary test")

    print("v0.6.6 AI request decision boundary and tool selection criteria tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
