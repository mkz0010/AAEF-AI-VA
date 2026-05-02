"""Print v0.3.4 negative preflight evidence examples as JSON.

This is a demo generator only. It does not collect live evidence, does not
call ZAP, does not start external processes, and does not perform network
activity.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "prototypes" / "tool-gateway"))

from preflight_evidence_negative_examples import (  # noqa: E402
    build_negative_preflight_evidence_examples,
    summarize_negative_preflight_evidence_examples,
    validate_negative_preflight_evidence_examples,
)


def main() -> int:
    examples = build_negative_preflight_evidence_examples()
    errors = validate_negative_preflight_evidence_examples(examples)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    payload = {
        "artifact_type": "negative_preflight_evidence_examples_demo",
        "version": "v0.3.4",
        "live_evidence_records_generated": False,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "ready_for_runtime_execution": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "network_activity_allowed": False,
        "scan_execution_allowed": False,
        "raw_artifact_capture_permitted": False,
        "summary": summarize_negative_preflight_evidence_examples(),
        "examples": examples,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
