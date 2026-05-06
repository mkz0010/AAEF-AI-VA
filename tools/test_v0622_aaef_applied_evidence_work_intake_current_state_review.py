from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/99-v0622-aaef-applied-evidence-work-intake-and-current-state-review.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains(text: str, phrase: str) -> bool:
    return re.sub(r"\s+", " ", phrase).strip() in re.sub(r"\s+", " ", text).strip()


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0093-add-v0622-aaef-applied-evidence-work-intake-current-state-review.md")
    issue = read_text("planning/issues/0092-add-v0622-aaef-applied-evidence-work-intake-current-state-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.22 current-state review")
    require("v0.6.22 AAEF Applied Evidence Work Intake and Current-state Review" in doc, "v0.6.22 doc must exist")
    require("AAEF applied evidence record" in doc, "doc must focus on AAEF applied evidence record")
    require("Model output is not authority." in doc, "doc must preserve AAEF thesis")
    require("v0.6.21" in doc, "doc must record current latest tag baseline")
    require("ba97047" in doc, "doc must record current latest commit baseline")

    sections = [
        "AAEF-side request summary",
        "Current repository state captured",
        "Repository inventory summary",
        "Existing validators and checks",
        "Existing Tool Gateway and local-lab related files",
        "Public and private boundary",
        "Safe local lab scope boundary",
        "Required applied evidence chain",
        "Minimum scenario set",
        "Reviewer walkthrough requirement",
        "AAEF five questions mapping requirement",
        "Structural validator posture",
        "Optimal work ordering from here",
        "Completion signal expected by AAEF side",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in sections:
        require(section in doc, f"doc must include section: {section}")

    phrases = [
        "This checkpoint is intake, inventory, and work-ordering only.",
        "The next work should prioritize evidence-package planning before additional validator implementation.",
        "AI output is treated as a request, not authority.",
        "AI may generate `tool_action_request`, but gates decide execution.",
        "Dispatch and non-dispatch must be separated from gate decision.",
        "Non-execution evidence is first-class evidence.",
        "The purpose is not to prove vulnerability detection accuracy.",
        "The purpose is to show how AI-generated diagnostic intent is controlled and evidenced.",
        "Patent-sensitive browser/dynamic-state reconstruction details remain outside public repository materials.",
        "Validator success must not be described as semantic correctness, evidence sufficiency, assessment sufficiency, production readiness, audit sufficiency, or legal sufficiency.",
        "v0.6.23 AAEF Applied Evidence Package Design",
    ]
    for phrase in phrases:
        require(contains(doc, phrase), f"doc must include phrase: {phrase}")

    chain_terms = [
        "`tool_action_request`",
        "`gate_decision`",
        "`dispatch_decision`",
        "`execution_result`",
        "`non_execution_result`",
        "`evidence_event`",
        "`review_summary`",
    ]
    for term in chain_terms:
        require(term in doc, f"doc must include evidence chain term: {term}")

    scenarios = [
        "permitted safe diagnostic",
        "denied out-of-scope request",
        "human approval required",
        "not-executed / expired",
    ]
    for scenario in scenarios:
        require(scenario in doc, f"doc must include minimum scenario: {scenario}")

    five_questions = [
        "Who or what acted?",
        "On whose behalf?",
        "With what authority?",
        "Was the action allowed at the point of execution?",
        "What evidence proves what happened?",
    ]
    for question in five_questions:
        require(question in doc, f"doc must include AAEF question: {question}")

    false_markers = [
        "required_node_checks_implemented = false",
        "applied_evidence_package_generated = false",
        "fixture_generated = false",
        "fixture_live_evidence = false",
        "validator_authorizes_execution = false",
        "validator_authorizes_scanning = false",
        "validator_authorizes_docker = false",
        "validator_authorizes_delivery = false",
        "docker_compose_file_created = false",
        "docker_compose_executed = false",
        "docker_image_pulled = false",
        "container_started = false",
        "port_bound = false",
        "docker_execution_authorized = false",
        "execution_authorized = false",
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "customer_target = false",
        "external_network_target = false",
        "delivery_authorized = false",
    ]
    for marker in false_markers:
        require(marker in doc, f"doc must preserve false marker: {marker}")

    forbidden_claims = [
        "this checkpoint implements required-node checks",
        "this checkpoint generates fixture files",
        "this checkpoint creates docker compose files",
        "this checkpoint pulls docker images",
        "this checkpoint starts containers",
        "this checkpoint binds ports",
        "this checkpoint enables runtime execution",
        "this checkpoint allows scan execution",
        "this checkpoint permits credential injection",
        "this checkpoint allows customer target operation",
        "this checkpoint authorizes delivery",
        "this checkpoint proves vulnerability detection accuracy",
        "this checkpoint is production ready",
        "this checkpoint provides implementation conformance",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
        "external framework equivalence is established",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_claims:
        require(claim not in combined, f"forbidden claim found: {claim}")

    require("Add v0.6.22 AAEF applied evidence work intake and current-state review" in adr, "ADR must record v0.6.22 decision")
    require("Completed by v0.6.22 candidate" in issue, "Issue must record v0.6.22 completion status")
    require("## v0.6.22 - AAEF applied evidence work intake and current-state review" in changelog, "CHANGELOG must include v0.6.22")
    require("## v0.6.22 AAEF applied evidence work intake and current-state review" in roadmap, "ROADMAP must include v0.6.22")
    require("test_v0622_aaef_applied_evidence_work_intake_current_state_review.py" in run_all, "run_all must include v0.6.22 test")

    print("v0.6.22 AAEF applied evidence work intake and current-state review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
