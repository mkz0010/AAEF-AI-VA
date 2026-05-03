from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/94-v0617-static-fixture-validator-scaffold-planning.md"


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
    adr = read_text("planning/decisions/ADR-0088-add-v0617-static-fixture-validator-scaffold-planning.md")
    issue = read_text("planning/issues/0087-add-v0617-static-fixture-validator-scaffold-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.17 static fixture validator scaffold checkpoint")
    require("v0.6.17 Static Fixture Validator Scaffold Planning" in doc, "v0.6.17 doc must exist")

    sections = [
        "Public-safe design boundary",
        "Planning proposition",
        "Validator scaffold posture",
        "Scaffold responsibility model",
        "Validator input boundary",
        "Validator output boundary",
        "Planned validation stages",
        "Fail-closed behavior planning",
        "Failure category model",
        "Negative-test handling planning",
        "Validator review record planning",
        "Future implementation order",
        "Registration gate planning",
        "Generated artifact boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    phrases = [
        "This checkpoint is validator scaffold planning only.",
        "This proposition is intentionally non-executing.",
        "The scaffold is not validator code.",
        "The scaffold should not run tools, start containers, or validate live assessment evidence.",
        "Future validator inputs should be static fixture artifacts only.",
        "Input boundary violations should fail closed.",
        "Validator output must not authorize execution.",
        "The stages are planning concepts, not implemented functions.",
        "Future validator behavior should be fail-closed.",
        "Fail-closed behavior should prefer human review over permissive assumptions.",
        "Every unsafe fixture failure should be blocking.",
        "Negative-test handling is not implemented by this checkpoint.",
        "Validator review records should not become execution authorization records.",
        "Positive fixture generation should not precede negative test expectations.",
        "Registration is not runtime authorization.",
        "Public repository content should contain planning, not generated private fixture outputs.",
        "v0.6.18 Static Fixture Validator Minimal Scaffold Design",
    ]
    for phrase in phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    terms = [
        "`load_fixture_manifest`",
        "`check_required_nodes`",
        "`check_reference_integrity`",
        "`check_no_secret_like_content`",
        "`check_no_customer_like_content`",
        "`check_no_runtime_markers`",
        "`check_no_runnable_configuration`",
        "`check_no_delivery_implication`",
        "`check_no_overclaiming`",
        "`emit_review_record`",
        "`missing_manifest`",
        "`missing_required_node`",
        "`invalid_node_envelope`",
        "`invalid_reference`",
        "`runtime_marker_not_false`",
        "`runnable_configuration_detected`",
        "`delivery_implication_detected`",
        "`overclaiming_detected`",
        "`validator_uncertainty`",
        "`validator_review_id`",
        "`validation_status`",
        "private-not-in-git/static-fixture-validator-scaffolds/",
        "private-not-in-git/static-fixture-validator-review-records/",
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
    require("Add v0.6.17 static fixture validator scaffold planning" in adr, "ADR must record v0.6.17 decision")
    require("Completed by v0.6.17 candidate" in issue, "Issue must record v0.6.17 completion status")
    require("## v0.6.17 - Static fixture validator scaffold planning" in changelog, "CHANGELOG must include v0.6.17")
    require("## v0.6.17 Static fixture validator scaffold planning" in roadmap, "ROADMAP must include v0.6.17")
    require("test_v0617_static_fixture_validator_scaffold_planning.py" in run_all, "run_all must include v0.6.17 test")

    print("v0.6.17 static fixture validator scaffold planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
