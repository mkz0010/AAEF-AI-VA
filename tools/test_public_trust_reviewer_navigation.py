from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/73-public-trust-and-reviewer-navigation-checkpoint.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0067-add-public-trust-reviewer-navigation-checkpoint.md")
    issue = read_text("planning/issues/0066-add-public-trust-reviewer-navigation-checkpoint.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link public trust reviewer navigation checkpoint")
    require("Public Trust and Reviewer Navigation" in readme, "README must mention public trust reviewer navigation")
    require("Public Trust and Reviewer Navigation Checkpoint" in doc, "public trust reviewer navigation doc must exist")

    required_sections = [
        "Public trust signals",
        "Public first-time reader path",
        "Technical reviewer path",
        "Security reviewer path",
        "Commercial reviewer path",
        "Licensing reviewer path",
        "Maintainer operations reviewer path",
        "Recommended review questions",
        "Product introduction boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"navigation doc must include section: {section}")

    required_phrases = [
        "The public repository may function as a product introduction.",
        "This checkpoint is a public navigation aid only.",
        "show the control model",
        "show the safety posture",
        "show the validation posture",
        "show licensing and commercial-use boundaries",
        "show governance readiness",
        "show release operations",
        "avoid claiming production readiness",
        "avoid claiming certification",
        "avoid claiming legal approval",
        "avoid claiming audit opinion",
        "avoid claiming scan authorization",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"navigation doc must include phrase: {phrase}")

    required_paths = [
        "README.md",
        "SECURITY.md",
        "LICENSE",
        "NOTICE",
        "AUTHORS",
        "COPYRIGHT",
        "COMMERCIAL-LICENSE.md",
        "TRADEMARKS.md",
        "CONTRIBUTING.md",
        "tools/run_all_local_checks.py",
        ".github/workflows/validate.yml",
        "CHANGELOG.md",
        "ROADMAP.md",
    ]
    for path in required_paths:
        require(path in doc, f"navigation doc must include path: {path}")

    required_related_docs = [
        "docs/54-licensing-and-commercial-use-boundary.md",
        "docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md",
        "docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md",
        "docs/60-github-actions-ci-scaffold.md",
        "docs/66-commercial-adoption-preparation-checkpoint.md",
        "docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md",
        "docs/69-licensing-trademark-authorship-protection-checkpoint.md",
        "docs/70-dependency-and-repository-governance-readiness-checkpoint.md",
        "docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md",
        "docs/72-release-governance-and-maintainer-operations-checklist.md",
    ]
    for related_doc in required_related_docs:
        require(related_doc in doc, f"navigation doc must link related doc: {related_doc}")

    reviewer_roles = [
        "technical reviewers",
        "security reviewers",
        "commercial reviewers",
        "licensing reviewers",
        "maintainer operations reviewers",
        "public first-time readers",
    ]
    for role in reviewer_roles:
        require(role in doc, f"navigation doc must include reviewer role: {role}")

    review_questions = [
        "What does the project claim to be?",
        "What does the project explicitly refuse to claim?",
        "What actions remain blocked?",
        "What evidence shows that runtime execution remains disabled?",
        "What tests can be run locally?",
        "What happens to generated private outputs?",
        "How are vulnerability reports handled?",
        "How are commercial inquiries separated from vulnerability reports?",
        "How are project names and related phrases controlled?",
        "How is release governance recorded?",
    ]
    for question in review_questions:
        require(question in doc, f"navigation doc must include review question: {question}")

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
        require(marker in doc, f"navigation doc must preserve marker: {marker}")

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
    ]
    for claim in claims_to_avoid:
        require(claim in claims_section, f"navigation claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "production deployment approved",
        "runtime execution enabled",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
        "certified compliant",
        "legal approval granted",
        "audit opinion issued",
        "commercial license granted",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden public trust navigation claim found: {claim}")

    require("Add public trust and reviewer navigation checkpoint" in adr, "ADR must record public trust navigation decision")
    require("Completed by v0.5.7 candidate" in issue, "Issue must record v0.5.7 completion status")
    require("## v0.5.7 - Public trust and reviewer navigation checkpoint" in changelog, "CHANGELOG must include v0.5.7")
    require("## v0.5.7 Public trust and reviewer navigation checkpoint" in roadmap, "ROADMAP must include v0.5.7")
    require("test_public_trust_reviewer_navigation.py" in run_all, "run_all must include public trust reviewer navigation test")

    print("Public trust and reviewer navigation tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
