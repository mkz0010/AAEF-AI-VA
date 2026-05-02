from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/75-public-evidence-and-capability-boundary-summary.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0069-add-public-evidence-capability-boundary-summary.md")
    issue = read_text("planning/issues/0068-add-public-evidence-capability-boundary-summary.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link public evidence and capability boundary summary")
    require("Public Evidence and Capability Boundary Summary" in readme, "README must mention evidence/capability boundary summary")
    require("Public Evidence and Capability Boundary Summary" in doc, "evidence/capability boundary summary doc must exist")

    required_sections = [
        "Summary statement",
        "What is demonstrated",
        "What is evidence-backed",
        "What remains intentionally blocked",
        "What is not demonstrated",
        "Capability boundary table",
        "Reviewer interpretation guidance",
        "Evidence artifacts and private outputs",
        "Public communication boundary",
        "Relationship to front page polish",
        "Relationship to public trust navigation",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"evidence/capability doc must include section: {section}")

    required_phrases = [
        "This checkpoint is an evidence and capability explanation only.",
        "It does not demonstrate live scanning.",
        "It does not demonstrate customer-target operation.",
        "It does not demonstrate production deployment.",
        "AI output is treated as a request, not execution authority.",
        "Runtime execution remains disabled.",
        "Scan execution remains blocked.",
        "Credential injection remains blocked.",
        "Customer-target operation remains blocked.",
        "Commercial license | Not granted by repository",
        "Requires separate written agreement",
        "generated local outputs stay under `private-not-in-git/`",
        "supports commercial licensing discussions",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"evidence/capability doc must include phrase: {phrase}")

    demonstrated_test_paths = [
        "tools/test_tool_gateway_runner.py",
        "tools/test_human_approval_gate.py",
        "tools/test_evidence_chain_linkage.py",
        "tools/test_report_finding_promotion_gate.py",
        "tools/test_delivery_authorization_gate.py",
        "tools/test_runtime_readiness_gate.py",
        "tools/test_preflight_evidence_negative_examples.py",
        "tools/test_licensing_trademark_authorship_protection.py",
        "tools/test_public_front_page_landing_polish.py",
    ]
    for path in demonstrated_test_paths:
        require(path in doc, f"evidence/capability doc must include demonstrated test path: {path}")

    blocked_capabilities = [
        "runtime execution",
        "network activity",
        "scan execution",
        "credential injection",
        "raw artifact capture",
        "customer-target operation",
        "external network testing",
        "production deployment",
        "managed-service operation",
    ]
    blocked_section = doc.split("## What remains intentionally blocked", 1)[1].split("## What is not demonstrated", 1)[0].lower()
    for capability in blocked_capabilities:
        require(capability in blocked_section, f"blocked capability section must include: {capability}")

    not_demonstrated = [
        "live vulnerability scanning",
        "external network testing",
        "customer-target testing",
        "credential injection against real systems",
        "production service deployment",
        "multi-tenant SaaS operation",
        "managed security service operation",
        "legal dependency review completion",
        "full software bill of materials completion",
        "compliance certification",
        "legal approval",
        "audit opinion",
        "equivalence with any external framework",
        "customer-ready managed assessment platform operation",
    ]
    not_demonstrated_section = doc.split("## What is not demonstrated", 1)[1].split("## Capability boundary table", 1)[0].lower()
    for item in not_demonstrated:
        require(item.lower() in not_demonstrated_section, f"not-demonstrated section must include: {item}")

    interpretation_terms = [
        "a safety-first reference implementation",
        "a control-boundary demonstration",
        "a local validation corpus",
        "a governance and release-readiness artifact",
        "a commercial discussion starting point",
        "a production scanner",
        "an autonomous vulnerability scanner",
        "permission to scan third-party systems",
    ]
    for term in interpretation_terms:
        require(term in doc, f"reviewer interpretation guidance must include: {term}")

    related_docs = [
        "docs/74-public-front-page-and-repository-landing-polish-checkpoint.md",
        "docs/73-public-trust-and-reviewer-navigation-checkpoint.md",
    ]
    for related_doc in related_docs:
        require(related_doc in doc, f"evidence/capability doc must link related doc: {related_doc}")

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
        require(marker in doc, f"evidence/capability doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"evidence/capability claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "production deployment approved",
        "runtime execution enabled",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
        "is certified compliant",
        "legal approval is granted",
        "audit opinion is issued",
        "commercial license is granted automatically",
        "safety is guaranteed",
        "is externally framework equivalent",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden evidence/capability claim found: {claim}")

    require("Add public evidence and capability boundary summary" in adr, "ADR must record evidence/capability summary decision")
    require("Completed by v0.5.9 candidate" in issue, "Issue must record v0.5.9 completion status")
    require("## v0.5.9 - Public evidence and capability boundary summary" in changelog, "CHANGELOG must include v0.5.9")
    require("## v0.5.9 Public evidence and capability boundary summary" in roadmap, "ROADMAP must include v0.5.9")
    require("test_public_evidence_capability_boundary_summary.py" in run_all, "run_all must include evidence/capability boundary summary test")

    print("Public evidence and capability boundary summary tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
