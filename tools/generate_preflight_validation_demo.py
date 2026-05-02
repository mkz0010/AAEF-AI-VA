from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from bounded_execution_transition import (
    build_bounded_execution_transition_candidate,
    evaluate_bounded_execution_transition_gate,
)
from execution_authorization import build_execution_authorization_scaffold, evaluate_execution_authorization_gate
from local_execution_plan import build_local_only_execution_plan, evaluate_local_execution_plan_review_gate
from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate
from preflight_validation import build_preflight_validation_scaffold, evaluate_preflight_validation_gate
from runtime_destination_binding import (
    build_scope_registry_runtime_destination_binding,
    evaluate_runtime_destination_binding_gate,
)
from runtime_enforcement_design import build_runtime_enforcement_design, evaluate_runtime_enforcement_design_gate
from runtime_readiness import build_zap_runtime_profile, evaluate_local_runtime_readiness
from runtime_safety_policy import build_runtime_safety_policy, evaluate_runtime_safety_policy_gate


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    decision = sys.argv[1] if len(sys.argv) > 1 else "preflight_scaffold_recorded"

    runtime_profile = build_zap_runtime_profile()
    runtime_readiness = evaluate_local_runtime_readiness(
        runtime_profile,
        lookup={"zap.sh": None, "zap.bat": None, "zaproxy": None, "zap": None},
    )
    lab_profile = build_local_target_lab_profile()
    lab_gate = evaluate_local_target_lab_gate(lab_profile)
    binding = build_scope_registry_runtime_destination_binding(
        runtime_profile,
        runtime_readiness,
        lab_profile,
        lab_gate,
    )
    binding_gate = evaluate_runtime_destination_binding_gate(binding)
    transition_candidate = build_bounded_execution_transition_candidate(binding, binding_gate)
    transition_gate = evaluate_bounded_execution_transition_gate(transition_candidate)
    plan = build_local_only_execution_plan(transition_candidate, transition_gate)
    plan_gate = evaluate_local_execution_plan_review_gate(plan)
    policy = build_runtime_safety_policy(plan, plan_gate)
    policy_gate = evaluate_runtime_safety_policy_gate(policy)
    design = build_runtime_enforcement_design(policy, policy_gate)
    design_gate = evaluate_runtime_enforcement_design_gate(design)
    authorization = build_execution_authorization_scaffold(design, design_gate)
    authorization_gate = evaluate_execution_authorization_gate(authorization)

    preflight = build_preflight_validation_scaffold(authorization, authorization_gate)
    gate = evaluate_preflight_validation_gate(preflight, preflight_review_decision=decision)

    out_dir = ROOT / "private-not-in-git" / "preflight-validation" / "demo"
    authorization_path = out_dir / "execution-authorization.generated.json"
    authorization_gate_path = out_dir / "execution-authorization-gate-result.generated.json"
    preflight_path = out_dir / "preflight-validation.generated.json"
    gate_path = out_dir / "preflight-validation-gate-result.generated.json"

    write_json(authorization_path, authorization)
    write_json(authorization_gate_path, authorization_gate)
    write_json(preflight_path, preflight)
    write_json(gate_path, gate)

    print(f"preflight validation:      {preflight_path}")
    print(f"preflight validation gate: {gate_path}")
    print(f"preflight gate status:     {gate['preflight_validation_gate_status']}")
    print(f"preflight satisfied:       {gate['preflight_satisfied']}")
    print(f"execution authorized:      {gate['execution_authorized']}")
    print(f"real execution permitted:  {gate['real_execution_permitted']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
