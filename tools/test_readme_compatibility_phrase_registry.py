from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0062-add-readme-compatibility-phrase-registry-test-design-hardening.md")
    issue = read_text("planning/issues/0061-add-readme-compatibility-phrase-registry-test-design-hardening.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link README compatibility phrase registry")
    require("README Compatibility Phrase Registry" in readme, "README must mention compatibility registry")
    require("README Compatibility Phrase Registry and Test Design Hardening" in doc, "registry doc must exist")
    require("Reject unsafe positive claims." in doc, "registry must reject unsafe positive claims")
    require("Allow explicit negative boundary statements." in doc, "registry must allow negative boundary statements")
    require("README-facing tests should avoid broad substring bans." in doc, "registry must discourage broad substring bans")

    required_headings = [
        "## Current public baseline",
        "## Core principle",
        "## What this is",
        "## What this is not",
        "## Commercial adoption entrypoint",
        "## Publication Hygiene and Private Artifact Boundary",
        "## Security Policy",
        "## Public Repository Metadata",
        "## License and commercial-use boundary",
        "## Publication and release checkpoints",
        "## Commercial Adoption Preparation",
    ]
    for heading in required_headings:
        require(heading in doc, f"registry must record heading: {heading}")

    required_phrases = [
        "AI output is not authority to perform assessment actions.",
        "Runtime execution remains disabled.",
        "Live scanning | Not authorized",
        "Customer-target operation | Not authorized",
        "private-not-in-git/",
        "SECURITY.md",
        ".github/workflows/validate.yml",
        "tools/run_all_local_checks.py",
        "GNU Affero General Public License v3.0",
        "CC BY 4.0",
        "Creative Commons Attribution 4.0 International",
        "https://github.com/mkz0010/agentic-authority-evidence-framework",
        "commercial licensing inquiries",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"registry must record phrase: {phrase}")
        require(phrase in readme, f"README must preserve phrase: {phrase}")

    required_links = [
        "docs/54-licensing-and-commercial-use-boundary.md",
        "docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md",
        "docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md",
        "docs/62-public-facing-repository-metadata-and-announcement-pack.md",
        "docs/63-public-repository-launch-checkpoint.md",
        "docs/64-public-release-notes-and-launch-announcement-package.md",
        "docs/65-github-release-publication-checkpoint.md",
        "docs/66-commercial-adoption-preparation-checkpoint.md",
        "docs/67-readme-public-baseline-and-commercial-entrypoint-cleanup.md",
    ]
    for link in required_links:
        require(link in doc, f"registry must record link: {link}")

    forbidden_positive_claims = [
        "runtime execution enabled",
        "network activity allowed",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
        "is a production scanner",
        "is a production-ready scanner",
        "is an autonomous vulnerability scanner",
        "is a customer-ready assessment platform",
        "certified compliant",
        "legal approval granted",
        "audit opinion issued",
    ]
    for claim in forbidden_positive_claims:
        require(claim in doc, f"registry must record forbidden positive claim: {claim}")

    allowed_negative_examples = [
        "not a production scanner",
        "not an autonomous vulnerability scanner",
        "not a customer-ready managed assessment platform",
    ]
    for example in allowed_negative_examples:
        require(example in doc, f"registry must record allowed negative example: {example}")

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
        require(marker in doc, f"registry must preserve marker: {marker}")

    require("Add README compatibility phrase registry and test design hardening" in adr, "ADR must record registry decision")
    require("Completed by v0.5.2 candidate" in issue, "Issue must record v0.5.2 completion status")
    require("## v0.5.2 - README compatibility phrase registry and test design hardening" in changelog, "CHANGELOG must include v0.5.2")
    require("## v0.5.2 README compatibility phrase registry and test design hardening" in roadmap, "ROADMAP must include v0.5.2")
    require("test_readme_compatibility_phrase_registry.py" in run_all, "run_all must include registry test")

    print("README compatibility phrase registry tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
