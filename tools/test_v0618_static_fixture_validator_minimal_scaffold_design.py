from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/95-v0618-static-fixture-validator-minimal-scaffold-design.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains(text: str, phrase: str) -> bool:
    return re.sub(r"\s+", " ", phrase).strip() in re.sub(r"\s+", " ", text).strip()


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0089-add-v0618-static-fixture-validator-minimal-scaffold-design.md")
    issue = read_text("planning/issues/0088-add-v0618-static-fixture-validator-minimal-scaffold-design.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.18 static fixture validator minimal scaffold checkpoint")
    require("v0.6.18 Static Fixture Validator Minimal Scaffold Design" in doc, "v0.6.18 doc must exist")

    sections = [
        "Public-safe design boundary",
        "Design proposition",
        "Minimal scaffold posture",
        "Planned module boundary",
        "Planned CLI boundary",
        "Planned input model",
        "Planned output model",
        "Planned function boundaries",
        "Failure result model",
        "Fail-closed behavior design",
        "Planned registration conditions",
        "Future implementation order",
        "Generated artifact boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    phrases = [
        "This checkpoint is minimal scaffold design only.",
        "This proposition is intentionally non-executing.",
        "The minimal scaffold design is not validator code.",
        "These are planned module boundaries, not implemented modules.",
        "The planned CLI must be read-only.",
        "The CLI boundary is not implemented by this checkpoint.",
        "Input boundary violations should fail closed.",
        "Validator output must not authorize execution.",
        "These function boundaries are not implemented by this checkpoint.",
        "Every unsafe or uncertain failure should be blocking.",
        "Fail-closed behavior should prefer human review over permissive assumptions.",
        "Registration is not runtime authorization.",
        "Positive fixture generation should not precede negative tests.",
        "Public repository content should contain planning, not generated private fixture outputs.",
        "v0.6.19 Static Fixture Validator Implementation Readiness Review",
    ]
    for phrase in phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    terms = [
        "`static_fixture_validator`",
        "`fixture_loader`",
        "`manifest_checks`",
        "`node_checks`",
        "`reference_checks`",
        "`trace_checks`",
        "`safety_checks`",
        "`failure_model`",
        "`review_output`",
        "python tools/validate_static_lab_fixtures.py --fixture-dir <path>",
        "`load_manifest`",
        "`load_fixture_nodes`",
        "`check_required_nodes`",
        "`check_reference_integrity`",
        "`check_trace_integrity`",
        "`check_no_secret_like_content`",
        "`check_no_customer_like_content`",
        "`check_no_runtime_markers`",
        "`check_no_runnable_configuration`",
        "`check_no_delivery_implication`",
        "`check_no_overclaiming`",
        "`emit_review_result`",
        "`failure_id`",
        "`failure_category`",
        "`fixture_ref`",
        "private-not-in-git/static-fixture-validator-minimal-designs/",
        "private-not-in-git/static-fixture-validator-cli-reviews/",
    ]
    for term in terms:
        require(term in doc, f"doc must include term: {term}")

    false_markers = [
        "fixture_schema_implemented = false",
        "fixture_validator_implemented = false",
        "negative_tests_implemented = false",
        "fixture_generated = false",
        "fixture_live_evidence = false",
        "validator_code_exists = false",
        "validator_checks_execute = false",
        "validator_cli_implemented = false",
        "static_sketch_runnable = false",
        "docker_compose_file_created = false",
        "docker_compose_executed = false",
        "docker_image_pulled = false",
        "container_started = false",
        "port_bound = false",
        "docker_execution_authorized = false",
        "preflight_satisfied = false",
        "execution_authorized = false",
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "customer_target = false",
        "external_network_target = false",
        "delivery_authorized = false",
    ]
    for marker in false_markers:
        require(marker in doc, f"doc must preserve marker: {marker}")

    forbidden_claims = [
        "this checkpoint implements fixture schemas",
        "this checkpoint implements fixture validators",
        "this checkpoint implements cli behavior",
        "this checkpoint implements negative tests",
        "this checkpoint generates fixture files",
        "this checkpoint creates docker compose files",
        "this checkpoint pulls docker images",
        "this checkpoint starts containers",
        "this checkpoint binds ports",
        "this checkpoint enables runtime execution",
        "this checkpoint allows scan execution",
        "this checkpoint permits credential injection",
        "this checkpoint allows customer target operation",
        "this checkpoint authorizes delivery",
        "this checkpoint is production ready",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("private advanced feature details" in doc, "public materials must keep advanced private workstream details abstract")
    require("Add v0.6.18 static fixture validator minimal scaffold design" in adr, "ADR must record v0.6.18 decision")
    require("Completed by v0.6.18 candidate" in issue, "Issue must record v0.6.18 completion status")
    require("## v0.6.18 - Static fixture validator minimal scaffold design" in changelog, "CHANGELOG must include v0.6.18")
    require("## v0.6.18 Static fixture validator minimal scaffold design" in roadmap, "ROADMAP must include v0.6.18")
    require("test_v0618_static_fixture_validator_minimal_scaffold_design.py" in run_all, "run_all must include v0.6.18 test")

    print("v0.6.18 static fixture validator minimal scaffold design tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
