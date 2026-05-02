from __future__ import annotations

from typing import Any

from .base import BaseToolAdapter, ToolAdapterError
from .command_plan import artifact_refs, make_plan_id, require_no_secret_material


class ZapAdapter(BaseToolAdapter):
    tool_name = "zap"
    supported_operations = {"passive_scan", "authenticated_crawl"}

    def build_command_plan(
        self,
        request: dict[str, Any],
        decision: dict[str, Any],
        credential_resolved_by: str | None,
    ) -> dict[str, Any]:
        if decision["operation"] not in self.supported_operations:
            raise ToolAdapterError(f"Unsupported ZAP operation: {decision['operation']}")

        execution_id = f"exec-{request['tool_action_request_id'].removeprefix('tar-')}"
        refs = artifact_refs("zap", execution_id)

        plan = {
            "plan_id": make_plan_id("zap", decision["operation"], decision["target_id"]),
            "execution_mode": "dry_run_plan_only",
            "external_process_execution": False,
            "adapter": "zap",
            "tool": "zap",
            "operation": decision["operation"],
            "target_id": decision["target_id"],
            "scope_id": decision["scope_id"],
            "credential_ref": decision.get("credential_ref"),
            "credential_resolved_by": credential_resolved_by,
            "secret_material_included": False,
            "approved_constraints": decision["constraints"],
            "planned_steps": [
                "Load approved target alias from scope registry.",
                "Create or select ZAP context for approved target.",
                "Apply authentication profile using credential_ref through Tool Gateway only.",
                "Run only the approved ZAP operation.",
                "Write raw ZAP output to ignored private artifact path.",
                "Pass raw output to Sanitizer / Normalizer before AI-visible use.",
            ],
            "artifact_refs": refs,
            "blocked_behaviors": [
                "No arbitrary command construction from AI text.",
                "No direct AI access to ZAP API.",
                "No raw credential exposure in command plan.",
                "No external discovery unless explicitly authorized.",
                "No destructive tests.",
            ],
        }
        require_no_secret_material(plan)
        return plan

    def execute(
        self,
        request: dict[str, Any],
        decision: dict[str, Any],
        credential_resolved_by: str | None,
    ) -> dict[str, Any]:
        if decision["operation"] not in self.supported_operations:
            raise ToolAdapterError(f"Unsupported ZAP operation: {decision['operation']}")

        command_plan = self.build_command_plan(request, decision, credential_resolved_by)
        result = self._mock_result(request, decision, credential_resolved_by)
        result["command_plan"] = command_plan
        return result
