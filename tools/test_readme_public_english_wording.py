from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains_japanese(text: str) -> bool:
    return bool(re.search(r"[\u3040-\u30ff\u3400-\u9fff]", text))


def main() -> int:
    readme = read_text("README.md")
    doc = read_text("docs/61-readme-public-english-wording-cleanup.md")
    adr = read_text("planning/decisions/ADR-0055-clean-up-readme-public-english-wording.md")
    issue = read_text("planning/issues/0054-clean-up-readme-public-english-wording.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    forbidden_readme_phrases = [
        "AAEF制御型AI脆弱性診断基盤のローカル管理リポジトリ",
        "AIの出力は診断行為の権限ではない",
        "AIは診断行為を要求できるが",
        "契約スコープ",
        "人間レビュー",
    ]

    for phrase in forbidden_readme_phrases:
        require(phrase not in readme, f"README must not contain Japanese/internal phrase: {phrase}")

    require(not contains_japanese(readme), "README should be English-first and contain no Japanese characters")
    require(
        "A safety-first reference implementation for AI-assisted vulnerability assessment control boundaries." in readme,
        "README must contain English public positioning",
    )
    require(
        "AI output is not authority to perform assessment actions." in readme,
        "README must contain English AI authority boundary",
    )
    require(
        "AI may request assessment actions, but execution is decided by the AAEF Authorization Gateway, Tool Gateway, contractual scope, and human review." in readme,
        "README must contain English execution-decision boundary",
    )

    required_readme_markers = [
        "GNU Affero General Public License v3.0",
        "SECURITY.md",
        ".github/workflows/validate.yml",
        "private-not-in-git/",
        "tools/run_all_local_checks.py",
    ]
    for marker in required_readme_markers:
        require(marker in readme, f"README must preserve marker: {marker}")

    require("README Public English Wording Cleanup" in doc, "README wording cleanup doc must exist")
    require("English-first" in doc, "README wording cleanup doc must define English-first posture")
    require("does not change any runtime authorization boundary" in doc, "doc must preserve runtime boundary")
    require("Clean up README public English wording" in adr, "ADR must record README cleanup decision")
    require("Completed by v0.4.2 candidate" in issue, "Issue must record v0.4.2 completion status")
    require("## v0.4.2 - README public English wording cleanup" in changelog, "CHANGELOG must include v0.4.2")
    require("## v0.4.2 README public English wording cleanup" in roadmap, "ROADMAP must include v0.4.2")
    require("test_readme_public_english_wording.py" in run_all, "run_all must include README wording test")

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
        "is a production-ready scanner",
        "is a production scanner",
        "is an autonomous vulnerability scanner",
        "is a customer-ready assessment platform",
    ]
    combined_public_text = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined_public_text, f"Forbidden README cleanup claim found: {claim}")

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

    print("README public English wording tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
