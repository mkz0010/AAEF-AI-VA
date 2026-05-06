from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/116-v0639-public-example-structural-validator-implementation-readiness-review.md"


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
    adr = read_text("planning/decisions/ADR-0110-add-v0639-public-example-structural-validator-implementation-readiness-review.md")
    issue = read_text("planning/issues/0109-add-v0639-public-example-structural-validator-implementation-readiness-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.39 checkpoint")
    require("v0.6.39 Public Example Structural Validator Implementation Readiness Review" in doc, "v0.6.39 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must reference public sample directory")
    require("public_example_structural_validation_planning_completed = true" in doc, "doc must reference v0.6.38 planning")

    sections = [
        "Readiness input",
        "Readiness outcome",
        "Implementation prerequisites",
        "Allowed implementation scope",
        "Prohibited implementation behavior",
        "Expected validator checks",
        "Expected validator output",
        "Fail-closed behavior",
        "Remaining blockers before implementation",
        "Readiness assessment",
        "AAEF-side reporting note",
        "Relationship to diagnostic execution",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    required_phrases = [
        "This checkpoint is validator implementation readiness review only.",
        "This proposition authorizes only implementation readiness review for a future public example structural validator.",
        "This outcome permits only a later implementation checkpoint to be considered. It does not implement or execute the validator.",
        "The validator should be read-only and public-example scoped.",
        "Fail-closed behavior is a safety requirement, not optional behavior.",
        "The project is ready to consider a later read-only public example validator implementation candidate.",
        "The next safe step is a read-only public example structural validator implementation candidate, not live diagnostic execution.",
        "v0.6.40 Public Example Structural Validator Implementation Candidate",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    blockers = [
        "`validator_code_not_implemented`",
        "`validator_cli_not_defined`",
        "`validator_output_format_not_finalized`",
        "`negative_fixture_strategy_not_defined`",
        "`overclaim_phrase_list_not_finalized`",
        "`private_path_exclusion_check_not_implemented`",
        "`human_review_after_implementation_not_recorded`",
    ]
    for blocker in blockers:
        require(blocker in doc, f"doc must include blocker: {blocker}")

    expected_checks = [
        "Root check",
        "Package artifacts",
        "Scenario coverage",
        "Scenario artifacts",
        "Naming",
        "Linkage",
        "Scenario posture",
        "Non-proof visibility",
        "Five questions",
        "Hygiene",
        "Boundary flags",
        "Overclaim text",
    ]
    for check in expected_checks:
        require(check in doc, f"doc must include expected check: {check}")

    markers = [
        "public_example_structural_validator_implementation_readiness_review_completed = true",
        "public_example_structural_validator_implementation_may_be_considered = true",
        "public_example_structural_validation_planning_completed = true",
        "public_example_structural_validator_implementation_ready = true",
        "public_example_structural_validator_implemented = false",
        "public_example_structural_validator_checks_execute = false",
        "sanitized_public_sample_track_close_ready = true",
        "retain_limited_public_example = true",
        "sanitized_public_sample_candidate_generated = true",
        "public_sample_publication_review_completed = true",
        "publication_review_record_generated = true",
        "private_artifact_copied_to_public = false",
        "structural_validator_implemented = false",
        "structural_validator_checks_execute = false",
        "tool_backed_diagnostic_capture_started = false",
        "local_lab_diagnostic_system_built = false",
        "fixture_live_evidence = false",
        "validator_authorizes_execution = false",
        "validator_authorizes_scanning = false",
        "validator_authorizes_docker = false",
        "validator_authorizes_delivery = false",
        "docker_compose_file_created = false",
        "docker_compose_executed = false",
        "docker_image_pulled = false",
        "container_started = false",
        "port_bound = false",
        "docker_execution_authorized = false",
        "execution_authorized = false",
        "runtime_execution_authorized = false",
        "scanner_execution_authorized = false",
        "real_execution_permitted = false",
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "customer_target = false",
        "customer_target_authorized = false",
        "external_network_target = false",
        "delivery_authorized = false",
    ]
    for marker in markers:
        require(marker in doc, f"doc must preserve marker: {marker}")

    forbidden_claims = [
        "this checkpoint implements structural validators",
        "this checkpoint executes structural validator checks",
        "this checkpoint builds the local-lab diagnostic system",
        "this checkpoint creates docker compose files",
        "this checkpoint pulls docker images",
        "this checkpoint starts containers",
        "this checkpoint binds ports",
        "this checkpoint enables runtime execution",
        "this checkpoint allows scan execution",
        "this checkpoint permits credential injection",
        "this checkpoint allows customer target operation",
        "this checkpoint authorizes delivery",
        "this checkpoint proves vulnerability detection accuracy",
        "this checkpoint is production ready",
        "this checkpoint provides implementation conformance",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
        "external framework equivalence is established",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("Add v0.6.39 public example structural validator implementation readiness review" in adr, "ADR must record v0.6.39 decision")
    require("Completed by v0.6.39 candidate" in issue, "Issue must record v0.6.39 completion status")
    require("## v0.6.39 - Public example structural validator implementation readiness review" in changelog, "CHANGELOG must include v0.6.39")
    require("## v0.6.39 Public example structural validator implementation readiness review" in roadmap, "ROADMAP must include v0.6.39")
    require("test_v0639_public_example_structural_validator_implementation_readiness_review.py" in run_all, "run_all must include v0.6.39 test")

    print("v0.6.39 public example structural validator implementation readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
