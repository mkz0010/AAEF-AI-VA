from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/87-v0610-safe-docker-lab-roadmap-and-local-target-candidate-planning.md"


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
    adr = read_text("planning/decisions/ADR-0081-add-v0610-safe-docker-lab-roadmap-local-target-candidate-planning.md")
    issue = read_text("planning/issues/0080-add-v0610-safe-docker-lab-roadmap-local-target-candidate-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.10 safe Docker lab roadmap checkpoint")
    require("v0.6.10 Safe Docker Lab Roadmap and Local Target Candidate Planning" in readme, "README must mention v0.6.10 safe Docker lab roadmap")
    require("v0.6.10 Safe Docker Lab Roadmap and Local Target Candidate Planning" in doc, "v0.6.10 safe Docker lab roadmap doc must exist")

    required_sections = [
        "Public-safe design boundary",
        "Roadmap proposition",
        "Candidate local targets",
        "Candidate acceptance criteria",
        "Candidate exclusion criteria",
        "Phased safe Docker lab roadmap",
        "Required preflight evidence for future advancement",
        "Human review expectations",
        "Network boundary requirements",
        "Tool interaction boundary",
        "Generated artifact boundary",
        "Synthetic data requirement",
        "What this roadmap does not prove",
        "Relationship to v0.6.5",
        "Relationship to v0.6.6",
        "Relationship to v0.6.7",
        "Relationship to v0.6.8 and v0.6.9",
        "Recommended next checkpoint",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.10 safe Docker lab roadmap doc must include section: {section}")

    required_phrases = [
        "This checkpoint is roadmap and candidate planning only.",
        "The roadmap is intentionally non-executing.",
        "This checkpoint covers L0 only.",
        "It may describe later phases, but it does not authorize them.",
        "Preflight evidence planning is not execution authorization.",
        "Human review remains a gate.",
        "this checkpoint does not authorize tools to run.",
        "Public repository content should contain planning, not generated private lab outputs.",
        "Candidate only means:",
        "not installed,",
        "not run,",
        "not scanned,",
        "not integrated,",
        "not treated as authorized execution.",
        "v0.6.11 Local Lab Candidate Profile and Preflight Evidence Planning",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"v0.6.10 safe Docker lab roadmap doc must include phrase: {phrase}")

    candidates = [
        "DVWA",
        "OWASP Juice Shop",
        "WebGoat",
        "Synthetic local API",
        "Static fixture target",
    ]
    for candidate in candidates:
        require(candidate in doc, f"candidate local targets must include: {candidate}")

    acceptance_criteria = [
        "Ownership",
        "Network boundary",
        "External network",
        "Customer data",
        "Secrets",
        "Credentials",
        "Reset behavior",
        "Licensing",
        "Resource profile",
        "Safety posture",
        "Evidence posture",
        "Public claim posture",
    ]
    for criterion in acceptance_criteria:
        require(criterion in doc, f"candidate acceptance criteria must include: {criterion}")

    phases = [
        "L0",
        "L1",
        "L2",
        "L3",
        "L4",
        "L5",
        "L6",
        "L7",
        "Candidate planning",
        "Static lab profile",
        "Compose design review",
        "Preflight model review",
        "Dry-run planning",
        "Bounded local execution proposal",
        "Bounded local execution implementation",
        "Demonstration packet",
    ]
    for phase in phases:
        require(phase in doc, f"phased roadmap must include: {phase}")

    preflight_items = [
        "`local_target_profile`",
        "`target_ownership_statement`",
        "`network_isolation_statement`",
        "`external_network_block_statement`",
        "`synthetic_data_statement`",
        "`credential_policy`",
        "`reset_teardown_plan`",
        "`resource_limit_plan`",
        "`tool_action_taxonomy_mapping`",
        "`human_review_checkpoint`",
        "`non_proof_statement`",
    ]
    for item in preflight_items:
        require(item in doc, f"preflight evidence requirements must include: {item}")

    private_paths = [
        "private-not-in-git/local-lab-roadmaps/",
        "private-not-in-git/local-target-candidates/",
        "private-not-in-git/docker-lab-design-reviews/",
        "private-not-in-git/local-lab-preflight-reviews/",
        "private-not-in-git/local-lab-dry-run-plans/",
    ]
    for path in private_paths:
        require(path in doc, f"generated artifact boundary must include: {path}")

    non_proofs = [
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
    non_proof_section = doc.split("## What this roadmap does not prove", 1)[1].split("## Relationship to v0.6.5", 1)[0]
    for item in non_proofs:
        require(item in non_proof_section, f"non-proof statement must include: {item}")

    required_false_markers = [
        "docker_execution_authorized = false",
        "container_started = false",
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
        require(marker in doc, f"v0.6.10 safe Docker lab roadmap doc must preserve marker: {marker}")

    claims_section = doc.split("## Claims to avoid", 1)[1].split("## Required local checks", 1)[0].lower()
    claims_to_avoid = [
        "docker execution approval",
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
        require(claim in claims_section, f"v0.6.10 claims-to-avoid section must include: {claim}")

    forbidden_public_claims = [
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
        "this checkpoint starts containers",
        "this repository starts containers",
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
        require(claim not in combined, f"Forbidden v0.6.10 safe Docker lab roadmap claim found: {claim}")

    require("private advanced feature details" in doc, "public materials must keep advanced private workstream details abstract")
    require("Add v0.6.10 safe Docker lab roadmap and local target candidate planning" in adr, "ADR must record v0.6.10 decision")
    require("Completed by v0.6.10 candidate" in issue, "Issue must record v0.6.10 completion status")
    require("## v0.6.10 - Safe Docker lab roadmap and local target candidate planning" in changelog, "CHANGELOG must include v0.6.10")
    require("## v0.6.10 Safe Docker lab roadmap and local target candidate planning" in roadmap, "ROADMAP must include v0.6.10")
    require("test_v0610_safe_docker_lab_roadmap_local_target_candidate_planning.py" in run_all, "run_all must include v0.6.10 safe Docker lab roadmap test")

    print("v0.6.10 safe Docker lab roadmap and local target candidate planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
