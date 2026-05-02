from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/76-public-faq-and-reviewer-objections-handling.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0070-add-public-faq-reviewer-objections-handling.md")
    issue = read_text("planning/issues/0069-add-public-faq-reviewer-objections-handling.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link public FAQ reviewer objections checkpoint")
    require("Public FAQ and Reviewer Objections Handling" in readme, "README must mention public FAQ reviewer objections")
    require("Public FAQ and Reviewer Objections Handling" in doc, "public FAQ reviewer objections doc must exist")

    required_sections = [
        "Short answer",
        "FAQ",
        "Reviewer objections and direct responses",
        "Evidence-backed answer pattern",
        "Relationship to evidence and capability summary",
        "Relationship to public front page polish",
        "Relationship to public trust navigation",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"FAQ doc must include section: {section}")

    required_phrases = [
        "This checkpoint is explanatory material only.",
        "AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability",
        "It is not a live scanner.",
        "It does not authorize third-party scanning.",
        "It does not authorize customer-target operation.",
        "Runtime execution remains disabled.",
        "Live scanning is not authorized.",
        "Customer-target operation is not authorized.",
        "No commercial license is granted without a separate written agreement.",
        "Commercial licensing inquiries are separate from vulnerability reports.",
        "Security reports should follow `SECURITY.md`.",
        "It does not replace professional security judgment.",
        "AI output is not authority to perform assessment actions.",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"FAQ doc must include phrase: {phrase}")

    faq_questions = [
        "Is AAEF-AI-VA a vulnerability scanner?",
        "Does AAEF-AI-VA run live scans?",
        "Can this be used against customer targets?",
        "What does the project actually demonstrate?",
        "What does the project not demonstrate?",
        "Why is runtime execution intentionally blocked?",
        "Is the project safe to use as-is in production?",
        "Is this compliance certification?",
        "Is this legal advice?",
        "Why AGPL-3.0?",
        "Can a company use the public repository commercially?",
        "Why would a company talk to the author instead of just using the repository?",
        "Are commercial inquiries the same as vulnerability reports?",
        "Does this replace human security professionals?",
        "Does this make AI output trustworthy?",
    ]
    for question in faq_questions:
        require(question in doc, f"FAQ doc must include question: {question}")

    objection_phrases = [
        "This is not a real scanner yet.",
        "Why should I care if it does not scan?",
        "Can I use this directly in customer work?",
        "Is AGPL-3.0 a barrier?",
        "Can someone fork it?",
        "Does this prove compliance?",
        "What is the strongest current evidence?",
    ]
    for phrase in objection_phrases:
        require(phrase in doc, f"FAQ doc must include reviewer objection: {phrase}")

    related_docs = [
        "docs/75-public-evidence-and-capability-boundary-summary.md",
        "docs/74-public-front-page-and-repository-landing-polish-checkpoint.md",
        "docs/73-public-trust-and-reviewer-navigation-checkpoint.md",
    ]
    for related_doc in related_docs:
        require(related_doc in doc, f"FAQ doc must link related doc: {related_doc}")

    answer_pattern_terms = [
        "State what is demonstrated.",
        "State what remains blocked.",
        "Link to the supporting artifact.",
        "Avoid unsupported production, certification, legal, audit, or scan-authorization claims.",
    ]
    for term in answer_pattern_terms:
        require(term in doc, f"FAQ doc must include evidence-backed answer pattern term: {term}")

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
        require(marker in doc, f"FAQ doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"FAQ claims-to-avoid section must include: {claim}")

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
        require(claim not in combined, f"Forbidden FAQ/reviewer-objection claim found: {claim}")

    require("Add public FAQ and reviewer objections handling" in adr, "ADR must record FAQ decision")
    require("Completed by v0.5.10 candidate" in issue, "Issue must record v0.5.10 completion status")
    require("## v0.5.10 - Public FAQ and reviewer objections handling" in changelog, "CHANGELOG must include v0.5.10")
    require("## v0.5.10 Public FAQ and reviewer objections handling" in roadmap, "ROADMAP must include v0.5.10")
    require("test_public_faq_reviewer_objections.py" in run_all, "run_all must include public FAQ reviewer objections test")

    print("Public FAQ and reviewer objections tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
