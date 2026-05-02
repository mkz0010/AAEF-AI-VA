from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    notice = read_text("NOTICE")
    authors = read_text("AUTHORS")
    copyright_text = read_text("COPYRIGHT")
    commercial = read_text("COMMERCIAL-LICENSE.md")
    trademarks = read_text("TRADEMARKS.md")
    contributing = read_text("CONTRIBUTING.md")
    doc = read_text("docs/69-licensing-trademark-authorship-protection-checkpoint.md")
    adr = read_text("planning/decisions/ADR-0063-add-licensing-trademark-authorship-protection-hardening.md")
    issue = read_text("planning/issues/0062-add-licensing-trademark-authorship-protection-hardening.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    for file_name in [
        "NOTICE",
        "AUTHORS",
        "COPYRIGHT",
        "COMMERCIAL-LICENSE.md",
        "TRADEMARKS.md",
        "CONTRIBUTING.md",
        "docs/69-licensing-trademark-authorship-protection-checkpoint.md",
    ]:
        require(file_name in readme, f"README must link {file_name}")

    required_common = [
        "AAEF-AI-VA",
        "GNU Affero General Public License v3.0",
        "CC BY 4.0",
        "Creative Commons Attribution 4.0 International",
        "https://github.com/mkz0010/agentic-authority-evidence-framework",
    ]

    for phrase in required_common:
        require(phrase in notice, f"NOTICE must include {phrase}")
        require(phrase in authors or phrase == "GNU Affero General Public License v3.0", f"AUTHORS must include parent/project attribution for {phrase}")
        require(phrase in copyright_text, f"COPYRIGHT must include {phrase}")

    require("commercial licensing inquiries" in notice, "NOTICE must include commercial inquiry boundary")
    require("Security reports should follow SECURITY.md" in notice, "NOTICE must include security reporting boundary")

    require("mkz0010" in authors, "AUTHORS must include project author")
    require("Future contributors" in authors, "AUTHORS must include contributor path")

    require("No separate commercial license is granted unless a separate written agreement" in commercial, "commercial license doc must deny implied grant")
    require("not legal advice" in commercial.lower(), "commercial license doc must include not legal advice")
    require("Commercial licensing inquiries are separate from vulnerability reports" in commercial, "commercial license doc must separate commercial and security reports")
    require("private-not-in-git/" in commercial, "commercial license doc must keep private proposal materials private")

    require("No registered trademark claim" in trademarks, "TRADEMARKS must avoid registered trademark overclaim")
    require("does not claim that\nAAEF-AI-VA is a registered trademark" in trademarks, "TRADEMARKS must explicitly avoid registered trademark claim")
    require("must not imply endorsement" in trademarks, "TRADEMARKS must prohibit false endorsement")
    require("Model output is not authority" in trademarks, "TRADEMARKS must include project identifier slogan")

    require("Inbound contribution license" in contributing, "CONTRIBUTING must include inbound contribution license")
    require("GNU Affero General Public License v3.0" in contributing, "CONTRIBUTING must preserve AGPL inbound boundary")
    require("Do not submit sensitive vulnerability details" in contributing, "CONTRIBUTING must protect vulnerability disclosure")
    require("commercial license" in contributing.lower(), "CONTRIBUTING must separate commercial license")

    require("Licensing, Trademark, Authorship, and Commercial-Use Protection Checkpoint" in doc, "protection checkpoint doc must exist")
    require("not legal advice" in doc.lower(), "protection checkpoint must avoid legal advice overclaim")
    require("does not claim registered trademark status" in doc, "checkpoint must avoid trademark overclaim")
    require("No commercial license is granted without a separate written agreement" in doc, "checkpoint must preserve no implied commercial grant")

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
        require(marker in doc, f"protection checkpoint must preserve marker: {marker}")

    forbidden_positive_claims = [
        "registered trademark of",
        "this document grants a commercial license",
        "a commercial license is granted by this document",
        "commercial license is granted by this repository",
        "commercial license is granted automatically",
        "runtime execution enabled",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
        "permission granted to scan",
        "certified compliant",
        "legal approval granted",
        "audit opinion issued",
    ]
    combined = "\n".join([readme, notice, authors, copyright_text, commercial, trademarks, contributing, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden protection claim found: {claim}")

    require("not legal advice" in combined, "documents must include not legal advice boundary")
    require("no separate commercial license is granted unless a separate written agreement" in combined, "documents must preserve no implied commercial license grant boundary")
    require("no commercial license grant is created" in combined, "documents must preserve contribution commercial license boundary")

    require("Add licensing, trademark, authorship, and commercial-use protection hardening" in adr, "ADR must record protection decision")
    require("Completed by v0.5.3 candidate" in issue, "Issue must record v0.5.3 completion status")
    require("## v0.5.3 - Licensing, trademark, authorship, and commercial-use protection hardening" in changelog, "CHANGELOG must include v0.5.3")
    require("## v0.5.3 Licensing, trademark, authorship, and commercial-use protection hardening" in roadmap, "ROADMAP must include v0.5.3")
    require("test_licensing_trademark_authorship_protection.py" in run_all, "run_all must include protection test")

    print("Licensing, trademark, authorship, and commercial-use protection tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
