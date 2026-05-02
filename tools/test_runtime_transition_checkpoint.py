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

from runtime_transition_checkpoint import (
    RuntimeTransitionCheckpointError,
    build_runtime_transition_checkpoint,
    format_runtime_transition_checkpoint_markdown,
    validate_runtime_transition_checkpoint,
)
from generate_runtime_transition_checkpoint_demo import build_demo_preflight_pair


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_checkpoint_error(fn, message: str) -> None:
    try:
        fn()
    except RuntimeTransitionCheckpointError:
        return
    raise AssertionError(message)


def main() -> int:
    preflight, preflight_gate = build_demo_preflight_pair()
    checkpoint = build_runtime_transition_checkpoint(preflight, preflight_gate)
    validate_runtime_transition_checkpoint(checkpoint)

    assert_true(checkpoint["checkpoint_status"] == "passed_execution_blocked", "checkpoint status mismatch")
    assert_true(checkpoint["current_version_target"] == "v0.2.9", "version target mismatch")
    assert_true(len(checkpoint["transition_layers"]) == 9, "transition layer count mismatch")
    assert_true(checkpoint["readiness_summary"]["ready_for_preflight_implementation"] is True, "should be ready for preflight implementation")
    assert_true(checkpoint["readiness_summary"]["ready_for_runtime_execution"] is False, "must not be ready for runtime execution")
    assert_true(checkpoint["readiness_summary"]["ready_for_customer_target"] is False, "must not be ready for customer target")
    assert_true(checkpoint["readiness_summary"]["ready_for_external_network"] is False, "must not be ready for external network")
    assert_true(checkpoint["safety_invariants"]["preflight_satisfied"] is False, "preflight must not be satisfied")
    assert_true(checkpoint["safety_invariants"]["execution_authorized"] is False, "execution must not be authorized")
    assert_true(checkpoint["safety_invariants"]["real_execution_permitted"] is False, "real execution must be false")
    assert_true(checkpoint["safety_invariants"]["external_process_execution_allowed"] is False, "external process execution must be false")
    assert_true(checkpoint["safety_invariants"]["network_activity_allowed"] is False, "network activity must be false")
    assert_true(all(item["execution_authority"] is False for item in checkpoint["transition_layers"]), "all layers must lack execution authority")

    markdown = format_runtime_transition_checkpoint_markdown(checkpoint)
    assert_true("# Runtime Transition Checkpoint" in markdown, "checkpoint markdown title missing")
    assert_true("Safety Invariants" in markdown, "safety invariants section missing")
    assert_true("Required Preflight Checks" in markdown, "preflight section missing")

    bad = copy.deepcopy(checkpoint)
    bad["safety_invariants"]["execution_authorized"] = True
    expect_checkpoint_error(lambda: validate_runtime_transition_checkpoint(bad), "execution_authorized true should fail closed")

    bad = copy.deepcopy(checkpoint)
    bad["safety_invariants"]["preflight_satisfied"] = True
    expect_checkpoint_error(lambda: validate_runtime_transition_checkpoint(bad), "preflight_satisfied true should fail closed")

    bad = copy.deepcopy(checkpoint)
    bad["readiness_summary"]["ready_for_runtime_execution"] = True
    expect_checkpoint_error(lambda: validate_runtime_transition_checkpoint(bad), "ready_for_runtime_execution true should fail closed")

    bad = copy.deepcopy(checkpoint)
    bad["transition_layers"][0]["execution_authority"] = True
    expect_checkpoint_error(lambda: validate_runtime_transition_checkpoint(bad), "transition layer execution authority true should fail closed")

    bad = copy.deepcopy(checkpoint)
    bad["required_preflight_checks"] = []
    expect_checkpoint_error(lambda: validate_runtime_transition_checkpoint(bad), "missing preflight checks should fail closed")

    bad_gate = copy.deepcopy(preflight_gate)
    bad_gate["scope_id"] = "other-scope"
    expect_checkpoint_error(
        lambda: build_runtime_transition_checkpoint(preflight, bad_gate),
        "preflight/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_runtime_transition_checkpoint_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "runtime-transition-checkpoint" / "demo" / "runtime-transition-checkpoint.generated.json"
    generated_md = ROOT / "private-not-in-git" / "runtime-transition-checkpoint" / "demo" / "runtime-transition-checkpoint.generated.md"
    assert_true(generated.exists(), "generated runtime transition checkpoint missing")
    assert_true(generated_md.exists(), "generated runtime transition checkpoint markdown missing")

    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["checkpoint_status"] == "passed_execution_blocked", "generated checkpoint should pass")
    assert_true(data["readiness_summary"]["ready_for_runtime_execution"] is False, "generated checkpoint must not be runtime-ready")
    assert_true(data["safety_invariants"]["execution_authorized"] is False, "generated checkpoint must not authorize execution")

    print("Runtime transition checkpoint tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
