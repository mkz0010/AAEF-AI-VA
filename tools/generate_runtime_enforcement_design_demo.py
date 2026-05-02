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
from local_execution_plan import build_local_only_execution_plan, evaluate_local_execution_plan_review_gate
from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate
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
    decision = sys.argv[1] if len(sys.argv) > 1 else "design_recorded"

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
    gate = evaluate_runtime_enforcement_design_gate(design, design_review_decision=decision)

    out_dir = ROOT / "private-not-in-git" / "runtime-enforcement-design" / "demo"
    policy_path = out_dir / "runtime-safety-policy.generated.json"
    policy_gate_path = out_dir / "runtime-safety-policy-gate-result.generated.json"
    design_path = out_dir / "runtime-enforcement-design.generated.json"
    gate_path = out_dir / "runtime-enforcement-design-gate-result.generated.json"

    write_json(policy_path, policy)
    write_json(policy_gate_path, policy_gate)
    write_json(design_path, design)
    write_json(gate_path, gate)

    print(f"runtime enforcement design:      {design_path}")
    print(f"runtime enforcement design gate: {gate_path}")
    print(f"enforcement design gate status:  {gate['runtime_enforcement_design_gate_status']}")
    print(f"runtime enforcement implemented: {gate['runtime_enforcement_implemented']}")
    print(f"real execution permitted:        {gate['real_execution_permitted']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
