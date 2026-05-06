from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/105-v0628-static-mock-applied-evidence-package-generation-readiness-review.md"


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
    adr = read_text("planning/decisions/ADR-0099-add-v0628-static-mock-applied-evidence-generation-readiness-review.md")
    issue = read_text("planning/issues/0098-add-v0628-static-mock-applied-evidence-generation-readiness-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.28 checkpoint")
    require("v0.6.28 Static/Mock Applied Evidence Package Generation Readiness Review" in doc, "v0.6.28 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")

    sections = [
        "Readiness summary",
        "Required readiness inputs",
        "Static/mock generation readiness criteria",
        "Private-first generation posture",
        "Public-safe promotion criteria",
        "Blocker categories",
        "Minimum generated package candidate",
        "Evidence package generation sequence",
        "Structural validator readiness relationship",
        "Reviewer review requirement",
        "Diagnostic system timing",
        "Completion signal for AAEF side",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    artifacts = [
        "`package_manifest.generated.json`",
        "`tool_action_request.generated.json`",
        "`gate_decision.generated.json`",
        "`dispatch_decision.generated.json`",
        "`execution_result.generated.json`",
        "`non_execution_result.generated.json`",
        "`evidence_event.generated.json`",
        "`review_summary.generated.md`",
        "`non_proof_statement.generated.md`",
        "`reviewer_walkthrough.generated.md`",
        "`aaef_five_questions_mapping.generated.md`",
    ]
    for artifact in artifacts:
        require(artifact in doc, f"doc must include generated artifact planning term: {artifact}")

    blockers = [
        "`package_structure_unstable`",
        "`scenario_set_unstable`",
        "`fixture_artifact_plan_unstable`",
        "`identifier_linkage_unstable`",
        "`non_execution_evidence_unclear`",
        "`reviewer_walkthrough_unclear`",
        "`five_questions_mapping_unclear`",
        "`non_proof_statement_missing`",
        "`overclaim_prevention_unclear`",
        "`public_private_boundary_unclear`",
        "`runtime_implication_detected`",
        "`scanner_output_implication_detected`",
        "`credential_implication_detected`",
        "`customer_target_implication_detected`",
        "`delivery_authorization_implication_detected`",
        "`patent_sensitive_detail_detected`",
        "`human_review_missing`",
    ]
    for blocker in blockers:
        require(blocker in doc, f"doc must include blocker category: {blocker}")

    required_phrases = [
        "This checkpoint is generation-readiness review only.",
        "This proposition is intentionally non-executing.",
        "The readiness review result is conditional readiness for a private-first static/mock generation checkpoint, not authorization to run diagnostic tools.",
        "The next safe movement is private-first static/mock package generation planning or a minimal private generation candidate, not live diagnostic execution.",
        "Any uncertainty should block generation or route it to human review.",
        "The first generated package should be private-first.",
        "Public-safe promotion is not delivery authorization.",
        "Every blocker should prevent generation.",
        "Generation should not run Docker or scanners.",
        "Structural validator planning is sufficient for generation readiness review, but not sufficient for public promotion.",
        "Human review remains a gate.",
        "The earliest safe next step is not live diagnostic execution.",
        "v0.6.29 Static/Mock Applied Evidence Package Private Generation Candidate",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    false_markers = [
        "generation_readiness_review_completed = true",
        "static_mock_generation_authorized_for_public = false",
        "static_mock_generation_started = false",
        "static_mock_package_generated = false",
        "structural_validator_implemented = false",
        "structural_validator_checks_execute = false",
        "reviewer_walkthrough_generated = false",
        "five_questions_mapping_generated = false",
        "static_applied_evidence_fixtures_generated = false",
        "applied_evidence_scenarios_generated = false",
        "applied_evidence_package_generated = false",
        "static_mock_evidence_capture_started = false",
        "tool_backed_diagnostic_capture_started = false",
        "local_lab_diagnostic_system_built = false",
        "fixture_generated = false",
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
        "this checkpoint generates static/mock packages",
        "this checkpoint generates evidence packages",
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
        "this checkpoint approves public samples",
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

    require("Add v0.6.28 static/mock applied evidence package generation readiness review" in adr, "ADR must record v0.6.28 decision")
    require("Completed by v0.6.28 candidate" in issue, "Issue must record v0.6.28 completion status")
    require("## v0.6.28 - Static/mock applied evidence package generation readiness review" in changelog, "CHANGELOG must include v0.6.28")
    require("## v0.6.28 Static/mock applied evidence package generation readiness review" in roadmap, "ROADMAP must include v0.6.28")
    require("test_v0628_static_mock_applied_evidence_generation_readiness_review.py" in run_all, "run_all must include v0.6.28 test")

    print("v0.6.28 static/mock applied evidence package generation readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
