from __future__ import annotations

import json
from typing import Any

from sanitizer import validate_sanitized_artifact


class FindingCandidateError(ValueError):
    pass


REQUIRED_CANDIDATE_FIELDS = [
    "finding_candidate_id",
    "finding_candidate_status",
    "source_type",
    "source_sanitized_artifact_ref",
    "tool",
    "operation",
    "target_id",
    "scope_id",
    "title",
    "summary",
    "initial_severity",
    "initial_confidence",
    "ai_visible_allowed",
    "secret_exposed_to_ai",
    "requires_human_review",
    "report_ready",
    "evidence_required",
    "redaction_summary",
    "candidate_observations",
    "limitations",
]


FORBIDDEN_LITERAL_FRAGMENTS = [
    "Authorization: Bearer",
    "Cookie:",
    "Set-Cookie:",
    "password=",
    "password:",
    "csrf_token=",
    "sessionid=",
    "api_key=",
    "x-api-key",
    "192.168.",
    "10.0.",
]


def _safe_id_part(value: str) -> str:
    return value.replace("/", "-").replace(":", "-").replace("_", "-")


def _redaction_categories(redaction_summary: list[dict[str, Any]]) -> list[str]:
    return sorted({str(item.get("category", "uncategorized")) for item in redaction_summary})


def build_finding_candidate_from_sanitized_artifact(
    sanitized_artifact: dict[str, Any],
    *,
    tool: str,
    operation: str,
    target_id: str,
    scope_id: str,
    evidence_id: str | None = None,
) -> dict[str, Any]:
    validate_sanitized_artifact(sanitized_artifact)

    redaction_summary = list(sanitized_artifact.get("redaction_summary", []))
    categories = _redaction_categories(redaction_summary)
    candidate_id_parts = [
        "finding-candidate",
        _safe_id_part(tool),
        _safe_id_part(operation),
        _safe_id_part(target_id),
    ]
    finding_candidate_id = "-".join(candidate_id_parts)

    observations = [
        {
            "observation_type": "sanitized_artifact_available",
            "description": "A sanitized tool artifact is available for review.",
            "source_ref": sanitized_artifact["sanitized_artifact_ref"],
        },
        {
            "observation_type": "redaction_applied",
            "description": (
                "Sensitive values were redacted before AI-visible use."
                if sanitized_artifact.get("redaction_count", 0) > 0
                else "No redactions were reported by the sanitizer."
            ),
            "redaction_count": sanitized_artifact.get("redaction_count", 0),
            "redaction_categories": categories,
        },
    ]

    candidate = {
        "finding_candidate_id": finding_candidate_id,
        "finding_candidate_status": "candidate_requires_human_review",
        "source_type": "sanitized_adapter_artifact",
        "source_sanitized_artifact_ref": sanitized_artifact["sanitized_artifact_ref"],
        "tool": tool,
        "operation": operation,
        "target_id": target_id,
        "scope_id": scope_id,
        "evidence_id": evidence_id,
        "title": "Sanitized tool observation requires human review",
        "summary": (
            "A sanitized adapter artifact was converted into a finding candidate. "
            "This is not a confirmed vulnerability and must be reviewed by a human."
        ),
        "initial_severity": "informational",
        "initial_confidence": "low",
        "ai_visible_allowed": True,
        "secret_exposed_to_ai": False,
        "requires_human_review": True,
        "report_ready": False,
        "evidence_required": True,
        "sanitizer_policy_version": sanitized_artifact.get("sanitizer_policy_version"),
        "redaction_summary": redaction_summary,
        "candidate_observations": observations,
        "limitations": [
            "This candidate is derived from sanitized artifact metadata and summaries only.",
            "It is not a confirmed vulnerability.",
            "It must not be included in a customer-facing report without human validation.",
            "Raw adapter output is not embedded in this candidate.",
        ],
    }

    validate_finding_candidate(candidate)
    return candidate


def validate_finding_candidate(candidate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_CANDIDATE_FIELDS if field not in candidate]
    if missing:
        raise FindingCandidateError(f"finding candidate missing required fields: {missing}")

    if candidate.get("finding_candidate_status") != "candidate_requires_human_review":
        raise FindingCandidateError("finding candidate must require human review in current MVP")

    if candidate.get("ai_visible_allowed") is not True:
        raise FindingCandidateError("finding candidate must be AI-visible only after sanitizer-derived construction")

    if candidate.get("secret_exposed_to_ai") is not False:
        raise FindingCandidateError("finding candidate must keep secret_exposed_to_ai=false")

    if candidate.get("requires_human_review") is not True:
        raise FindingCandidateError("finding candidate must require human review")

    if candidate.get("report_ready") is not False:
        raise FindingCandidateError("finding candidate must not be report-ready in current MVP")

    if candidate.get("evidence_required") is not True:
        raise FindingCandidateError("finding candidate must require evidence")

    source_ref = candidate.get("source_sanitized_artifact_ref")
    if not isinstance(source_ref, str) or not source_ref.startswith("private-not-in-git/"):
        raise FindingCandidateError("source_sanitized_artifact_ref must point to ignored/private path")

    if "raw_artifact_ref" in candidate:
        raise FindingCandidateError("finding candidate must not embed raw_artifact_ref")

    serialized = json.dumps(candidate, ensure_ascii=False)
    for fragment in FORBIDDEN_LITERAL_FRAGMENTS:
        if fragment.lower() in serialized.lower():
            raise FindingCandidateError(f"finding candidate contains forbidden literal: {fragment}")
