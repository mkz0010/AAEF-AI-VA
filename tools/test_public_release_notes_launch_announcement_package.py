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
    doc = read_text("docs/64-public-release-notes-and-launch-announcement-package.md")
    adr = read_text("planning/decisions/ADR-0058-add-public-release-notes-launch-announcement-package.md")
    issue = read_text("planning/issues/0057-add-public-release-notes-launch-announcement-package.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require("## Public Release Notes and Launch Announcement Package" in readme, "README must include release notes package section")
    require("docs/64-public-release-notes-and-launch-announcement-package.md" in readme, "README must link release notes package doc")
    require(not contains_japanese(readme), "README must remain English-first")

    require("Public Release Notes and Launch Announcement Package" in doc, "release notes package doc must exist")
    require(REPO_URL in doc, "release notes package must include repository URL")
    require("GitHub Release notes draft" in doc, "release notes package must include GitHub Release notes draft")
    require("Short public introduction" in doc, "release notes package must include short introduction")
    require("Longer public announcement" in doc, "release notes package must include longer announcement")
    require("LinkedIn-style announcement draft" in doc, "release notes package must include LinkedIn draft")
    require("Zenn/Qiita-style technical article lead" in doc, "release notes package must include technical article lead")
    require("Commercial inquiry wording" in doc, "release notes package must include commercial inquiry wording")
    require("Security reporting wording" in doc, "release notes package must include security reporting wording")
    require("Claims to use" in doc, "release notes package must include claims to use")
    require("Claims to avoid" in doc, "release notes package must include claims to avoid")
    require("Manual publication checklist" in doc, "release notes package must include manual publication checklist")

    required_phrases = [
        "AI output is not authority to perform assessment actions.",
        "This is not a live scanner",
        "does not authorize third-party scanning",
        "Private vulnerability reporting is enabled",
        "AGPL-3.0",
        "separate commercial license discussion",
        "runtime execution remains disabled",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"release notes package must include phrase: {phrase}")

    require("Add public release notes and launch announcement package" in adr, "ADR must record release notes package decision")
    require("Completed by v0.4.5 candidate" in issue, "Issue must record v0.4.5 completion status")
    require("## v0.4.5 - Public release notes and launch announcement package" in changelog, "CHANGELOG must include v0.4.5")
    require("## v0.4.5 Public release notes and launch announcement package" in roadmap, "ROADMAP must include v0.4.5")
    require("test_public_release_notes_launch_announcement_package.py" in run_all, "run_all must include release notes package test")

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
        require(marker in doc, f"release notes package doc must preserve marker: {marker}")

    claims_to_avoid_section = doc.split("Claims to avoid", 1)[1].split("## Runtime and scanning boundary", 1)[0].lower()
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
            f"release notes package must explicitly list avoided claim: {avoided_claim}",
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
        require(claim not in combined_public_text, f"Forbidden release notes package claim found: {claim}")

    print("Public release notes and launch announcement package tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
