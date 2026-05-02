from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


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
    gitignore = read_text(".gitignore")
    readme = read_text("README.md")
    doc = read_text("docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md")
    adr = read_text("planning/decisions/ADR-0050-add-publication-hygiene-private-artifact-exclusion-checkpoint.md")
    issue = read_text("planning/issues/0049-add-publication-hygiene-private-artifact-exclusion-checkpoint.md")
    run_all = read_text("tools/run_all_local_checks.py")

    required_gitignore_patterns = [
        "private-not-in-git/",
        "*.generated.json",
        "*.generated.md",
        "__pycache__/",
        "*.py[cod]",
        ".env",
        ".env.*",
        "*.local",
        "*.log",
    ]

    for pattern in required_gitignore_patterns:
        require(pattern in gitignore, f".gitignore must contain pattern: {pattern}")

    tracked = git_ls_files()

    private_tracked = [path for path in tracked if path.startswith("private-not-in-git/")]
    require(not private_tracked, f"private-not-in-git files must not be tracked: {private_tracked[:5]}")

    cache_tracked = [
        path
        for path in tracked
        if "__pycache__/" in path or path.endswith(".pyc") or path.endswith(".pyo")
    ]
    require(not cache_tracked, f"Python cache files must not be tracked: {cache_tracked[:5]}")

    generated_tracked = [
        path
        for path in tracked
        if (path.endswith(".generated.json") or path.endswith(".generated.md"))
        and not path.startswith("examples/")
    ]
    require(
        not generated_tracked,
        f"generated local output files must not be tracked outside examples/: {generated_tracked[:5]}",
    )

    require("Publication Hygiene and Private Artifact Boundary" in readme, "README must mention publication hygiene")
    require("private-not-in-git/" in readme, "README must mention private artifact boundary")
    require("publication hygiene" in doc.lower(), "publication hygiene document must describe checkpoint")
    require("does not authorize runtime execution" in doc.lower(), "publication hygiene must not authorize execution")
    require("private-not-in-git/" in doc, "publication hygiene doc must mention private-not-in-git/")
    require(".gitignore" in doc, "publication hygiene doc must mention .gitignore")
    require("publication hygiene" in adr.lower(), "ADR must record publication hygiene decision")
    require("Completed by v0.3.7 candidate" in issue, "Issue must record v0.3.7 completion status")
    require(
        "test_publication_hygiene_private_artifact_exclusion.py" in run_all,
        "run_all must include publication hygiene test",
    )

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
        require(marker in doc, f"Publication hygiene document must preserve marker: {marker}")

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
        require(
            claim not in combined_public_text,
            f"Forbidden positive publication hygiene claim found: {claim}",
        )

    print("Publication hygiene and private artifact exclusion tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
