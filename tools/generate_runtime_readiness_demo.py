from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from runtime_readiness import build_zap_runtime_profile, evaluate_local_runtime_readiness


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "not-detected"

    if mode == "detected":
        lookup = {"zap.bat": "C:/Program Files/ZAP/Zed Attack Proxy/zap.bat"}
    else:
        lookup = {"zap.bat": None, "zap.sh": None, "zaproxy": None, "zap": None}

    profile = build_zap_runtime_profile()
    result = evaluate_local_runtime_readiness(profile, lookup=lookup)

    out_dir = ROOT / "private-not-in-git" / "runtime-readiness" / "demo"
    profile_path = out_dir / "runtime-profile.generated.json"
    result_path = out_dir / "runtime-readiness-result.generated.json"

    write_json(profile_path, profile)
    write_json(result_path, result)

    print(f"runtime profile: {profile_path}")
    print(f"runtime readiness: {result_path}")
    print(f"runtime readiness status: {result['runtime_readiness_status']}")
    print(f"runtime detected: {result['runtime_detected']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
