from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/121-v0644-public-validator-negative-fixture-planning.md"

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
    adr = read_text("planning/decisions/ADR-0115-add-v0644-public-validator-negative-fixture-planning.md")
    issue = read_text("planning/issues/0114-add-v0644-public-validator-negative-fixture-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.44 checkpoint")
    require("v0.6.44 Public Validator Negative Fixture Planning" in doc, "v0.6.44 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("tools/validate_public_example_structure.py" in doc, "doc must reference public validator")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must reference positive public example")
    require("examples/applied-evidence/public-validator-negative-fixtures/" in doc, "doc must include planned negative fixture root")
    require("v0.6.45 Public Validator Negative Fixture Implementation Readiness Review" in doc, "doc must recommend v0.6.45")

    sections = [
        "Planning classification",
        "Planning proposition",
        "Public-safe planning boundary",
        "Planning input",
        "Planned fixture root",
        "Planned negative fixture categories",
        "Planned expected blocker mapping",
        "Planned fixture construction rules",
        "Planned validation harness behavior",
        "Public example positive control",
        "AAEF handback relationship",
        "Readiness assessment",
        "Runtime and scanning boundary",
        "Claims to avoid",
        "Recommended next checkpoint",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    required_phrases = [
        "This checkpoint is negative fixture planning only.",
        "This proposition authorizes only negative fixture planning for the public validator.",
        "This path is a planned candidate. It is not created by v0.6.44.",
        "Negative fixtures should prove fail-closed behavior only in the structural validator sense.",
        "The boundary-violation fixture should remain a static file mutation, not a runtime action.",
        "Future negative fixture work should preserve this positive control.",
        "The project is ready to consider a later negative fixture implementation readiness review.",
        "AAEF main should not receive implementation-sensitive fixture-generation details, patent-sensitive diagnostic reconstruction details, commercial strategy, pricing strategy, customer lists, NDA-assumed material, raw scanner output, private generated artifacts, or credential material.",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    categories = [
        "`missing-package-artifact`",
        "`missing-scenario-artifact`",
        "`missing-scenario-directory`",
        "`malformed-json`",
        "`broken-linkage`",
        "`scenario-posture-contradiction`",
        "`non-example-name`",
        "`missing-non-proof-statement`",
        "`missing-five-questions-mapping`",
        "`hygiene-not-passed`",
        "`forbidden-text-leakage`",
        "`overclaim-language`",
        "`boundary-flag-violation`",
    ]
    for category in categories:
        require(category in doc, f"doc must include category: {category}")

    blockers = [
        "`package_artifact_missing:*`",
        "`scenario_artifact_missing:*`",
        "`scenario_missing:*`",
        "`malformed_json:*`",
        "`identifier_linkage_broken:*`",
        "`scenario_posture_contradiction:*`",
        "`non_example_artifact_name_detected:*`",
        "`non_proof_statement_missing_or_incomplete:*`",
        "`five_questions_mapping_missing:*`",
        "`publication_hygiene_not_passed`",
        "`forbidden_fragment_detected:*`",
        "`overclaim_detected:*`",
        "`runtime_boundary_flag_not_false:*`",
    ]
    for blocker in blockers:
        require(blocker in doc, f"doc must include blocker mapping: {blocker}")

    markers = [
        "public_validator_negative_fixture_planning_completed = true",
        "public_validator_negative_fixtures_ready_to_consider = true",
        "negative_fixtures_implemented = false",
        "negative_fixture_harness_implemented = false",
        "validator_behavior_modified = false",
        "aaef_applied_implementation_handback_review_completed = true",
        "aaef_applied_implementation_handback_sufficient_for_main = true",
        "aaef_handback_category_applied_implementation = true",
        "aaef_core_promotion = false",
        "aaef_profile_promotion = false",
        "aaef_practical_package_promotion = false",
        "excluded_material_boundary_preserved = true",
        "public_example_structural_validator_review_completed = true",
        "public_example_structural_validation_track_close_ready = true",
        "public_example_structural_validation_status = passed",
        "public_example_structural_validator_implemented = true",
        "public_example_structural_validator_checks_execute = true",
        "public_example_structural_validator_read_only = true",
        "public_example_structural_validator_public_example_scoped = true",
        "public_example_structural_validator_authorizes_execution = false",
        "sanitized_public_sample_track_close_ready = true",
        "retain_limited_public_example = true",
        "sanitized_public_sample_candidate_generated = true",
        "public_sample_publication_review_completed = true",
        "publication_review_record_generated = true",
        "private_artifact_copied_to_public = false",
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
        "this checkpoint implements negative fixtures",
        "this checkpoint modifies validator behavior",
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

    require("Add v0.6.44 public validator negative fixture planning" in adr, "ADR must record v0.6.44 decision")
    require("Completed by v0.6.44 candidate" in issue, "Issue must record v0.6.44 completion status")
    require("## v0.6.44 - Public validator negative fixture planning" in changelog, "CHANGELOG must include v0.6.44")
    require("## v0.6.44 Public validator negative fixture planning" in roadmap, "ROADMAP must include v0.6.44")
    require("test_v0644_public_validator_negative_fixture_planning.py" in run_all, "run_all must include v0.6.44 test")

    print("v0.6.44 public validator negative fixture planning tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
