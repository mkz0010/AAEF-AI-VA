from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/113-v0636-sanitized-public-sample-publication-review-record.md"
EXAMPLE_ROOT = REPO / "examples/applied-evidence/sanitized-static-mock"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_cmd(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(REPO), text=True, capture_output=True, check=False)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    generator = read_text("tools/generate_sanitized_public_sample_publication_review_record.py")
    adr = read_text("planning/decisions/ADR-0107-add-v0636-sanitized-public-sample-publication-review-record.md")
    issue = read_text("planning/issues/0106-add-v0636-sanitized-public-sample-publication-review-record.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.36 checkpoint")
    require("v0.6.36 Sanitized Public Sample Publication Review Record" in doc, "v0.6.36 doc must exist")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("examples/applied-evidence/sanitized-static-mock/" in doc, "doc must reference public sample directory")

    forbidden_runtime_terms = [
        "os.system(",
        "requests.",
        "urllib.request",
        "socket.",
        "docker run",
        "nmap -",
        "zap-cli",
        "nuclei -",
    ]
    generator_lower = generator.lower()
    for term in forbidden_runtime_terms:
        require(term.lower() not in generator_lower, f"generator must not include runtime behavior: {term}")

    sample_proc = run_cmd([sys.executable, "tools/generate_sanitized_public_sample.py"])
    require(sample_proc.returncode == 0, sample_proc.stderr or sample_proc.stdout)

    review_proc = run_cmd([sys.executable, "tools/generate_sanitized_public_sample_publication_review_record.py"])
    require(review_proc.returncode == 0, review_proc.stderr or review_proc.stdout)
    payload = json.loads(review_proc.stdout)

    require(payload["status"] == "reviewed_retain_limited_public_example", "review status mismatch")
    require(payload["publication_limit"] == "limited_synthetic_non_executing_example", "publication limit mismatch")
    require(payload["scenario_count"] == 4, "scenario count mismatch")
    require(payload["hygiene_status"] == "passed", "hygiene status mismatch")
    require(payload["blocker_categories"] == [], "blockers must be empty")
    require(payload["runtime_boundary"]["runtime_execution_authorized"] is False, "runtime execution must remain false")
    require(payload["runtime_boundary"]["scanner_execution_authorized"] is False, "scanner execution must remain false")
    require(payload["runtime_boundary"]["customer_target"] is False, "customer target must remain false")
    require(payload["runtime_boundary"]["delivery_authorized"] is False, "delivery must remain false")

    record_json = EXAMPLE_ROOT / "publication_review_record.example.json"
    record_md = EXAMPLE_ROOT / "publication_review_record.example.md"
    require(record_json.exists(), "publication review JSON missing")
    require(record_md.exists(), "publication review MD missing")
    record = load_json(record_json)
    markdown = record_md.read_text(encoding="utf-8")

    require(record["publication_review_status"] == "reviewed_retain_limited_public_example", "record status mismatch")
    require(record["all_example_names"] is True, "all public artifact names must be example-safe")
    require(record["linkage_ok"] is True, "linkage must be ok")
    require(record["boundary_ok"] is True, "boundary must be ok")
    require(record["non_proof_visible"] is True, "non-proof must be visible")
    require(record["blocker_categories"] == [], "record blockers must be empty")
    require("does not authorize runtime execution" in markdown, "markdown boundary statement missing")

    public_files = [p for p in EXAMPLE_ROOT.rglob("*") if p.is_file()]
    require(public_files, "public example files must exist")
    for path in public_files:
        name = path.name
        rel = path.relative_to(EXAMPLE_ROOT).as_posix()
        require(name == "README.md" or ".example." in name, f"non-example public artifact name: {rel}")
        text = path.read_text(encoding="utf-8")
        forbidden_fragments = [
            "private-not-in-git",
            ".generated.",
            "BEGIN RSA PRIVATE KEY",
            "customer.example.com",
            "docker run",
            "127.0.0.1",
            "192.168.",
            "10.0.",
        ]
        for fragment in forbidden_fragments:
            require(fragment.lower() not in text.lower(), f"public file contains forbidden fragment {fragment}: {rel}")

    required_doc_phrases = [
        "This checkpoint is sanitized public sample publication review recording only.",
        "This proposition authorizes only publication review recording for the sanitized public example.",
        "The generated review record is a public example review artifact, not a customer deliverable.",
        "The review is publication-oriented, not diagnostic assurance.",
        "This status does not elevate the example into production guidance, implementation conformance, audit evidence, legal advice, or customer deliverable material.",
        "Any blocker should prevent treating the sample as reviewed.",
        "The next safe step is structural validation planning for public examples or a public sample close-readiness review, not live diagnostic execution.",
        "v0.6.37 Sanitized Public Sample Close-Readiness Review",
    ]
    for phrase in required_doc_phrases:
        require(phrase in doc, f"doc must include phrase: {phrase}")

    markers = [
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
    combined = "\n".join([readme, doc, generator, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("Add v0.6.36 sanitized public sample publication review record" in adr, "ADR must record v0.6.36 decision")
    require("Completed by v0.6.36 candidate" in issue, "Issue must record v0.6.36 completion status")
    require("## v0.6.36 - Sanitized public sample publication review record" in changelog, "CHANGELOG must include v0.6.36")
    require("## v0.6.36 Sanitized public sample publication review record" in roadmap, "ROADMAP must include v0.6.36")
    require("test_v0636_sanitized_public_sample_publication_review_record.py" in run_all, "run_all must include v0.6.36 test")

    print("v0.6.36 sanitized public sample publication review record tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
