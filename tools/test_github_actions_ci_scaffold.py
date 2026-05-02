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


def main() -> int:
    workflow_path = REPO / ".github" / "workflows" / "validate.yml"
    require(workflow_path.exists(), "GitHub Actions workflow must exist")

    workflow = workflow_path.read_text(encoding="utf-8")
    readme = read_text("README.md")
    doc = read_text("docs/60-github-actions-ci-scaffold.md")
    adr = read_text("planning/decisions/ADR-0054-add-github-actions-ci-scaffold.md")
    issue = read_text("planning/issues/0053-add-github-actions-ci-scaffold.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require("name: Validate AAEF-AI-VA artifacts" in workflow, "workflow must have validation name")
    require("push:" in workflow and "pull_request:" in workflow and "workflow_dispatch:" in workflow, "workflow must define expected triggers")
    require("permissions:" in workflow and "contents: read" in workflow, "workflow must use read-only contents permission")
    require("runs-on: ubuntu-latest" in workflow, "workflow must run on ubuntu-latest")
    require("uses: actions/checkout@v4" in workflow, "workflow must use checkout")
    require("uses: actions/setup-python@v6" in workflow, "workflow must use setup-python")
    require("python-version: '3.13'" in workflow, "workflow must pin initial Python version")
    require("python tools/run_all_local_checks.py" in workflow, "workflow must run local checks")

    forbidden_workflow_terms = [
        "secrets.",
        "credential",
        "password",
        "token",
        "zap",
        "active scan",
        "spider",
        "curl ",
        "wget ",
        "nmap",
        "nikto",
        "sqlmap",
        "git push",
        "git remote add",
    ]
    workflow_lower = workflow.lower()
    for term in forbidden_workflow_terms:
        require(term not in workflow_lower, f"workflow must not contain forbidden term: {term}")

    require("GitHub Actions CI Scaffold" in readme, "README must mention CI scaffold")
    require(".github/workflows/validate.yml" in readme, "README must mention workflow path")
    require("docs/60-github-actions-ci-scaffold.md" in readme, "README must link CI scaffold doc")

    require("GitHub Actions CI Scaffold" in doc, "CI scaffold doc must exist")
    require("does not authorize runtime execution" in doc.lower(), "CI doc must preserve runtime boundary")
    require("python tools/run_all_local_checks.py" in doc, "CI doc must document local checks command")
    require("permissions:" in doc and "contents: read" in doc, "CI doc must document read-only permission")
    require("free of secrets" in doc.lower(), "CI doc must prohibit secrets")
    require("free of credentials" in doc.lower(), "CI doc must prohibit credentials")
    require("free of ZAP execution".lower() in doc.lower(), "CI doc must prohibit ZAP execution")
    require("free of network scan execution" in doc.lower(), "CI doc must prohibit network scans")

    require("Add GitHub Actions CI scaffold" in adr, "ADR must record CI scaffold decision")
    require("must not run scans" in adr.lower(), "ADR must prohibit scans")
    require("Completed by v0.4.1 candidate" in issue, "Issue must record v0.4.1 completion status")
    require("test_github_actions_ci_scaffold.py" in run_all, "run_all must include CI scaffold test")

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
        require(marker in doc, f"CI scaffold doc must preserve marker: {marker}")

    forbidden_positive_claims = [
        "runtime execution enabled",
        "network activity allowed",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
        "is a production-ready scanner",
        "is an autonomous vulnerability scanner",
    ]
    combined_public_text = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined_public_text, f"Forbidden CI scaffold claim found: {claim}")

    remotes = git_remotes()
    if remotes:
        print(f"GitHub Actions CI scaffold note: existing remotes detected: {', '.join(remotes)}")
    else:
        print("GitHub Actions CI scaffold note: no git remotes detected.")

    print("GitHub Actions CI scaffold tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
