from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def git_config_remotes() -> list[str]:
    result = subprocess.run(
        ["git", "remote"],
        cwd=str(REPO),
        text=True,
        capture_output=True,
        check=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    readme = read_text("README.md")
    doc = read_text("docs/58-first-publication-repository-settings-checklist.md")
    adr = read_text("planning/decisions/ADR-0052-add-first-publication-repository-settings-checklist.md")
    issue = read_text("planning/issues/0051-add-first-publication-repository-settings-checklist.md")
    run_all = read_text("tools/run_all_local_checks.py")
    security = read_text("SECURITY.md")
    gitignore = read_text(".gitignore")

    require("First Publication Repository Settings" in readme, "README must mention first publication settings")
    require("docs/58-first-publication-repository-settings-checklist.md" in readme, "README must link checklist doc")

    require("First-Publication Repository Settings Checklist" in doc, "Checklist document must exist")
    require("does not create a remote repository" in doc, "Checklist must not create remote")
    require("does not authorize runtime execution" in doc.lower(), "Checklist must preserve runtime boundary")
    require("Repository visibility must be a manual author decision" in doc, "Visibility must be manual")
    require("Private-first" in doc and "Public" in doc and "Staged public" in doc, "Visibility options must be recorded")
    require("private vulnerability reporting" in doc.lower(), "Security setting must mention private vulnerability reporting")
    require("branch protection" in doc.lower(), "Checklist must mention branch protection")
    require("ruleset" in doc.lower(), "Checklist must mention rulesets")
    require("git remote add origin <REMOTE_URL>" in doc, "Checklist must show manual remote command placeholder")
    require("git push -u origin main" in doc, "Checklist must show manual main push candidate")
    require("git push origin --tags" in doc, "Checklist must show manual tag push candidate")
    require("Do not run these commands until" in doc, "Push commands must be explicitly gated")
    require("private-not-in-git/" in doc, "Checklist must preserve private artifact boundary")

    require("first-publication repository settings checklist" in adr.lower(), "ADR must record checklist decision")
    require("must not create a remote repository" in adr.lower(), "ADR must preserve no-remote behavior")
    require("Completed by v0.3.9 candidate" in issue, "Issue must record v0.3.9 completion status")
    require("test_first_publication_repository_settings_checklist.py" in run_all, "run_all must include first publication test")

    require("# Security Policy" in security, "SECURITY.md must still exist")
    require("private-not-in-git/" in gitignore, ".gitignore must still exclude private-not-in-git/")

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
        require(marker in doc, f"First publication checklist must preserve marker: {marker}")

    forbidden_positive_claims = [
        "remote repository created",
        "origin has been added",
        "pushed to github",
        "runtime execution enabled",
        "network activity allowed",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
    ]
    combined_public_text = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined_public_text, f"Forbidden first-publication claim found: {claim}")

    # Current local project is expected to remain local-only unless the author manually adds a remote.
    # If a remote is later added, this test should not fail solely because publication has progressed.
    remotes = git_config_remotes()
    if remotes:
        print(f"First publication checklist note: existing remotes detected: {', '.join(remotes)}")
    else:
        print("First publication checklist note: no git remotes detected.")

    print("First-publication repository settings checklist tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
