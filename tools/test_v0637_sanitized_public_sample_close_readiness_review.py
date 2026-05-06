from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/114-v0637-sanitized-public-sample-close-readiness-review.md"


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
    adr = read_text("planning/decisions/ADR-0108-add-v0637-sanitized-public-sample-close-readiness-review.md")
    issue = read_text("planning/issues/0107-add-v0637-sanitized-public-sample-close-readiness-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.37 checkpoint")
    require("v0.6.37 Sanitized Public Sample Close-Readiness Review" in doc, "v0.6.37 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("publication_review_status = reviewed_retain_limited_public_example" in doc, "doc must reference v0.6.36 review status")
    require("hygiene_status = passed" in doc, "doc must reference hygiene status")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must reference public sample directory")

    sections = [
        "Review inputs",
        "Close-readiness criteria",
        "Close-readiness assessment",
        "Remaining limitations",
        "Close recommendation",
        "Next-track options",
        "AAEF-side reporting note",
        "Relationship to diagnostic execution",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    required_phrases = [
        "This checkpoint is close-readiness review only.",
        "This proposition authorizes only close-readiness recording for the sanitized public sample track.",
        "The public sample track can be treated as close-ready for now.",
        "The sanitized public sample track can be closed as a limited public example track.",
        "The recommended next step is public example structural validation planning before returning to runtime-oriented work.",
        "The next safe step is public example structural validation planning, not live diagnostic execution.",
        "v0.6.38 Public Example Structural Validation Planning",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    limitations = [
        "vulnerability detection accuracy",
        "diagnostic completeness",
        "production readiness",
        "implementation conformance",
        "audit sufficiency",
        "legal sufficiency",
        "compliance certification",
        "external-framework equivalence",
        "customer-target authorization",
        "report delivery authorization",
        "managed service readiness",
        "safety guarantee",
    ]
    for limitation in limitations:
        require(limitation in doc, f"doc must include limitation: {limitation}")

    markers = [
        "sanitized_public_sample_track_close_ready = true",
        "close_sanitized_public_sample_track = true",
        "retain_limited_public_example = true",
        "public_example_structural_validation_planning_recommended = true",
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

    require("Add v0.6.37 sanitized public sample close-readiness review" in adr, "ADR must record v0.6.37 decision")
    require("Completed by v0.6.37 candidate" in issue, "Issue must record v0.6.37 completion status")
    require("## v0.6.37 - Sanitized public sample close-readiness review" in changelog, "CHANGELOG must include v0.6.37")
    require("## v0.6.37 Sanitized public sample close-readiness review" in roadmap, "ROADMAP must include v0.6.37")
    require("test_v0637_sanitized_public_sample_close_readiness_review.py" in run_all, "run_all must include v0.6.37 test")

    print("v0.6.37 sanitized public sample close-readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
