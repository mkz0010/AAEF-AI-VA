from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


class SanitizerError(ValueError):
    pass


DEFAULT_REDACTION_POLICY_PATH = Path("prototypes/tool-gateway/redaction_policy/policy.json")


DEFAULT_REPLACEMENTS = {
    "authorization_header": "[REDACTED_AUTHORIZATION_HEADER]",
    "cookie_header": "[REDACTED_COOKIE_HEADER]",
    "set_cookie_header": "[REDACTED_SET_COOKIE_HEADER]",
    "bearer_token": "[REDACTED_BEARER_TOKEN]",
    "api_key": "[REDACTED_API_KEY]",
    "csrf_token": "[REDACTED_CSRF_TOKEN]",
    "session_id": "[REDACTED_SESSION_ID]",
    "password": "[REDACTED_PASSWORD]",
    "private_ip": "[REDACTED_PRIVATE_IP]",
}


DEFAULT_PATTERNS = [
    {
        "name": "authorization_header",
        "category": "credential_or_token",
        "pattern": r"(?i)Authorization:\s*[^\r\n]+",
        "replacement": DEFAULT_REPLACEMENTS["authorization_header"],
    },
    {
        "name": "cookie_header",
        "category": "session_material",
        "pattern": r"(?i)Cookie:\s*[^\r\n]+",
        "replacement": DEFAULT_REPLACEMENTS["cookie_header"],
    },
    {
        "name": "set_cookie_header",
        "category": "session_material",
        "pattern": r"(?i)Set-Cookie:\s*[^\r\n]+",
        "replacement": DEFAULT_REPLACEMENTS["set_cookie_header"],
    },
    {
        "name": "bearer_token",
        "category": "credential_or_token",
        "pattern": r"(?i)Bearer\s+[A-Za-z0-9._~+/=-]{12,}",
        "replacement": DEFAULT_REPLACEMENTS["bearer_token"],
    },
    {
        "name": "api_key",
        "category": "credential_or_token",
        "pattern": r"(?i)(api[_-]?key|x-api-key|apikey)\s*[:=]\s*[A-Za-z0-9._~+/=-]{8,}",
        "replacement": DEFAULT_REPLACEMENTS["api_key"],
    },
    {
        "name": "csrf_token",
        "category": "session_material",
        "pattern": r"(?i)(csrf[_-]?token|xsrf[_-]?token)\s*[:=]\s*[A-Za-z0-9._~+/=-]{8,}",
        "replacement": DEFAULT_REPLACEMENTS["csrf_token"],
    },
    {
        "name": "session_id",
        "category": "session_material",
        "pattern": r"(?i)(sessionid|session_id|sid)\s*[:=]\s*[A-Za-z0-9._~+/=-]{8,}",
        "replacement": DEFAULT_REPLACEMENTS["session_id"],
    },
    {
        "name": "password",
        "category": "credential_or_token",
        "pattern": r"(?i)(password|passwd|pwd)\s*[:=]\s*[^&\s\r\n]+",
        "replacement": DEFAULT_REPLACEMENTS["password"],
    },
    {
        "name": "private_ip",
        "category": "internal_network",
        "pattern": r"\b(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3})\b",
        "replacement": DEFAULT_REPLACEMENTS["private_ip"],
    },
]


def load_default_redaction_policy() -> dict[str, Any]:
    if DEFAULT_REDACTION_POLICY_PATH.exists():
        return json.loads(DEFAULT_REDACTION_POLICY_PATH.read_text(encoding="utf-8"))
    return {"policy_version": "builtin-default", "patterns": DEFAULT_PATTERNS}


