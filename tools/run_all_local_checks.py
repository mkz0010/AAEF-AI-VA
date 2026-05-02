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
    run([sys.executable, "tools/test_local_execution_plan_review.py"])
    run([sys.executable, "tools/test_runtime_safety_policy.py"])
    run([sys.executable, "tools/test_runtime_enforcement_design.py"])
    run([sys.executable, "tools/test_execution_authorization_gate.py"])
    run([sys.executable, "tools/test_preflight_validation.py"])
    run([sys.executable, "tools/test_runtime_transition_checkpoint.py"])
    run([sys.executable, "tools/test_preflight_check_implementation.py"])
    run([sys.executable, "tools/test_preflight_evidence_record_model.py"])
    run([sys.executable, "tools/test_preflight_evidence_examples.py"])
    run([sys.executable, "tools/test_preflight_evidence_validation_rules.py"])
    run([sys.executable, "tools/test_preflight_evidence_negative_examples.py"])
    run([sys.executable, "tools/test_licensing_and_commercial_use_boundary.py"])
    run([sys.executable, "tools/test_public_repository_readiness_checkpoint.py"])
    run([sys.executable, "tools/test_publication_hygiene_private_artifact_exclusion.py"])
    run([sys.executable, "tools/test_public_security_policy_vulnerability_disclosure.py"])
    run([sys.executable, "tools/test_first_publication_repository_settings_checklist.py"])
    run([sys.executable, "tools/test_v040_publication_preparation_release.py"])
    run([sys.executable, "tools/test_github_actions_ci_scaffold.py"])
    run([sys.executable, "tools/test_readme_public_english_wording.py"])
    run([sys.executable, "tools/test_public_facing_repository_metadata_announcement_pack.py"])
    run([sys.executable, "tools/test_public_repository_launch_checkpoint.py"])
    run([sys.executable, "tools/test_public_release_notes_launch_announcement_package.py"])
    run([sys.executable, "tools/test_github_release_publication_checkpoint.py"])
    print("All local checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
