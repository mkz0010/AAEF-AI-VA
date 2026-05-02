from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from preflight_check_implementation import (
    build_preflight_check_implementation_scaffold,
    evaluate_preflight_check_implementation_gate,
)
from generate_runtime_transition_checkpoint_demo import build_demo_preflight_pair
from runtime_transition_checkpoint import (
    build_runtime_transition_checkpoint,
    format_runtime_transition_checkpoint_markdown,
)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    decision = sys.argv[1] if len(sys.argv) > 1 else "implementation_scaffold_recorded"

    preflight, preflight_gate = build_demo_preflight_pair()
    checkpoint = build_runtime_transition_checkpoint(preflight, preflight_gate)
    implementation = build_preflight_check_implementation_scaffold(checkpoint)
    gate = evaluate_preflight_check_implementation_gate(implementation, implementation_review_decision=decision)

    out_dir = ROOT / "private-not-in-git" / "preflight-check-implementation" / "demo"
    checkpoint_path = out_dir / "runtime-transition-checkpoint.generated.json"
    checkpoint_md_path = out_dir / "runtime-transition-checkpoint.generated.md"
    implementation_path = out_dir / "preflight-check-implementation.generated.json"
    gate_path = out_dir / "preflight-check-implementation-gate-result.generated.json"

    write_json(checkpoint_path, checkpoint)
    write_text(checkpoint_md_path, format_runtime_transition_checkpoint_markdown(checkpoint))
    write_json(implementation_path, implementation)
    write_json(gate_path, gate)

    print(f"preflight check implementation:      {implementation_path}")
    print(f"preflight check implementation gate: {gate_path}")
    print(f"implementation gate status:          {gate['preflight_check_implementation_gate_status']}")
    print(f"concrete checks implemented:         {gate['concrete_checks_implemented']}")
    print(f"preflight satisfied:                 {gate['preflight_satisfied']}")
    print(f"execution authorized:                {gate['execution_authorized']}")
    print(f"ready for runtime execution:         {gate['ready_for_runtime_execution']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
