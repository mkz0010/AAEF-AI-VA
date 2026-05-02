from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from lifecycle_checkpoint import (
    LifecycleCheckpointError,
    build_lifecycle_checkpoint_summary,
    format_lifecycle_checkpoint_markdown,
    validate_lifecycle_checkpoint_bundle,
    validate_lifecycle_checkpoint_summary,
)
from generate_lifecycle_checkpoint import build_demo_bundle


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_checkpoint_error(fn, message: str) -> None:
    try:
        fn()
    except LifecycleCheckpointError:
        return
    raise AssertionError(message)


def main() -> int:
    bundle = build_demo_bundle()
    validate_lifecycle_checkpoint_bundle(bundle)

    summary = build_lifecycle_checkpoint_summary(bundle)
    validate_lifecycle_checkpoint_summary(summary)

    assert_true(summary["checkpoint_status"] == "passed", "checkpoint should pass")
    assert_true(summary["current_version_target"] == "v0.1.30", "version target mismatch")
    assert_true(summary["safety_invariants"]["real_execution_permitted"] is False, "real execution must be false")
    assert_true(summary["safety_invariants"]["customer_delivery_ready"] is False, "customer delivery must be false")
    assert_true(summary["safety_invariants"]["report_ready"] is False, "report_ready must be false")
    assert_true(summary["safety_invariants"]["delivery_dispatched"] is False, "delivery dispatch must be false")
    assert_true(summary["safety_invariants"]["model_output_was_not_execution_authority"] is True, "authority invariant missing")
    assert_true("No real ZAP/Burp/Nmap/nuclei execution in v0.1.x" in summary["explicit_non_goals"], "non-goal missing")
    assert_true(any("v0.2.0" in item for item in summary["next_phase_candidates"]), "v0.2.0 next phase missing")

    forbidden = json.dumps(summary, ensure_ascii=False).lower()
    assert_true("final_report_finding" not in forbidden, "forbidden final term found")
    assert_true("final finding" not in forbidden, "forbidden final finding term found")

    markdown = format_lifecycle_checkpoint_markdown(summary)
    assert_true("# Lifecycle Integration Checkpoint" in markdown, "markdown title missing")
    assert_true("Stable Capabilities" in markdown, "capabilities section missing")
    assert_true("Explicit Non-Goals" in markdown, "non-goals section missing")
    assert_true("Safety Invariants" in markdown, "safety invariants section missing")

    bad = copy.deepcopy(bundle)
    bad["readiness_result"]["real_execution_permitted"] = True
    expect_checkpoint_error(
        lambda: build_lifecycle_checkpoint_summary(bad),
        "real_execution_permitted=true should fail checkpoint",
    )

    bad = copy.deepcopy(bundle)
    bad["delivery_package"]["customer_delivery_ready"] = True
    expect_checkpoint_error(
        lambda: build_lifecycle_checkpoint_summary(bad),
        "customer_delivery_ready=true should fail checkpoint",
    )

    bad = copy.deepcopy(bundle)
    bad["delivery_package"]["delivery_dispatched"] = True
    expect_checkpoint_error(
        lambda: build_lifecycle_checkpoint_summary(bad),
        "delivery_dispatched=true should fail checkpoint",
    )

    bad_summary = copy.deepcopy(summary)
    bad_summary["explicit_non_goals"].append("final_report_finding placeholder")
    expect_checkpoint_error(
        lambda: validate_lifecycle_checkpoint_summary(bad_summary),
        "final lifecycle term should fail checkpoint",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_lifecycle_checkpoint.py")], check=True)

    generated_json = ROOT / "private-not-in-git" / "lifecycle-checkpoints" / "demo" / "lifecycle-checkpoint.generated.json"
    generated_md = ROOT / "private-not-in-git" / "lifecycle-checkpoints" / "demo" / "lifecycle-checkpoint.generated.md"

    assert_true(generated_json.exists(), "generated lifecycle checkpoint JSON missing")
    assert_true(generated_md.exists(), "generated lifecycle checkpoint Markdown missing")

    generated = json.loads(generated_json.read_text(encoding="utf-8"))
    assert_true(generated["checkpoint_status"] == "passed", "generated checkpoint should pass")
    assert_true(generated["safety_invariants"]["customer_delivery_ready"] is False, "generated delivery readiness should be false")
    assert_true(generated["safety_invariants"]["real_execution_permitted"] is False, "generated real execution should be false")

    print("Lifecycle integration checkpoint tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
