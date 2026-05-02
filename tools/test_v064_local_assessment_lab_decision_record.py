from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/81-v064-local-assessment-lab-decision-record.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0075-add-v064-local-assessment-lab-decision-record.md")
    issue = read_text("planning/issues/0074-add-v064-local-assessment-lab-decision-record.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.4 local assessment lab decision record")
    require("v0.6.4 Local Assessment Lab Decision Record" in readme, "README must mention v0.6.4 local lab decision")
    require("v0.6.4 Local Assessment Lab Decision Record" in doc, "v0.6.4 local lab decision doc must exist")

    required_sections = [
        "Decision summary",
        "Rationale",
        "Decision options considered",
        "Selected maturity level",
        "Local lab profile scope",
        "Local-only assumptions",
        "Allowed artifacts for the next phase",
        "Prohibited behavior",
        "Entry criteria for future dry-run lab",
        "Entry criteria for future localhost-only controlled behavior",
        "Exit criteria for this decision",
        "Impact on v0.6.x sequence",
        "Commercial implication",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.4 local lab decision doc must include section: {section}")

    required_phrases = [
        "Proceed with a documentation-only local lab profile and dry-run planning.",
        "Do not build localhost-only controlled execution yet.",
        "This checkpoint is a decision record only.",
        "This checkpoint does not build a local lab.",
        "Documentation-only local lab, with dry-run planning allowed as future work.",
        "The project should not jump directly to a working local scanner, live test harness, or customer-like model environment.",
        "L0-L1: Concept recorded and documentation-only profile planning.",
        "The profile must remain local-only and non-executing at this stage.",
        "Dry-run behavior must not produce real external effects.",
        "Commercial PoC readiness remains future work",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"v0.6.4 local lab decision doc must include phrase: {phrase}")

    decision_options = [
        "No local lab yet",
        "Documentation-only local lab",
        "Static fixture local lab",
        "Dry-run local lab",
        "Localhost-only controlled lab",
        "Deferred commercial PoC lab",
    ]
    for option in decision_options:
        require(option in doc, f"decision options must include: {option}")

    local_only_assumptions = [
        "Target mode",
        "localhost-only or documentation-only",
        "owned lab target only",
        "Third-party target",
        "not allowed",
        "Customer target",
        "External network testing",
        "Runtime execution",
        "Scan execution",
        "Credential injection",
        "Raw sensitive artifact capture",
        "Generated outputs",
        "under `private-not-in-git/`",
    ]
    for assumption in local_only_assumptions:
        require(assumption in doc, f"local-only assumptions must include: {assumption}")

    allowed_artifacts = [
        "documentation-only local lab profile",
        "local lab target profile template",
        "allowed and denied action taxonomy draft",
        "preflight evidence requirement draft",
        "dry-run scenario plan",
        "demo walkthrough plan",
        "generated-output directory plan",
        "review checklist",
        "what this lab does not prove",
        "local validation for documentation consistency",
    ]
    for artifact in allowed_artifacts:
        require(artifact in doc, f"allowed artifacts must include: {artifact}")

    prohibited_behavior = [
        "live vulnerability scanning",
        "external network testing",
        "customer-target testing",
        "real credential injection",
        "raw sensitive artifact capture",
        "production deployment",
        "managed-service operation",
        "multi-tenant SaaS operation",
        "automatic delivery to customers",
    ]
    for behavior in prohibited_behavior:
        require(behavior in doc, f"prohibited behavior must include: {behavior}")

    dry_run_criteria = [
        "documentation-only local lab profile",
        "allowed and denied action taxonomy",
        "preflight evidence requirement model",
        "human review requirement model",
        "generated-output private artifact policy",
        "demo purpose statement",
        "demo non-proof statement",
        "local validation test",
        "public claim boundary review",
    ]
    for criterion in dry_run_criteria:
        require(criterion in doc, f"dry-run entry criteria must include: {criterion}")

    localhost_controlled_criteria = [
        "dry-run lab validation",
        "concrete preflight checks",
        "explicit local-only target binding",
        "explicit action authorization model",
        "explicit deny-by-default behavior",
        "explicit no-credential-injection policy",
        "explicit no-external-network policy",
        "explicit evidence retention policy",
        "explicit human review workflow",
        "explicit rollback and cleanup plan",
    ]
    for criterion in localhost_controlled_criteria:
        require(criterion in doc, f"localhost-only controlled behavior criteria must include: {criterion}")

    next_sequence = [
        "v0.6.5 Documentation-Only Local Lab Profile and Action Taxonomy",
        "v0.6.6 Demo Scenario and Reviewer Walkthrough Planning",
        "v0.6.7 Runtime Gate Hardening Plan",
        "v0.6.8 Evidence and Report UX Improvement Plan",
        "v0.6.9 Dry-Run Local Lab Decision",
    ]
    for item in next_sequence:
        require(item in doc, f"updated v0.6.x sequence must include: {item}")

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
        require(marker in doc, f"v0.6.4 local lab decision doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"v0.6.4 claims-to-avoid section must include: {claim}")

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
        require(claim not in combined, f"Forbidden v0.6.4 local lab decision claim found: {claim}")

    require("Add v0.6.4 local assessment lab decision record" in adr, "ADR must record v0.6.4 local lab decision")
    require("Completed by v0.6.4 candidate" in issue, "Issue must record v0.6.4 completion status")
    require("## v0.6.4 - Local assessment lab decision record" in changelog, "CHANGELOG must include v0.6.4")
    require("## v0.6.4 Local assessment lab decision record" in roadmap, "ROADMAP must include v0.6.4")
    require("test_v064_local_assessment_lab_decision_record.py" in run_all, "run_all must include v0.6.4 local lab decision test")

    print("v0.6.4 local assessment lab decision record tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
