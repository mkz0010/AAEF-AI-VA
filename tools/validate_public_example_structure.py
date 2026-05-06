from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_ROOT = Path("examples/applied-evidence/sanitized-static-mock")

EXPECTED_PACKAGE_ARTIFACTS = [
    "README.md",
    "package_manifest.example.json",
    "reviewer_walkthrough.example.md",
    "aaef_five_questions_mapping.example.md",
    "non_proof_statement.example.md",
    "publication_hygiene_report.example.json",
    "publication_hygiene_report.example.md",
    "publication_review_record.example.json",
    "publication_review_record.example.md",
]

EXPECTED_SCENARIOS = {
    "permitted-safe-diagnostic": "execution_result.example.json",
    "denied-out-of-scope-request": "non_execution_result.example.json",
    "human-approval-required": "non_execution_result.example.json",
    "not-executed-expired": "non_execution_result.example.json",
}

COMMON_SCENARIO_ARTIFACTS = [
    "tool_action_request.example.json",
    "gate_decision.example.json",
    "dispatch_decision.example.json",
    "evidence_event.example.json",
    "review_summary.example.md",
    "non_proof_statement.example.md",
]

REQUIRED_NON_PROOF_CLAIMS = [
    "vulnerability detection accuracy",
    "production readiness",
    "implementation conformance",
    "audit sufficiency",
    "legal sufficiency",
    "compliance certification",
    "external-framework equivalence",
    "customer-target authorization",
    "delivery authorization",
]

REQUIRED_FIVE_QUESTIONS = [
    "Who or what acted?",
    "On whose behalf?",
    "With what authority?",
    "Was the action allowed at the point of execution?",
    "What evidence proves what happened?",
]

FORBIDDEN_TEXT_FRAGMENTS = [
    "private-not-in-git",
    ".generated.",
    "BEGIN RSA PRIVATE KEY",
    "customer.example.com",
    "127.0.0.1",
    "192.168.",
    "10.0.",
]

FORBIDDEN_OVERCLAIMS = [
    # Positive-claim phrases only. Non-proof statements intentionally mention
    # concepts such as audit opinion or legal approval in a negated form.
    "this example is certified compliant",
    "this sample is certified compliant",
    "project claims certified compliance",
    "this example is production ready",
    "this sample is production ready",
    "this checkpoint claims production readiness",
    "this example provides implementation conformance",
    "this sample provides implementation conformance",
    "this example provides audit opinion",
    "this sample provides audit opinion",
    "audit opinion is issued",
    "legal approval is granted",
    "external-framework equivalence claim is established",
    "customer target operation is authorized",
    "delivery is authorized",
    "authorized for customer target operation",
    "authorized for delivery package",
]

BOUNDARY_FLAGS_FALSE = [
    "runtime_execution_authorized",
    "scanner_execution_authorized",
    "scan_execution_allowed",
    "credential_injection_permitted",
    "customer_target",
    "customer_target_authorized",
    "delivery_authorized",
    "customer_deliverable",
]


def read_json(path: Path, blockers: list[str]) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        blockers.append(f"malformed_json:{path.as_posix()}")
        return {}


