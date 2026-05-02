from __future__ import annotations

from .base import BaseToolAdapter
from .browser_adapter import BrowserAdapter
from .nmap_adapter import NmapAdapter
from .nuclei_adapter import NucleiAdapter
from .zap_adapter import ZapAdapter


_REGISTRY: dict[str, BaseToolAdapter] = {
    "zap": ZapAdapter(),
    "nmap": NmapAdapter(),
    "nuclei": NucleiAdapter(),
    "browser": BrowserAdapter(),
}


def get_adapter(tool_name: str) -> BaseToolAdapter:
    if tool_name not in _REGISTRY:
        raise KeyError(f"No adapter registered for tool: {tool_name}")
    return _REGISTRY[tool_name]


def registered_adapter_names() -> list[str]:
    return sorted(_REGISTRY.keys())
