from __future__ import annotations

from external_discovery_fail_closed import evaluate_external_discovery_fail_closed


BASE_REQUEST = {
    "external_discovery": True,
    "runtime_destination_binding": "binding-scoped-external",
    "scope_supports_external_discovery": True,
}

BASE_DECISION = {
    "external_discovery_allowed": True,
    "scope_supports_external_discovery": True,
}

BASE_BOUNDARY = {
    "target_mode": "scoped_external",
    "runtime_destination_binding": "binding-scoped-external",
    "scope_supports_external_discovery": True,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_blocked_with_category(result, category: str) -> None:
    require(result.allowed_to_continue is False, f"{category} must fail closed")
    require(result.status == "blocked", f"{category} status must be blocked")
    require(category in result.block_categories, f"{category} must be recorded")


def result_for(request_updates=None, decision_updates=None, boundary_updates=None, *, request=None, decision=None, boundary=None, authorization_result=None):
    req = dict(BASE_REQUEST if request is None else request)
    dec = dict(BASE_DECISION if decision is None else decision)
    bnd = dict(BASE_BOUNDARY if boundary is None else boundary)
    if request_updates:
        req.update(request_updates)
    if decision_updates:
        dec.update(decision_updates)
    if boundary_updates:
        bnd.update(boundary_updates)
    return evaluate_external_discovery_fail_closed(
        req,
        dec,
        target_boundary=bnd,
        authorization_result=authorization_result,
    )


def main() -> int:
    external_false = evaluate_external_discovery_fail_closed(
        {"external_discovery": False},
        {},
        target_boundary=None,
    )
    require(external_false.allowed_to_continue is True, "external_discovery=false must continue existing checks")
    require(external_false.reason == "external_discovery_not_requested", "external false reason mismatch")

    external_missing = evaluate_external_discovery_fail_closed(
        {},
        {},
        target_boundary=None,
    )
    require(external_missing.allowed_to_continue is True, "external_discovery missing and not required must continue existing checks")

    allowed = result_for()
    require(allowed.allowed_to_continue is True, "explicitly allowed boundary-compatible external discovery must continue existing checks")
    require(allowed.reason == "external_discovery_explicitly_allowed_and_boundary_compatible", "allowed reason mismatch")

    no_decision_allowance = result_for(decision={})
    assert_blocked_with_category(no_decision_allowance, "external_discovery_requested_without_decision_allowance")

    allowance_false = result_for(decision_updates={"external_discovery_allowed": False})
    assert_blocked_with_category(allowance_false, "external_discovery_requested_without_decision_allowance")

    localhost_only = result_for(boundary_updates={"target_mode": "localhost_only"})
    assert_blocked_with_category(localhost_only, "external_discovery_requested_against_localhost_only_boundary")

    local_lab_only = result_for(boundary_updates={"target_mode": "local_lab_only"})
    assert_blocked_with_category(local_lab_only, "external_discovery_requested_against_local_lab_only_boundary")

    missing_destination = evaluate_external_discovery_fail_closed(
        {"external_discovery": True, "scope_supports_external_discovery": True},
        {"external_discovery_allowed": True, "scope_supports_external_discovery": True},
        target_boundary={"target_mode": "scoped_external", "scope_supports_external_discovery": True},
    )
    assert_blocked_with_category(missing_destination, "external_discovery_requested_without_runtime_destination_binding")

    malformed_destination = result_for(boundary_updates={"runtime_destination_binding": ""})
    assert_blocked_with_category(malformed_destination, "external_discovery_requested_with_malformed_destination_binding")

    missing_scope_support = evaluate_external_discovery_fail_closed(
        {"external_discovery": True, "runtime_destination_binding": "binding-scoped-external"},
        {"external_discovery_allowed": True},
        target_boundary={"target_mode": "scoped_external", "runtime_destination_binding": "binding-scoped-external"},
    )
    assert_blocked_with_category(missing_scope_support, "external_discovery_requested_without_scope_support")

    ambiguous_boundary = evaluate_external_discovery_fail_closed(
        BASE_REQUEST,
        BASE_DECISION,
        target_boundary={"runtime_destination_binding": "binding-scoped-external", "scope_supports_external_discovery": True},
    )
    assert_blocked_with_category(ambiguous_boundary, "external_discovery_requested_with_ambiguous_target_boundary")

    invalid_auth = result_for(authorization_result={"allowed_to_continue": False, "status": "blocked"})
    assert_blocked_with_category(invalid_auth, "external_discovery_requested_with_expired_or_invalid_authorization")

    malformed_flag = evaluate_external_discovery_fail_closed(
        {"external_discovery": "true"},
        BASE_DECISION,
        target_boundary=BASE_BOUNDARY,
    )
    assert_blocked_with_category(malformed_flag, "malformed_external_discovery_flag")

    evidence = result_for(
        request_updates={"runtime_destination_binding": "binding-super-secret"},
        boundary_updates={"runtime_destination_binding": "binding-super-secret"},
    ).as_evidence()
    evidence_text = str(evidence).lower()
    for forbidden in [
        "binding-super-secret",
        "secret-value",
        "password",
        "token",
        "scanner_output",
        "customer",
        "third-party-target.example",
    ]:
        require(forbidden not in evidence_text, f"evidence should not include sensitive material: {forbidden}")
    require("allowed_to_continue" in evidence, "evidence must include allowed_to_continue")
    require("checked_fields" in evidence, "evidence must include checked_fields")

    print("External discovery fail-closed helper tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
