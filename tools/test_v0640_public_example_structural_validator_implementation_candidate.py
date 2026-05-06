from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/117-v0640-public-example-structural-validator-implementation-candidate.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_cmd(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(REPO), text=True, capture_output=True, check=False)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    validator = read_text("tools/validate_public_example_structure.py")
    adr = read_text("planning/decisions/ADR-0111-add-v0640-public-example-structural-validator-implementation-candidate.md")
    issue = read_text("planning/issues/0110-add-v0640-public-example-structural-validator-implementation-candidate.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.40 checkpoint")
    require("v0.6.40 Public Example Structural Validator Implementation Candidate" in doc, "v0.6.40 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("tools/validate_public_example_structure.py" in doc, "doc must reference validator")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must reference public sample directory")

    forbidden_runtime_terms = [
        "os.system(",
        "requests.",
        "urllib.request",
        "socket.",
        "nmap -",
        "zap-cli",
        "nuclei -",
    ]
    validator_lower = validator.lower()
    for term in forbidden_runtime_terms:
        require(term.lower() not in validator_lower, f"validator must not include runtime behavior: {term}")

    generator_proc = run_cmd([sys.executable, "tools/generate_sanitized_public_sample.py"])
    require(generator_proc.returncode == 0, generator_proc.stderr or generator_proc.stdout)

    review_proc = run_cmd([sys.executable, "tools/generate_sanitized_public_sample_publication_review_record.py"])
    require(review_proc.returncode == 0, review_proc.stderr or review_proc.stdout)

    proc = run_cmd([sys.executable, "tools/validate_public_example_structure.py", "--json"])
    require(proc.returncode == 0, proc.stderr or proc.stdout)
    result = json.loads(proc.stdout)

    require(result["public_example_structural_validation_status"] == "passed", "validator status must pass")
    require(result["scenario_count"] == 4, "scenario count must be 4")
    require(result["expected_scenario_count"] == 4, "expected scenario count must be 4")
    require(result["hygiene_status"] == "passed", "hygiene status must pass")
    require(result["publication_review_status"] == "reviewed_retain_limited_public_example", "publication review status mismatch")
    require(result["blocker_categories"] == [], "blockers must be empty")
    require(result["runtime_boundary"]["public_example_structural_validator_read_only"] is True, "validator must be read-only")
    require(result["runtime_boundary"]["public_example_structural_validator_public_example_scoped"] is True, "validator must be public-example scoped")
    require(result["runtime_boundary"]["public_example_structural_validator_authorizes_execution"] is False, "validator must not authorize execution")
    require(result["runtime_boundary"]["runtime_execution_authorized"] is False, "runtime must remain false")
    require(result["runtime_boundary"]["scanner_execution_authorized"] is False, "scanner must remain false")
    require(result["runtime_boundary"]["customer_target"] is False, "customer target must remain false")
    require(result["runtime_boundary"]["delivery_authorized"] is False, "delivery must remain false")

    scenario_ids = {review["scenario_id"] for review in result["scenario_reviews"]}
    require(scenario_ids == {"permitted-safe-diagnostic", "denied-out-of-scope-request", "human-approval-required", "not-executed-expired"}, "scenario set mismatch")
    for review in result["scenario_reviews"]:
        require(review["linkage_ok"] is True, f"linkage must pass for {review['scenario_id']}")
        require(review["boundary_ok"] is True, f"boundary must pass for {review['scenario_id']}")
        require(review["non_proof_visible"] is True, f"non-proof must be visible for {review['scenario_id']}")
        require(review["posture_ok"] is True, f"posture must pass for {review['scenario_id']}")

    required_doc_phrases = [
        "This checkpoint is read-only structural validator implementation only.",
        "This proposition authorizes only read-only public example structural validation implementation.",
        "The validator does not mutate public examples.",
        "The output is local validation output, not certification, legal approval, audit opinion, compliance evidence, or customer deliverable material.",
        "Fail-closed behavior is implemented as a validation failure.",
        "The next safe step is public example structural validator review and close-readiness, not live diagnostic execution.",
        "v0.6.41 Public Example Structural Validator Review and Close-Readiness",
    ]
    for phrase in required_doc_phrases:
        require(phrase in doc, f"doc must include phrase: {phrase}")

    markers = [
        "public_example_structural_validator_implementation_candidate_completed = true",
        "public_example_structural_validator_implemented = true",
        "public_example_structural_validator_checks_execute = true",
        "public_example_structural_validator_read_only = true",
        "public_example_structural_validator_public_example_scoped = true",
        "public_example_structural_validator_authorizes_execution = false",
        "public_example_structural_validation_planning_completed = true",
        "public_example_structural_validator_implementation_readiness_review_completed = true",
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
    combined = "\n".join([readme, doc, validator, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("Add v0.6.40 public example structural validator implementation candidate" in adr, "ADR must record v0.6.40 decision")
    require("Completed by v0.6.40 candidate" in issue, "Issue must record v0.6.40 completion status")
    require("## v0.6.40 - Public example structural validator implementation candidate" in changelog, "CHANGELOG must include v0.6.40")
    require("## v0.6.40 Public example structural validator implementation candidate" in roadmap, "ROADMAP must include v0.6.40")
    require("test_v0640_public_example_structural_validator_implementation_candidate.py" in run_all, "run_all must include v0.6.40 test")

    print("v0.6.40 public example structural validator implementation candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
