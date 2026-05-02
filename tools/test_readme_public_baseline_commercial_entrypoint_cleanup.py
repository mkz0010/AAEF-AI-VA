from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/mkz0010/AAEF-AI-VA"
RELEASE_URL = "https://github.com/mkz0010/AAEF-AI-VA/releases/tag/v0.4.5"
RELEASE_TITLE = "AAEF-AI-VA v0.4.5 Public Launch Communication Package"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains_japanese(text: str) -> bool:
    return bool(re.search(r"[\u3040-\u30ff\u3400-\u9fff]", text))


def main() -> int:
    readme = read_text("README.md")
    doc = read_text("docs/67-readme-public-baseline-and-commercial-entrypoint-cleanup.md")
    adr = read_text("planning/decisions/ADR-0061-clean-up-readme-public-baseline-commercial-entrypoint.md")
    issue = read_text("planning/issues/0060-clean-up-readme-public-baseline-commercial-entrypoint.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(readme.startswith("# AAEF-AI-VA"), "README must start with project title")
    first_1200 = readme[:1200]
    require("## Current public baseline" in first_1200, "README must present current public baseline near the top")
    require("v0.3.4 Negative preflight evidence examples" not in first_1200, "README must not lead with old v0.3.4 checkpoint")
    require("This repository is local-first and private by default." not in readme, "README must not contain obsolete local-first/private-by-default wording")
    require("AI output is not authority to perform assessment actions.AI may request" not in readme, "README must not jam authority sentences together")
    require("AI output is not authority to perform assessment actions.\n\nAI may request assessment actions" in readme, "README must separate authority-boundary sentences")
    require("## What this is" in readme, "README must include What this is")
    require("## What this is not" in readme, "README must include What this is not")
    require("## Commercial adoption entrypoint" in readme, "README must include commercial adoption entrypoint")
    require("Runtime execution remains disabled." in readme, "README must preserve runtime disabled statement")
    require("Live scanning | Not authorized" in readme, "README must record live scanning boundary")
    require("Customer-target operation | Not authorized" in readme, "README must record customer-target boundary")
    require(REPO_URL in readme, "README must include repository URL")
    require(RELEASE_URL in readme, "README must include release URL")
    require(RELEASE_TITLE in readme, "README must include release title")
    require("GNU Affero General Public License v3.0" in readme, "README must include AGPL-3.0 license text")
    require("CC BY 4.0" in readme, "README must preserve AAEF CC BY 4.0 short-form attribution")
    require("Creative Commons Attribution 4.0 International" in readme, "README must preserve AAEF CC BY 4.0 attribution")
    require("https://github.com/mkz0010/agentic-authority-evidence-framework" in readme, "README must preserve parent AAEF repository URL")
    require("SECURITY.md" in readme, "README must include SECURITY.md")
    require("## Security Policy" in readme, "README must preserve Security Policy heading compatibility")
    require(".github/workflows/validate.yml" in readme, "README must include workflow path")
    require("private-not-in-git/" in readme, "README must include private artifact boundary")
    require("Publication Hygiene and Private Artifact Boundary" in readme, "README must preserve publication hygiene compatibility phrase")
    require("tools/run_all_local_checks.py" in readme, "README must include local checks entrypoint")
    require("docs/66-commercial-adoption-preparation-checkpoint.md" in readme, "README must link commercial adoption checkpoint")
    require("commercial licensing inquiries" in readme, "README must preserve commercial licensing inquiry wording")
    require("docs/65-github-release-publication-checkpoint.md" in readme, "README must link release publication checkpoint")
    require("docs/63-public-repository-launch-checkpoint.md" in readme, "README must link public launch checkpoint")
    require("## Public Repository Metadata" in readme, "README must preserve Public Repository Metadata heading compatibility")
    require(not contains_japanese(readme), "README must remain English-first")

    require("README Public Baseline and Commercial Entrypoint Cleanup" in doc, "cleanup doc must exist")
    require("does not change any runtime authorization boundary" in doc, "cleanup doc must preserve runtime boundary")
    require("README compatibility note" in doc, "README cleanup doc must include compatibility note")
    require("test_public_facing_repository_metadata_announcement_pack.py" in doc, "README cleanup doc must mention metadata pack compatibility")
    require("Clean up README public baseline and commercial entrypoint" in adr, "ADR must record README cleanup decision")
    require("Completed by v0.5.1 candidate" in issue, "Issue must record v0.5.1 completion status")
    require("## v0.5.1 - README public baseline and commercial entrypoint cleanup" in changelog, "CHANGELOG must include v0.5.1")
    require("## v0.5.1 README public baseline and commercial entrypoint cleanup" in roadmap, "ROADMAP must include v0.5.1")
    require("test_readme_public_baseline_commercial_entrypoint_cleanup.py" in run_all, "run_all must include README public baseline cleanup test")

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
        require(marker in doc, f"README cleanup doc must preserve marker: {marker}")

    forbidden_positive_claims = [
        "runtime execution: enabled",
        "runtime execution enabled",
        "network activity: allowed",
        "network activity allowed",
        "scan execution: allowed",
        "scan execution allowed",
        "credential injection: permitted",
        "credential injection permitted",
        "customer target operation: allowed",
        "customer target operation allowed",
        "is a production scanner",
        "is an autonomous vulnerability scanner",
        "is a customer-ready managed assessment platform",
        "certified compliant",
        "legal approval granted",
        "audit opinion issued",
    ]
    combined_public_text = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined_public_text, f"Forbidden README baseline claim found: {claim}")

    what_this_is_not = readme.split("## What this is not", 1)[1].split("## Commercial adoption entrypoint", 1)[0].lower()
    for avoided_claim in [
        "production scanner",
        "autonomous vulnerability scanner",
        "customer-ready managed assessment platform",
        "compliance certification scheme",
        "legal advice",
        "audit opinion",
        "permission to scan third-party systems",
        "permission to inject credentials",
        "permission to operate against customer targets",
    ]:
        require(
            avoided_claim in what_this_is_not,
            f"README What this is not must explicitly list avoided claim: {avoided_claim}",
        )

    print("README public baseline and commercial entrypoint cleanup tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
