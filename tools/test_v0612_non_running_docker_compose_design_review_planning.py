from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/89-v0612-non-running-docker-compose-design-review-planning.md"


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
    adr = read_text("planning/decisions/ADR-0083-add-v0612-non-running-docker-compose-design-review-planning.md")
    issue = read_text("planning/issues/0082-add-v0612-non-running-docker-compose-design-review-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.12 non-running Docker Compose checkpoint")
    require("v0.6.12 Non-running Docker Compose Design Review Planning" in readme, "README must mention v0.6.12 non-running Docker Compose")
    require("v0.6.12 Non-running Docker Compose Design Review Planning" in doc, "v0.6.12 non-running Docker Compose doc must exist")

    required_sections = [
        "Public-safe design boundary",
        "Planning proposition",
        "Non-running Compose design review model",
        "Candidate design posture",
        "Network boundary review",
        "Port exposure review",
        "Image provenance review",
        "Environment variable and secret review",
        "Volume and persistence review",
        "Reset and teardown review",
        "Resource limit review",
        "Image retrieval and assessment activity separation",
        "Preflight evidence expectations",
        "Advancement gate model",
        "Human review requirements",
        "Generated artifact boundary",
        "What this checkpoint does not prove",
        "Relationship to v0.6.10",
        "Relationship to v0.6.11",
        "Recommended next checkpoint",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.12 non-running Docker Compose doc must include section: {section}")

    required_phrases = [
        "This checkpoint is non-running design review planning only.",
        "This proposition is intentionally non-executing.",
        "A Compose design review is not a Compose file.",
        "A Compose design review is not an execution plan.",
        "This checkpoint should keep design status at planning-only or review-only values.",
        "Port exposure planning is not permission to bind ports.",
        "Image review is not image approval.",
        "Reset and teardown planning is not execution.",
        "This separation prevents dependency setup from being confused with assessment execution.",
        "Preflight evidence planning is not preflight satisfaction.",
        "This checkpoint does not introduce an execution-approved state.",
        "Human review remains a gate.",
        "Public repository content should contain planning, not generated private Compose design review outputs.",
        "v0.6.13 Static Compose Design Sketch and Network Boundary Review",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"v0.6.12 non-running Docker Compose doc must include phrase: {phrase}")

    review_fields = [
        "`compose_design_review_id`",
        "`candidate_profile_ref`",
        "`design_status`",
        "`compose_file_created`",
        "`image_pull_required`",
        "`container_start_required`",
        "`network_boundary`",
        "`port_exposure_plan`",
        "`service_inventory`",
        "`image_provenance_review`",
        "`environment_variable_review`",
        "`volume_persistence_review`",
        "`reset_teardown_review`",
        "`resource_limit_review`",
        "`external_network_review`",
        "`tool_interaction_review`",
        "`preflight_evidence_required`",
        "`human_review_required`",
        "`advancement_state`",
        "`non_proof_statement_ref`",
    ]
    for field in review_fields:
        require(field in doc, f"non-running Compose design review model must include: {field}")

    posture_values = [
        "`not_created`",
        "`concept_only`",
        "`draft_for_review`",
        "`requires_human_review`",
        "`blocked_missing_evidence`",
        "`blocked_by_network_boundary`",
        "`blocked_by_secret_or_credential_risk`",
        "`accepted_for_non_running_design_review`",
        "`not_approved_for_execution`",
    ]
    for posture in posture_values:
        require(posture in doc, f"candidate design posture must include: {posture}")

    preflight_items = [
        "`candidate_profile_ref`",
        "`compose_design_review_ref`",
        "`network_boundary_evidence`",
        "`port_exposure_evidence`",
        "`image_provenance_evidence`",
        "`image_pull_separation_evidence`",
        "`environment_variable_evidence`",
        "`volume_persistence_evidence`",
        "`reset_teardown_evidence`",
        "`resource_limit_evidence`",
        "`external_network_block_evidence`",
        "`tool_interaction_boundary_evidence`",
        "`human_review_evidence`",
        "`non_proof_evidence`",
    ]
    for item in preflight_items:
        require(item in doc, f"preflight evidence expectations must include: {item}")

    advancement_states = [
        "`compose_design_recorded`",
        "`compose_design_incomplete`",
        "`preflight_evidence_planned`",
        "`preflight_evidence_requires_review`",
        "`blocked_missing_evidence`",
        "`blocked_by_network_boundary`",
        "`blocked_by_port_exposure`",
        "`blocked_by_secret_or_credential_risk`",
        "`blocked_by_image_provenance`",
        "`accepted_for_non_running_review`",
        "`not_approved_for_execution`",
    ]
    for state in advancement_states:
        require(state in doc, f"advancement gate model must include: {state}")

    private_paths = [
        "private-not-in-git/docker-compose-design-reviews/",
        "private-not-in-git/docker-compose-preflight-evidence/",
        "private-not-in-git/docker-compose-network-reviews/",
        "private-not-in-git/docker-compose-advancement-gates/",
    ]
    for path in private_paths:
        require(path in doc, f"generated artifact boundary must include: {path}")

    non_proofs = [
        "Docker Compose files can be created",
        "Docker images can be pulled",
        "containers can be started",
        "Docker lab execution works",
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
        "docker_compose_file_created = false",
        "docker_compose_executed = false",
        "docker_image_pulled = false",
        "container_started = false",
        "docker_execution_authorized = false",
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
        require(marker in doc, f"v0.6.12 non-running Docker Compose doc must preserve marker: {marker}")

    claims_section = doc.split("## Claims to avoid", 1)[1].split("## Required local checks", 1)[0].lower()
    claims_to_avoid = [
        "docker compose file creation",
        "docker execution approval",
        "image pull approval",
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
        require(claim in claims_section, f"v0.6.12 claims-to-avoid section must include: {claim}")

    forbidden_public_claims = [
        "this checkpoint creates docker compose files",
        "this repository creates docker compose files",
        "this checkpoint pulls docker images",
        "this repository pulls docker images",
        "this checkpoint starts containers",
        "this repository starts containers",
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
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
        require(claim not in combined, f"Forbidden v0.6.12 non-running Docker Compose claim found: {claim}")

    require("private advanced feature details" in doc, "public materials must keep advanced private workstream details abstract")
    require("Add v0.6.12 non-running Docker Compose design review planning" in adr, "ADR must record v0.6.12 decision")
    require("Completed by v0.6.12 candidate" in issue, "Issue must record v0.6.12 completion status")
    require("## v0.6.12 - Non-running Docker Compose design review planning" in changelog, "CHANGELOG must include v0.6.12")
    require("## v0.6.12 Non-running Docker Compose design review planning" in roadmap, "ROADMAP must include v0.6.12")
    require("test_v0612_non_running_docker_compose_design_review_planning.py" in run_all, "run_all must include v0.6.12 non-running Docker Compose design review test")

    print("v0.6.12 non-running Docker Compose design review planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
