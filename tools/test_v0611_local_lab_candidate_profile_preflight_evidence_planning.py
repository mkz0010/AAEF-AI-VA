from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/88-v0611-local-lab-candidate-profile-and-preflight-evidence-planning.md"


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
    adr = read_text("planning/decisions/ADR-0082-add-v0611-local-lab-candidate-profile-preflight-evidence-planning.md")
    issue = read_text("planning/issues/0081-add-v0611-local-lab-candidate-profile-preflight-evidence-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.11 local lab candidate profile checkpoint")
    require("v0.6.11 Local Lab Candidate Profile and Preflight Evidence Planning" in readme, "README must mention v0.6.11 local lab candidate profile")
    require("v0.6.11 Local Lab Candidate Profile and Preflight Evidence Planning" in doc, "v0.6.11 local lab candidate profile doc must exist")

    required_sections = [
        "Public-safe design boundary",
        "Planning proposition",
        "Candidate profile model",
        "Candidate profile examples",
        "Candidate comparison criteria",
        "Preflight evidence package model",
        "Preflight evidence status model",
        "Advancement gate model",
        "Candidate rejection criteria",
        "Human review requirements",
        "Network and target boundary",
        "Tool action taxonomy planning",
        "Generated artifact boundary",
        "Synthetic data requirement",
        "What this checkpoint does not prove",
        "Relationship to v0.6.10",
        "Recommended next checkpoint",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.11 local lab candidate profile doc must include section: {section}")

    required_phrases = [
        "This checkpoint is candidate-profile and preflight-evidence planning only.",
        "This proposition is intentionally non-executing.",
        "It creates a reviewable planning layer before implementation.",
        "A candidate profile is not an execution plan.",
        "These examples are not selected for execution.",
        "These examples are not installed, started, scanned, integrated, or treated as authorized execution.",
        "Candidate comparison is not candidate approval.",
        "Preflight evidence planning is not preflight satisfaction.",
        "This checkpoint should keep preflight satisfied as false.",
        "This checkpoint does not introduce an execution-approved state.",
        "Rejection protects the project boundary.",
        "Human review remains a gate.",
        "Public repository content should contain planning, not generated private candidate profile outputs.",
        "v0.6.12 Non-running Docker Compose Design Review Planning",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"v0.6.11 local lab candidate profile doc must include phrase: {phrase}")

    profile_fields = [
        "`candidate_id`",
        "`candidate_name`",
        "`candidate_type`",
        "`candidate_status`",
        "`target_mode`",
        "`ownership_statement`",
        "`network_boundary`",
        "`external_network_policy`",
        "`data_policy`",
        "`credential_policy`",
        "`secret_policy`",
        "`reset_teardown_expectation`",
        "`resource_expectation`",
        "`licensing_review_status`",
        "`tool_action_taxonomy_mapping`",
        "`preflight_evidence_required`",
        "`human_review_required`",
        "`advancement_state`",
        "`non_proof_statement_ref`",
    ]
    for field in profile_fields:
        require(field in doc, f"candidate profile model must include: {field}")

    candidates = [
        "DVWA",
        "OWASP Juice Shop",
        "WebGoat",
        "Synthetic local API",
        "Static fixture target",
    ]
    for candidate in candidates:
        require(candidate in doc, f"candidate profile examples must include: {candidate}")

    preflight_items = [
        "`candidate_profile_ref`",
        "`local_ownership_evidence`",
        "`network_boundary_evidence`",
        "`external_network_block_evidence`",
        "`synthetic_data_evidence`",
        "`synthetic_credential_evidence`",
        "`secret_exclusion_evidence`",
        "`reset_teardown_evidence`",
        "`resource_limit_evidence`",
        "`licensing_review_evidence`",
        "`action_taxonomy_evidence`",
        "`human_review_evidence`",
        "`non_proof_evidence`",
    ]
    for item in preflight_items:
        require(item in doc, f"preflight evidence package must include: {item}")

    status_values = [
        "`not_collected`",
        "`planned`",
        "`drafted_for_review`",
        "`requires_review`",
        "`accepted_for_planning`",
        "`rejected`",
        "`not_applicable`",
    ]
    for status in status_values:
        require(status in doc, f"preflight evidence status model must include: {status}")

    advancement_states = [
        "`candidate_recorded`",
        "`profile_incomplete`",
        "`preflight_evidence_planned`",
        "`preflight_evidence_requires_review`",
        "`blocked_missing_evidence`",
        "`blocked_by_network_boundary`",
        "`blocked_by_credential_policy`",
        "`blocked_by_licensing_review`",
        "`accepted_for_static_planning`",
        "`not_approved_for_execution`",
    ]
    for state in advancement_states:
        require(state in doc, f"advancement gate model must include: {state}")

    private_paths = [
        "private-not-in-git/local-lab-candidate-profiles/",
        "private-not-in-git/local-lab-preflight-evidence/",
        "private-not-in-git/local-lab-profile-reviews/",
        "private-not-in-git/local-lab-advancement-gates/",
    ]
    for path in private_paths:
        require(path in doc, f"generated artifact boundary must include: {path}")

    non_proofs = [
        "Docker lab execution works",
        "containers can be started",
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
    non_proof_section = doc.split("## What this checkpoint does not prove", 1)[1].split("## Relationship to v0.6.10", 1)[0]
    for item in non_proofs:
        require(item in non_proof_section, f"non-proof statement must include: {item}")

    required_false_markers = [
        "docker_execution_authorized = false",
        "container_started = false",
        "candidate_selected_for_execution = false",
        "preflight_evidence_collected = false",
        "preflight_satisfied = false",
        "execution_authorized = false",
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
        require(marker in doc, f"v0.6.11 local lab candidate profile doc must preserve marker: {marker}")

    claims_section = doc.split("## Claims to avoid", 1)[1].split("## Required local checks", 1)[0].lower()
    claims_to_avoid = [
        "docker execution approval",
        "container startup approval",
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
        require(claim in claims_section, f"v0.6.11 claims-to-avoid section must include: {claim}")

    forbidden_public_claims = [
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
        "this checkpoint starts containers",
        "this repository starts containers",
        "this checkpoint collects live preflight evidence",
        "this checkpoint satisfies preflight",
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
    for claim in forbidden_public_claims:
        require(claim not in combined, f"Forbidden v0.6.11 local lab candidate profile claim found: {claim}")

    require("private advanced feature details" in doc, "public materials must keep advanced private workstream details abstract")
    require("Add v0.6.11 local lab candidate profile and preflight evidence planning" in adr, "ADR must record v0.6.11 decision")
    require("Completed by v0.6.11 candidate" in issue, "Issue must record v0.6.11 completion status")
    require("## v0.6.11 - Local lab candidate profile and preflight evidence planning" in changelog, "CHANGELOG must include v0.6.11")
    require("## v0.6.11 Local lab candidate profile and preflight evidence planning" in roadmap, "ROADMAP must include v0.6.11")
    require("test_v0611_local_lab_candidate_profile_preflight_evidence_planning.py" in run_all, "run_all must include v0.6.11 local lab candidate profile test")

    print("v0.6.11 local lab candidate profile and preflight evidence planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
