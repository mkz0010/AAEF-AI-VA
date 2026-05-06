from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/107-v0630-static-mock-applied-evidence-package-review-and-promotion-gate-planning.md"


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
    adr = read_text("planning/decisions/ADR-0101-add-v0630-static-mock-applied-evidence-review-promotion-gate-planning.md")
    issue = read_text("planning/issues/0100-add-v0630-static-mock-applied-evidence-review-promotion-gate-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.30 checkpoint")
    require("v0.6.30 Static/Mock Applied Evidence Package Review and Promotion Gate Planning" in doc, "v0.6.30 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("private-not-in-git/applied-evidence-runs/static-mock-demo/" in doc, "doc must reference v0.6.29 private package path")

    sections = [
        "Review input package",
        "Review objectives",
        "Private package review criteria",
        "Promotion gate criteria",
        "Promotion blocker categories",
        "Promotion outcomes",
        "Public sample planning boundary",
        "AAEF-side reporting boundary",
        "Runtime and diagnostic execution separation",
        "Structural validator relationship",
        "Rollback posture",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    blockers = [
        "`private_package_missing`",
        "`scenario_missing`",
        "`artifact_missing`",
        "`identifier_linkage_broken`",
        "`non_execution_evidence_missing`",
        "`reviewer_walkthrough_missing`",
        "`five_questions_mapping_missing`",
        "`non_proof_statement_missing`",
        "`secret_or_credential_detected`",
        "`customer_target_implication_detected`",
        "`third_party_target_implication_detected`",
        "`live_scanner_output_detected`",
        "`runtime_execution_implication_detected`",
        "`docker_execution_implication_detected`",
        "`delivery_authorization_implication_detected`",
        "`audit_or_legal_sufficiency_claim_detected`",
        "`certification_or_compliance_claim_detected`",
        "`external_framework_equivalence_claim_detected`",
        "`patent_sensitive_detail_detected`",
        "`human_review_missing`",
    ]
    for blocker in blockers:
        require(blocker in doc, f"doc must include blocker category: {blocker}")

    outcomes = [
        "`keep_private`",
        "`revise_private_package`",
        "`approve_sanitized_public_sample_planning`",
        "`reject_public_promotion`",
    ]
    for outcome in outcomes:
        require(outcome in doc, f"doc must include promotion outcome: {outcome}")

    required_phrases = [
        "This checkpoint is review and promotion gate planning only.",
        "This proposition is intentionally non-executing.",
        "This review input is private-first and not intended to be committed.",
        "The review is not an audit opinion.",
        "Any uncertainty should block public promotion.",
        "Public sample promotion is not delivery authorization.",
        "Every blocker should keep the package private.",
        "No outcome authorizes runtime execution, scanner execution, customer-target testing, or report delivery.",
        "Public sample planning should not include tool-backed local-lab execution.",
        "Do not expose private generated contents if the package remains private.",
        "The earliest next step is review / promotion gate work, not live diagnostic execution.",
        "Rollback is a safety control, not a failure.",
        "v0.6.31 Static/Mock Applied Evidence Package Private Review Record",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    false_markers = [
        "promotion_gate_planning_completed = true",
        "public_sample_promotion_authorized = false",
        "public_sample_generated = false",
        "private_package_review_record_generated = false",
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
        "real_execution_permitted = false",
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
        "this checkpoint promotes public samples",
        "this checkpoint generates public sample artifacts",
        "this checkpoint generates a private review record",
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

    require("Add v0.6.30 static/mock applied evidence package review and promotion gate planning" in adr, "ADR must record v0.6.30 decision")
    require("Completed by v0.6.30 candidate" in issue, "Issue must record v0.6.30 completion status")
    require("## v0.6.30 - Static/mock applied evidence package review and promotion gate planning" in changelog, "CHANGELOG must include v0.6.30")
    require("## v0.6.30 Static/mock applied evidence package review and promotion gate planning" in roadmap, "ROADMAP must include v0.6.30")
    require("test_v0630_static_mock_applied_evidence_review_promotion_gate_planning.py" in run_all, "run_all must include v0.6.30 test")

    print("v0.6.30 static/mock applied evidence review and promotion gate planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
