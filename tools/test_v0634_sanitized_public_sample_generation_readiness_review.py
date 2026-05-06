from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/111-v0634-sanitized-public-sample-generation-readiness-review.md"


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
    adr = read_text("planning/decisions/ADR-0105-add-v0634-sanitized-public-sample-generation-readiness-review.md")
    issue = read_text("planning/issues/0104-add-v0634-sanitized-public-sample-generation-readiness-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.34 checkpoint")
    require("v0.6.34 Sanitized Public Sample Generation Readiness Review" in doc, "v0.6.34 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("docs/110-v0633-sanitized-public-sample-planning.md" in doc, "doc must reference v0.6.33 planning input")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must include candidate public directory")

    sections = [
        "Readiness input",
        "Readiness outcome",
        "Readiness criteria",
        "Readiness assessment",
        "Remaining blockers before generation",
        "Candidate generation constraints",
        "Candidate public artifact set",
        "Publication hygiene readiness",
        "Human review readiness",
        "AAEF-side reporting note",
        "Relationship to diagnostic execution",
        "Rollback posture",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    artifacts = [
        "package_manifest.example.json",
        "tool_action_request.example.json",
        "gate_decision.example.json",
        "dispatch_decision.example.json",
        "execution_result.example.json",
        "non_execution_result.example.json",
        "evidence_event.example.json",
        "review_summary.example.md",
        "non_proof_statement.example.md",
        "reviewer_walkthrough.example.md",
        "aaef_five_questions_mapping.example.md",
    ]
    for artifact in artifacts:
        require(artifact in doc, f"doc must include candidate artifact name: {artifact}")

    blockers = [
        "`public_sample_generator_not_implemented`",
        "`publication_hygiene_validator_not_implemented`",
        "`sanitized_artifact_content_not_generated`",
        "`human_publication_review_not_recorded`",
        "`public_sample_diff_not_reviewed`",
        "`private_path_absence_not_verified`",
        "`secret_absence_not_verified`",
        "`credential_absence_not_verified`",
        "`customer_target_absence_not_verified`",
        "`patent_sensitive_absence_not_verified`",
        "`overclaim_absence_not_verified`",
    ]
    for blocker in blockers:
        require(blocker in doc, f"doc must include blocker: {blocker}")

    required_phrases = [
        "This checkpoint is sanitized public sample generation readiness review only.",
        "This proposition is intentionally non-executing.",
        "Private generated artifacts remain private.",
        "This outcome permits only a later generation candidate checkpoint to be considered. It does not authorize generated public artifacts.",
        "Any uncertainty should block generation.",
        "The assessment supports consideration of a later generation candidate only.",
        "Every unresolved blocker prevents public generation.",
        "The candidate must be reviewable before commit.",
        "This checkpoint does not create those files.",
        "Hygiene uncertainty should fail closed.",
        "Human publication review is a gate, not a formality.",
        "AAEF-side reporting should not expose private generated contents.",
        "The earliest next step is a sanitized public sample generation candidate, not live diagnostic execution.",
        "Rollback remains a safety control, not a failure.",
        "v0.6.35 Sanitized Public Sample Generation Candidate",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    markers = [
        "sanitized_public_sample_generation_readiness_review_completed = true",
        "sanitized_public_sample_generation_candidate_may_be_considered = true",
        "public_sample_generation_authorized = false",
        "public_sample_promotion_authorized = false",
        "public_sample_generated = false",
        "public_artifact_generated = false",
        "private_package_review_record_generated = true",
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
        "this checkpoint generates public sample artifacts",
        "this checkpoint copies private generated artifacts into the public repository",
        "this checkpoint implements structural validators",
        "this checkpoint executes validator checks",
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

    require("Add v0.6.34 sanitized public sample generation readiness review" in adr, "ADR must record v0.6.34 decision")
    require("Completed by v0.6.34 candidate" in issue, "Issue must record v0.6.34 completion status")
    require("## v0.6.34 - Sanitized public sample generation readiness review" in changelog, "CHANGELOG must include v0.6.34")
    require("## v0.6.34 Sanitized public sample generation readiness review" in roadmap, "ROADMAP must include v0.6.34")
    require("test_v0634_sanitized_public_sample_generation_readiness_review.py" in run_all, "run_all must include v0.6.34 test")

    print("v0.6.34 sanitized public sample generation readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
