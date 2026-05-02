from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/74-public-front-page-and-repository-landing-polish-checkpoint.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0068-add-public-front-page-repository-landing-polish-checkpoint.md")
    issue = read_text("planning/issues/0067-add-public-front-page-repository-landing-polish-checkpoint.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link public front page landing polish checkpoint")
    require("Public Front Page and Repository Landing Polish" in readme, "README must mention public front page landing polish")
    require("Public Front Page and Repository Landing Polish Checkpoint" in doc, "front page landing polish doc must exist")

    required_sections = [
        "First-minute reviewer goals",
        "Above-the-fold README expectations",
        "Public value proposition",
        "Product introduction boundary",
        "Reviewer landing paths",
        "Trust-signal placement",
        "Commercial-use placement",
        "Security placement",
        "Validation placement",
        "README compatibility relationship",
        "Relationship to reviewer navigation",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"front page polish doc must include section: {section}")

    required_phrases = [
        "The repository may be discovered before any direct sales conversation",
        "This checkpoint is presentation and navigation polish only.",
        "This checkpoint does not create commercial sales material.",
        "AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.",
        "AI output is not authority to perform assessment actions.",
        "Runtime execution remains disabled.",
        "Live scanning is not authorized.",
        "Customer-target operation is not authorized.",
        "commercial licensing inquiries",
        "private vulnerability reporting is enabled",
        "python tools/run_all_local_checks.py",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"front page polish doc must include phrase: {phrase}")

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
        "docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md",
        "docs/73-public-trust-and-reviewer-navigation-checkpoint.md",
    ]
    for path in required_paths:
        require(path in doc, f"front page polish doc must include path: {path}")

    reviewer_landing_terms = [
        "First-time reader",
        "Technical reviewer",
        "Security reviewer",
        "Commercial reviewer",
        "Licensing reviewer",
        "Maintainer operations reviewer",
        "Public trust reviewer",
    ]
    for term in reviewer_landing_terms:
        require(term in doc, f"front page polish doc must include reviewer landing term: {term}")

    product_boundary_terms = [
        "show the control model",
        "show the safety posture",
        "show the validation posture",
        "show licensing and commercial-use boundaries",
        "show governance readiness",
        "show release operations",
        "show reviewer navigation",
        "show what remains blocked",
    ]
    for term in product_boundary_terms:
        require(term in doc, f"front page polish doc must include product boundary term: {term}")

    compatibility_phrases = [
        "AI output is not authority to perform assessment actions.",
        "Runtime execution remains disabled.",
        "Live scanning | Not authorized",
        "Customer-target operation | Not authorized",
        "commercial licensing inquiries",
        "CC BY 4.0",
        "GNU Affero General Public License v3.0",
    ]
    for phrase in compatibility_phrases:
        require(phrase in doc, f"front page polish doc must include compatibility phrase: {phrase}")

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
        require(marker in doc, f"front page polish doc must preserve marker: {marker}")

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
    ]
    for claim in claims_to_avoid:
        require(claim in claims_section, f"front page claims-to-avoid section must include: {claim}")

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
        "safety guaranteed",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden front page polish claim found: {claim}")

    require("Add public front page and repository landing polish checkpoint" in adr, "ADR must record front page polish decision")
    require("Completed by v0.5.8 candidate" in issue, "Issue must record v0.5.8 completion status")
    require("## v0.5.8 - Public front page and repository landing polish checkpoint" in changelog, "CHANGELOG must include v0.5.8")
    require("## v0.5.8 Public front page and repository landing polish checkpoint" in roadmap, "ROADMAP must include v0.5.8")
    require("test_public_front_page_landing_polish.py" in run_all, "run_all must include public front page landing polish test")

    print("Public front page and repository landing polish tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
