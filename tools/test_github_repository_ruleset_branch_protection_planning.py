from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0065-add-github-repository-ruleset-branch-protection-planning-checkpoint.md")
    issue = read_text("planning/issues/0064-add-github-repository-ruleset-branch-protection-planning-checkpoint.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link repository ruleset and branch protection planning checkpoint")
    require("GitHub Repository Ruleset and Branch Protection Planning" in readme, "README must mention repository ruleset planning")
    require("GitHub Repository Ruleset and Branch Protection Planning Checkpoint" in doc, "ruleset planning doc must exist")

    required_phrases = [
        "This checkpoint is planning only.",
        "This checkpoint does not configure GitHub branch protection.",
        "This checkpoint does not configure GitHub rulesets.",
        "This checkpoint does not apply these settings.",
        "This checkpoint does not configure tag protection.",
        "python tools/run_all_local_checks.py",
        "Private vulnerability reporting: enabled",
        "Runtime execution: disabled",
        "Live scanning: not authorized",
        "Customer-target operation: not authorized",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"ruleset planning doc must include phrase: {phrase}")

    required_sections = [
        "Planned protection scope",
        "Planned `main` branch protections",
        "Planned required checks",
        "Planned release tag protections",
        "High-risk change review expectations",
        "Emergency exception planning",
        "Maintainer responsibility planning",
        "GitHub administration checklist",
        "Relationship to existing checkpoints",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"ruleset planning doc must include section: {section}")

    required_existing_links = [
        "docs/55-public-repository-readiness-checkpoint.md",
        "docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md",
        "docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md",
        "docs/60-github-actions-ci-scaffold.md",
        "docs/65-github-release-publication-checkpoint.md",
        "docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md",
        "docs/69-licensing-trademark-authorship-protection-checkpoint.md",
        "docs/70-dependency-and-repository-governance-readiness-checkpoint.md",
    ]
    for link in required_existing_links:
        require(link in doc, f"ruleset planning doc must link related checkpoint: {link}")

    high_risk_terms = [
        "runtime execution",
        "network activity",
        "scanning",
        "credential handling",
        "target binding",
        "customer-target operation",
        "AGPL-3.0 license boundary",
        "commercial licensing boundary",
        "public claims",
    ]
    for term in high_risk_terms:
        require(term in doc, f"ruleset planning doc must include high-risk review term: {term}")

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
        require(marker in doc, f"ruleset planning doc must preserve marker: {marker}")

    claims_section = doc.split("## Claims to avoid", 1)[1].split("## Required local checks", 1)[0].lower()
    claims_to_avoid = [
        "github branch protection configured",
        "github rulesets configured",
        "tag protection configured",
        "mandatory pull request workflow enabled",
        "production deployment approval",
        "runtime execution readiness",
        "scan authorization",
        "customer-target authorization",
        "compliance certification",
        "legal approval",
        "audit opinion",
    ]
    for claim in claims_to_avoid:
        require(claim in claims_section, f"ruleset planning claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "github branch protection configured.",
        "github rulesets configured.",
        "tag protection configured.",
        "mandatory pull request workflow enabled.",
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
        require(claim not in combined, f"Forbidden ruleset planning claim found: {claim}")

    require("Add GitHub repository ruleset and branch protection planning checkpoint" in adr, "ADR must record ruleset planning decision")
    require("Completed by v0.5.5 candidate" in issue, "Issue must record v0.5.5 completion status")
    require("## v0.5.5 - GitHub repository ruleset and branch protection planning checkpoint" in changelog, "CHANGELOG must include v0.5.5")
    require("## v0.5.5 GitHub repository ruleset and branch protection planning checkpoint" in roadmap, "ROADMAP must include v0.5.5")
    require("test_github_repository_ruleset_branch_protection_planning.py" in run_all, "run_all must include repository ruleset planning test")

    print("GitHub repository ruleset and branch protection planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
