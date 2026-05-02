from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/mkz0010/AAEF-AI-VA"
BADGE = "[![Validate AAEF-AI-VA artifacts](https://github.com/mkz0010/AAEF-AI-VA/actions/workflows/validate.yml/badge.svg)](https://github.com/mkz0010/AAEF-AI-VA/actions/workflows/validate.yml)"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains_japanese(text: str) -> bool:
    return bool(re.search(r"[\u3040-\u30ff\u3400-\u9fff]", text))


def main() -> int:
    readme = read_text("README.md")
    doc = read_text("docs/62-public-facing-repository-metadata-and-announcement-pack.md")
    adr = read_text("planning/decisions/ADR-0056-add-public-facing-repository-metadata-announcement-pack.md")
    issue = read_text("planning/issues/0055-add-public-facing-repository-metadata-announcement-pack.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(BADGE in readme, "README must include GitHub Actions validation badge")
    require("## Public Repository Metadata" in readme, "README must include public repository metadata section")
    require(REPO_URL in readme, "README must include repository URL")
    require("Safety-first reference implementation for AI-assisted vulnerability assessment control boundaries" in readme, "README must preserve public description")
    require("ai-security" in readme and "vulnerability-assessment" in readme, "README must include topic candidates")
    require(not contains_japanese(readme), "README must remain English-first")

    require("Public-Facing Repository Metadata and Announcement Pack" in doc, "metadata pack doc must exist")
    require(REPO_URL in doc, "metadata pack must record repository URL")
    require(BADGE in doc, "metadata pack must record README badge")
    require("Recommended topics:" in doc, "metadata pack must include recommended topics")
    require("Announcement draft" in doc, "metadata pack must include announcement draft")
    require("Claims to use" in doc, "metadata pack must include acceptable claims")
    require("Claims to avoid" in doc, "metadata pack must include claims to avoid")
    require("AI output is not authority to perform assessment actions." in doc, "metadata pack must preserve authority boundary")
    require("This is not a live scanner." in doc, "announcement must avoid live scanner implication")
    require("does not authorize runtime execution" in doc.lower(), "metadata pack must preserve runtime boundary")

    required_topics = [
        "ai-security",
        "vulnerability-assessment",
        "agentic-ai",
        "security-automation",
        "auditability",
        "agpl",
    ]
    for topic in required_topics:
        require(topic in doc, f"metadata pack must include topic: {topic}")

    require("Add public-facing repository metadata and announcement pack" in adr, "ADR must record metadata pack decision")
    require("Completed by v0.4.3 candidate" in issue, "Issue must record v0.4.3 completion status")
    require("## v0.4.3 - Public-facing repository metadata and announcement pack" in changelog, "CHANGELOG must include v0.4.3")
    require("## v0.4.3 Public-facing repository metadata and announcement pack" in roadmap, "ROADMAP must include v0.4.3")
    require("test_public_facing_repository_metadata_announcement_pack.py" in run_all, "run_all must include metadata pack test")

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
        require(marker in doc, f"metadata pack doc must preserve marker: {marker}")

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
        "is a production-ready scanner",
        "is a production scanner",
        "is an autonomous vulnerability scanner",
        "is a customer-ready assessment platform",
        "is a customer-ready managed assessment platform",
    ]
    combined_public_text = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined_public_text, f"Forbidden metadata pack claim found: {claim}")

    if "## What this is not" in readme:
        what_this_is_not = readme.split("## What this is not", 1)[1].split("## Commercial adoption entrypoint", 1)[0].lower()
        for avoided_claim in [
            "production scanner",
            "autonomous vulnerability scanner",
            "customer-ready managed assessment platform",
            "permission to scan third-party systems",
            "permission to inject credentials",
            "permission to operate against customer targets",
        ]:
            require(
                avoided_claim in what_this_is_not,
                f"README What this is not must explicitly list avoided claim: {avoided_claim}",
            )

    print("Public-facing repository metadata and announcement pack tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
