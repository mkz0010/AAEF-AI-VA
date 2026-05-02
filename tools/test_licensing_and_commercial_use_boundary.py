from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def assert_contains(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing {label}: {needle}")


def test_license_file() -> None:
    license_text = read("LICENSE")
    assert_contains(license_text, "GNU AFFERO GENERAL PUBLIC LICENSE", "AGPL title")
    assert_contains(license_text, "Version 3, 19 November 2007", "AGPL version")
    assert_contains(license_text, "Everyone is permitted to copy and distribute verbatim copies", "AGPL verbatim-copy notice")


def test_readme_license_boundary() -> None:
    readme = read("README.md")
    assert_contains(readme, "GNU Affero General Public License v3.0", "README AGPL statement")
    assert_contains(readme, "Agentic Authority & Evidence Framework", "README AAEF attribution")
    assert_contains(readme, "Creative Commons Attribution 4.0 International", "README CC BY attribution")
    assert_contains(readme, "https://github.com/mkz0010/agentic-authority-evidence-framework", "README AAEF URL")
    assert_contains(readme, "commercial licensing inquiries", "README commercial inquiry language")


def test_boundary_doc() -> None:
    doc = read("docs/54-licensing-and-commercial-use-boundary.md")
    required = [
        "AGPL-3.0",
        "CC BY 4.0",
        "commercial license",
        "not legal advice",
        "third-party dependency license compatibility",
        "CLA",
        "execution_authorized = false",
        "preflight_satisfied = false",
        "ready_for_runtime_execution = false",
        "real_execution_permitted = false",
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "raw_artifact_capture_permitted = false",
    ]
    for item in required:
        assert_contains(doc, item, f"boundary doc item {item}")


def test_planning_records() -> None:
    adr = read("planning/decisions/ADR-0048-adopt-agpl-commercial-boundary.md")
    issue = read("planning/issues/0047-add-licensing-and-commercial-use-boundary.md")
    assert_contains(adr, "Accepted for v0.3.5", "ADR status")
    assert_contains(adr, "AGPL-3.0", "ADR AGPL decision")
    assert_contains(adr, "does not authorize runtime execution", "ADR safety non-goal")
    assert_contains(issue, "LICENSE", "issue license task")
    assert_contains(issue, "Local checks pass", "issue acceptance criteria")


def main() -> int:
    test_license_file()
    test_readme_license_boundary()
    test_boundary_doc()
    test_planning_records()
    print("Licensing and commercial-use boundary tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
