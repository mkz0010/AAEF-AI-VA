from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/118-v0641-public-example-structural-validator-review-and-close-readiness.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains(text: str, phrase: str) -> bool:
    return re.sub(r"\s+", " ", phrase).strip() in re.sub(r"\s+", " ", text).strip()


def run_cmd(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(REPO), text=True, capture_output=True, check=False)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0112-add-v0641-public-example-structural-validator-review-and-close-readiness.md")
    issue = read_text("planning/issues/0111-add-v0641-public-example-structural-validator-review-and-close-readiness.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.41 checkpoint")
    require("v0.6.41 Public Example Structural Validator Review and Close-Readiness" in doc, "v0.6.41 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("tools/validate_public_example_structure.py" in doc, "doc must reference validator")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must reference evidence package")
    require("AAEF Applied Implementation handback" in doc, "doc must include AAEF handback section")

    generator_proc = run_cmd([sys.executable, "tools/generate_sanitized_public_sample.py"])
    require(generator_proc.returncode == 0, generator_proc.stderr or generator_proc.stdout)

    review_proc = run_cmd([sys.executable, "tools/generate_sanitized_public_sample_publication_review_record.py"])
    require(review_proc.returncode == 0, review_proc.stderr or review_proc.stdout)

    validator_proc = run_cmd([sys.executable, "tools/validate_public_example_structure.py", "--json"])
    require(validator_proc.returncode == 0, validator_proc.stderr or validator_proc.stdout)
    result = json.loads(validator_proc.stdout)

    require(result["public_example_structural_validation_status"] == "passed", "validator status must pass")
    require(result["scenario_count"] == 4, "scenario count must be 4")
    require(result["expected_scenario_count"] == 4, "expected scenario count must be 4")
    require(result["hygiene_status"] == "passed", "hygiene status must pass")
    require(result["publication_review_status"] == "reviewed_retain_limited_public_example", "publication review status mismatch")
    require(result["blocker_categories"] == [], "blocker categories must be empty")
    require(result["runtime_boundary"]["public_example_structural_validator_read_only"] is True, "validator must be read-only")
    require(result["runtime_boundary"]["public_example_structural_validator_public_example_scoped"] is True, "validator must be public-example scoped")
    require(result["runtime_boundary"]["public_example_structural_validator_authorizes_execution"] is False, "validator must not authorize execution")
    require(result["runtime_boundary"]["runtime_execution_authorized"] is False, "runtime execution must remain false")
    require(result["runtime_boundary"]["scanner_execution_authorized"] is False, "scanner execution must remain false")
    require(result["runtime_boundary"]["customer_target"] is False, "customer target must remain false")
    require(result["runtime_boundary"]["delivery_authorized"] is False, "delivery must remain false")

    sections = [
        "Review input",
        "Validator result reviewed",
        "Close-readiness criteria",
        "Close-readiness assessment",
        "Remaining limitations",
        "AAEF Applied Implementation handback",
        "AAEF handback checklist",
        "Evidence package structure",
        "Close recommendation",
        "Next-track options",
        "Relationship to diagnostic execution",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    required_phrases = [
        "This checkpoint is validator review and close-readiness only.",
        "This proposition authorizes only validator review and close-readiness recording.",
        "The validator result is structural evidence about the public example set, not evidence of diagnostic correctness.",
        "The public example structural validation track can be treated as close-ready for now.",
        "The handback should not include AAEF-AI-VA detailed implementation, patent-sensitive browser-state or diagnostic reconstruction detail, commercial strategy, pricing strategy, customer lists, or NDA-assumed content.",
        "The public example structural validation track can be closed as a read-only public example validation track.",
        "The recommended next step is an AAEF handback summary or public validator hardening planning, not live diagnostic execution.",
        "The next safe step is AAEF Applied Implementation handback or public validator hardening planning, not live diagnostic execution.",
        "v0.6.42 AAEF Applied Implementation Handback Summary",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    handback_items = [
        "PR URL or commit URL",
        "execution log",
        "changed file list",
        "`tools/run_all_local_checks.py` result",
        "scenario list",
        "evidence package structure",
        "reviewer walkthrough location",
        "validator location",
        "validator result summary",
        "AAEF five-questions mapping location",
        "non-proof statement location",
    ]
    for item in handback_items:
        require(item in doc, f"doc must include handback item: {item}")

    markers = [
        "public_example_structural_validator_review_completed = true",
        "public_example_structural_validation_track_close_ready = true",
        "close_public_example_structural_validation_track = true",
        "retain_read_only_public_example_validator = true",
        "public_example_structural_validation_status = passed",
        "public_example_structural_validator_implemented = true",
        "public_example_structural_validator_checks_execute = true",
        "public_example_structural_validator_read_only = true",
        "public_example_structural_validator_public_example_scoped = true",
        "public_example_structural_validator_authorizes_execution = false",
        "aaef_applied_implementation_handback_recommended = true",
        "sanitized_public_sample_track_close_ready = true",
        "retain_limited_public_example = true",
        "sanitized_public_sample_candidate_generated = true",
        "public_sample_publication_review_completed = true",
        "publication_review_record_generated = true",
        "private_artifact_copied_to_public = false",
        "structural_validator_implemented = true",
        "structural_validator_checks_execute = true",
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

    require("Add v0.6.41 public example structural validator review and close-readiness" in adr, "ADR must record v0.6.41 decision")
    require("Completed by v0.6.41 candidate" in issue, "Issue must record v0.6.41 completion status")
    require("## v0.6.41 - Public example structural validator review and close-readiness" in changelog, "CHANGELOG must include v0.6.41")
    require("## v0.6.41 Public example structural validator review and close-readiness" in roadmap, "ROADMAP must include v0.6.41")
    require("test_v0641_public_example_structural_validator_review_close_readiness.py" in run_all, "run_all must include v0.6.41 test")

    print("v0.6.41 public example structural validator review and close-readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
