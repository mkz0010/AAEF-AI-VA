from __future__ import annotations

from request_decision_constraint_diff import evaluate_request_decision_constraint_diff


BASE_REQUEST = {
    "tool_action": "zap-baseline",
    "target": "local-lab",
    "target_mode": "localhost_only",
    "scope_id": "scope-demo",
    "execution_mode": "dry_run",
    "external_discovery": False,
    "destination_binding": "binding-localhost",
    "credential_ref": "credential_ref:demo",
}

BASE_DECISION = {
    "authorized_tool_action": "zap-baseline",
    "authorized_target": "local-lab",
    "target_mode": "localhost_only",
    "authorized_scope": "scope-demo",
    "authorized_execution_mode": "dry_run",
    "external_discovery_allowed": False,
    "destination_binding": "binding-localhost",
    "authorized_credential_ref": "credential_ref:demo",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def result_for(request_updates=None, decision_updates=None, *, request=None, decision=None):
    req = dict(BASE_REQUEST if request is None else request)
    dec = dict(BASE_DECISION if decision is None else decision)
    if request_updates:
        req.update(request_updates)
    if decision_updates:
        dec.update(decision_updates)
    return evaluate_request_decision_constraint_diff(req, dec)


def assert_blocked_with_category(result, category: str) -> None:
    require(result.allowed_to_continue is False, f"{category} must fail closed")
    require(result.status == "blocked", f"{category} status must be blocked")
    require(category in result.diff_categories, f"{category} must be recorded")


def main() -> int:
    exact = result_for()
    require(exact.allowed_to_continue is True, "exact request/decision match must continue existing checks")
    require(exact.status == "continue_existing_checks", "exact match status mismatch")
    require(exact.reason == "request_decision_constraints_match", "exact match reason mismatch")

    assert_blocked_with_category(result_for({"tool_action": "nmap-scan"}), "tool_action_mismatch")
    assert_blocked_with_category(result_for({"target": "external-target"}), "target_mismatch")
    assert_blocked_with_category(result_for({"destination_binding": "binding-external"}), "destination_binding_mismatch")
    assert_blocked_with_category(result_for({"target_mode": "external"}), "target_mode_mismatch")
    assert_blocked_with_category(result_for({"scope_id": "scope-other"}), "scope_mismatch")
    assert_blocked_with_category(result_for({"credential_ref": "credential_ref:other"}), "credential_ref_mismatch")
    assert_blocked_with_category(result_for({"execution_mode": "live"}), "execution_mode_mismatch")
    assert_blocked_with_category(result_for({"external_discovery": True}), "external_discovery_escalation")

    missing_request = dict(BASE_REQUEST)
    del missing_request["scope_id"]
    assert_blocked_with_category(result_for(request=missing_request), "missing_required_request_field")

    missing_decision = dict(BASE_DECISION)
    del missing_decision["authorized_scope"]
    assert_blocked_with_category(result_for(decision=missing_decision), "missing_required_decision_field")

    malformed_request = evaluate_request_decision_constraint_diff("not-a-request", BASE_DECISION)
    assert_blocked_with_category(malformed_request, "malformed_request_constraints")

    malformed_decision = evaluate_request_decision_constraint_diff(BASE_REQUEST, "not-a-decision")
    assert_blocked_with_category(malformed_decision, "malformed_decision_constraints")

    evidence = result_for({"credential_ref": "credential_ref:super-secret"}).as_evidence()
    evidence_text = str(evidence).lower()
    for forbidden in [
        "super-secret",
        "secret-value",
        "password",
        "token",
        "scanner_output",
        "customer",
    ]:
        require(forbidden not in evidence_text, f"evidence should not include sensitive material: {forbidden}")
    require("credential_ref_mismatch" in evidence_text, "evidence should include safe diff category")
    require("credential_ref" in evidence_text, "evidence should include safe field name")

    print("Request/decision constraint-diff helper tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
