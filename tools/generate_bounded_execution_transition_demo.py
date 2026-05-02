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
from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate
from runtime_destination_binding import (
    build_scope_registry_runtime_destination_binding,
    evaluate_runtime_destination_binding_gate,
)
from runtime_readiness import build_zap_runtime_profile, evaluate_local_runtime_readiness


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "candidate_recorded"

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

    candidate = build_bounded_execution_transition_candidate(binding, binding_gate)
    gate = evaluate_bounded_execution_transition_gate(candidate, transition_review_decision=mode)

    out_dir = ROOT / "private-not-in-git" / "bounded-execution-transition" / "demo"
    binding_path = out_dir / "runtime-destination-binding.generated.json"
    binding_gate_path = out_dir / "runtime-destination-binding-gate-result.generated.json"
    candidate_path = out_dir / "bounded-execution-transition-candidate.generated.json"
    gate_path = out_dir / "bounded-execution-transition-gate-result.generated.json"

    write_json(binding_path, binding)
    write_json(binding_gate_path, binding_gate)
    write_json(candidate_path, candidate)
    write_json(gate_path, gate)

    print(f"bounded execution transition candidate: {candidate_path}")
    print(f"bounded execution transition gate:      {gate_path}")
    print(f"transition gate status:                 {gate['bounded_execution_transition_gate_status']}")
    print(f"real execution permitted:               {gate['real_execution_permitted']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
