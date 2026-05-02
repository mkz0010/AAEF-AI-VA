from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from preflight_evidence_examples import (
    build_preflight_evidence_example_set,
    evaluate_preflight_evidence_example_gate,
)
from preflight_evidence_record import (
    build_preflight_evidence_record_model,
    evaluate_preflight_evidence_record_model_gate,
)
from preflight_check_implementation import (
    build_preflight_check_implementation_scaffold,
    evaluate_preflight_check_implementation_gate,
)
from generate_runtime_transition_checkpoint_demo import build_demo_preflight_pair
from runtime_transition_checkpoint import build_runtime_transition_checkpoint


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    decision = sys.argv[1] if len(sys.argv) > 1 else "examples_recorded"

    preflight, preflight_gate = build_demo_preflight_pair()
    checkpoint = build_runtime_transition_checkpoint(preflight, preflight_gate)
    implementation = build_preflight_check_implementation_scaffold(checkpoint)
    implementation_gate = evaluate_preflight_check_implementation_gate(implementation)
    model = build_preflight_evidence_record_model(implementation, implementation_gate)
    model_gate = evaluate_preflight_evidence_record_model_gate(model)
    example_set = build_preflight_evidence_example_set(model, model_gate)
    gate = evaluate_preflight_evidence_example_gate(example_set, example_review_decision=decision)

    out_dir = ROOT / "private-not-in-git" / "preflight-evidence-examples" / "demo"
    model_path = out_dir / "preflight-evidence-record-model.generated.json"
    model_gate_path = out_dir / "preflight-evidence-record-model-gate-result.generated.json"
    example_set_path = out_dir / "preflight-evidence-example-set.generated.json"
    gate_path = out_dir / "preflight-evidence-example-gate-result.generated.json"

    write_json(model_path, model)
    write_json(model_gate_path, model_gate)
    write_json(example_set_path, example_set)
    write_json(gate_path, gate)

    print(f"preflight evidence example set:  {example_set_path}")
    print(f"preflight evidence example gate: {gate_path}")
    print(f"example gate status:             {gate['preflight_evidence_example_gate_status']}")
    print(f"example records generated:       {gate['example_records_generated']}")
    print(f"live evidence records generated: {gate['live_evidence_records_generated']}")
    print(f"preflight satisfied:             {gate['preflight_satisfied']}")
    print(f"execution authorized:            {gate['execution_authorized']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
