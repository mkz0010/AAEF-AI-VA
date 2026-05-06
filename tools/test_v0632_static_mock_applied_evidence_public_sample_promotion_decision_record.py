from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/109-v0632-static-mock-applied-evidence-package-public-sample-promotion-decision-record.md"


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
    adr = read_text("planning/decisions/ADR-0103-add-v0632-static-mock-applied-evidence-public-sample-promotion-decision-record.md")
    issue = read_text("planning/issues/0102-add-v0632-static-mock-applied-evidence-public-sample-promotion-decision-record.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.32 checkpoint")
    require("v0.6.32 Static/Mock Applied Evidence Package Public Sample Promotion Decision Record" in doc, "v0.6.32 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("reviewed_keep_private" in doc, "doc must reference v0.6.31 review status")
    require("promotion_status = keep_private" in doc, "doc must reference promotion status")

    sections = [
        "Decision inputs",
        "Decision outcome",
        "Rationale",
        "Later planning conditions",
        "Remaining blockers to public generation",
        "AAEF-side reporting note",
        "Relationship to runtime execution",
        "Rollback posture",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    required_phrases = [
        "This checkpoint is promotion decision recording only.",
        "This proposition is intentionally non-executing.",
        "This outcome allows only the next planning discussion. It does not authorize generated public artifacts.",
        "A separate planning checkpoint should exist before any public sample artifact is created.",
        "Planning must precede public sample generation.",
        "Every unresolved blocker prevents public generation.",
        "AAEF-side reporting should not expose private generated contents.",
        "The earliest next step is public sample planning, not public sample generation and not live diagnostic execution.",
        "Rollback is a safety control, not a failure.",
        "v0.6.33 Sanitized Public Sample Planning",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    blockers = [
        "`public_sample_scope_not_defined`",
        "`sanitized_artifact_naming_not_defined`",
        "`public_directory_placement_not_defined`",
        "`publication_hygiene_not_planned`",
        "`patent_sensitive_review_not_recorded`",
        "`structural_validator_not_implemented`",
        "`public_non_proof_visibility_not_verified`",
        "`public_overclaim_prevention_not_verified`",
        "`human_publication_review_not_recorded`",
    ]
    for blocker in blockers:
        require(blocker in doc, f"doc must include blocker: {blocker}")

    markers = [
        "promotion_decision_recorded = true",
        "public_sample_planning_may_be_considered = true",
        "public_sample_generation_authorized = false",
        "public_sample_promotion_authorized = false",
        "public_sample_generated = false",
        "public_artifact_generated = false",
        "private_package_review_record_generated = true",
        "structural_validator_implemented = false",
        "structural_validator_checks_execute = false",
        "tool_backed_diagnostic_capture_started = false",
        "local_lab_diagnostic_system_built = false",
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
        "this checkpoint promotes public samples",
        "this checkpoint generates public sample artifacts",
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

    require("Add v0.6.32 static/mock applied evidence public sample promotion decision record" in adr, "ADR must record v0.6.32 decision")
    require("Completed by v0.6.32 candidate" in issue, "Issue must record v0.6.32 completion status")
    require("## v0.6.32 - Static/mock applied evidence package public sample promotion decision record" in changelog, "CHANGELOG must include v0.6.32")
    require("## v0.6.32 Static/mock applied evidence package public sample promotion decision record" in roadmap, "ROADMAP must include v0.6.32")
    require("test_v0632_static_mock_applied_evidence_public_sample_promotion_decision_record.py" in run_all, "run_all must include v0.6.32 test")

    print("v0.6.32 static/mock applied evidence public sample promotion decision record tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
