from __future__ import annotations

from typing import Any


def artifact_refs(tool: str, execution_id: str) -> dict[str, str]:
    return {
        "raw_artifact_ref": f"private-not-in-git/raw-artifacts/{tool}/{execution_id}.json",
        "sanitized_artifact_ref": f"private-not-in-git/prototype-runs/{execution_id}/sanitized-result.json",
    }


def make_plan_id(tool: str, operation: str, target_id: str) -> str:
    safe_target = target_id.replace("/", "-").replace(":", "-")
    return f"plan-{tool}-{operation}-{safe_target}"


def require_no_secret_material(plan: dict[str, Any]) -> None:
    if plan.get("secret_material_included") is not False:
        raise ValueError("command plan must not include secret material")
    for key in ["username", "password", "api_key", "secret", "cookie", "authorization"]:
        if key in plan:
            raise ValueError(f"command plan contains forbidden secret-like field: {key}")
