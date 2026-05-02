from __future__ import annotations

from typing import Any


class ToolAdapterError(RuntimeError):
    """Raised when a Tool Gateway adapter cannot handle a request."""


class BaseToolAdapter:
    tool_name: str = ""

    def execute(
        self,
        request: dict[str, Any],
        decision: dict[str, Any],
        credential_resolved_by: str | None,
    ) -> dict[str, Any]:
        raise NotImplementedError

    def _mock_result(
        self,
        request: dict[str, Any],
        decision: dict[str, Any],
        credential_resolved_by: str | None,
    ) -> dict[str, Any]:
        return {
            "adapter": self.tool_name,
            "mock_execution": True,
            "target_id": decision["target_id"],
            "scope_id": decision["scope_id"],
            "tool": decision["tool"],
            "operation": decision["operation"],
            "credential_ref_used": decision.get("credential_ref"),
            "credential_resolved_by": credential_resolved_by,
            "observation_summary": (
                f"Mock {self.tool_name} adapter accepted operation "
                f"{decision['operation']} for {decision['target_id']}."
            ),
        }
