from __future__ import annotations

from typing import Any

from .base import BaseToolAdapter, ToolAdapterError


class NmapAdapter(BaseToolAdapter):
    tool_name = "nmap"
    supported_operations = {"safe_port_discovery", "service_version_detection"}

    def execute(
        self,
        request: dict[str, Any],
        decision: dict[str, Any],
        credential_resolved_by: str | None,
    ) -> dict[str, Any]:
        if decision["operation"] not in self.supported_operations:
            raise ToolAdapterError(f"Unsupported Nmap operation: {decision['operation']}")
        return self._mock_result(request, decision, credential_resolved_by)