def sanitize_text(text: str, policy: dict[str, Any] | None = None) -> tuple[str, list[dict[str, Any]]]:
    policy_data = policy if policy is not None else load_default_redaction_policy()
    redactions: list[dict[str, Any]] = []
    sanitized = text

    for rule in policy_data.get("patterns", DEFAULT_PATTERNS):
        pattern = rule["pattern"]
        replacement = rule["replacement"]
        matches = re.findall(pattern, sanitized)
        if matches:
            sanitized, count = re.subn(pattern, replacement, sanitized)
            redactions.append(
                {
                    "rule": rule["name"],
                    "category": rule.get("category", "uncategorized"),
                    "replacement": replacement,
                    "occurrences": count,
                }
            )

    return sanitized, redactions


def sanitize_value(value: Any, policy: dict[str, Any] | None = None) -> tuple[Any, list[dict[str, Any]]]:
    if isinstance(value, str):
        return sanitize_text(value, policy=policy)

    if isinstance(value, list):
        sanitized_list = []
        redactions: list[dict[str, Any]] = []
        for item in value:
            sanitized_item, item_redactions = sanitize_value(item, policy=policy)
            sanitized_list.append(sanitized_item)
            redactions.extend(item_redactions)
        return sanitized_list, redactions

    if isinstance(value, dict):
        sanitized_dict = {}
        redactions: list[dict[str, Any]] = []
        for key, item in value.items():
            # Preserve keys for structure, sanitize values.
            sanitized_item, item_redactions = sanitize_value(item, policy=policy)
            sanitized_dict[key] = sanitized_item
            redactions.extend(item_redactions)
        return sanitized_dict, redactions

    return value, []


def merge_redaction_counts(redactions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[tuple[str, str, str], int] = {}
    for item in redactions:
        key = (item["rule"], item["category"], item["replacement"])
        merged[key] = merged.get(key, 0) + int(item["occurrences"])

    return [
        {
            "rule": rule,
            "category": category,
            "replacement": replacement,
            "occurrences": occurrences,
        }
        for (rule, category, replacement), occurrences in sorted(merged.items())
    ]


def sanitize_raw_artifact(
    raw_artifact: dict[str, Any],
    *,
    raw_artifact_ref: str,
    sanitized_artifact_ref: str,
    policy: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not raw_artifact_ref.startswith("private-not-in-git/"):
        raise SanitizerError("raw_artifact_ref must point to ignored/private path")

    if not sanitized_artifact_ref.startswith("private-not-in-git/"):
        raise SanitizerError("sanitized_artifact_ref must point to ignored/private path")

    sanitized_content, redactions = sanitize_value(raw_artifact, policy=policy)
    summary = merge_redaction_counts(redactions)

    artifact = {
        "sanitizer_status": "completed",
        "sanitizer_policy_version": (policy or load_default_redaction_policy()).get("policy_version", "unknown"),
        "raw_artifact_ref": raw_artifact_ref,
        "sanitized_artifact_ref": sanitized_artifact_ref,
        "secret_exposed_to_ai": False,
        "ai_visible_allowed": True,
        "redaction_count": sum(item["occurrences"] for item in summary),
        "redaction_summary": summary,
        "sanitized_content": sanitized_content,
    }

    validate_sanitized_artifact(artifact)
    return artifact


def validate_sanitized_artifact(artifact: dict[str, Any]) -> None:
    if artifact.get("sanitizer_status") != "completed":
        raise SanitizerError("sanitizer_status must be completed")

    if artifact.get("secret_exposed_to_ai") is not False:
        raise SanitizerError("secret_exposed_to_ai must be false")

    if artifact.get("ai_visible_allowed") is not True:
        raise SanitizerError("ai_visible_allowed must be true only after sanitizer completion")

    text = json.dumps(artifact.get("sanitized_content", {}), ensure_ascii=False)

    forbidden_literals = [
        "Authorization: Bearer",
        "Cookie:",
        "Set-Cookie:",
        "password=",
        "password:",
        "csrf_token=",
        "sessionid=",
        "192.168.",
        "10.0.",
    ]

    for literal in forbidden_literals:
        if literal.lower() in text.lower():
            raise SanitizerError(f"sanitized artifact still contains forbidden literal: {literal}")
