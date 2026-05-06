from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/110-v0633-sanitized-public-sample-planning.md"


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
    adr = read_text("planning/decisions/ADR-0104-add-v0633-sanitized-public-sample-planning.md")
    issue = read_text("planning/issues/0103-add-v0633-sanitized-public-sample-planning.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.33 checkpoint")
    require("v0.6.33 Sanitized Public Sample Planning" in doc, "v0.6.33 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must include candidate public directory")
    require("private-not-in-git/applied-evidence-runs/static-mock-demo/" in doc, "doc must reference private source lineage")

    sections = [
        "Public sample scope",
        "Candidate public directory placement",
        "Sanitized artifact naming",
        "Scenario coverage plan",
        "Private-to-public transformation rules",
        "Synthetic-only requirements",
        "Publication hygiene checks",
        "Patent-sensitive detail exclusion",
        "Non-proof visibility",
        "Overclaim prevention",
        "Human publication review",
        "Future generation gate",
        "AAEF-side reporting note",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    artifacts = [
        "`package_manifest.example.json`",
        "`tool_action_request.example.json`",
        "`gate_decision.example.json`",
        "`dispatch_decision.example.json`",
        "`execution_result.example.json`",
        "`non_execution_result.example.json`",
        "`evidence_event.example.json`",
        "`review_summary.example.md`",
        "`non_proof_statement.example.md`",
        "`reviewer_walkthrough.example.md`",
        "`aaef_five_questions_mapping.example.md`",
    ]
    for artifact in artifacts:
        require(artifact in doc, f"doc must include sanitized artifact name: {artifact}")

    required_phrases = [
        "This checkpoint is sanitized public sample planning only.",
        "This proposition is intentionally non-executing.",
        "This checkpoint does not create that directory.",
        "Private paths should not be copied directly into the public tree.",
        "Generated private filenames should not be exposed as if they were public evidence.",
        "The scenario set should remain synthetic and non-executing.",
        "Transformation must be reviewable before publication.",
        "They must not contain customer data, production data, secrets, credentials, live scan output, third-party target details, or operational runtime traces.",
        "Any uncertainty should block publication.",
        "Do not include private advanced feature details, claim drafts, prior-art analysis, patent strategy, or implementation details that were intentionally kept private.",
        "Non-proof statements should not be hidden in JSON only.",
        "Overclaim prevention is a blocker for publication.",
        "Human publication review remains a gate.",
        "Planning acceptance is not generation authorization.",
        "v0.6.34 Sanitized Public Sample Generation Readiness Review",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    markers = [
        "sanitized_public_sample_planning_completed = true",
        "sanitized_public_sample_generation_ready = false",
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

    require("Add v0.6.33 sanitized public sample planning" in adr, "ADR must record v0.6.33 decision")
    require("Completed by v0.6.33 candidate" in issue, "Issue must record v0.6.33 completion status")
    require("## v0.6.33 - Sanitized public sample planning" in changelog, "CHANGELOG must include v0.6.33")
    require("## v0.6.33 Sanitized public sample planning" in roadmap, "ROADMAP must include v0.6.33")
    require("test_v0633_sanitized_public_sample_planning.py" in run_all, "run_all must include v0.6.33 test")

    print("v0.6.33 sanitized public sample planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
