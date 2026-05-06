from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/120-v0643-applied-implementation-handback-review-and-next-direction.md"


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
    adr = read_text("planning/decisions/ADR-0114-add-v0643-applied-implementation-handback-review-next-direction.md")
    issue = read_text("planning/issues/0113-add-v0643-applied-implementation-handback-review-next-direction.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.43 checkpoint")
    require("v0.6.43 Applied Implementation Handback Review and Next Direction" in doc, "v0.6.43 doc must exist")
    require("AAEF category = Applied Implementation" in doc, "doc must classify handback as Applied Implementation")
    require("docs/119-v0642-aaef-applied-implementation-handback-summary.md" in doc, "doc must reference v0.6.42 handback")
    require("7051942" in doc, "doc must include v0.6.42 commit id")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("v0.6.44 Public Validator Negative Fixture Planning" in doc, "doc must recommend v0.6.44")

    sections = [
        "Review classification",
        "Public-safe handback review boundary",
        "Review proposition",
        "Handback sufficiency criteria",
        "Handback review result",
        "AAEF main handback package",
        "Scenario handback summary",
        "Evidence-interface lessons",
        "Next-direction options",
        "Recommended branch of work",
        "Optional next checkpoints",
        "Handback completion note",
        "Runtime and scanning boundary",
        "Claims to avoid",
        "Recommended next checkpoint",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    required_phrases = [
        "This checkpoint is handback review and next-direction planning only.",
        "This checkpoint does not move AAEF-AI-VA material into AAEF Core, Profile, or Practical Package.",
        "The handback remains evidence/interface-level material.",
        "This proposition authorizes only handback review and next-direction planning.",
        "The v0.6.42 handback is sufficient for AAEF main as an Applied Implementation handback.",
        "The scenarios remain synthetic examples and are not live diagnostic evidence.",
        "These lessons may inform AAEF Core/Profile/Package planning, but they do not promote AAEF-AI-VA implementation details into those layers.",
        "The recommended next direction is public validator hardening or local-lab/preflight planning return, not live diagnostic execution.",
        "The most implementation-safe next checkpoint is public validator negative fixture planning.",
        "No patent-sensitive or commercial detail is needed for AAEF main.",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    handback_items = [
        "Repository:",
        "Tag:",
        "Commit:",
        "Primary handback document:",
        "Reviewer walkthrough:",
        "AAEF five-questions mapping:",
        "Validator:",
        "Validation result:",
    ]
    for item in handback_items:
        require(item in doc, f"doc must include handback package item: {item}")

    scenarios = [
        "`permitted-safe-diagnostic`",
        "`denied-out-of-scope-request`",
        "`human-approval-required`",
        "`not-executed-expired`",
    ]
    for scenario in scenarios:
        require(scenario in doc, f"doc must include scenario: {scenario}")

    options = [
        "Public validator hardening",
        "Local-lab/preflight planning return",
        "AAEF handback only",
        "Applied evidence track pause",
        "Runtime execution readiness review",
    ]
    for option in options:
        require(option in doc, f"doc must include next option: {option}")

    markers = [
        "aaef_applied_implementation_handback_review_completed = true",
        "aaef_applied_implementation_handback_sufficient_for_main = true",
        "aaef_handback_category_applied_implementation = true",
        "aaef_core_promotion = false",
        "aaef_profile_promotion = false",
        "aaef_practical_package_promotion = false",
        "excluded_material_boundary_preserved = true",
        "public_validator_hardening_recommended = true",
        "local_lab_preflight_planning_return_allowed_later = true",
        "runtime_execution_readiness_review_deferred = true",
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

    excluded = [
        "patent-sensitive browser-state details",
        "patent-sensitive diagnostic reconstruction detail",
        "commercial strategy",
        "pricing strategy",
        "customer lists",
        "NDA-assumed material",
        "private generated artifacts",
        "scanner output",
        "credential material",
    ]
    for item in excluded:
        require(item in doc, f"doc must include exclusion: {item}")

    forbidden_claims = [
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

    require("Add v0.6.43 Applied Implementation handback review and next direction" in adr, "ADR must record v0.6.43 decision")
    require("Completed by v0.6.43 candidate" in issue, "Issue must record v0.6.43 completion status")
    require("## v0.6.43 - Applied Implementation handback review and next direction" in changelog, "CHANGELOG must include v0.6.43")
    require("## v0.6.43 Applied Implementation handback review and next direction" in roadmap, "ROADMAP must include v0.6.43")
    require("test_v0643_applied_implementation_handback_review_next_direction.py" in run_all, "run_all must include v0.6.43 test")

    print("v0.6.43 Applied Implementation handback review and next direction tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
