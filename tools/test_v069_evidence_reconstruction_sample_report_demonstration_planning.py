from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/86-v069-evidence-reconstruction-and-sample-report-demonstration-planning.md"


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
    adr = read_text("planning/decisions/ADR-0080-add-v069-evidence-reconstruction-sample-report-demonstration-planning.md")
    issue = read_text("planning/issues/0079-add-v069-evidence-reconstruction-sample-report-demonstration-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.9 evidence reconstruction checkpoint")
    require("v0.6.9 Evidence Reconstruction and Sample Report Demonstration Planning" in readme, "README must mention v0.6.9 evidence reconstruction")
    require("v0.6.9 Evidence Reconstruction and Sample Report Demonstration Planning" in doc, "v0.6.9 evidence reconstruction doc must exist")

    required_sections = [
        "Public-safe design boundary",
        "Demonstration proposition",
        "Evidence reconstruction scope",
        "Evidence reconstruction chain",
        "Sample evidence packet planning",
        "Sample report demonstration packet",
        "Report finding demonstration boundary",
        "Evidence-to-report transition",
        "Reviewer walkthrough for evidence and report",
        "Evidence sufficiency posture",
        "Human review and delivery boundary",
        "Private artifact boundary",
        "Synthetic data requirement",
        "What this demonstration does not prove",
        "Relationship to v0.6.6",
        "Relationship to v0.6.7",
        "Relationship to v0.6.8",
        "Recommended next checkpoint",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.9 evidence reconstruction doc must include section: {section}")

    required_phrases = [
        "This checkpoint is planning only.",
        "This proposition is intentionally non-executing.",
        "It explains reviewability and traceability without implying a working scanner, customer-target operation, production readiness, or commercial PoC readiness.",
        "The scope is demonstration planning only.",
        "These nodes are planning concepts at this stage.",
        "They are not runtime records.",
        "These artifacts should use illustrative, synthetic, non-customer data only.",
        "The report demonstration packet is not a customer deliverable.",
        "The report demonstration packet is not evidence of live assessment capability.",
        "The evidence-to-report transition should remain review-bound.",
        "The transition must not imply automatic promotion or delivery.",
        "The demonstration must not claim audit sufficiency or compliance sufficiency.",
        "A report-like output should not become a deliverable merely because it exists.",
        "Public repository content should contain planning, not generated private artifacts.",
        "v0.6.10 Safe Docker Lab Roadmap and Local Target Candidate Planning",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"v0.6.9 evidence reconstruction doc must include phrase: {phrase}")

    chain_nodes = [
        "`scope_summary`",
        "`diagnostic_context_summary`",
        "`normalization_loss_summary`",
        "`tool_action_request_record`",
        "`gate_decision_summary`",
        "`expected_evidence_summary`",
        "`finding_candidate_summary`",
        "`finding_review_summary`",
        "`report_finding_demo`",
        "`report_packet_demo`",
        "`delivery_authorization_boundary`",
        "`non_proof_statement`",
    ]
    for node in chain_nodes:
        require(node in doc, f"evidence reconstruction chain must include: {node}")

    sample_artifacts = [
        "`sample_scope_summary`",
        "`sample_context_package_summary`",
        "`sample_tool_action_request`",
        "`sample_gate_decision`",
        "`sample_expected_evidence`",
        "`sample_review_note`",
        "`sample_finding_candidate`",
        "`sample_finding_review`",
        "`sample_report_finding`",
        "`sample_report_packet`",
        "`sample_delivery_boundary`",
        "`sample_non_proof_statement`",
    ]
    for artifact in sample_artifacts:
        require(artifact in doc, f"sample evidence packet planning must include: {artifact}")

    report_packet_items = [
        "report title",
        "demonstration scope",
        "scope exclusions",
        "assessment action summary",
        "AI request summary",
        "gate decision summary",
        "evidence expectation summary",
        "finding candidate summary",
        "finding review status",
        "report finding demonstration",
        "residual uncertainty",
        "human review status",
        "delivery authorization status",
        "non-proof statement",
    ]
    for item in report_packet_items:
        require(item in doc, f"sample report demonstration packet must include: {item}")

    transition_states = [
        "`candidate_recorded`",
        "`needs_more_information`",
        "`reviewed_for_demo`",
        "`promoted_to_report_finding_demo`",
        "`report_packet_demo_recorded`",
        "`delivery_authorization_required`",
        "`not_deliverable`",
    ]
    for state in transition_states:
        require(state in doc, f"evidence-to-report transition must include: {state}")

    posture_labels = [
        "`illustrative_only`",
        "`insufficient_for_assessment_conclusion`",
        "`requires_human_review`",
        "`requires_more_observation`",
        "`blocked_from_execution`",
        "`not_deliverable`",
        "`demo_packet_only`",
    ]
    for label in posture_labels:
        require(label in doc, f"evidence sufficiency posture must include: {label}")

    private_paths = [
        "private-not-in-git/evidence-demonstrations/",
        "private-not-in-git/report-demonstrations/",
        "private-not-in-git/reviewer-walkthroughs/",
        "private-not-in-git/delivery-boundary-demonstrations/",
    ]
    for path in private_paths:
        require(path in doc, f"private artifact boundary must include: {path}")

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
        "audit sufficiency exists",
        "delivery authorization exists",
        "safety is guaranteed",
    ]
    non_proof_section = doc.split("## What this demonstration does not prove", 1)[1].split("## Relationship to v0.6.6", 1)[0]
    for item in non_proofs:
        require(item in non_proof_section, f"non-proof statement must include: {item}")

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
        "delivery_authorized = false",
        "customer_deliverable = false",
    ]
    for marker in required_false_markers:
        require(marker in doc, f"v0.6.9 evidence reconstruction doc must preserve marker: {marker}")

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
        "delivery authorization",
    ]
    for claim in claims_to_avoid:
        require(claim in claims_section, f"v0.6.9 claims-to-avoid section must include: {claim}")

    # Public-sensitive wording checks are intentionally abstract.
    # Detailed private-term inventories belong outside tracked public files.
    require(
        "private advanced feature details" in doc,
        "public materials must keep advanced private workstream details abstract",
    )


    forbidden_positive_claims = [
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
        "this checkpoint permits credential injection",
        "this repository permits credential injection",
        "this checkpoint allows customer target operation",
        "this repository allows customer target operation",
        "this checkpoint authorizes delivery",
        "this repository authorizes delivery",
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
        require(claim not in combined, f"Forbidden v0.6.9 evidence reconstruction claim found: {claim}")

    require("Add v0.6.9 evidence reconstruction and sample report demonstration planning" in adr, "ADR must record v0.6.9 decision")
    require("Completed by v0.6.9 candidate" in issue, "Issue must record v0.6.9 completion status")
    require("## v0.6.9 - Evidence reconstruction and sample report demonstration planning" in changelog, "CHANGELOG must include v0.6.9")
    require("## v0.6.9 Evidence reconstruction and sample report demonstration planning" in roadmap, "ROADMAP must include v0.6.9")
    require("test_v069_evidence_reconstruction_sample_report_demonstration_planning.py" in run_all, "run_all must include v0.6.9 evidence reconstruction test")

    print("v0.6.9 evidence reconstruction and sample report demonstration planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
