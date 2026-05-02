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

from local_target_lab import (
    LocalTargetLabError,
    build_local_target_lab_profile,
    evaluate_local_target_lab_gate,
    validate_local_target_lab_gate_result,
    validate_local_target_lab_profile,
)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_lab_error(fn, message: str) -> None:
    try:
        fn()
    except LocalTargetLabError:
        return
    raise AssertionError(message)


def main() -> int:
    localhost_profile = build_local_target_lab_profile()
    validate_local_target_lab_profile(localhost_profile)
    localhost_gate = evaluate_local_target_lab_gate(localhost_profile)

    assert_true(localhost_gate["target_lab_gate_status"] == "target_defined_execution_blocked", "localhost gate status mismatch")
    assert_true(localhost_gate["target_allowed_for_future_runtime_transition"] is True, "local target should be allowed for future transition")
    assert_true(localhost_gate["customer_target"] is False, "customer target must be false")
    assert_true(localhost_gate["external_network_target"] is False, "external network must be false")
    assert_true(localhost_gate["scan_execution_allowed"] is False, "scan execution must remain false")
    assert_true(localhost_gate["network_activity_allowed"] is False, "network activity must remain false")
    assert_true(localhost_gate["credential_injection_allowed"] is False, "credential injection must remain false")
    validate_local_target_lab_gate_result(localhost_gate)

    docker_profile = build_local_target_lab_profile(
        target_mode="docker_internal_only",
        target_url="http://juice-shop:3000",
        target_id="local-docker-juice-shop-001",
    )
    docker_gate = evaluate_local_target_lab_gate(docker_profile)
    assert_true(docker_gate["target_mode"] == "docker_internal_only", "docker target mode mismatch")
    assert_true(docker_gate["scan_execution_allowed"] is False, "docker scan execution must remain false")
    validate_local_target_lab_gate_result(docker_gate)

    lab_profile = build_local_target_lab_profile(
        target_mode="intentionally_vulnerable_lab_only",
        target_url="http://target.local:8080",
        target_id="local-vulnapp-001",
    )
    lab_gate = evaluate_local_target_lab_gate(lab_profile)
    assert_true(lab_gate["target_mode"] == "intentionally_vulnerable_lab_only", "lab target mode mismatch")

    bad = copy.deepcopy(localhost_profile)
    bad["target_url"] = "https://example.com"
    expect_lab_error(lambda: validate_local_target_lab_profile(bad), "external hostname should fail localhost mode")

    bad = copy.deepcopy(localhost_profile)
    bad["customer_target"] = True
    expect_lab_error(lambda: validate_local_target_lab_profile(bad), "customer target true should fail closed")

    bad = copy.deepcopy(localhost_profile)
    bad["external_network_target"] = True
    expect_lab_error(lambda: validate_local_target_lab_profile(bad), "external network target true should fail closed")

    bad = copy.deepcopy(localhost_profile)
    bad["scan_execution_allowed"] = True
    expect_lab_error(lambda: validate_local_target_lab_profile(bad), "scan execution allowed should fail closed")

    bad = copy.deepcopy(localhost_profile)
    bad["network_activity_allowed"] = True
    expect_lab_error(lambda: validate_local_target_lab_profile(bad), "network activity allowed should fail closed")

    bad = copy.deepcopy(localhost_profile)
    bad["credential_injection_allowed"] = True
    expect_lab_error(lambda: validate_local_target_lab_profile(bad), "credential injection allowed should fail closed")

    bad = copy.deepcopy(docker_profile)
    bad["target_url"] = "http://example.com"
    expect_lab_error(lambda: validate_local_target_lab_profile(bad), "external docker host should fail closed")

    bad_gate = copy.deepcopy(localhost_gate)
    bad_gate["network_activity_allowed"] = True
    expect_lab_error(lambda: validate_local_target_lab_gate_result(bad_gate), "gate network activity true should fail closed")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_local_target_lab_profile_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "local-target-lab" / "demo" / "local-target-lab-gate-result.generated.json"
    assert_true(generated.exists(), "generated local target lab gate result missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["scan_execution_allowed"] is False, "generated target gate must block scan execution")
    assert_true(data["network_activity_allowed"] is False, "generated target gate must block network activity")

    print("Local target lab profile tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
