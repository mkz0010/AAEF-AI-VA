from __future__ import annotations

from typing import Any


class LifecycleCheckpointError(ValueError):
    pass


REQUIRED_OBJECTS = [
    "readiness_result",
    "operator_review",
    "human_approval_gate_result",
    "evidence_chain",
    "reconstruction_report",
    "sanitized_artifact",
    "finding_candidate",
    "finding_review_gate_result",
    "report_finding_promotion_gate_result",
    "report_review_gate_result",
    "report_packet_review_gate_result",
    "delivery_authorization_gate_result",
    "delivery_package",
]


def _require_object(bundle: dict[str, Any], key: str) -> dict[str, Any]:
    value = bundle.get(key)
    if not isinstance(value, dict):
        raise LifecycleCheckpointError(f"missing lifecycle object: {key}")
    return value


def _require_false(obj: dict[str, Any], field: str, label: str) -> None:
    if obj.get(field) is not False:
        raise LifecycleCheckpointError(f"{label}.{field} must be false")


def _require_true(obj: dict[str, Any], field: str, label: str) -> None:
    if obj.get(field) is not True:
        raise LifecycleCheckpointError(f"{label}.{field} must be true")


def _require_equal(left: Any, right: Any, label: str) -> None:
    if left != right:
        raise LifecycleCheckpointError(f"lifecycle mismatch for {label}: {left!r} != {right!r}")


def validate_lifecycle_checkpoint_bundle(bundle: dict[str, Any]) -> None:
    for key in REQUIRED_OBJECTS:
        _require_object(bundle, key)

    readiness = bundle["readiness_result"]
    operator_review = bundle["operator_review"]
    approval_gate = bundle["human_approval_gate_result"]
    evidence_chain = bundle["evidence_chain"]
    reconstruction_report = bundle["reconstruction_report"]
    sanitized = bundle["sanitized_artifact"]
    candidate = bundle["finding_candidate"]
    finding_review_gate = bundle["finding_review_gate_result"]
    promotion_gate = bundle["report_finding_promotion_gate_result"]
    report_review_gate = bundle["report_review_gate_result"]
    packet_review_gate = bundle["report_packet_review_gate_result"]
    delivery_gate = bundle["delivery_authorization_gate_result"]
    delivery_package = bundle["delivery_package"]

    _require_false(readiness, "real_execution_permitted", "readiness_result")
    _require_false(approval_gate, "real_execution_permitted", "human_approval_gate_result")
    _require_false(evidence_chain, "real_execution_permitted", "evidence_chain")
    _require_false(reconstruction_report, "real_execution_permitted", "reconstruction_report")

    _require_false(evidence_chain, "secret_exposed_to_ai", "evidence_chain")
    _require_false(reconstruction_report, "secret_exposed_to_ai", "reconstruction_report")
    _require_false(sanitized, "secret_exposed_to_ai", "sanitized_artifact")
    _require_false(candidate, "secret_exposed_to_ai", "finding_candidate")
    _require_false(finding_review_gate, "secret_exposed_to_ai", "finding_review_gate_result")
    _require_false(promotion_gate, "secret_exposed_to_ai", "report_finding_promotion_gate_result")
    _require_false(report_review_gate, "secret_exposed_to_ai", "report_review_gate_result")
    _require_false(packet_review_gate, "secret_exposed_to_ai", "report_packet_review_gate_result")
    _require_false(delivery_gate, "secret_exposed_to_ai", "delivery_authorization_gate_result")
    _require_false(delivery_package, "secret_exposed_to_ai", "delivery_package")

    _require_true(sanitized, "ai_visible_allowed", "sanitized_artifact")
    _require_true(candidate, "ai_visible_allowed", "finding_candidate")
    _require_true(candidate, "requires_human_review", "finding_candidate")
    _require_true(delivery_package, "package_generated", "delivery_package")
    _require_true(delivery_package, "requires_export_control_review", "delivery_package")

    for label, obj in [
        ("finding_candidate", candidate),
        ("finding_review_gate_result", finding_review_gate),
        ("report_finding_promotion_gate_result", promotion_gate),
        ("report_review_gate_result", report_review_gate),
        ("report_packet_review_gate_result", packet_review_gate),
        ("delivery_authorization_gate_result", delivery_gate),
        ("delivery_package", delivery_package),
    ]:
        _require_false(obj, "report_ready", label)

    for label, obj in [
        ("report_finding_promotion_gate_result", promotion_gate),
        ("report_review_gate_result", report_review_gate),
        ("report_packet_review_gate_result", packet_review_gate),
        ("delivery_authorization_gate_result", delivery_gate),
        ("delivery_package", delivery_package),
    ]:
        _require_false(obj, "customer_delivery_ready", label)

    _require_false(delivery_gate, "delivery_dispatched", "delivery_authorization_gate_result")
    _require_false(delivery_gate, "customer_delivery_performed", "delivery_authorization_gate_result")
    _require_false(delivery_package, "delivery_dispatched", "delivery_package")
    _require_false(delivery_package, "customer_delivery_performed", "delivery_package")

    if "command_plan_is_dry_run_only" not in readiness.get("blockers", []):
        raise LifecycleCheckpointError("readiness_result must record command_plan_is_dry_run_only blocker")

    if operator_review.get("decision_recommendation") != "do_not_execute":
        raise LifecycleCheckpointError("operator_review must recommend do_not_execute in current MVP")

    if reconstruction_report.get("safety_assertions", {}).get("model_output_was_not_execution_authority") is not True:
        raise LifecycleCheckpointError("reconstruction report must assert model output was not execution authority")

    _require_equal(
        evidence_chain.get("target_id"),
        reconstruction_report.get("target_id"),
        "evidence_chain/reconstruction_report target_id",
    )
    _require_equal(
        evidence_chain.get("scope_id"),
        reconstruction_report.get("scope_id"),
        "evidence_chain/reconstruction_report scope_id",
    )
    _require_equal(
        candidate.get("target_id"),
        delivery_package.get("target_id"),
        "finding_candidate/delivery_package target_id",
    )
    _require_equal(
        candidate.get("scope_id"),
        delivery_package.get("scope_id"),
        "finding_candidate/delivery_package scope_id",
    )


