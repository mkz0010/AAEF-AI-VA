from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/82-v065-documentation-only-local-lab-profile-and-action-taxonomy.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0076-add-v065-documentation-only-local-lab-profile-action-taxonomy.md")
    issue = read_text("planning/issues/0075-add-v065-documentation-only-local-lab-profile-action-taxonomy.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.5 documentation-only local lab profile")
    require("v0.6.5 Documentation-Only Local Lab Profile and Action Taxonomy" in readme, "README must mention v0.6.5 local lab profile")
    require("v0.6.5 Documentation-Only Local Lab Profile and Action Taxonomy" in doc, "v0.6.5 local lab profile doc must exist")

    required_sections = [
        "Decision carried forward",
        "Documentation-only local lab profile",
        "Local-only assumptions",
        "Allowed action taxonomy",
        "Denied action taxonomy",
        "Preflight evidence requirements",
        "Human review requirements",
        "Generated output policy",
        "What this lab does not prove",
        "Dry-run planning readiness",
        "Localhost-only controlled behavior remains deferred",
        "Acceptance criteria for this checkpoint",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.5 local lab profile doc must include section: {section}")

    required_phrases = [
        "This checkpoint is documentation-only.",
        "This checkpoint does not build a local lab.",
        "This profile is not an execution profile.",
        "This profile is not a scanner configuration.",
        "This profile is not a customer-target authorization record.",
        "Allowed means documentation-allowed only at this stage.",
        "Allowed does not mean execution-authorized.",
        "Denied actions should fail closed in later fixture, dry-run, or validation work.",
        "Preflight evidence requirements are documentation requirements at this stage.",
        "They are not execution authorization.",
        "Human review is part of the control model, not a cosmetic approval step.",
        "This checkpoint makes dry-run planning more feasible, but does not authorize dry-run behavior yet.",
        "Localhost-only controlled behavior remains deferred.",
        "v0.6.6 Demo Scenario and Reviewer Walkthrough Planning",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"v0.6.5 local lab profile doc must include phrase: {phrase}")

    profile_fields = [
        "`profile_id`",
        "`profile_type`",
        "`target_mode`",
        "`target_ownership`",
        "`third_party_target_allowed`",
        "`customer_target_allowed`",
        "`external_network_testing_allowed`",
        "`runtime_execution_allowed`",
        "`scan_execution_allowed`",
        "`credential_injection_allowed`",
        "`raw_sensitive_artifact_capture_allowed`",
        "`generated_output_root`",
        "`human_review_required`",
        "`delivery_authorization_required`",
        "`public_claim_mode`",
    ]
    for field in profile_fields:
        require(field in doc, f"profile field must include: {field}")

    allowed_actions = [
        "`document_scope`",
        "`record_target_profile`",
        "`record_allowed_action`",
        "`record_denied_action`",
        "`record_preflight_requirement`",
        "`record_human_review_requirement`",
        "`generate_static_fixture`",
        "`simulate_dry_run_request`",
        "`record_expected_evidence`",
        "`record_expected_denial`",
        "`record_demo_non_proof`",
        "`record_private_output_policy`",
    ]
    for action in allowed_actions:
        require(action in doc, f"allowed action taxonomy must include: {action}")

    denied_actions = [
        "`run_live_scan`",
        "`test_external_network`",
        "`test_customer_target`",
        "`inject_real_credentials`",
        "`capture_raw_sensitive_artifact`",
        "`invoke_external_process`",
        "`perform_network_activity`",
        "`bypass_preflight`",
        "`bypass_human_review`",
        "`auto_promote_finding`",
        "`auto_deliver_report`",
        "`claim_production_readiness`",
        "`claim_compliance_certification`",
        "`claim_legal_approval`",
        "`claim_audit_opinion`",
        "`claim_commercial_license_grant`",
    ]
    for action in denied_actions:
        require(action in doc, f"denied action taxonomy must include: {action}")

    evidence_requirements = [
        "`scope_statement`",
        "`target_profile`",
        "`target_ownership_statement`",
        "`network_boundary_statement`",
        "`allowed_action_taxonomy`",
        "`denied_action_taxonomy`",
        "`credential_policy`",
        "`artifact_policy`",
        "`human_review_requirement`",
        "`generated_output_policy`",
        "`non_proof_statement`",
        "`public_claim_boundary`",
    ]
    for requirement in evidence_requirements:
        require(requirement in doc, f"preflight evidence requirements must include: {requirement}")

    review_checkpoints = [
        "Scope review",
        "Target profile review",
        "Action taxonomy review",
        "Preflight evidence review",
        "Finding review",
        "Report review",
        "Delivery authorization review",
        "Public claim review",
    ]
    for checkpoint in review_checkpoints:
        require(checkpoint in doc, f"human review requirements must include: {checkpoint}")

    generated_paths = [
        "private-not-in-git/local-lab-profiles/",
        "private-not-in-git/local-lab-taxonomy/",
        "private-not-in-git/local-lab-dry-run-plans/",
        "private-not-in-git/local-lab-review-records/",
        "private-not-in-git/local-lab-non-proof-statements/",
    ]
    for path in generated_paths:
        require(path in doc, f"generated output policy must include: {path}")

    non_proofs = [
        "live scanning works",
        "customer-target operation is authorized",
        "external network testing is safe",
        "credential injection is safe",
        "runtime execution is ready",
        "production deployment is ready",
        "managed-service operation is ready",
        "compliance certification exists",
        "legal approval exists",
        "audit opinion exists",
        "commercial PoC readiness exists",
        "commercial license is granted",
    ]
    non_proof_section = doc.split("## What this lab does not prove", 1)[1].split("## Dry-run planning readiness", 1)[0]
    for item in non_proofs:
        require(item in non_proof_section, f"what-this-lab-does-not-prove section must include: {item}")

    dry_run_prereqs = [
        "static local lab profile artifact",
        "static allowed and denied action taxonomy artifact",
        "preflight evidence requirement artifact",
        "human review requirement artifact",
        "dry-run request and response schema",
        "dry-run non-proof statement",
        "local validation for dry-run fixture behavior",
        "safety boundary review update",
        "public claim boundary review",
    ]
    for item in dry_run_prereqs:
        require(item in doc, f"dry-run planning readiness must include: {item}")

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
        require(marker in doc, f"v0.6.5 local lab profile doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"v0.6.5 claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
        "this checkpoint permits credential injection",
        "this repository permits credential injection",
        "this checkpoint allows customer target operation",
        "this repository allows customer target operation",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
        "commercial license is granted automatically by this repository",
        "safety is guaranteed by this checkpoint",
        "production deployment is approved by this checkpoint",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden v0.6.5 local lab profile claim found: {claim}")

    require("Add v0.6.5 documentation-only local lab profile and action taxonomy" in adr, "ADR must record v0.6.5 local lab profile decision")
    require("Completed by v0.6.5 candidate" in issue, "Issue must record v0.6.5 completion status")
    require("## v0.6.5 - Documentation-only local lab profile and action taxonomy" in changelog, "CHANGELOG must include v0.6.5")
    require("## v0.6.5 Documentation-only local lab profile and action taxonomy" in roadmap, "ROADMAP must include v0.6.5")
    require("test_v065_documentation_only_local_lab_profile_action_taxonomy.py" in run_all, "run_all must include v0.6.5 local lab profile test")

    print("v0.6.5 documentation-only local lab profile and action taxonomy tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
