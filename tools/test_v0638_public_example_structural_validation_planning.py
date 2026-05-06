from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/115-v0638-public-example-structural-validation-planning.md"


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
    adr = read_text("planning/decisions/ADR-0109-add-v0638-public-example-structural-validation-planning.md")
    issue = read_text("planning/issues/0108-add-v0638-public-example-structural-validation-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.38 checkpoint")
    require("v0.6.38 Public Example Structural Validation Planning" in doc, "v0.6.38 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must reference public sample directory")
    require("sanitized_public_sample_track_close_ready = true" in doc, "doc must reference v0.6.37 close-readiness")

    sections = [
        "Validation input scope",
        "Planned validation objectives",
        "Planned required-artifact checks",
        "Planned scenario checks",
        "Planned naming checks",
        "Planned linkage checks",
        "Planned scenario posture checks",
        "Planned non-proof checks",
        "Planned AAEF five-questions checks",
        "Planned publication hygiene checks",
        "Planned runtime boundary checks",
        "Planned failure categories",
        "Planned validator output",
        "AAEF-side reporting note",
        "Relationship to diagnostic execution",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    required_phrases = [
        "This checkpoint is structural validation planning only.",
        "This proposition authorizes only structural validation planning for public examples.",
        "A missing required artifact should fail closed.",
        "Identifier linkage checks are structural checks, not proof that an action was safe.",
        "Non-proof visibility is a validation requirement.",
        "The five-questions mapping is reviewer guidance, not audit opinion.",
        "Any validation uncertainty should fail closed.",
        "This output should not be treated as diagnostic evidence.",
        "The next safe step is public example structural validator implementation readiness review or minimal validator implementation, not live diagnostic execution.",
        "v0.6.39 Public Example Structural Validator Implementation Readiness Review",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    artifacts = [
        "`package_manifest.example.json`",
        "`reviewer_walkthrough.example.md`",
        "`aaef_five_questions_mapping.example.md`",
        "`non_proof_statement.example.md`",
        "`publication_hygiene_report.example.json`",
        "`publication_review_record.example.json`",
        "`tool_action_request.example.json`",
        "`gate_decision.example.json`",
        "`dispatch_decision.example.json`",
        "`execution_result.example.json`",
        "`non_execution_result.example.json`",
        "`evidence_event.example.json`",
        "`review_summary.example.md`",
    ]
    for artifact in artifacts:
        require(artifact in doc, f"doc must include artifact: {artifact}")

    failures = [
        "`example_root_missing`",
        "`package_artifact_missing`",
        "`scenario_missing`",
        "`scenario_artifact_missing`",
        "`non_example_artifact_name_detected`",
        "`private_generated_artifact_name_detected`",
        "`identifier_linkage_broken`",
        "`scenario_posture_contradiction`",
        "`non_execution_evidence_missing`",
        "`non_proof_statement_missing`",
        "`five_questions_mapping_missing`",
        "`publication_hygiene_missing`",
        "`publication_hygiene_not_passed`",
        "`private_path_leakage_detected`",
        "`secret_or_credential_detected`",
        "`customer_target_implication_detected`",
        "`runtime_execution_implication_detected`",
        "`scanner_execution_implication_detected`",
        "`delivery_authorization_implication_detected`",
        "`overclaim_detected`",
    ]
    for failure in failures:
        require(failure in doc, f"doc must include failure category: {failure}")

    markers = [
        "public_example_structural_validation_planning_completed = true",
        "public_example_structural_validator_implementation_ready = false",
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

    require("Add v0.6.38 public example structural validation planning" in adr, "ADR must record v0.6.38 decision")
    require("Completed by v0.6.38 candidate" in issue, "Issue must record v0.6.38 completion status")
    require("## v0.6.38 - Public example structural validation planning" in changelog, "CHANGELOG must include v0.6.38")
    require("## v0.6.38 Public example structural validation planning" in roadmap, "ROADMAP must include v0.6.38")
    require("test_v0638_public_example_structural_validation_planning.py" in run_all, "run_all must include v0.6.38 test")

    print("v0.6.38 public example structural validation planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
