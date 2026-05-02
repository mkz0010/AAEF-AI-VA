from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    license_text = read_text("LICENSE")
    readme = read_text("README.md")
    doc = read_text("docs/55-public-repository-readiness-checkpoint.md")
    adr = read_text("planning/decisions/ADR-0049-add-public-repository-readiness-checkpoint.md")
    issue = read_text("planning/issues/0048-add-public-repository-readiness-checkpoint.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require("GNU AFFERO GENERAL PUBLIC LICENSE" in license_text, "LICENSE must contain AGPL-3.0 text")
    require("Version 3, 19 November 2007" in license_text, "LICENSE must include AGPL-3.0 version marker")

    require("GNU Affero General Public License v3.0" in readme, "README must mention AGPL-3.0")
    require("Agentic Authority & Evidence Framework" in readme, "README must attribute AAEF")
    require("CC BY 4.0" in readme, "README must mention AAEF CC BY 4.0 boundary")
    require("commercial" in readme.lower(), "README must mention commercial licensing path")
    require("private-not-in-git/" in readme, "README must mention private-not-in-git boundary")

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
        require(marker in doc, f"Public readiness document must preserve marker: {marker}")

    require("public repository readiness" in doc.lower(), "Public readiness document must describe checkpoint")
    require("does not authorize runtime execution" in doc.lower(), "Public readiness must not authorize execution")
    require(
        ("does not create a GitHub repository" in doc)
        or ("This checkpoint does not:" in doc and "create a GitHub repository" in doc),
        "Public readiness must not create remote repository",
    )
    require("private-not-in-git/" in doc, "Public readiness must preserve private artifact boundary")
    require("AGPL-3.0" in doc, "Public readiness doc must mention AGPL-3.0")
    require("CC BY 4.0" in doc, "Public readiness doc must mention CC BY 4.0")
    require("commercial" in doc.lower(), "Public readiness doc must mention commercial boundary")

    require("public repository readiness checkpoint" in adr.lower(), "ADR must record public readiness decision")
    require("does not authorize runtime execution" in adr.lower(), "ADR must preserve execution boundary")
    require("Completed by v0.3.6 candidate" in issue, "Issue must record v0.3.6 completion status")
    require("test_public_repository_readiness_checkpoint.py" in run_all, "run_all must include public readiness test")

    forbidden_claims = [
        "runtime execution is enabled",
        "network activity is allowed",
        "scan execution is allowed",
        "credential injection is permitted",
        "customer target operation is allowed",
    ]

    combined_public_text = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined_public_text, f"Forbidden public-readiness claim found: {claim}")

    print("Public repository readiness checkpoint tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
