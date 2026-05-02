from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def git_remotes() -> list[str]:
    result = subprocess.run(
        ["git", "remote"],
        cwd=str(REPO),
        text=True,
        capture_output=True,
        check=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def git_ls_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=str(REPO),
        text=True,
        capture_output=True,
        check=True,
    )
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    readme = read_text("README.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    doc = read_text("docs/59-v040-publication-preparation-release.md")
    adr = read_text("planning/decisions/ADR-0053-prepare-v040-publication-preparation-release.md")
    issue = read_text("planning/issues/0052-prepare-v040-publication-preparation-release.md")
    run_all = read_text("tools/run_all_local_checks.py")
    license_text = read_text("LICENSE")
    security = read_text("SECURITY.md")
    gitignore = read_text(".gitignore")

    require("v0.4.0 Public Publication Preparation Release" in readme, "README must mention v0.4.0 publication preparation")
    require("docs/59-v040-publication-preparation-release.md" in readme, "README must link v0.4.0 doc")
    require("## v0.4.0 - Public publication preparation release" in changelog, "CHANGELOG must include v0.4.0")
    require("## v0.4.0 Public publication preparation release" in roadmap, "ROADMAP must include v0.4.0")

    require("v0.4.0 Public Publication Preparation Release" in doc, "v0.4.0 document must exist")
    for version in ["v0.3.5", "v0.3.6", "v0.3.7", "v0.3.8", "v0.3.9"]:
        require(version in doc, f"v0.4.0 doc must summarize {version}")

    require("staged public" in doc.lower(), "v0.4.0 doc must recommend staged public path")
    require("git remote add origin <REMOTE_URL>" in doc, "v0.4.0 doc must include manual remote candidate")
    require("git push -u origin main" in doc, "v0.4.0 doc must include manual main push candidate")
    require("git push origin --tags" in doc, "v0.4.0 doc must include manual tag push candidate")
    require("These commands are intentionally documented, not automated." in doc, "v0.4.0 doc must state commands are not automated")
    require("Announcement draft" in doc, "v0.4.0 doc must include announcement draft")
    require("Claims to avoid" in doc, "v0.4.0 doc must include claim boundaries")
    require("not a production scanner" in doc.lower(), "v0.4.0 doc must avoid production scanner claim")
    require("does not authorize live scanning" in doc.lower(), "v0.4.0 doc must preserve scanning boundary")
    require("AGPL-3.0" in doc, "v0.4.0 doc must mention AGPL-3.0")
    require("commercial licensing" in doc.lower(), "v0.4.0 doc must mention commercial licensing path")

    require("Prepare v0.4.0 public publication preparation release" in adr, "ADR must record v0.4.0 decision")
    require("must not create a remote repository" in adr.lower(), "ADR must prohibit automated remote creation")
    require("Completed by v0.4.0 candidate" in issue, "Issue must record v0.4.0 completion status")
    require("test_v040_publication_preparation_release.py" in run_all, "run_all must include v0.4.0 test")

    require("GNU AFFERO GENERAL PUBLIC LICENSE" in license_text, "LICENSE must remain AGPL-3.0")
    require("# Security Policy" in security, "SECURITY.md must remain present")
    require("private-not-in-git/" in gitignore, ".gitignore must exclude private-not-in-git/")

    required_docs = [
        "docs/54-licensing-and-commercial-use-boundary.md",
        "docs/55-public-repository-readiness-checkpoint.md",
        "docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md",
        "docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md",
        "docs/58-first-publication-repository-settings-checklist.md",
    ]
    tracked = set(git_ls_files())
    for required in required_docs:
        require(required in tracked, f"Required publication-readiness doc must be tracked: {required}")

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
        require(marker in doc, f"v0.4.0 document must preserve marker: {marker}")

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
        require(claim not in combined_public_text, f"Forbidden v0.4.0 claim found: {claim}")

    claims_to_avoid_section = doc.split("Claims to avoid:", 1)[1].split("## Announcement draft", 1)[0]
    for avoided_claim in [
        "production-ready scanner",
        "autonomous vulnerability scanner",
        "customer-ready assessment platform",
    ]:
        require(
            avoided_claim in claims_to_avoid_section.lower(),
            f"v0.4.0 doc must explicitly list avoided claim: {avoided_claim}",
        )

    remotes = git_remotes()
    if remotes:
        print(f"v0.4.0 publication preparation note: existing remotes detected: {', '.join(remotes)}")
    else:
        print("v0.4.0 publication preparation note: no git remotes detected.")

    print("v0.4.0 publication preparation release tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
