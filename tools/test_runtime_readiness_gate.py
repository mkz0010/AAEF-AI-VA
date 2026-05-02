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

from runtime_readiness import (
    RuntimeReadinessError,
    build_zap_runtime_profile,
    evaluate_local_runtime_readiness,
    validate_runtime_profile,
    validate_runtime_readiness_result,
)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_runtime_error(fn, message: str) -> None:
    try:
        fn()
    except RuntimeReadinessError:
        return
    raise AssertionError(message)


def main() -> int:
    profile = build_zap_runtime_profile()
    validate_runtime_profile(profile)

    not_detected = evaluate_local_runtime_readiness(
        profile,
        lookup={"zap.sh": None, "zap.bat": None, "zaproxy": None, "zap": None},
    )
    assert_true(not_detected["runtime_detected"] is False, "runtime should not be detected")
    assert_true(not_detected["runtime_readiness_status"] == "not_detected_execution_blocked", "not detected status mismatch")
    assert_true("runtime_binary_not_detected" in not_detected["blockers"], "runtime not detected blocker missing")
    assert_true(not_detected["real_execution_permitted"] is False, "real execution must remain false")
    assert_true(not_detected["external_process_executed"] is False, "external process must not be executed")
    assert_true(not_detected["network_activity_performed"] is False, "network activity must not be performed")
    validate_runtime_readiness_result(not_detected)

    detected = evaluate_local_runtime_readiness(
        profile,
        lookup={"zap.bat": "C:/Program Files/ZAP/Zed Attack Proxy/zap.bat"},
    )
    assert_true(detected["runtime_detected"] is True, "runtime should be detected")
    assert_true(detected["detected_binary_path"], "detected path should be populated")
    assert_true(detected["runtime_readiness_status"] == "detected_but_execution_blocked", "detected status mismatch")
    assert_true("runtime_binary_not_detected" not in detected["blockers"], "runtime not detected blocker should be absent")
    assert_true(detected["real_execution_permitted"] is False, "detected runtime must still not permit execution")
    assert_true(detected["credential_injection_permitted"] is False, "credential injection must remain false")
    assert_true(detected["raw_artifact_capture_permitted"] is False, "raw artifact capture must remain false")
    validate_runtime_readiness_result(detected)

    bad_profile = copy.deepcopy(profile)
    bad_profile["real_execution_allowed"] = True
    expect_runtime_error(lambda: validate_runtime_profile(bad_profile), "real_execution_allowed true should fail closed")

    bad_profile = copy.deepcopy(profile)
    bad_profile["network_activity_allowed"] = True
    expect_runtime_error(lambda: validate_runtime_profile(bad_profile), "network_activity_allowed true should fail closed")

    bad_profile = copy.deepcopy(profile)
    bad_profile["allowed_target_modes"] = ["customer_network"]
    expect_runtime_error(lambda: validate_runtime_profile(bad_profile), "unsupported target mode should fail closed")

    bad_result = copy.deepcopy(detected)
    bad_result["external_process_executed"] = True
    expect_runtime_error(lambda: validate_runtime_readiness_result(bad_result), "external_process_executed true should fail closed")

    bad_result = copy.deepcopy(detected)
    bad_result["network_activity_performed"] = True
    expect_runtime_error(lambda: validate_runtime_readiness_result(bad_result), "network_activity_performed true should fail closed")

    bad_result = copy.deepcopy(detected)
    bad_result["real_execution_permitted"] = True
    expect_runtime_error(lambda: validate_runtime_readiness_result(bad_result), "real_execution_permitted true should fail closed")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_runtime_readiness_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "runtime-readiness" / "demo" / "runtime-readiness-result.generated.json"
    assert_true(generated.exists(), "generated runtime readiness result missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["real_execution_permitted"] is False, "generated readiness must block execution")
    assert_true(data["external_process_executed"] is False, "generated readiness must not execute process")

    print("Runtime readiness gate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
