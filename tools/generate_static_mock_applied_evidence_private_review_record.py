from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_PACKAGE_DIR = Path("private-not-in-git/applied-evidence-runs/static-mock-demo")
DEFAULT_OUTPUT_DIR = Path("private-not-in-git/applied-evidence-review-records/static-mock-demo")
GENERATOR_VERSION = "v0.6.31-static-mock-private-review-record"

EXPECTED_SCENARIOS = [
    "permitted-safe-diagnostic",
    "denied-out-of-scope-request",
    "human-approval-required",
    "not-executed-expired",
]

RUNTIME_BOUNDARY: dict[str, bool] = {
    "private_package_review_record_generated": True,
    "promotion_gate_result_generated": True,
    "public_sample_promotion_authorized": False,
    "public_sample_generated": False,
    "public_artifact_generated": False,
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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_md(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")


def artifact_exists(path: Path) -> bool:
    return path.exists() and path.is_file()


def review_scenario(package_dir: Path, scenario_id: str) -> dict[str, Any]:
    scenario_dir = package_dir / "scenarios" / scenario_id
    expected_result = (
        "execution_result.generated.json"
        if scenario_id == "permitted-safe-diagnostic"
        else "non_execution_result.generated.json"
    )
    artifacts = {
        "tool_action_request": scenario_dir / "tool_action_request.generated.json",
        "gate_decision": scenario_dir / "gate_decision.generated.json",
        "dispatch_decision": scenario_dir / "dispatch_decision.generated.json",
        "result": scenario_dir / expected_result,
        "evidence_event": scenario_dir / "evidence_event.generated.json",
        "review_summary": scenario_dir / "review_summary.generated.md",
        "non_proof_statement": scenario_dir / "non_proof_statement.generated.md",
    }
    presence = {name: artifact_exists(path) for name, path in artifacts.items()}
    blockers: list[str] = []

    if not scenario_dir.exists():
        blockers.append("scenario_missing")
    for name, present in presence.items():
        if not present:
            blockers.append(f"artifact_missing:{name}")

    linkage_ok = False
    boundary_ok = False
    if all(presence.values()):
        request = load_json(artifacts["tool_action_request"])
        decision = load_json(artifacts["gate_decision"])
        dispatch = load_json(artifacts["dispatch_decision"])
        result = load_json(artifacts["result"])
        evidence = load_json(artifacts["evidence_event"])

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

        runtime_boundary = result.get("runtime_boundary", {})
        boundary_ok = (
            runtime_boundary.get("scan_execution_allowed") is False
            and runtime_boundary.get("customer_target") is False
            and runtime_boundary.get("delivery_authorized") is False
            and runtime_boundary.get("real_execution_permitted") is False
        )
        if not boundary_ok:
            blockers.append("runtime_or_delivery_boundary_issue")

    return {
        "scenario_id": scenario_id,
        "scenario_dir": str(scenario_dir),
        "artifact_presence": presence,
        "linkage_ok": linkage_ok,
        "runtime_delivery_boundary_ok": boundary_ok,
        "blockers": blockers,
    }


def generate_review(package_dir: Path, output_dir: Path) -> dict[str, Any]:
    blockers: list[str] = []
    if not package_dir.exists():
        blockers.append("missing_private_package")

    manifest_path = package_dir / "package_manifest.generated.json"
    summary_path = package_dir / "package_summary.generated.json"
    walkthrough_path = package_dir / "reviewer_walkthrough.generated.md"
    mapping_path = package_dir / "aaef_five_questions_mapping.generated.md"
    non_proof_path = package_dir / "non_proof_statement.generated.md"

    required_package_artifacts = {
        "package_manifest": manifest_path,
        "package_summary": summary_path,
        "reviewer_walkthrough": walkthrough_path,
        "five_questions_mapping": mapping_path,
        "non_proof_statement": non_proof_path,
    }
    package_presence = {name: artifact_exists(path) for name, path in required_package_artifacts.items()}
    for name, present in package_presence.items():
        if not present:
            blockers.append(f"missing_{name}")

    scenario_reviews = [review_scenario(package_dir, scenario_id) for scenario_id in EXPECTED_SCENARIOS]
    for scenario in scenario_reviews:
        blockers.extend(scenario["blockers"])

    scenario_count = sum(1 for scenario in scenario_reviews if not any(b.startswith("scenario_missing") for b in scenario["blockers"]))
    linkage_ok = all(scenario["linkage_ok"] for scenario in scenario_reviews)
    boundaries_ok = all(scenario["runtime_delivery_boundary_ok"] for scenario in scenario_reviews)

    if not linkage_ok:
        blockers.append("identifier_linkage_broken")
    if not boundaries_ok:
        blockers.append("runtime_boundary_issue")

    status = "reviewed_keep_private" if not blockers else "review_requires_human_attention"
    promotion_status = "keep_private"

    review_record = {
        "review_id": "private-review-static-mock-demo-v0631",
        "generator_version": GENERATOR_VERSION,
        "reviewed_package_dir": str(package_dir),
        "output_dir": str(output_dir),
        "review_status": status,
        "promotion_status": promotion_status,
        "scenario_count": scenario_count,
        "expected_scenario_count": len(EXPECTED_SCENARIOS),
        "package_artifact_presence": package_presence,
        "scenario_reviews": scenario_reviews,
        "linkage_ok": linkage_ok,
        "runtime_delivery_boundaries_ok": boundaries_ok,
        "blocker_categories": sorted(set(blockers)),
        "human_review_recommended": True,
        "runtime_boundary": RUNTIME_BOUNDARY,
        "non_authorization_statement": (
            "This private review record is review-only. It does not authorize public "
            "sample promotion, execution, scanning, customer-target operation, delivery, "
            "certification, legal approval, or audit opinion."
        ),
    }

    promotion_gate = {
        "gate_id": "promotion-gate-static-mock-demo-v0631",
        "review_id": review_record["review_id"],
        "promotion_status": promotion_status,
        "public_sample_promotion_authorized": False,
        "public_sample_generated": False,
        "delivery_authorized": False,
        "runtime_execution_authorized": False,
        "scanner_execution_authorized": False,
        "customer_target_authorized": False,
        "reason": "Private review record generated; package remains private pending later decision.",
        "blocker_categories": review_record["blocker_categories"],
        "runtime_boundary": RUNTIME_BOUNDARY,
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "private-review-record.generated.json", review_record)
    write_json(output_dir / "promotion-gate-result.generated.json", promotion_gate)
    write_md(output_dir / "private-review-record.generated.md", review_markdown(review_record))
    write_md(output_dir / "promotion-gate-result.generated.md", promotion_markdown(promotion_gate))

    return review_record


def review_markdown(record: dict[str, Any]) -> str:
    scenarios = "\n".join(
        f"- `{s['scenario_id']}`: linkage_ok={s['linkage_ok']}, boundary_ok={s['runtime_delivery_boundary_ok']}"
        for s in record["scenario_reviews"]
    )
    blockers = "\n".join(f"- `{b}`" for b in record["blocker_categories"]) or "- none"
    return f"""
# Private review record: static/mock applied evidence package

Review status: `{record['review_status']}`  
Promotion status: `{record['promotion_status']}`

Reviewed package:

~~~text
{record['reviewed_package_dir']}
~~~

## Scenario review summary

{scenarios}

## Blocker categories

{blockers}

## Boundary statement

This private review record does not authorize public sample promotion, runtime
execution, scanner execution, customer-target operation, delivery, certification,
legal approval, or audit opinion.
"""


def promotion_markdown(gate: dict[str, Any]) -> str:
    return f"""
# Promotion gate result

Promotion status: `{gate['promotion_status']}`

Public sample promotion authorized: `{str(gate['public_sample_promotion_authorized']).lower()}`  
Delivery authorized: `{str(gate['delivery_authorized']).lower()}`  
Runtime execution authorized: `{str(gate['runtime_execution_authorized']).lower()}`  
Scanner execution authorized: `{str(gate['scanner_execution_authorized']).lower()}`  
Customer target authorized: `{str(gate['customer_target_authorized']).lower()}`

Reason:

{gate['reason']}
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a private review record for a static/mock applied evidence package.")
    parser.add_argument("--package-dir", default=str(DEFAULT_PACKAGE_DIR), help="Private static/mock package directory.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Private review output directory.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    record = generate_review(Path(args.package_dir), Path(args.output_dir))
    print(json.dumps({
        "status": record["review_status"],
        "promotion_status": record["promotion_status"],
        "output_dir": record["output_dir"],
        "scenario_count": record["scenario_count"],
        "blocker_categories": record["blocker_categories"],
        "runtime_boundary": RUNTIME_BOUNDARY,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