def read_text(path: Path, blockers: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        blockers.append(f"unreadable_file:{path.as_posix()}")
        return ""


def is_public_example_name(path: Path) -> bool:
    return path.name == "README.md" or ".example." in path.name


def check_forbidden_text(root: Path, blockers: list[str]) -> None:
    if not root.exists():
        return
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for fragment in FORBIDDEN_TEXT_FRAGMENTS:
            if fragment.lower() in lowered:
                blockers.append(f"forbidden_fragment_detected:{path.relative_to(root).as_posix()}")
        for phrase in FORBIDDEN_OVERCLAIMS:
            if phrase.lower() in lowered:
                blockers.append(f"overclaim_detected:{path.relative_to(root).as_posix()}")


def check_package(root: Path, blockers: list[str]) -> dict[str, bool]:
    presence: dict[str, bool] = {}
    for artifact in EXPECTED_PACKAGE_ARTIFACTS:
        exists = (root / artifact).is_file()
        presence[artifact] = exists
        if not exists:
            blockers.append(f"package_artifact_missing:{artifact}")

    for path in root.rglob("*"):
        if path.is_file() and not is_public_example_name(path):
            blockers.append(f"non_example_artifact_name_detected:{path.relative_to(root).as_posix()}")

    mapping_path = root / "aaef_five_questions_mapping.example.md"
    if mapping_path.is_file():
        mapping = mapping_path.read_text(encoding="utf-8")
        for question in REQUIRED_FIVE_QUESTIONS:
            if question not in mapping:
                blockers.append(f"five_questions_mapping_missing:{question}")
    else:
        blockers.append("five_questions_mapping_missing")

    package_non_proof = root / "non_proof_statement.example.md"
    if package_non_proof.is_file():
        text = package_non_proof.read_text(encoding="utf-8")
        for claim in REQUIRED_NON_PROOF_CLAIMS:
            if claim not in text:
                blockers.append(f"package_non_proof_claim_missing:{claim}")
    else:
        blockers.append("package_non_proof_statement_missing")

    return presence


def expected_scenario_artifacts(scenario_id: str) -> list[str]:
    return COMMON_SCENARIO_ARTIFACTS + [EXPECTED_SCENARIOS[scenario_id]]


def check_boundary_flags(data: dict[str, Any], scenario_id: str, artifact: str, blockers: list[str]) -> None:
    boundary = data.get("runtime_boundary", {})
    if not isinstance(boundary, dict):
        blockers.append(f"runtime_boundary_missing:{scenario_id}:{artifact}")
        return
    for flag in BOUNDARY_FLAGS_FALSE:
        if boundary.get(flag) is not False:
            blockers.append(f"runtime_boundary_flag_not_false:{scenario_id}:{artifact}:{flag}")


def check_scenario(root: Path, scenario_id: str, blockers: list[str]) -> dict[str, Any]:
    scenario_dir = root / "scenarios" / scenario_id
    review: dict[str, Any] = {
        "scenario_id": scenario_id,
        "artifact_presence": {},
        "linkage_ok": False,
        "boundary_ok": False,
        "non_proof_visible": False,
        "posture_ok": False,
    }

    if not scenario_dir.is_dir():
        blockers.append(f"scenario_missing:{scenario_id}")
        return review

    for artifact in expected_scenario_artifacts(scenario_id):
        present = (scenario_dir / artifact).is_file()
        review["artifact_presence"][artifact] = present
        if not present:
            blockers.append(f"scenario_artifact_missing:{scenario_id}:{artifact}")

    if not all(review["artifact_presence"].values()):
        return review

    request = read_json(scenario_dir / "tool_action_request.example.json", blockers)
    decision = read_json(scenario_dir / "gate_decision.example.json", blockers)
    dispatch = read_json(scenario_dir / "dispatch_decision.example.json", blockers)
    result_name = EXPECTED_SCENARIOS[scenario_id]
    result = read_json(scenario_dir / result_name, blockers)
    evidence = read_json(scenario_dir / "evidence_event.example.json", blockers)

    linkage_ok = (
        decision.get("linked_request_id") == request.get("request_id")
        and dispatch.get("linked_decision_id") == decision.get("decision_id")
        and result.get("linked_dispatch_decision_id") == dispatch.get("dispatch_decision_id")
        and evidence.get("linked_request_id") == request.get("request_id")
        and evidence.get("linked_decision_id") == decision.get("decision_id")
        and evidence.get("linked_dispatch_decision_id") == dispatch.get("dispatch_decision_id")
        and evidence.get("linked_result_id") == result.get("result_id")
    )
    review["linkage_ok"] = linkage_ok
    if not linkage_ok:
        blockers.append(f"identifier_linkage_broken:{scenario_id}")

    check_boundary_flags(result, scenario_id, result_name, blockers)
    boundary = result.get("runtime_boundary", {})
    boundary_ok = isinstance(boundary, dict) and all(boundary.get(flag) is False for flag in BOUNDARY_FLAGS_FALSE)
    review["boundary_ok"] = boundary_ok

    non_proof_text = read_text(scenario_dir / "non_proof_statement.example.md", blockers)
    review["non_proof_visible"] = all(claim in non_proof_text for claim in REQUIRED_NON_PROOF_CLAIMS)
    if not review["non_proof_visible"]:
        blockers.append(f"non_proof_statement_missing_or_incomplete:{scenario_id}")

    if scenario_id == "permitted-safe-diagnostic":
        posture_ok = result.get("real_execution_occurred") is False and dispatch.get("dispatch_attempted") is True
    else:
        posture_ok = (
            result_name == "non_execution_result.example.json"
            and result.get("execution_occurred") is False
            and result.get("real_execution_occurred") is False
            and dispatch.get("dispatch_attempted") is False
            and bool(result.get("non_execution_reason"))
        )
    review["posture_ok"] = posture_ok
    if not posture_ok:
        blockers.append(f"scenario_posture_contradiction:{scenario_id}")

    return review


def validate(root: Path) -> dict[str, Any]:
    blockers: list[str] = []
    if not root.is_dir():
        blockers.append("example_root_missing")
        return build_result(root, blockers, {}, [], "missing", "missing")

    package_presence = check_package(root, blockers)
    check_forbidden_text(root, blockers)

    scenario_reviews = [check_scenario(root, scenario_id, blockers) for scenario_id in EXPECTED_SCENARIOS]

    hygiene_status = "missing"
    hygiene_path = root / "publication_hygiene_report.example.json"
    if hygiene_path.is_file():
        hygiene = read_json(hygiene_path, blockers)
        hygiene_status = str(hygiene.get("hygiene_status"))
        if hygiene_status != "passed":
            blockers.append("publication_hygiene_not_passed")
    else:
        blockers.append("publication_hygiene_missing")

    publication_review_status = "missing"
    publication_review_path = root / "publication_review_record.example.json"
    if publication_review_path.is_file():
        publication_review = read_json(publication_review_path, blockers)
        publication_review_status = str(publication_review.get("publication_review_status"))
        if publication_review_status != "reviewed_retain_limited_public_example":
            blockers.append("publication_review_status_not_limited_public_example")
    else:
        blockers.append("publication_review_record_missing")

    return build_result(root, blockers, package_presence, scenario_reviews, hygiene_status, publication_review_status)


def build_result(
    root: Path,
    blockers: list[str],
    package_presence: dict[str, bool],
    scenario_reviews: list[dict[str, Any]],
    hygiene_status: str,
    publication_review_status: str,
) -> dict[str, Any]:
    unique_blockers = sorted(set(blockers))
    scenario_count = len([r for r in scenario_reviews if r.get("artifact_presence")])
    status = "passed" if not unique_blockers else "failed"
    return {
        "public_example_structural_validation_status": status,
        "checked_root": str(root),
        "scenario_count": scenario_count,
        "expected_scenario_count": len(EXPECTED_SCENARIOS),
        "hygiene_status": hygiene_status,
        "publication_review_status": publication_review_status,
        "blocker_categories": unique_blockers,
        "package_artifact_presence": package_presence,
        "scenario_reviews": scenario_reviews,
        "runtime_boundary": {
            "public_example_structural_validator_read_only": True,
            "public_example_structural_validator_public_example_scoped": True,
            "public_example_structural_validator_authorizes_execution": False,
            "runtime_execution_authorized": False,
            "scanner_execution_authorized": False,
            "scan_execution_allowed": False,
            "credential_injection_permitted": False,
            "customer_target": False,
            "customer_target_authorized": False,
            "delivery_authorized": False,
            "customer_deliverable": False,
        },
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate sanitized public example structure.")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="Public example root directory.")
    parser.add_argument("--json", action="store_true", help="Emit JSON summary.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = validate(Path(args.root))
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"public example structural validation status: {result['public_example_structural_validation_status']}")
        print(f"scenario count: {result['scenario_count']}")
        print(f"hygiene status: {result['hygiene_status']}")
        print(f"publication review status: {result['publication_review_status']}")
        if result["blocker_categories"]:
            print("blockers:")
            for blocker in result["blocker_categories"]:
                print(f"- {blocker}")
    return 0 if result["public_example_structural_validation_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
