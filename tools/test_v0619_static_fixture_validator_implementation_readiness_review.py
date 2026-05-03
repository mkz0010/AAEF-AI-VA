from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/96-v0619-static-fixture-validator-implementation-readiness-review.md"


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
    adr = read_text("planning/decisions/ADR-0090-add-v0619-static-fixture-validator-implementation-readiness-review.md")
    issue = read_text("planning/issues/0089-add-v0619-static-fixture-validator-implementation-readiness-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.19 static fixture validator readiness checkpoint")
    require("v0.6.19 Static Fixture Validator Implementation Readiness Review" in doc, "v0.6.19 doc must exist")

    sections = [
        "Public-safe design boundary",
        "Readiness proposition",
        "Readiness review posture",
        "Read-only readiness checklist",
        "Fail-closed readiness checklist",
        "Negative-test-first readiness checklist",
        "Input boundary readiness",
        "Output boundary readiness",
        "Implementation gate checklist",
        "Registration readiness checklist",
        "Readiness review record model",
        "Blocking issue categories",
        "Private output boundary readiness",
        "Future implementation order",
        "Human review requirements",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    phrases = [
        "This checkpoint is implementation-readiness review only.",
        "This proposition is intentionally non-executing.",
        "Readiness review is not implementation approval for runtime behavior.",
        "If read-only behavior is ambiguous, implementation should remain blocked.",
        "If failure behavior is permissive or unclear, implementation should remain blocked.",
        "Positive fixture generation should not precede negative test readiness.",
        "Input boundary readiness should fail closed on ambiguity.",
        "Output boundary readiness should confirm validator output cannot authorize execution.",
        "Implementation gate review is not runtime authorization.",
        "Registration readiness is not runtime authorization.",
        "Readiness review records should not become execution authorization records.",
        "Every blocking issue should prevent implementation advancement.",
        "Implementation should not begin if readiness review is blocked.",
        "Human review remains a gate.",
        "v0.6.20 Static Fixture Validator Read-only Implementation Scaffold",
    ]
    for phrase in phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    terms = [
        "`readiness_review_id`",
        "`read_only_result`",
        "`fail_closed_result`",
        "`negative_test_first_result`",
        "`input_boundary_result`",
        "`output_boundary_result`",
        "`registration_readiness_result`",
        "`blocking_issues`",
        "`read_only_boundary_unclear`",
        "`fail_closed_behavior_unclear`",
        "`negative_tests_not_first`",
        "`input_boundary_unclear`",
        "`output_boundary_unclear`",
        "`registration_conditions_unclear`",
        "`private_output_boundary_unclear`",
        "`runtime_implication_detected`",
        "`delivery_implication_detected`",
        "`overclaiming_detected`",
        "`human_review_missing`",
        "private-not-in-git/static-fixture-validator-readiness-reviews/",
        "private-not-in-git/static-fixture-validator-implementation-reviews/",
    ]
    for term in terms:
        require(term in doc, f"doc must include term: {term}")

    false_markers = [
        "implementation_started = false",
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
        "this checkpoint starts implementation",
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
    require("Add v0.6.19 static fixture validator implementation readiness review" in adr, "ADR must record v0.6.19 decision")
    require("Completed by v0.6.19 candidate" in issue, "Issue must record v0.6.19 completion status")
    require("## v0.6.19 - Static fixture validator implementation readiness review" in changelog, "CHANGELOG must include v0.6.19")
    require("## v0.6.19 Static fixture validator implementation readiness review" in roadmap, "ROADMAP must include v0.6.19")
    require("test_v0619_static_fixture_validator_implementation_readiness_review.py" in run_all, "run_all must include v0.6.19 test")

    print("v0.6.19 static fixture validator implementation readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
