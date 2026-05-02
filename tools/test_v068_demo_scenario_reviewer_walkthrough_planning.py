from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/85-v068-demo-scenario-and-reviewer-walkthrough-planning.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def contains(text: str, phrase: str) -> bool:
    return normalize(phrase) in normalize(text)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0079-add-v068-demo-scenario-reviewer-walkthrough-planning.md")
    issue = read_text("planning/issues/0078-add-v068-demo-scenario-reviewer-walkthrough-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.8 demo scenario checkpoint")
    require("v0.6.8 Demo Scenario and Reviewer Walkthrough Planning" in readme, "README must mention v0.6.8 demo scenario")
    require("v0.6.8 Demo Scenario and Reviewer Walkthrough Planning" in doc, "v0.6.8 demo scenario doc must exist")

    required_sections = [
        "Public-safe design boundary",
        "Core walkthrough proposition",
        "Walkthrough audience",
        "Demo scenario shape",
        "Reviewer walkthrough sequence",
        "Walkthrough artifacts",
        "AI-visible information in the walkthrough",
        "What AI may do in the walkthrough",
        "What gates should show in the walkthrough",
        "Outcome model for the walkthrough",
        "Non-proof statement",
        "Reviewer questions",
        "Demo success criteria",
        "Private workstream separation",
        "Relationship to v0.6.6",
        "Relationship to v0.6.7",
        "Recommended next checkpoint",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.8 demo scenario doc must include section: {section}")

    required_phrases = [
        "This checkpoint is planning only.",
        "This proposition is intentionally non-executing.",
        "It explains the control model without implying a working scanner, customer-target operation, or production-ready service.",
        "The scenario should remain non-executing.",
        "These are planning artifacts at this stage.",
        "They are not runtime artifacts.",
        "These actions are still request-generation activities.",
        "They do not authorize execution.",
        "The walkthrough must not introduce an `executed` outcome.",
        "This non-proof statement should be visible in any future demo package.",
        "The public walkthrough must not include private advanced feature details.",
        "Public wording should stay at the level of general AAEF-AI-VA principles.",
        "v0.6.9 Evidence Reconstruction and Sample Report Demonstration Planning",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"v0.6.8 demo scenario doc must include phrase: {phrase}")

    scenario_steps = [
        "a scope statement",
        "an approved diagnostic context package summary",
        "an AI-generated `tool_action_request`",
        "a gate decision",
        "expected evidence",
        "human review checkpoint",
        "result state",
        "what the walkthrough does not prove",
    ]
    for step in scenario_steps:
        require(step in doc, f"demo scenario shape must include: {step}")

    artifacts = [
        "`demo_scope_summary`",
        "`demo_diagnostic_context_summary`",
        "`demo_missing_information_summary`",
        "`demo_tool_action_request`",
        "`demo_gate_decision_summary`",
        "`demo_expected_evidence_summary`",
        "`demo_human_review_checkpoint`",
        "`demo_non_proof_statement`",
        "`demo_reviewer_question_list`",
        "`demo_walkthrough_record`",
    ]
    for artifact in artifacts:
        require(artifact in doc, f"walkthrough artifacts must include: {artifact}")

    ai_visible = [
        "approved diagnostic context package summary",
        "sanitized observation summary",
        "extracted signal summary",
        "missing information",
        "confidence and uncertainty",
        "safety notes",
        "expected evidence categories",
        "human review recommendation",
    ]
    for item in ai_visible:
        require(item in doc, f"AI-visible information boundary must include: {item}")

    gate_items = [
        "scope binding check",
        "target binding check",
        "action taxonomy check",
        "denied action check",
        "preflight evidence check",
        "diagnostic sufficiency check",
        "human review requirement",
        "evidence expectation",
        "blocked or documentation-only outcome",
        "reason for keeping execution blocked",
    ]
    for item in gate_items:
        require(item in doc, f"gate walkthrough must include: {item}")

    outcomes = [
        "`documentation_recorded`",
        "`request_recorded`",
        "`requires_more_observation`",
        "`requires_human_review`",
        "`requires_preflight_evidence`",
        "`blocked_by_scope`",
        "`blocked_by_action_taxonomy`",
        "`execution_not_authorized`",
    ]
    for outcome in outcomes:
        require(outcome in doc, f"outcome model must include: {outcome}")

    non_proofs = [
        "live scanning works",
        "runtime execution is ready",
        "customer-target operation is authorized",
        "external network testing is authorized",
        "credential injection is authorized",
        "raw sensitive artifact capture is authorized",
        "production deployment is ready",
        "managed-service operation is ready",
        "commercial PoC readiness exists",
        "compliance certification exists",
        "legal approval exists",
        "audit opinion exists",
        "safety is guaranteed",
    ]
    non_proof_section = doc.split("## Non-proof statement", 1)[1].split("## Reviewer questions", 1)[0]
    for item in non_proofs:
        require(item in non_proof_section, f"non-proof statement must include: {item}")

    reviewer_questions = [
        "What context did AI receive?",
        "What context did AI not receive?",
        "What uncertainty did AI identify?",
        "What `tool_action_request` did AI generate?",
        "Which observations supported the request?",
        "Which gate evaluated the request?",
        "What evidence would be expected?",
        "Why did execution remain blocked?",
        "Where would human review be required?",
        "What does this walkthrough not prove?",
    ]
    for question in reviewer_questions:
        require(question in doc, f"reviewer questions must include: {question}")

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
        require(marker in doc, f"v0.6.8 demo scenario doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"v0.6.8 claims-to-avoid section must include: {claim}")

    forbidden_sensitive_terms = [
        "Browser State Intelligence",
        "Gated AI Diagnostic Request",
        "Browser State Evidence Reconstruction",
        "AI Disclosure Gate",
        "Diagnostic Context Reconstruction",
        "Browser State Snapshot",
        "Evidence-bound Browser State Reconstruction",
        "AeyeScan",
        "claim draft",
        "claim element",
        "invention disclosure",
        "prior art",
        "patent-sensitive",
        "patent prep",
        "特許出願",
        "請求項",
        "発明提案書",
        "先行技術",
        "弁理士",
    ]
    combined_case_sensitive = "\n".join([readme, doc, adr, issue])
    for term in forbidden_sensitive_terms:
        require(term not in combined_case_sensitive, f"Forbidden private/sensitive term found in v0.6.8 public materials: {term}")

    forbidden_positive_claims = [
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
        "this checkpoint permits credential injection",
        "this repository permits credential injection",
        "this checkpoint allows customer target operation",
        "this repository allows customer target operation",
        "this checkpoint proves live scanning works",
        "this repository proves live scanning works",
        "this checkpoint is production ready",
        "this repository is production ready",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
        "commercial license is granted automatically by this repository",
        "safety is guaranteed by this checkpoint",
        "production deployment is approved by this checkpoint",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden v0.6.8 demo scenario claim found: {claim}")

    require("Add v0.6.8 demo scenario and reviewer walkthrough planning" in adr, "ADR must record v0.6.8 decision")
    require("Completed by v0.6.8 candidate" in issue, "Issue must record v0.6.8 completion status")
    require("## v0.6.8 - Demo scenario and reviewer walkthrough planning" in changelog, "CHANGELOG must include v0.6.8")
    require("## v0.6.8 Demo scenario and reviewer walkthrough planning" in roadmap, "ROADMAP must include v0.6.8")
    require("test_v068_demo_scenario_reviewer_walkthrough_planning.py" in run_all, "run_all must include v0.6.8 demo scenario test")

    print("v0.6.8 demo scenario and reviewer walkthrough planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
