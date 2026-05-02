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

from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate
from runtime_destination_binding import (
    RuntimeDestinationBindingError,
    build_scope_registry_runtime_destination_binding,
    evaluate_runtime_destination_binding_gate,
    validate_runtime_destination_binding_gate_result,
    validate_scope_registry_runtime_destination_binding,
)
from runtime_readiness import build_zap_runtime_profile, evaluate_local_runtime_readiness


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_binding_error(fn, message: str) -> None:
    try:
        fn()
    except RuntimeDestinationBindingError:
        return
    raise AssertionError(message)


def build_demo_binding(runtime_detected: bool = False):
    runtime_profile = build_zap_runtime_profile()
    if runtime_detected:
        lookup = {"zap.bat": "C:/Program Files/ZAP/Zed Attack Proxy/zap.bat"}
    else:
        lookup = {"zap.sh": None, "zap.bat": None, "zaproxy": None, "zap": None}
    runtime_readiness = evaluate_local_runtime_readiness(runtime_profile, lookup=lookup)
    lab_profile = build_local_target_lab_profile()
    lab_gate = evaluate_local_target_lab_gate(lab_profile)
    binding = build_scope_registry_runtime_destination_binding(
        runtime_profile,
        runtime_readiness,
        lab_profile,
        lab_gate,
    )
    return runtime_profile, runtime_readiness, lab_profile, lab_gate, binding


def main() -> int:
    runtime_profile, runtime_readiness, lab_profile, lab_gate, binding = build_demo_binding(runtime_detected=False)
    validate_scope_registry_runtime_destination_binding(binding)

    assert_true(binding["binding_status"] == "bound_execution_blocked", "binding status mismatch")
    assert_true(binding["bounded_execution_transition_candidate_allowed"] is True, "binding should allow future transition candidate")
    assert_true(binding["scan_execution_allowed"] is False, "scan execution must remain false")
    assert_true(binding["network_activity_allowed"] is False, "network activity must remain false")
    assert_true(binding["real_execution_permitted"] is False, "real execution must remain false")
    assert_true(binding["credential_injection_permitted"] is False, "credential injection must remain false")
    assert_true(binding["raw_artifact_capture_permitted"] is False, "raw artifact capture must remain false")
    assert_true(binding["customer_target"] is False, "customer target must remain false")
    assert_true(binding["external_network_target"] is False, "external network target must remain false")
    assert_true("runtime_binary_not_detected" in binding["blockers"], "runtime not detected blocker should exist")

    gate = evaluate_runtime_destination_binding_gate(binding)
    assert_true(gate["runtime_destination_binding_gate_status"] == "bound_execution_blocked", "gate status mismatch")
    assert_true(gate["bounded_execution_transition_candidate_allowed"] is True, "gate should allow future transition candidate")
    assert_true(gate["scan_execution_allowed"] is False, "gate scan execution must be false")
    assert_true(gate["network_activity_allowed"] is False, "gate network activity must be false")
    validate_runtime_destination_binding_gate_result(gate)

    _, _, _, _, detected_binding = build_demo_binding(runtime_detected=True)
    assert_true(detected_binding["runtime_detected"] is True, "detected binding should record runtime_detected true")
    assert_true("runtime_binary_not_detected" not in detected_binding["blockers"], "detected binding should not include not detected blocker")
    assert_true(detected_binding["real_execution_permitted"] is False, "detected binding still must not permit execution")

    bad_binding = copy.deepcopy(binding)
    bad_binding["scan_execution_allowed"] = True
    expect_binding_error(
        lambda: validate_scope_registry_runtime_destination_binding(bad_binding),
        "scan_execution_allowed true should fail closed",
    )

    bad_binding = copy.deepcopy(binding)
    bad_binding["network_activity_allowed"] = True
    expect_binding_error(
        lambda: validate_scope_registry_runtime_destination_binding(bad_binding),
        "network_activity_allowed true should fail closed",
    )

    bad_binding = copy.deepcopy(binding)
    bad_binding["real_execution_permitted"] = True
    expect_binding_error(
        lambda: validate_scope_registry_runtime_destination_binding(bad_binding),
        "real_execution_permitted true should fail closed",
    )

    bad_binding = copy.deepcopy(binding)
    bad_binding["customer_target"] = True
    expect_binding_error(
        lambda: validate_scope_registry_runtime_destination_binding(bad_binding),
        "customer_target true should fail closed",
    )

    bad_gate = copy.deepcopy(gate)
    bad_gate["external_network_target"] = True
    expect_binding_error(
        lambda: validate_runtime_destination_binding_gate_result(bad_gate),
        "external_network_target true should fail closed",
    )

    bad_runtime = copy.deepcopy(runtime_readiness)
    bad_runtime["runtime_profile_id"] = "other-runtime"
    expect_binding_error(
        lambda: build_scope_registry_runtime_destination_binding(runtime_profile, bad_runtime, lab_profile, lab_gate),
        "runtime profile/readiness mismatch should fail closed",
    )

    bad_lab_gate = copy.deepcopy(lab_gate)
    bad_lab_gate["lab_profile_id"] = "other-lab"
    expect_binding_error(
        lambda: build_scope_registry_runtime_destination_binding(runtime_profile, runtime_readiness, lab_profile, bad_lab_gate),
        "lab profile/gate mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_runtime_destination_binding_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "runtime-destination-bindings" / "demo" / "runtime-destination-binding-gate-result.generated.json"
    assert_true(generated.exists(), "generated runtime destination binding gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["scan_execution_allowed"] is False, "generated gate must block scan execution")
    assert_true(data["network_activity_allowed"] is False, "generated gate must block network activity")
    assert_true(data["real_execution_permitted"] is False, "generated gate must block real execution")

    print("Runtime destination binding tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
