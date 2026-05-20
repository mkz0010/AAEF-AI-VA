from __future__ import annotations

import argparse
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from gateway import run_mock_tool_gateway
from models import load_json, write_json
from policy import load_default_vault_metadata


EXAMPLE_DIR = THIS_DIR / "examples"

SCENARIOS = {
    "allowed-action": {
        "request": EXAMPLE_DIR / "allowed-action.tool-action-request.json",
        "decision": EXAMPLE_DIR / "allowed-action.authorization-decision.json",
    },
    "denied-action": {
        "request": EXAMPLE_DIR / "denied-action.tool-action-request.json",
        "decision": EXAMPLE_DIR / "denied-action.authorization-decision.json",
    },
    "human-approval-required": {
        "request": EXAMPLE_DIR / "human-approval-required.tool-action-request.json",
        "decision": EXAMPLE_DIR / "human-approval-required.authorization-decision.json",
    },
}


def run_scenario(scenario: str, out_dir: Path) -> tuple[Path, Path]:
    if scenario not in SCENARIOS:
        raise SystemExit(f"Unknown scenario: {scenario}. Choose one of: {', '.join(SCENARIOS)}")

    request = load_json(SCENARIOS[scenario]["request"])
    decision = load_json(SCENARIOS[scenario]["decision"])
    vault_metadata = load_default_vault_metadata()

    result, evidence = run_mock_tool_gateway(request, decision, vault_metadata=vault_metadata)

    scenario_dir = out_dir / scenario
    result_path = scenario_dir / "tool-execution-result.generated.json"
    evidence_path = scenario_dir / "evidence-record.generated.json"

    write_json(result_path, result)
    write_json(evidence_path, evidence)

    return result_path, evidence_path


def _mock_dry_run_raw_status(result):
    if isinstance(result, dict):
        return result.get("status") or result.get("execution_status") or result.get("raw_execution_status")
    return None


def _reviewer_status_for_mock_dry_run(scenario, result):
    raw_status = _mock_dry_run_raw_status(result)
    if raw_status == "completed":
        return "mock_dry_run_completed_no_real_execution"
    if raw_status in {"blocked", "requires_human_approval"}:
        return raw_status
    return str(raw_status)


def _format_mock_dry_run_status_line(scenario, result):
    raw_status = _mock_dry_run_raw_status(result)
    reviewer_status = _reviewer_status_for_mock_dry_run(scenario, result)
    if raw_status == "completed" and reviewer_status == "mock_dry_run_completed_no_real_execution":
        return (
            f"{scenario}: raw_execution_status={raw_status}; "
            f"reviewer_status={reviewer_status}; "
            "external_process_executed=false; "
            "network_activity_performed=false"
        )
    return f"{scenario}: {reviewer_status}"

def main() -> int:
    parser = argparse.ArgumentParser(description="Run MVP Tool Gateway mock scenarios.")
    parser.add_argument(
        "scenario",
        choices=sorted(SCENARIOS.keys()) + ["all"],
        help="Scenario to run.",
    )
    parser.add_argument(
        "--out-dir",
        default="private-not-in-git/prototype-runs",
        help="Directory for generated outputs. Defaults to ignored local private area.",
    )

    args = parser.parse_args()
    out_dir = Path(args.out_dir)

    scenarios = sorted(SCENARIOS.keys()) if args.scenario == "all" else [args.scenario]

    for scenario in scenarios:
        result_path, evidence_path = run_scenario(scenario, out_dir)
        result = load_json(result_path)
        print(_format_mock_dry_run_status_line(scenario, result))
        print(f"  result:   {result_path}")
        print(f"  evidence: {evidence_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
