from __future__ import annotations

from typing import Any


BLOCKER_CATEGORIES = {
    "real_execution_disabled": "execution_enablement",
    "runtime_configured_not_ready": "runtime",
    "egress_profile_configured_not_ready": "network_egress",
    "artifact_paths_private_not_ready": "artifact_protection",
    "sanitizer_configured_not_ready": "sanitization",
    "stop_timeout_configured_not_ready": "runtime_safety",
    "evidence_emission_required_not_ready": "evidence",
    "target_binding_approved_not_ready": "scope_and_target",
    "credential_injection_policy_configured_not_ready": "credential_handling",
    "human_approval_not_satisfied": "human_approval",
    "command_plan_is_dry_run_only": "execution_mode",
}


NEXT_ACTIONS = {
    "real_execution_disabled": "Keep real execution disabled unless a future release explicitly enables bounded execution.",
    "runtime_configured_not_ready": "Define and review the approved real tool runtime before execution.",
    "egress_profile_configured_not_ready": "Define the allowed network egress profile and deny all other egress paths.",
    "artifact_paths_private_not_ready": "Ensure raw and sanitized artifacts are written only to ignored/private paths.",
    "sanitizer_configured_not_ready": "Define sanitizer rules before any tool output becomes AI-visible.",
    "stop_timeout_configured_not_ready": "Define timeout, stop, and kill conditions for future execution.",
    "evidence_emission_required_not_ready": "Require evidence emission for every future execution path.",
    "target_binding_approved_not_ready": "Confirm the target binding is approved through the scope registry.",
    "credential_injection_policy_configured_not_ready": "Define credential injection policy before resolving or injecting secrets.",
    "human_approval_not_satisfied": "Obtain human approval or mark the operation as not requiring human approval.",
    "command_plan_is_dry_run_only": "Introduce a future explicit execution-mode transition before real execution.",
}


def summarize_readiness_for_operator(readiness_result: dict[str, Any]) -> dict[str, Any]:
    blockers = list(readiness_result.get("blockers", []))
    categories: dict[str, list[str]] = {}

    for blocker in blockers:
        category = BLOCKER_CATEGORIES.get(blocker, "uncategorized")
        categories.setdefault(category, []).append(blocker)

    next_actions = [
        {
            "blocker": blocker,
            "category": BLOCKER_CATEGORIES.get(blocker, "uncategorized"),
            "next_action": NEXT_ACTIONS.get(blocker, "Review this blocker and define an owner/action."),
        }
        for blocker in blockers
    ]

    if readiness_result.get("real_execution_permitted") is True and not blockers:
        recommendation = "approve_for_future_bounded_execution_review"
        review_status = "ready_for_operator_approval"
    else:
        recommendation = "do_not_execute"
        review_status = "blocked"

    return {
        "review_type": "real_execution_readiness_operator_review",
        "review_status": review_status,
        "decision_recommendation": recommendation,
        "real_execution_permitted": readiness_result.get("real_execution_permitted", False),
        "command_plan_id": readiness_result.get("command_plan_id"),
        "tool": readiness_result.get("tool"),
        "operation": readiness_result.get("operation"),
        "target_id": readiness_result.get("target_id"),
        "scope_id": readiness_result.get("scope_id"),
        "blocker_count": len(blockers),
        "blockers": blockers,
        "blocker_categories": categories,
        "next_actions": next_actions,
        "operator_notes_required": bool(blockers),
    }


def format_operator_review_markdown(summary: dict[str, Any]) -> str:
    lines: list[str] = [
        "# Operator Readiness Review",
        "",
        f"- Review status: `{summary['review_status']}`",
        f"- Decision recommendation: `{summary['decision_recommendation']}`",
        f"- Real execution permitted: `{summary['real_execution_permitted']}`",
        f"- Tool: `{summary.get('tool')}`",
        f"- Operation: `{summary.get('operation')}`",
        f"- Target ID: `{summary.get('target_id')}`",
        f"- Scope ID: `{summary.get('scope_id')}`",
        f"- Command plan ID: `{summary.get('command_plan_id')}`",
        f"- Blocker count: `{summary['blocker_count']}`",
        "",
        "## Blockers",
        "",
    ]

    if summary["blockers"]:
        for item in summary["next_actions"]:
            lines.append(f"- `{item['blocker']}` / `{item['category']}`: {item['next_action']}")
    else:
        lines.append("- None")

    lines.extend([
        "",
        "## Operator Decision",
        "",
        "- [ ] Approve future bounded execution review",
        "- [ ] Keep blocked",
        "- [ ] Request additional configuration",
        "- [ ] Request human approval",
        "",
        "## Operator Notes",
        "",
        "_Add review notes here._",
        "",
    ])

    return "\n".join(lines)
