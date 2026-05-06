from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/119-v0642-aaef-applied-implementation-handback-summary.md"


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
    adr = read_text("planning/decisions/ADR-0113-add-v0642-aaef-applied-implementation-handback-summary.md")
    issue = read_text("planning/issues/0112-add-v0642-aaef-applied-implementation-handback-summary.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.42 checkpoint")
    require("v0.6.42 AAEF Applied Implementation Handback Summary" in doc, "v0.6.42 doc must exist")
    require("AAEF category = Applied Implementation" in doc, "doc must classify handback as Applied Implementation")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must include evidence package path")
    require("tools/validate_public_example_structure.py" in doc, "doc must include validator path")
    require("reviewer_walkthrough.example.md" in doc, "doc must include reviewer walkthrough location")
    require("aaef_five_questions_mapping.example.md" in doc, "doc must include five-questions mapping location")

    generator_proc = run_cmd([sys.executable, "tools/generate_sanitized_public_sample.py"])
    require(generator_proc.returncode == 0, generator_proc.stderr or generator_proc.stdout)

    review_proc = run_cmd([sys.executable, "tools/generate_sanitized_public_sample_publication_review_record.py"])
    require(review_proc.returncode == 0, review_proc.stderr or review_proc.stdout)

    validator_proc = run_cmd([sys.executable, "tools/validate_public_example_structure.py", "--json"])
    require(validator_proc.returncode == 0, validator_proc.stderr or validator_proc.stdout)
    result = json.loads(validator_proc.stdout)
    require(result["public_example_structural_validation_status"] == "passed", "validator status must pass")
    require(result["scenario_count"] == 4, "scenario count must be 4")
    require(result["hygiene_status"] == "passed", "hygiene status must pass")
    require(result["publication_review_status"] == "reviewed_retain_limited_public_example", "publication review status mismatch")
    require(result["blocker_categories"] == [], "blocker categories must be empty")
    require(result["runtime_boundary"]["runtime_execution_authorized"] is False, "runtime must remain false")
    require(result["runtime_boundary"]["scanner_execution_authorized"] is False, "scanner must remain false")
    require(result["runtime_boundary"]["customer_target"] is False, "customer target must remain false")
    require(result["runtime_boundary"]["delivery_authorized"] is False, "delivery must remain false")

    sections = [
        "Classification",
        "Public-safe handback boundary",
        "Current checkpoint state",
        "Execution and repository references",
        "Validation summary",
        "Changed file list for this checkpoint",
        "Scenario list",
        "Evidence package structure",
        "Reviewer walkthrough location",
        "Validator result summary",
        "AAEF five questions handback",
        "Request-not-authority handback",
        "Gate decision handback",
        "Dispatch and non-dispatch handback",
        "Non-execution evidence handback",
        "Reviewer traceability handback",
        "Candidate lessons for AAEF main",
        "Excluded from handback",
        "Recommended AAEF handback package",
        "Runtime and scanning boundary",
        "Claims to avoid",
        "Recommended next checkpoint",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    required_phrases = [
        "This checkpoint is Applied Implementation handback summary only.",
        "This handback stays at the evidence/interface level.",
        "The handback is about what the Applied Implementation demonstrates at the evidence boundary.",
        "The track is close-ready as a limited synthetic non-executing public example and read-only validator.",
        "Commit URL should be supplied from the terminal log after merge and push.",
        "The handback is valid only if local checks pass before merge/tag/push.",
        "The scenarios are synthetic examples, not live diagnostic evidence.",
        "The evidence package uses `.example.` artifacts and remains synthetic and non-executing.",
        "The validator result is structural evidence about the public example set, not proof of diagnostic correctness.",
        "The request is not authority.",
        "Non-execution evidence is first-class evidence.",
        "A reviewer can reconstruct the decision path without needing private implementation details.",
        "These are candidate lessons only. They do not promote AAEF-AI-VA implementation details into AAEF Core.",
        "The public handback must remain conservative.",
        "v0.6.43 Applied Implementation Handback Review and Next Direction",
    ]
    for phrase in required_phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    handback_items = [
        "repository URL",
        "tag URL after push",
        "commit URL after merge",
        "local execution log excerpt showing `All local checks passed.`",
        "changed file list",
        "scenario list",
        "evidence package structure",
        "reviewer walkthrough location",
        "AAEF five-questions mapping location",
        "validator location",
        "validator result summary",
        "claim-boundary note",
        "excluded-material note",
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

    markers = [
        "aaef_applied_implementation_handback_summary_completed = true",
        "aaef_handback_category_applied_implementation = true",
        "aaef_core_promotion = false",
        "aaef_profile_promotion = false",
        "aaef_practical_package_promotion = false",
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

    require("Add v0.6.42 AAEF Applied Implementation handback summary" in adr, "ADR must record v0.6.42 decision")
    require("Completed by v0.6.42 candidate" in issue, "Issue must record v0.6.42 completion status")
    require("## v0.6.42 - AAEF Applied Implementation handback summary" in changelog, "CHANGELOG must include v0.6.42")
    require("## v0.6.42 AAEF Applied Implementation handback summary" in roadmap, "ROADMAP must include v0.6.42")
    require("test_v0642_aaef_applied_implementation_handback_summary.py" in run_all, "run_all must include v0.6.42 test")

    print("v0.6.42 AAEF Applied Implementation handback summary tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
