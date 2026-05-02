from __future__ import annotations

import subprocess
import sys


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> int:
    run([sys.executable, "-m", "compileall", "-q", "prototypes", "tools"])
    run([sys.executable, "tools/validate_mvp_schemas.py"])
    run([sys.executable, "tools/validate_mvp_examples.py"])
    run([sys.executable, "tools/test_scope_registry.py"])
    run([sys.executable, "tools/run_tool_gateway_example.py", "all"])
    run([sys.executable, "tools/validate_generated_outputs.py"])
    run([sys.executable, "tools/test_tool_gateway_runner.py"])
    run([sys.executable, "tools/test_tool_gateway_adapters.py"])
    run([sys.executable, "tools/test_controlled_executor_policy.py"])
    run([sys.executable, "tools/test_real_execution_readiness_gate.py"])
    run([sys.executable, "tools/test_operator_readiness_review.py"])
    run([sys.executable, "tools/test_human_approval_gate.py"])
    run([sys.executable, "tools/test_evidence_chain_linkage.py"])
    run([sys.executable, "tools/test_evidence_reconstruction_report.py"])
    run([sys.executable, "tools/test_sanitizer_redaction_policy.py"])
    run([sys.executable, "tools/test_finding_candidate_model.py"])
    run([sys.executable, "tools/test_finding_review_gate.py"])
    run([sys.executable, "tools/test_report_finding_promotion_gate.py"])
    run([sys.executable, "tools/test_report_review_gate.py"])
    run([sys.executable, "tools/test_report_packet_review_gate.py"])
    run([sys.executable, "tools/test_delivery_authorization_gate.py"])
    run([sys.executable, "tools/test_lifecycle_integration_checkpoint.py"])
    run([sys.executable, "tools/test_runtime_readiness_gate.py"])
    run([sys.executable, "tools/test_local_target_lab_profile.py"])
    run([sys.executable, "tools/test_runtime_destination_binding.py"])
    run([sys.executable, "tools/test_bounded_execution_transition_candidate.py"])
    print("All local checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
