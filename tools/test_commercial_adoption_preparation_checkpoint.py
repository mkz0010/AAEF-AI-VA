from __future__ import annotations

import re
import subprocess
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
    doc = read_text("docs/66-commercial-adoption-preparation-checkpoint.md")
    adr = read_text("planning/decisions/ADR-0060-add-commercial-adoption-preparation-checkpoint.md")
    issue = read_text("planning/issues/0059-add-commercial-adoption-preparation-checkpoint.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")
    gitignore = read_text(".gitignore")

    require("## Commercial Adoption Preparation" in readme, "README must include commercial adoption section")
    require("docs/66-commercial-adoption-preparation-checkpoint.md" in readme, "README must link commercial adoption doc")
    require(not contains_japanese(readme), "README must remain English-first")

    require("Commercial Adoption Preparation Checkpoint" in doc, "commercial adoption doc must exist")
    doc_lower = doc.lower()
    require(
        "public vs private material boundary" in doc_lower
        or "public/private commercial-material boundary" in doc_lower,
        "commercial adoption doc must record public/private boundary",
    )
    require("public repository material may include" in doc_lower, "commercial adoption doc must define public material")
    require("private material should include" in doc_lower, "commercial adoption doc must define private material")
    require("vulnerability assessment companies" in doc, "commercial adoption doc must mention target customers")
    require("MSSPs" in doc, "commercial adoption doc must mention MSSPs")
    require("AI output is not authority to perform assessment actions." in doc, "commercial adoption doc must preserve authority boundary")
    require("Difference from generic AI vulnerability assessment tools" in doc, "commercial adoption doc must include differentiation section")
    require("Suggested enterprise conversation flow" in doc, "commercial adoption doc must include conversation flow")
    require("Commercial inquiry wording" in doc, "commercial adoption doc must include commercial inquiry wording")
    require("private-not-in-git/commercial-adoption/v0.5.0-enterprise-sales-pack.md" in doc, "commercial adoption doc must record private sales pack path")
    require("This checkpoint does not set prices or contract terms." in doc, "commercial adoption doc must avoid finalized pricing/contracts")
    require("Commercial inquiries are separate from vulnerability reports" in doc, "commercial adoption doc must separate inquiries from vulnerability reports")
    require("does not authorize runtime execution" in doc.lower() or "does not authorize vulnerability scanning" in doc.lower(), "commercial adoption doc must preserve runtime boundary")

    require("Add commercial adoption preparation checkpoint" in adr, "ADR must record commercial adoption decision")
    require("Completed by v0.5.0 candidate" in issue, "Issue must record v0.5.0 completion status")
    require("## v0.5.0 - Commercial adoption preparation checkpoint" in changelog, "CHANGELOG must include v0.5.0")
    require("## v0.5.0 Commercial adoption preparation checkpoint" in roadmap, "ROADMAP must include v0.5.0")
    require("test_commercial_adoption_preparation_checkpoint.py" in run_all, "run_all must include commercial adoption test")

    require("private-not-in-git/" in gitignore, ".gitignore must exclude private-not-in-git/")
    tracked = git_ls_files()
    private_tracked = [path for path in tracked if path.startswith("private-not-in-git/")]
    require(not private_tracked, f"private-not-in-git files must not be tracked: {private_tracked[:5]}")

    forbidden_positive_terms = [
        "is guaranteed safe",
        "guaranteed safe for production",
        "certified compliant",
        "legal approval granted",
        "audit opinion issued",
        "permission granted to scan",
        "customer targets authorized",
        "pricing: $",
        "target account:",
    ]
    combined_public_text = "\n".join([readme, doc, adr, issue]).lower()
    for term in forbidden_positive_terms:
        require(term not in combined_public_text, f"Forbidden commercial adoption wording found: {term}")

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
        require(marker in doc, f"commercial adoption doc must preserve marker: {marker}")

    claims_to_avoid_section = doc.split("Avoid public claims:", 1)[1].split("## Private local sales pack", 1)[0].lower()
    for avoided_claim in [
        "production scanner",
        "autonomous vulnerability scanner",
        "customer-ready assessment platform",
        "commercial license terms are finalized",
        "compliance certification",
        "legal approval",
        "audit opinion",
        "guaranteed safe ai assessment",
        "permission to scan third-party systems",
        "replacement for professional security judgment",
    ]:
        require(
            avoided_claim in claims_to_avoid_section,
            f"commercial adoption doc must explicitly list avoided claim: {avoided_claim}",
        )

    print("Commercial adoption preparation checkpoint tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
