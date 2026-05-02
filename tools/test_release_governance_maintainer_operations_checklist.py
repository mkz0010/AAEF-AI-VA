from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/72-release-governance-and-maintainer-operations-checklist.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0066-add-release-governance-maintainer-operations-checklist.md")
    issue = read_text("planning/issues/0065-add-release-governance-maintainer-operations-checklist.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link release governance checklist")
    require("Release Governance and Maintainer Operations Checklist" in readme, "README must mention release governance checklist")
    require("Release Governance and Maintainer Operations Checklist" in doc, "release governance checklist doc must exist")

    required_phrases = [
        "This checkpoint is an operations checklist only.",
        "This checkpoint does not configure GitHub branch protection.",
        "This checkpoint does not configure GitHub rulesets.",
        "This checkpoint does not configure tag protection.",
        "python tools/run_all_local_checks.py",
        "git ls-files private-not-in-git",
        "Verify GitHub Actions after push.",
        "Emergency exceptions do not authorize runtime execution",
        "The expected result is no tracked files.",
        "GitHub Actions validation: enabled",
        "Runtime execution: disabled",
        "Live scanning: not authorized",
        "Customer-target operation: not authorized",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"release governance doc must include phrase: {phrase}")

    required_sections = [
        "Standard release workflow",
        "Pre-release checklist",
        "Commit and merge checklist",
        "Tag and push checklist",
        "GitHub Actions verification checklist",
        "Private artifact checklist",
        "Emergency exception checklist",
        "Post-release review checklist",
        "Relationship to existing checkpoints",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"release governance doc must include section: {section}")

    required_related_links = [
        "docs/60-github-actions-ci-scaffold.md",
        "docs/65-github-release-publication-checkpoint.md",
        "docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md",
        "docs/69-licensing-trademark-authorship-protection-checkpoint.md",
        "docs/70-dependency-and-repository-governance-readiness-checkpoint.md",
        "docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md",
    ]
    for link in required_related_links:
        require(link in doc, f"release governance doc must link related checkpoint: {link}")

    release_steps = [
        "Start from clean `main`",
        "Pull latest `origin/main` with fast-forward only",
        "Create a scoped feature branch",
        "Run `tools/run_all_local_checks.py`",
        "Fast-forward merge the feature branch",
        "Create a semantic version tag",
        "Push `main`",
        "Push the semantic version tag",
        "Verify GitHub Actions after push",
        "Confirm working tree is clean",
    ]
    for step in release_steps:
        require(step in doc, f"release governance doc must include workflow step: {step}")

    private_artifact_terms = [
        "`private-not-in-git/` is not tracked",
        "private sales materials remain under `private-not-in-git/`",
        "no customer-specific material is committed",
        "no secrets or credentials are committed",
        "no sensitive vulnerability details are committed",
    ]
    for term in private_artifact_terms:
        require(term in doc, f"release governance doc must include private artifact term: {term}")

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
        require(marker in doc, f"release governance doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"release governance claims-to-avoid section must include: {claim}")

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
        require(claim not in combined, f"Forbidden release governance claim found: {claim}")

    require("Add release governance and maintainer operations checklist" in adr, "ADR must record release governance decision")
    require("Completed by v0.5.6 candidate" in issue, "Issue must record v0.5.6 completion status")
    require("## v0.5.6 - Release governance and maintainer operations checklist" in changelog, "CHANGELOG must include v0.5.6")
    require("## v0.5.6 Release governance and maintainer operations checklist" in roadmap, "ROADMAP must include v0.5.6")
    require("test_release_governance_maintainer_operations_checklist.py" in run_all, "run_all must include release governance maintainer operations test")

    print("Release governance and maintainer operations checklist tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
