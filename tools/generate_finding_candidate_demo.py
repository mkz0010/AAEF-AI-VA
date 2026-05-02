from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from finding_candidate import build_finding_candidate_from_sanitized_artifact
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
        "finding_observation": "Potential issue was observed in sanitized demo artifact. password=hunter2",
    }

    out_dir = ROOT / "private-not-in-git" / "finding-candidates" / "demo"
    raw_path = out_dir / "raw-artifact.demo.json"
    sanitized_path = out_dir / "sanitized-artifact.generated.json"
    candidate_path = out_dir / "finding-candidate.generated.json"

    write_json(raw_path, raw)
    sanitized = sanitize_raw_artifact(
        raw,
        raw_artifact_ref="private-not-in-git/finding-candidates/demo/raw-artifact.demo.json",
        sanitized_artifact_ref="private-not-in-git/finding-candidates/demo/sanitized-artifact.generated.json",
    )
    write_json(sanitized_path, sanitized)

    candidate = build_finding_candidate_from_sanitized_artifact(
        sanitized,
        tool="zap",
        operation="authenticated_crawl",
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        evidence_id="evidence-demo-001",
    )
    write_json(candidate_path, candidate)

    print(f"raw artifact:       {raw_path}")
    print(f"sanitized artifact: {sanitized_path}")
    print(f"finding candidate:  {candidate_path}")
    print(f"candidate status:   {candidate['finding_candidate_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
