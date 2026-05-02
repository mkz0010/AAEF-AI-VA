from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

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
    mode = sys.argv[1] if len(sys.argv) > 1 else "localhost"

    runtime_profile = build_zap_runtime_profile()
    runtime_readiness = evaluate_local_runtime_readiness(
        runtime_profile,
        lookup={"zap.sh": None, "zap.bat": None, "zaproxy": None, "zap": None},
    )

    if mode == "docker":
        lab_profile = build_local_target_lab_profile(
            target_mode="docker_internal_only",
            target_id="local-docker-juice-shop-001",
            target_url="http://juice-shop:3000",
            target_label="Docker internal OWASP Juice Shop lab target",
        )
    else:
        lab_profile = build_local_target_lab_profile()

    lab_gate = evaluate_local_target_lab_gate(lab_profile)

    binding = build_scope_registry_runtime_destination_binding(
        runtime_profile,
        runtime_readiness,
        lab_profile,
        lab_gate,
    )
    gate = evaluate_runtime_destination_binding_gate(binding)

    out_dir = ROOT / "private-not-in-git" / "runtime-destination-bindings" / "demo"
    runtime_profile_path = out_dir / "runtime-profile.generated.json"
    runtime_readiness_path = out_dir / "runtime-readiness-result.generated.json"
    lab_profile_path = out_dir / "local-target-lab-profile.generated.json"
    lab_gate_path = out_dir / "local-target-lab-gate-result.generated.json"
    binding_path = out_dir / "runtime-destination-binding.generated.json"
    gate_path = out_dir / "runtime-destination-binding-gate-result.generated.json"

    write_json(runtime_profile_path, runtime_profile)
    write_json(runtime_readiness_path, runtime_readiness)
    write_json(lab_profile_path, lab_profile)
    write_json(lab_gate_path, lab_gate)
    write_json(binding_path, binding)
    write_json(gate_path, gate)

    print(f"runtime destination binding: {binding_path}")
    print(f"runtime destination gate:    {gate_path}")
    print(f"binding gate status:         {gate['runtime_destination_binding_gate_status']}")
    print(f"target mode:                 {gate['target_mode']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
