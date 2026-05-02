from __future__ import annotations

from typing import Any

from .base import BaseToolAdapter, ToolAdapterError


class ZapAdapter(BaseToolAdapter):
    tool_name = "zap"
    supported_operations = {"passive_scan", "authenticated_crawl"}

    def execute(
        self,
        request: dict[str, Any],
        decision: dict[str, Any],
        credential_resolved_by: str | None,
    ) -> dict[str, Any]:
        if decision["operation"] not in self.supported_operations:
            raise ToolAdapterError(f"Unsupported ZAP operation: {decision['operation']}")
        return self._mock_result(request, decision, credential_resolved_by)
