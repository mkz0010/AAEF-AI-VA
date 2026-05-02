from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from sanitizer import sanitize_raw_artifact


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    raw = {
        "adapter": "zap",
        "mock_raw_output": True,
        "request": "GET /account HTTP/1.1\nHost: demo.local\nAuthorization: Bearer abcdefghijklmnopqrstuvwxyz\nCookie: sessionid=abc123456789; theme=dark\n",
        "response": "HTTP/1.1 200 OK\nSet-Cookie: sessionid=def987654321; HttpOnly\n\ncsrf_token=tok_1234567890abcdef internal_ip=192.168.10.5",
        "finding_observation": "Demo observation from raw adapter artifact. password=hunter2",
    }

    out_dir = ROOT / "private-not-in-git" / "sanitized-artifacts" / "demo"
    raw_path = out_dir / "raw-artifact.demo.json"
    sanitized_path = out_dir / "sanitized-artifact.generated.json"

    write_json(raw_path, raw)
    sanitized = sanitize_raw_artifact(
        raw,
        raw_artifact_ref="private-not-in-git/sanitized-artifacts/demo/raw-artifact.demo.json",
        sanitized_artifact_ref="private-not-in-git/sanitized-artifacts/demo/sanitized-artifact.generated.json",
    )
    write_json(sanitized_path, sanitized)

    print(f"raw artifact:       {raw_path}")
    print(f"sanitized artifact: {sanitized_path}")
    print(f"redaction count:    {sanitized['redaction_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
