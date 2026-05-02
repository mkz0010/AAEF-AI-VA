from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/79-v062-evaluation-criteria-and-acceptance-model.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0073-add-v062-evaluation-criteria-acceptance-model.md")
    issue = read_text("planning/issues/0072-add-v062-evaluation-criteria-acceptance-model.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.2 evaluation criteria checkpoint")
    require("v0.6.2 Evaluation Criteria and Acceptance Model" in readme, "README must mention v0.6.2 evaluation criteria")
    require("v0.6.2 Evaluation Criteria and Acceptance Model" in doc, "v0.6.2 evaluation criteria doc must exist")

    required_sections = [
        "Evaluation principle",
        "Acceptance model summary",
        "Evaluation dimensions",
        "Maturity advancement rules",
        "Required acceptance gates",
        "Failure criteria",
        "Evidence requirements",
        "Evaluation records",
        "Local lab decision criteria",
        "Demo-readiness criteria",
        "Commercial PoC boundary criteria",
        "Scoring guidance",
        "Recommended next checkpoint",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.2 evaluation criteria doc must include section: {section}")

    evaluation_dimensions = [
        "Control clarity",
        "Safety preservation",
        "Evidence quality",
        "Reviewability",
        "Scope precision",
        "Testability",
        "Explainability",
        "Commercial boundary",
        "Operational repeatability",
        "Public claim safety",
    ]
    for dimension in evaluation_dimensions:
        require(dimension in doc, f"evaluation dimensions must include: {dimension}")

    acceptance_gates = [
        "Capability gate",
        "Evaluation gate",
        "Evidence gate",
        "Safety gate",
        "Scope gate",
        "Review gate",
        "Claim gate",
        "Regression gate",
        "Private artifact gate",
        "Commercial gate",
    ]
    for gate in acceptance_gates:
        require(gate in doc, f"acceptance gates must include: {gate}")

    maturity_movements = [
        "L0 to L1",
        "L1 to L2",
        "L2 to L3",
        "L3 to L4",
        "L4 to L5",
        "L5 to L6",
    ]
    for movement in maturity_movements:
        require(movement in doc, f"maturity advancement rules must include: {movement}")

    failure_criteria = [
        "enables runtime execution without explicit authorization work",
        "enables scan execution without explicit local-only scope and gate maturity",
        "permits credential injection without explicit safety design",
        "implies customer-target authorization",
        "implies production deployment approval",
        "implies compliance certification",
        "implies legal approval",
        "implies audit opinion",
        "stores private generated artifacts in tracked public files",
    ]
    for criterion in failure_criteria:
        require(criterion in doc, f"failure criteria must include: {criterion}")

    local_lab_criteria = [
        "capability inventory exists",
        "evaluation criteria exist",
        "safety boundary and non-goal review exists",
        "local lab decision record exists",
        "local-only target profile is explicit",
        "allowed and denied action taxonomy exists",
        "preflight evidence requirements are explicit",
        "generated output policy remains private",
    ]
    for criterion in local_lab_criteria:
        require(criterion in doc, f"local lab decision criteria must include: {criterion}")

    demo_criteria = [
        "it has a named purpose",
        "it maps to capability inventory",
        "it has evaluation criteria",
        "it does not imply live scanning",
        "it does not imply customer-target authorization",
        'it includes a "what this demo does not prove" section',
    ]
    for criterion in demo_criteria:
        require(criterion in doc, f"demo-readiness criteria must include: {criterion}")

    commercial_poc_terms = [
        "explicit commercial scope",
        "separate commercial agreement or licensing discussion",
        "target authorization model",
        "human review model",
        "evidence retention model",
        "delivery authorization model",
        "data handling boundary",
        "operational rollback plan",
    ]
    for term in commercial_poc_terms:
        require(term in doc, f"commercial PoC boundary criteria must include: {term}")

    scoring_values = [
        "Not evaluated",
        "Weak",
        "Partial",
        "Adequate for planning",
        "Adequate for local validation",
        "Adequate for dry-run demo",
        "Not sufficient for customer use",
    ]
    for value in scoring_values:
        require(value in doc, f"scoring guidance must include: {value}")

    required_phrases = [
        "The project should prefer evidence-backed improvement over feature expansion.",
        "AAEF-AI-VA must not imply L5 or L6 readiness based only on L0-L4 evidence.",
        "This repository does not currently provide commercial PoC readiness.",
        "v0.6.3 Safety Boundary and Non-Goal Review",
        "This checkpoint is evaluation planning only.",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"v0.6.2 evaluation criteria doc must include phrase: {phrase}")

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
        require(marker in doc, f"v0.6.2 evaluation criteria doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"v0.6.2 claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "runtime execution enabled",
        "scan execution allowed",
        "credential injection permitted",
        "customer target operation allowed",
        "is certified compliant",
        "legal approval is granted",
        "audit opinion is issued",
        "commercial license is granted automatically",
        "safety is guaranteed",
        "production deployment approved",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden v0.6.2 evaluation criteria claim found: {claim}")

    require("Add v0.6.2 evaluation criteria and acceptance model" in adr, "ADR must record v0.6.2 evaluation criteria decision")
    require("Completed by v0.6.2 candidate" in issue, "Issue must record v0.6.2 completion status")
    require("## v0.6.2 - Evaluation criteria and acceptance model" in changelog, "CHANGELOG must include v0.6.2")
    require("## v0.6.2 Evaluation criteria and acceptance model" in roadmap, "ROADMAP must include v0.6.2")
    require("test_v062_evaluation_criteria_acceptance_model.py" in run_all, "run_all must include v0.6.2 evaluation criteria test")

    print("v0.6.2 evaluation criteria and acceptance model tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
