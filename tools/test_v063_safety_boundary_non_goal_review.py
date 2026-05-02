from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/80-v063-safety-boundary-and-non-goal-review.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0074-add-v063-safety-boundary-non-goal-review.md")
    issue = read_text("planning/issues/0073-add-v063-safety-boundary-non-goal-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.3 safety boundary/non-goal review")
    require("v0.6.3 Safety Boundary and Non-Goal Review" in readme, "README must mention v0.6.3 safety boundary review")
    require("v0.6.3 Safety Boundary and Non-Goal Review" in doc, "v0.6.3 safety boundary doc must exist")

    required_sections = [
        "Core safety statement",
        "Hard non-goals",
        "Intentionally blocked capabilities",
        "Safety boundary inventory",
        "Non-goal preservation rules",
        "Fail-closed requirements",
        "Local lab constraints",
        "Demo constraints",
        "Runtime gate hardening constraints",
        "Commercial PoC constraints",
        "Unsafe implication checklist",
        "Advancement conditions",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.3 safety boundary doc must include section: {section}")

    required_phrases = [
        "This checkpoint is boundary review only.",
        "AI output is not authority to perform assessment actions.",
        "These blocks are not defects. They are part of the current safety posture.",
        "Runtime gate hardening must not be treated as runtime enablement.",
        "Commercial PoC readiness must not be inferred from this checkpoint.",
        "v0.6.4 Local Assessment Lab Decision Record",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"v0.6.3 safety boundary doc must include phrase: {phrase}")

    hard_non_goals = [
        "Production vulnerability scanner",
        "Autonomous vulnerability scanner",
        "Live scanning",
        "External network testing",
        "Customer-target operation",
        "Credential injection against real systems",
        "Production deployment",
        "Managed security service operation",
        "Multi-tenant SaaS operation",
        "Compliance certification",
        "Legal approval",
        "Audit opinion",
        "External framework equivalence",
        "Commercial license grant",
    ]
    for non_goal in hard_non_goals:
        require(non_goal in doc, f"hard non-goals must include: {non_goal}")

    blocked_capabilities = [
        "runtime execution",
        "network activity",
        "scan execution",
        "credential injection",
        "raw artifact capture",
        "customer-target operation",
        "external network testing",
        "production deployment",
        "managed-service operation",
        "multi-tenant SaaS operation",
    ]
    blocked_section = doc.split("## Intentionally blocked capabilities", 1)[1].split("## Safety boundary inventory", 1)[0].lower()
    for capability in blocked_capabilities:
        require(capability.lower() in blocked_section, f"blocked capabilities must include: {capability}")

    fail_closed_terms = [
        "scope is missing",
        "target binding is missing",
        "authorization is missing",
        "preflight evidence is missing",
        "human review is required but absent",
        "credential material is requested",
        "raw artifact capture is requested",
        "delivery authorization is missing",
        "public claims exceed demonstrated maturity",
    ]
    for term in fail_closed_terms:
        require(term in doc, f"fail-closed requirements must include: {term}")

    local_lab_constraints = [
        "local-only or localhost-only target mode",
        "owned lab target only",
        "no third-party target",
        "no customer target",
        "no external network testing",
        "no real credential injection",
        "generated outputs under `private-not-in-git/`",
        "explicit allowed and denied action taxonomy",
        "explicit preflight evidence requirements",
        "explicit human review requirements",
    ]
    for constraint in local_lab_constraints:
        require(constraint in doc, f"local lab constraints must include: {constraint}")

    demo_constraints = [
        "state what it proves",
        "state what it does not prove",
        "map to capability inventory",
        "map to evaluation criteria",
        "avoid live scan implication",
        "avoid customer-target implication",
        "avoid production-readiness implication",
    ]
    for constraint in demo_constraints:
        require(constraint in doc, f"demo constraints must include: {constraint}")

    unsafe_implications = [
        "local lab",
        "customer target",
        "dry-run",
        "live scan",
        "validation",
        "certification",
        "review gate",
        "legal approval",
        "delivery gate",
        "customer delivery authorization",
        "runtime gate",
        "runtime execution enabled",
    ]

    for term in unsafe_implications:
        require(term in doc, f"unsafe implication checklist must include: {term}")

    advancement_conditions = [
        "the changed capability is named",
        "the maturity movement is stated",
        "evidence exists",
        "safety boundaries remain intact",
        "public claims remain conservative",
        "private outputs remain private",
        "human review remains preserved where required",
        "commercial implications are separated from public use",
        "all local checks pass",
        "the next decision becomes clearer",
    ]
    for condition in advancement_conditions:
        require(condition in doc, f"advancement conditions must include: {condition}")

    required_false_markers = [
        "execution_authorized = false",
        "preflight_satisfied = false",
        "ready_for_runtime_execution = false",
        "real_execution_permitted = false",
        "external_process_execution_allowed = false",
        "network_activity_allowed = false",
        "scan_execution_allowed = false",
        "credential_injection_permitted = false",
        "raw_artifact_capture_permitted = false",
        "customer_target = false",
        "external_network_target = false",
    ]
    for marker in required_false_markers:
        require(marker in doc, f"v0.6.3 safety boundary doc must preserve marker: {marker}")

    claims_section = doc.split("## Claims to avoid", 1)[1].split("## Required local checks", 1)[0].lower()
    claims_to_avoid = [
        "production deployment approval",
        "runtime execution readiness",
        "scan authorization",
        "customer-target authorization",
        "compliance certification",
        "legal approval",
        "audit opinion",
        "completed legal review",
        "completed dependency audit",
        "managed service approval",
        "commercial license grant",
        "safety guarantee",
        "external framework equivalence",
        "audit sufficiency",
    ]
    for claim in claims_to_avoid:
        require(claim in claims_section, f"v0.6.3 claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
        "this checkpoint permits credential injection",
        "this repository permits credential injection",
        "this checkpoint allows customer target operation",
        "this repository allows customer target operation",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
        "commercial license is granted automatically by this repository",
        "safety is guaranteed by this checkpoint",
        "production deployment is approved by this checkpoint",
    ]

    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden v0.6.3 safety boundary claim found: {claim}")

    require("Add v0.6.3 safety boundary and non-goal review" in adr, "ADR must record v0.6.3 safety boundary decision")
    require("Completed by v0.6.3 candidate" in issue, "Issue must record v0.6.3 completion status")
    require("## v0.6.3 - Safety boundary and non-goal review" in changelog, "CHANGELOG must include v0.6.3")
    require("## v0.6.3 Safety boundary and non-goal review" in roadmap, "ROADMAP must include v0.6.3")
    require("test_v063_safety_boundary_non_goal_review.py" in run_all, "run_all must include v0.6.3 safety boundary test")

    print("v0.6.3 safety boundary and non-goal review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
