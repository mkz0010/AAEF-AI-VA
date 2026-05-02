from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "localhost"

    if mode == "docker":
        profile = build_local_target_lab_profile(
            target_mode="docker_internal_only",
            target_id="local-docker-juice-shop-001",
            target_url="http://juice-shop:3000",
            target_label="Docker internal OWASP Juice Shop lab target",
        )
    else:
        profile = build_local_target_lab_profile()

    result = evaluate_local_target_lab_gate(profile)

    out_dir = ROOT / "private-not-in-git" / "local-target-lab" / "demo"
    profile_path = out_dir / "local-target-lab-profile.generated.json"
    result_path = out_dir / "local-target-lab-gate-result.generated.json"

    write_json(profile_path, profile)
    write_json(result_path, result)

    print(f"local target lab profile: {profile_path}")
    print(f"local target lab gate:    {result_path}")
    print(f"target lab gate status:   {result['target_lab_gate_status']}")
    print(f"target mode:              {result['target_mode']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
