from __future__ import annotations

import re
import subprocess
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


def git_ls_files() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=str(REPO),
        text=True,
        capture_output=True,
        check=True,
    )
    return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}


def main() -> int:
    readme = read_text("README.md")
    doc = read_text("docs/65-github-release-publication-checkpoint.md")
    adr = read_text("planning/decisions/ADR-0059-add-github-release-publication-checkpoint.md")
    issue = read_text("planning/issues/0058-add-github-release-publication-checkpoint.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")
    gitignore = read_text(".gitignore")

    require("## GitHub Release Publication Checkpoint" in readme, "README must include GitHub Release publication checkpoint section")
    require("docs/65-github-release-publication-checkpoint.md" in readme, "README must link release publication checkpoint doc")
    require(RELEASE_URL in readme, "README must record release URL")
    require(RELEASE_TITLE in readme, "README must record release title")
    require(not contains_japanese(readme), "README must remain English-first")

    require("GitHub Release Publication Checkpoint" in doc, "release publication checkpoint doc must exist")
    require(REPO_URL in doc, "checkpoint must record repository URL")
    require(RELEASE_URL in doc, "checkpoint must record release URL")
    require(RELEASE_TITLE in doc, "checkpoint must record release title")
    require("Release tag: v0.4.5" in doc, "checkpoint must record release tag")
    require("Release type: Latest" in doc, "checkpoint must record latest release type")
    require("Release status: published" in doc, "checkpoint must record published status")
    require("private-not-in-git/release-notes/v0.4.5-release-notes.md" in doc, "checkpoint must record private release notes source")
    require("AI output is treated as a request, not authority." in doc, "checkpoint must preserve authority boundary")
    require("The release is not a live scanner." in doc, "checkpoint must preserve live scanner boundary")
    require("does not authorize third-party scanning, external network testing, credential injection, or customer-target operation" in doc, "checkpoint must preserve scan authorization boundary")
    require("Private vulnerability reporting is enabled" in doc, "checkpoint must record private vulnerability reporting")
    require("GitHub Actions validation is active" in doc, "checkpoint must record Actions validation")

    require("Add GitHub release publication checkpoint" in adr, "ADR must record release publication checkpoint decision")
    require("Completed by v0.4.6 candidate" in issue, "Issue must record v0.4.6 completion status")
    require("## v0.4.6 - GitHub release publication checkpoint" in changelog, "CHANGELOG must include v0.4.6")
    require("## v0.4.6 GitHub release publication checkpoint" in roadmap, "ROADMAP must include v0.4.6")
    require("test_github_release_publication_checkpoint.py" in run_all, "run_all must include release publication checkpoint test")

    require("private-not-in-git/" in gitignore, ".gitignore must exclude private-not-in-git/")
    tracked = git_ls_files()
    private_tracked = [path for path in tracked if path.startswith("private-not-in-git/")]
    require(not private_tracked, f"private-not-in-git files must not be tracked: {private_tracked[:5]}")

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
        require(marker in doc, f"release publication checkpoint doc must preserve marker: {marker}")

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
        "replacement for professional security judgment",
    ]:
        require(
            avoided_claim in claims_to_avoid_section,
            f"release publication checkpoint must explicitly list avoided claim: {avoided_claim}",
        )

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
        require(claim not in combined_public_text, f"Forbidden release publication checkpoint claim found: {claim}")

    print("GitHub Release publication checkpoint tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