def build_lifecycle_checkpoint_summary(bundle: dict[str, Any]) -> dict[str, Any]:
    validate_lifecycle_checkpoint_bundle(bundle)

    readiness = bundle["readiness_result"]
    evidence_chain = bundle["evidence_chain"]
    reconstruction_report = bundle["reconstruction_report"]
    sanitized = bundle["sanitized_artifact"]
    candidate = bundle["finding_candidate"]
    finding_review_gate = bundle["finding_review_gate_result"]
    promotion_gate = bundle["report_finding_promotion_gate_result"]
    report_review_gate = bundle["report_review_gate_result"]
    packet_review_gate = bundle["report_packet_review_gate_result"]
    delivery_gate = bundle["delivery_authorization_gate_result"]
    delivery_package = bundle["delivery_package"]

    return {
        "checkpoint_id": "v0.1.30-lifecycle-integration-checkpoint",
        "checkpoint_type": "lifecycle_integration_summary",
        "checkpoint_status": "passed",
        "project_phase": "v0.1.x-control-and-review-workflow",
        "current_version_target": "v0.1.30",
        "target_id": evidence_chain["target_id"],
        "scope_id": evidence_chain["scope_id"],
        "tool": evidence_chain["tool"],
        "operation": evidence_chain["operation"],
        "core_positioning": (
            "AAEF-controlled AI Vulnerability Assessment Platform: a control, review, "
            "evidence, and report lifecycle scaffold for AI-assisted vulnerability assessment."
        ),
        "stable_capabilities": [
            "Tool Gateway mock execution and generated evidence records",
            "credential_ref and mock Vault metadata validation",
            "scope registry target alias resolution",
            "controlled executor dry-run policy",
            "real execution readiness gate",
            "operator readiness review",
            "human approval record and approval gate",
            "evidence chain and reconstruction report",
            "sanitizer and redaction policy scaffold",
            "sanitized finding candidate model",
            "finding candidate review gate",
            "report finding promotion gate",
            "report review gate",
            "report packet review gate",
            "delivery authorization gate",
        ],
        "explicit_non_goals": [
            "No real ZAP/Burp/Nmap/nuclei execution in v0.1.x",
            "No external process execution",
            "No network activity",
            "No raw adapter artifact exposure to AI",
            "No customer delivery",
            "No delivery dispatch",
            "No report artifact marked as final",
            "No report_ready=true artifact",
            "No customer_delivery_ready=true artifact",
        ],
        "safety_invariants": {
            "model_output_was_not_execution_authority": True,
            "real_execution_permitted": False,
            "external_process_executed": False,
            "network_activity_performed": False,
            "secret_exposed_to_ai": False,
            "report_ready": False,
            "customer_delivery_ready": False,
            "delivery_dispatched": False,
            "customer_delivery_performed": False,
            "evidence_required": True,
        },
        "dry_run_and_review_status": {
            "readiness_gate": readiness["gate_result"],
            "readiness_blockers": readiness["blockers"],
            "evidence_chain_status": evidence_chain["chain_status"],
            "reconstruction_conclusion": reconstruction_report["conclusion"],
            "sanitizer_status": sanitized["sanitizer_status"],
            "redaction_count": sanitized["redaction_count"],
            "finding_candidate_status": candidate["finding_candidate_status"],
            "finding_review_gate_status": finding_review_gate["gate_status"],
            "report_finding_promotion_gate_status": promotion_gate["gate_status"],
            "report_review_gate_status": report_review_gate["gate_status"],
            "report_packet_review_gate_status": packet_review_gate["gate_status"],
            "delivery_authorization_gate_status": delivery_gate["gate_status"],
            "delivery_package_status": delivery_package["delivery_package_status"],
        },
        "next_phase_candidates": [
            "v0.2.0: controlled local ZAP runtime readiness",
            "local-only vulnerable target setup",
            "runtime detection without execution",
            "sanitizer coverage expansion",
            "scope registry runtime destination storage design",
            "bounded execution mode transition design",
        ],
        "checkpoint_notes": (
            "v0.1.30 records the current lifecycle as a stable local checkpoint before moving "
            "toward controlled local tool runtime integration. The checkpoint intentionally keeps "
            "real execution, customer delivery, and final lifecycle terminology out of scope."
        ),
    }


