from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/70-dependency-and-repository-governance-readiness-checkpoint.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0064-add-dependency-repository-governance-readiness-checkpoint.md")
    issue = read_text("planning/issues/0063-add-dependency-repository-governance-readiness-checkpoint.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link dependency and repository governance readiness checkpoint")
    require("Dependency and Repository Governance Readiness" in readme, "README must mention governance readiness")
    require("Dependency and Repository Governance Readiness Checkpoint" in doc, "governance readiness doc must exist")

    required_sections = [
        "Dependency and license inventory expectations",
        "Current dependency posture",
        "Branch protection and ruleset planning",
        "Release and tag governance",
        "Security and disclosure governance",
        "Commercial-readiness relationship",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"governance readiness doc must include section: {section}")

    required_phrases = [
        "This checkpoint does not configure branch protection by itself.",
        "It is not a completed legal dependency audit.",
        "Security reports must not be mixed with commercial licensing inquiries.",
        "Sensitive vulnerability details should not be posted in public issues.",
        "Keep under `private-not-in-git/`",
        "semantic version tags",
        "Run `tools/run_all_local_checks.py`",
        "verify GitHub Actions",
        "This checkpoint does not create a commercial contract.",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"governance readiness doc must include phrase: {phrase}")

    required_existing_files = [
        "SECURITY.md",
        "NOTICE",
        "AUTHORS",
        "COPYRIGHT",
        "COMMERCIAL-LICENSE.md",
        "TRADEMARKS.md",
        "CONTRIBUTING.md",
        "LICENSE",
    ]
    for file_name in required_existing_files:
        require((REPO / file_name).exists(), f"expected repository protection file to exist: {file_name}")

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
        require(marker in doc, f"governance readiness doc must preserve marker: {marker}")

    claims_to_avoid = [
        "completed legal dependency review",
        "full software bill of materials",
        "production deployment approval",
        "branch protection configuration",
        "compliance certification",
        "legal approval",
        "audit opinion",
        "runtime execution readiness",
        "scan authorization",
        "customer-target authorization",
    ]
    claims_section = doc.split("## Claims to avoid", 1)[1].split("## Required local checks", 1)[0].lower()
    for claim in claims_to_avoid:
        require(claim in claims_section, f"governance readiness claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "branch protection configured",
        "full sbom generated",
        "legal dependency review completed",
        "runtime execution enabled",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
        "certified compliant",
        "legal approval granted",
        "audit opinion issued",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden governance readiness claim found: {claim}")

    require("Add dependency and repository governance readiness checkpoint" in adr, "ADR must record governance readiness decision")
    require("Completed by v0.5.4 candidate" in issue, "Issue must record v0.5.4 completion status")
    require("## v0.5.4 - Dependency and repository governance readiness checkpoint" in changelog, "CHANGELOG must include v0.5.4")
    require("## v0.5.4 Dependency and repository governance readiness checkpoint" in roadmap, "ROADMAP must include v0.5.4")
    require("test_dependency_repository_governance_readiness.py" in run_all, "run_all must include governance readiness test")

    print("Dependency and repository governance readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
