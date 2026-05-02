from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/mkz0010/AAEF-AI-VA"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains_japanese(text: str) -> bool:
    return bool(re.search(r"[\u3040-\u30ff\u3400-\u9fff]", text))


def main() -> int:
    readme = read_text("README.md")
    doc = read_text("docs/63-public-repository-launch-checkpoint.md")
    adr = read_text("planning/decisions/ADR-0057-add-public-repository-launch-checkpoint.md")
    issue = read_text("planning/issues/0056-add-public-repository-launch-checkpoint.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require("## Public Repository Launch Checkpoint" in readme, "README must include public launch checkpoint section")
    require("docs/63-public-repository-launch-checkpoint.md" in readme, "README must link launch checkpoint doc")
    require(REPO_URL in readme, "README must record repository URL")
    require(not contains_japanese(readme), "README must remain English-first")

    require("Public Repository Launch Checkpoint" in doc, "launch checkpoint doc must exist")
    require(REPO_URL in doc, "launch checkpoint must record repository URL")
    require("Visibility: PUBLIC" in doc, "launch checkpoint must record public visibility")
    require("isPrivate: false" in doc, "launch checkpoint must record non-private state")
    require("origin: https://github.com/mkz0010/AAEF-AI-VA.git" in doc, "launch checkpoint must record origin URL")
    require("Private vulnerability reporting | Enabled" in doc, "launch checkpoint must record private vulnerability reporting")
    require("enabled: true" in doc, "launch checkpoint must record private vulnerability reporting verification")
    require("Validate AAEF-AI-VA artifacts" in doc, "launch checkpoint must record workflow name")
    require("workflow_dispatch run ID: 25254907292" in doc, "launch checkpoint must record observed workflow dispatch run")
    require("GitHub Actions status | Passing" in doc, "launch checkpoint must record passing Actions status")
    require("Safety-first reference implementation for AI-assisted vulnerability assessment control boundaries" in doc, "launch checkpoint must record description")
    require("Issues | Enabled" in doc, "launch checkpoint must record Issues enabled")
    require("Discussions | Disabled" in doc, "launch checkpoint must record Discussions disabled")
    require("Wiki | Disabled" in doc, "launch checkpoint must record Wiki disabled")
    require("Projects | Disabled" in doc, "launch checkpoint must record Projects disabled")

    required_topics = [
        "agentic-ai",
        "agpl",
        "ai-assurance",
        "ai-security",
        "auditability",
        "security-automation",
        "security-controls",
        "vulnerability-assessment",
    ]
    for topic in required_topics:
        require(topic in doc, f"launch checkpoint must record topic: {topic}")

    require("Add public repository launch checkpoint" in adr, "ADR must record launch checkpoint decision")
    require("Completed by v0.4.4 candidate" in issue, "Issue must record v0.4.4 completion status")
    require("## v0.4.4 - Public repository launch checkpoint" in changelog, "CHANGELOG must include v0.4.4")
    require("## v0.4.4 Public repository launch checkpoint" in roadmap, "ROADMAP must include v0.4.4")
    require("test_public_repository_launch_checkpoint.py" in run_all, "run_all must include launch checkpoint test")

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
        require(marker in doc, f"launch checkpoint doc must preserve marker: {marker}")

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
    ]
    combined_public_text = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined_public_text, f"Forbidden launch checkpoint claim found: {claim}")

    claims_to_avoid_section = doc.split("Claims to avoid:", 1)[1].split("## Required local checks", 1)[0].lower()
    for avoided_claim in [
        "production scanner",
        "autonomous vulnerability scanner",
        "customer-ready assessment platform",
        "permission to scan third-party systems",
        "credential-handling readiness",
        "compliance certification",
        "legal approval",
        "audit opinion",
    ]:
        require(
            avoided_claim in claims_to_avoid_section,
            f"launch checkpoint must explicitly list avoided claim: {avoided_claim}",
        )

    print("Public repository launch checkpoint tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
