from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_SAMPLE_DIR = Path("examples/applied-evidence/sanitized-static-mock")
GENERATOR_VERSION = "v0.6.36-public-sample-publication-review"

EXPECTED_SCENARIOS = [
    "permitted-safe-diagnostic",
    "denied-out-of-scope-request",
    "human-approval-required",
    "not-executed-expired",
]

RUNTIME_BOUNDARY: dict[str, bool] = {
    "sanitized_public_sample_candidate_generated": True,
    "public_sample_publication_review_completed": True,
    "publication_review_record_generated": True,
    "private_artifact_copied_to_public": False,
    "structural_validator_implemented": False,
    "structural_validator_checks_execute": False,
    "tool_backed_diagnostic_capture_started": False,
    "local_lab_diagnostic_system_built": False,
    "fixture_live_evidence": False,
    "validator_authorizes_execution": False,
    "validator_authorizes_scanning": False,
    "validator_authorizes_docker": False,
    "validator_authorizes_delivery": False,
    "docker_compose_file_created": False,
    "docker_compose_executed": False,
    "docker_image_pulled": False,
    "container_started": False,
    "port_bound": False,
    "docker_execution_authorized": False,
    "execution_authorized": False,
    "runtime_execution_authorized": False,
    "scanner_execution_authorized": False,
    "real_execution_permitted": False,
    "network_activity_allowed": False,
    "scan_execution_allowed": False,
    "credential_injection_permitted": False,
    "customer_target": False,
    "customer_target_authorized": False,
    "external_network_target": False,
    "delivery_authorized": False,
    "customer_deliverable": False,
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_md(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")


def exists(path: Path) -> bool:
    return path.exists() and path.is_file()


def expected_result_file(scenario_id: str) -> str:
    if scenario_id == "permitted-safe-diagnostic":
        return "execution_result.example.json"
    return "non_execution_result.example.json"


def review_scenario(root: Path, scenario_id: str) -> dict[str, Any]:
    scenario_dir = root / "scenarios" / scenario_id
    artifact_paths = {
        "request": scenario_dir / "tool_action_request.example.json",
        "gate_decision": scenario_dir / "gate_decision.example.json",
        "dispatch_decision": scenario_dir / "dispatch_decision.example.json",
        "result": scenario_dir / expected_result_file(scenario_id),
        "evidence_event": scenario_dir / "evidence_event.example.json",
        "review_summary": scenario_dir / "review_summary.example.md",
        "non_proof_statement": scenario_dir / "non_proof_statement.example.md",
    }
    presence = {name: exists(path) for name, path in artifact_paths.items()}
    blockers: list[str] = []

    if not scenario_dir.is_dir():
        blockers.append("scenario_missing")
    for name, present in presence.items():
        if not present:
            blockers.append(f"artifact_missing:{name}")

    linkage_ok = False
    boundary_ok = False
    non_proof_visible = presence["non_proof_statement"]

    if all(presence.values()):
        request = load_json(artifact_paths["request"])
        decision = load_json(artifact_paths["gate_decision"])
        dispatch = load_json(artifact_paths["dispatch_decision"])
        result = load_json(artifact_paths["result"])
        evidence = load_json(artifact_paths["evidence_event"])

        linkage_ok = (
            decision.get("linked_request_id") == request.get("request_id")
            and dispatch.get("linked_decision_id") == decision.get("decision_id")
            and result.get("linked_dispatch_decision_id") == dispatch.get("dispatch_decision_id")
            and evidence.get("linked_request_id") == request.get("request_id")
            and evidence.get("linked_decision_id") == decision.get("decision_id")
            and evidence.get("linked_dispatch_decision_id") == dispatch.get("dispatch_decision_id")
            and evidence.get("linked_result_id") == result.get("result_id")
        )
        if not linkage_ok:
            blockers.append("identifier_linkage_broken")

        rb = result.get("runtime_boundary", {})
        boundary_ok = (
            rb.get("runtime_execution_authorized") is False
            and rb.get("scanner_execution_authorized") is False
            and rb.get("scan_execution_allowed") is False
            and rb.get("customer_target") is False
            and rb.get("delivery_authorized") is False
        )
        if not boundary_ok:
            blockers.append("runtime_or_delivery_boundary_issue")

    return {
        "scenario_id": scenario_id,
        "artifact_presence": presence,
        "linkage_ok": linkage_ok,
        "boundary_ok": boundary_ok,
        "non_proof_visible": non_proof_visible,
        "blockers": blockers,
    }


def generate_review(sample_dir: Path) -> dict[str, Any]:
    blockers: list[str] = []
    if not sample_dir.is_dir():
        blockers.append("example_root_missing")

    package_artifacts = {
        "readme": sample_dir / "README.md",
        "package_manifest": sample_dir / "package_manifest.example.json",
        "reviewer_walkthrough": sample_dir / "reviewer_walkthrough.example.md",
        "five_questions_mapping": sample_dir / "aaef_five_questions_mapping.example.md",
        "package_non_proof_statement": sample_dir / "non_proof_statement.example.md",
        "publication_hygiene_report": sample_dir / "publication_hygiene_report.example.json",
    }
    package_presence = {name: exists(path) for name, path in package_artifacts.items()}
    for name, present in package_presence.items():
        if not present:
            blockers.append(f"{name}_missing")

    scenario_reviews = [review_scenario(sample_dir, scenario_id) for scenario_id in EXPECTED_SCENARIOS]
    for review in scenario_reviews:
        blockers.extend(review["blockers"])

    all_example_names = True
    for path in sample_dir.rglob("*"):
        if path.is_file():
            name = path.name
            if name != "README.md" and ".example." not in name:
                all_example_names = False
                blockers.append("non_example_artifact_name_detected")
                break

    hygiene_status = "missing"
    if package_presence["publication_hygiene_report"]:
        hygiene = load_json(package_artifacts["publication_hygiene_report"])
        hygiene_status = str(hygiene.get("hygiene_status"))
        if hygiene_status != "passed":
            blockers.append("hygiene_status_not_passed")

    linkage_ok = all(review["linkage_ok"] for review in scenario_reviews)
    boundary_ok = all(review["boundary_ok"] for review in scenario_reviews)
    non_proof_visible = package_presence["package_non_proof_statement"] and all(
        review["non_proof_visible"] for review in scenario_reviews
    )

    if not linkage_ok:
        blockers.append("identifier_linkage_broken")
    if not boundary_ok:
        blockers.append("runtime_boundary_issue")
    if not non_proof_visible:
        blockers.append("non_proof_statement_missing")

    unique_blockers = sorted(set(blockers))
    status = "reviewed_retain_limited_public_example" if not unique_blockers else "review_blocked"
    publication_limit = "limited_synthetic_non_executing_example"

    record = {
        "review_id": "publication-review-sanitized-static-mock-v0636",
        "generator_version": GENERATOR_VERSION,
        "sample_dir": str(sample_dir),
        "publication_review_status": status,
        "publication_limit": publication_limit,
        "scenario_count": len(scenario_reviews),
        "expected_scenario_count": len(EXPECTED_SCENARIOS),
        "package_artifact_presence": package_presence,
        "scenario_reviews": scenario_reviews,
        "all_example_names": all_example_names,
        "hygiene_status": hygiene_status,
        "linkage_ok": linkage_ok,
        "boundary_ok": boundary_ok,
        "non_proof_visible": non_proof_visible,
        "blocker_categories": unique_blockers,
        "runtime_boundary": RUNTIME_BOUNDARY,
        "non_authorization_statement": (
            "This publication review record is review-only. It does not authorize "
            "runtime execution, scanner execution, customer-target operation, delivery, "
            "certification, legal approval, or audit opinion."
        ),
    }

    write_json(sample_dir / "publication_review_record.example.json", record)
    write_md(sample_dir / "publication_review_record.example.md", review_markdown(record))
    return record


def review_markdown(record: dict[str, Any]) -> str:
    scenarios = "\n".join(
        f"- `{s['scenario_id']}`: linkage_ok={s['linkage_ok']}, boundary_ok={s['boundary_ok']}, non_proof_visible={s['non_proof_visible']}"
        for s in record["scenario_reviews"]
    )
    blockers = "\n".join(f"- `{b}`" for b in record["blocker_categories"]) or "- none"
    return f"""
# Publication review record

Publication review status: `{record['publication_review_status']}`  
Publication limit: `{record['publication_limit']}`  
Hygiene status: `{record['hygiene_status']}`

## Scenario review summary

{scenarios}

## Blocker categories

{blockers}

## Boundary statement

This publication review record does not authorize runtime execution, scanner
execution, customer-target operation, delivery, certification, legal approval, or
audit opinion.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate sanitized public sample publication review record.")
    parser.add_argument("--sample-dir", default=str(DEFAULT_SAMPLE_DIR), help="Sanitized public sample directory.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    record = generate_review(Path(args.sample_dir))
    print(json.dumps({
        "status": record["publication_review_status"],
        "publication_limit": record["publication_limit"],
        "scenario_count": record["scenario_count"],
        "hygiene_status": record["hygiene_status"],
        "blocker_categories": record["blocker_categories"],
        "runtime_boundary": RUNTIME_BOUNDARY,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
