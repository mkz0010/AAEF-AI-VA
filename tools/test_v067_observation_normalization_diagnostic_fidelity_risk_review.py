from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOC = "docs/84-v067-observation-normalization-and-diagnostic-fidelity-risk-review.md"


def read_text(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    readme = read_text("README.md")
    doc = read_text(DOC)
    adr = read_text("planning/decisions/ADR-0078-add-v067-observation-normalization-diagnostic-fidelity-risk-review.md")
    issue = read_text("planning/issues/0077-add-v067-observation-normalization-diagnostic-fidelity-risk-review.md")
    changelog = read_text("CHANGELOG.md")
    roadmap = read_text("ROADMAP.md")
    run_all = read_text("tools/run_all_local_checks.py")

    require(DOC in readme, "README must link v0.6.7 observation normalization checkpoint")
    require("v0.6.7 Observation Normalization and Diagnostic Fidelity Risk Review" in readme, "README must mention v0.6.7 observation normalization")
    require("v0.6.7 Observation Normalization and Diagnostic Fidelity Risk Review" in doc, "v0.6.7 observation normalization doc must exist")

    required_sections = [
        "Core concern",
        "Diagnostic Fidelity Risk",
        "Observation handling pipeline",
        "Raw artifact principle",
        "AI diagnostic context package",
        "Signal-preserving extraction",
        "Information that should not be sent directly to AI",
        "Information density criteria",
        "Diagnostic sufficiency criteria",
        "Normalization loss record",
        "Fidelity risk levels",
        "AI behavior under insufficient information",
        "Escalation paths",
        "Relationship to tool_action_request",
        "Relationship to sanitizer and normalizer",
        "Prompt injection and untrusted content",
        "What this checkpoint enables",
        "Recommended next checkpoint",
        "Public claim boundary",
        "Runtime and scanning boundary",
        "Claims to avoid",
    ]
    for section in required_sections:
        require(section in doc, f"v0.6.7 observation normalization doc must include section: {section}")

    required_phrases = [
        "Safety controls can reduce diagnostic accuracy if they remove or over-normalize important signals.",
        "This risk is not a reason to send raw artifacts directly to AI.",
        "AI should receive the AI diagnostic context package.",
        "AI should not receive uncontrolled raw responses, secrets, credentials, access tokens, session values, or customer-sensitive raw artifacts.",
        "Raw artifact retention does not mean AI access.",
        "Information density does not mean maximum content length.",
        "Information density means diagnostically useful, safe, structured signal.",
        "AI should instead request additional observation, human review, or sufficiency improvement.",
        "Normalization loss should be evidence, not hidden behavior.",
        "Escalation is not execution.",
        "AI should not be the component that decides whether unsafe raw content is acceptable.",
        "Prompt-injection handling must not erase diagnostic signals silently.",
        "This checkpoint does not enable runtime execution or scanning.",
        "v0.6.8 Demo Scenario and Reviewer Walkthrough Planning",
    ]
    for phrase in required_phrases:
        require(phrase in doc, f"v0.6.7 observation normalization doc must include phrase: {phrase}")

    context_fields = [
        "`context_id`",
        "`source_observation_refs`",
        "`raw_artifact_refs`",
        "`target_binding_ref`",
        "`observation_summary`",
        "`extracted_signals`",
        "`negative_signals`",
        "`normalization_loss_record_ref`",
        "`missing_information`",
        "`confidence`",
        "`uncertainty`",
        "`prompt_injection_risk`",
        "`credential_exposure_risk`",
        "`recommended_next_observation`",
        "`safety_notes`",
        "`human_review_recommended`",
    ]
    for field in context_fields:
        require(field in doc, f"AI diagnostic context package must include: {field}")

    signal_terms = [
        "status code",
        "redirect chain summary",
        "security header presence or absence",
        "cookie attribute summary without cookie values",
        "form field names and types",
        "hidden field presence without secret values",
        "reflected input indicators",
        "script source references",
        "endpoint candidates",
        "API schema hints",
        "authentication state indicators",
        "error signature summaries",
        "framework hints",
        "encoding and parser anomalies",
        "suspicious patterns",
    ]
    for term in signal_terms:
        require(term in doc, f"signal-preserving extraction must include: {term}")

    not_direct_to_ai = [
        "raw cookies",
        "session identifiers",
        "CSRF token values",
        "bearer tokens",
        "API keys",
        "passwords",
        "private keys",
        "access tokens",
        "refresh tokens",
        "customer personal data",
        "full raw HTML containing secrets",
        "full raw JavaScript containing secrets",
        "full stack traces containing sensitive paths or values",
        "raw vulnerability artifacts",
        "unreviewed prompt-injection content",
    ]
    for item in not_direct_to_ai:
        require(item in doc, f"information not sent directly to AI must include: {item}")

    sufficiency_criteria = [
        "Target binding",
        "Scope binding",
        "Observation source",
        "Sanitization status",
        "Normalization status",
        "Extracted signals",
        "Normalization loss",
        "Missing information",
        "Prompt-injection risk",
        "Credential exposure risk",
        "Human review need",
        "Expected evidence",
        "Denied action conflict",
    ]
    for criterion in sufficiency_criteria:
        require(criterion in doc, f"diagnostic sufficiency criteria must include: {criterion}")

    loss_fields = [
        "`loss_record_id`",
        "`raw_artifact_ref`",
        "`sanitized_artifact_ref`",
        "`normalized_observation_ref`",
        "`fields_removed`",
        "`fields_redacted`",
        "`fields_preserved_as_signals`",
        "`fields_summarized`",
        "`possible_diagnostic_loss`",
        "`fidelity_risk_level`",
        "`requires_human_review`",
        "`recommended_escalation`",
    ]
    for field in loss_fields:
        require(field in doc, f"normalization loss record must include: {field}")

    risk_levels = [
        "`low`",
        "`medium`",
        "`high`",
        "`unknown`",
    ]
    for level in risk_levels:
        require(level in doc, f"fidelity risk levels must include: {level}")

    ai_must_not = [
        "invent missing observations",
        "assume raw artifact content it has not received",
        "treat normalized summaries as complete raw evidence",
        "ignore normalization loss",
        "convert uncertainty into execution permission",
        "request secrets or raw credentials",
        "bypass gates",
    ]
    for item in ai_must_not:
        require(item in doc, f"AI behavior under insufficient information must include: {item}")

    escalations = [
        "`request_more_observation`",
        "`request_human_review`",
        "`request_preflight_evidence`",
        "`request_loss_record_review`",
        "`request_controlled_raw_reference_review`",
        "`keep_blocked`",
    ]
    for escalation in escalations:
        require(escalation in doc, f"escalation paths must include: {escalation}")

    components = [
        "Sanitizer / redactor",
        "Normalizer",
        "Signal extractor",
        "Loss recorder",
        "Sufficiency gate",
        "AI",
        "Gates",
    ]
    for component in components:
        require(component in doc, f"sanitizer/normalizer relationship must include: {component}")

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
        require(marker in doc, f"v0.6.7 observation normalization doc must preserve marker: {marker}")

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
        require(claim in claims_section, f"v0.6.7 claims-to-avoid section must include: {claim}")

    forbidden_positive_claims = [
        "this checkpoint enables runtime execution",
        "this repository enables runtime execution",
        "this checkpoint allows scan execution",
        "this repository allows scan execution",
        "this checkpoint permits credential injection",
        "this repository permits credential injection",
        "this checkpoint allows customer target operation",
        "this repository allows customer target operation",
        "this checkpoint sends raw responses directly to ai",
        "this repository sends raw responses directly to ai",
        "this checkpoint says ai has full diagnostic visibility",
        "this repository says ai has full diagnostic visibility",
        "this checkpoint says normalization has no diagnostic cost",
        "this repository says normalization has no diagnostic cost",
        "project is certified compliant",
        "legal approval is granted by this checkpoint",
        "audit opinion is issued by this checkpoint",
        "commercial license is granted automatically by this repository",
        "safety is guaranteed by this checkpoint",
        "production deployment is approved by this checkpoint",
    ]
    combined = "\n".join([readme, doc, adr, issue]).lower()
    for claim in forbidden_positive_claims:
        require(claim not in combined, f"Forbidden v0.6.7 observation normalization claim found: {claim}")

    require("Add v0.6.7 observation normalization and diagnostic fidelity risk review" in adr, "ADR must record v0.6.7 decision")
    require("Completed by v0.6.7 candidate" in issue, "Issue must record v0.6.7 completion status")
    require("## v0.6.7 - Observation normalization and diagnostic fidelity risk review" in changelog, "CHANGELOG must include v0.6.7")
    require("## v0.6.7 Observation normalization and diagnostic fidelity risk review" in roadmap, "ROADMAP must include v0.6.7")
    require("test_v067_observation_normalization_diagnostic_fidelity_risk_review.py" in run_all, "run_all must include v0.6.7 observation normalization test")

    print("v0.6.7 observation normalization and diagnostic fidelity risk review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