def validate_lifecycle_checkpoint_summary(summary: dict[str, Any]) -> None:
    if summary.get("checkpoint_status") != "passed":
        raise LifecycleCheckpointError("checkpoint_status must be passed")

    invariants = summary.get("safety_invariants", {})
    required_false = [
        "real_execution_permitted",
        "external_process_executed",
        "network_activity_performed",
        "secret_exposed_to_ai",
        "report_ready",
        "customer_delivery_ready",
        "delivery_dispatched",
        "customer_delivery_performed",
    ]
    for key in required_false:
        if invariants.get(key) is not False:
            raise LifecycleCheckpointError(f"safety invariant must be false: {key}")

    if invariants.get("model_output_was_not_execution_authority") is not True:
        raise LifecycleCheckpointError("model_output_was_not_execution_authority must be true")

    if invariants.get("evidence_required") is not True:
        raise LifecycleCheckpointError("evidence_required must be true")

    forbidden_terms = ["final_report", "final finding", "final_report_finding"]
    serialized = str(summary).lower()
    for term in forbidden_terms:
        if term in serialized:
            raise LifecycleCheckpointError(f"checkpoint summary contains forbidden lifecycle term: {term}")


def format_lifecycle_checkpoint_markdown(summary: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Lifecycle Integration Checkpoint")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Checkpoint ID: `{summary['checkpoint_id']}`")
    lines.append(f"- Checkpoint status: `{summary['checkpoint_status']}`")
    lines.append(f"- Project phase: `{summary['project_phase']}`")
    lines.append(f"- Version target: `{summary['current_version_target']}`")
    lines.append(f"- Target ID: `{summary['target_id']}`")
    lines.append(f"- Scope ID: `{summary['scope_id']}`")
    lines.append(f"- Tool: `{summary['tool']}`")
    lines.append(f"- Operation: `{summary['operation']}`")
    lines.append("")
    lines.append("## Core Positioning")
    lines.append("")
    lines.append(summary["core_positioning"])
    lines.append("")
    lines.append("## Stable Capabilities")
    lines.append("")
    for item in summary["stable_capabilities"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Explicit Non-Goals")
    lines.append("")
    for item in summary["explicit_non_goals"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Safety Invariants")
    lines.append("")
    for key, value in summary["safety_invariants"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## Dry-Run and Review Status")
    lines.append("")
    for key, value in summary["dry_run_and_review_status"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## Next Phase Candidates")
    lines.append("")
    for item in summary["next_phase_candidates"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(summary["checkpoint_notes"])
    lines.append("")
    return "\n".join(lines)
