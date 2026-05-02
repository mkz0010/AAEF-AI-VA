from __future__ import annotations

import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from scope_registry import ScopeRegistryError, load_default_scope_registry, resolve_target_binding


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_scope_error(*, target_id: str, scope_id: str, tool: str, operation: str, registry: dict | None = None) -> None:
    try:
        resolve_target_binding(target_id, scope_id, tool, operation, registry=registry)
    except ScopeRegistryError:
        return
    raise AssertionError("expected scope registry error")


def main() -> int:
    registry = load_default_scope_registry()

    binding = resolve_target_binding(
        "webapp-demo-001",
        "scope-demo-001",
        "zap",
        "authenticated_crawl",
        registry=registry,
    )

    assert_true(binding["target_id"] == "webapp-demo-001", "target_id mismatch")
    assert_true(binding["scope_id"] == "scope-demo-001", "scope_id mismatch")
    assert_true(binding["approved_for_tool"] is True, "target should be approved for tool")
    assert_true(binding["raw_destination_included"] is False, "raw destination must not be included")
    assert_true(binding["network_destination_ref"].startswith("scope-registry://"), "destination must be registry ref")

    expect_scope_error(
        target_id="missing-target",
        scope_id="scope-demo-001",
        tool="zap",
        operation="authenticated_crawl",
        registry=registry,
    )

    expect_scope_error(
        target_id="webapp-demo-001",
        scope_id="other-scope",
        tool="zap",
        operation="authenticated_crawl",
        registry=registry,
    )

    expect_scope_error(
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        tool="nmap",
        operation="authenticated_crawl",
        registry=registry,
    )

    expect_scope_error(
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        tool="zap",
        operation="safe_template_scan",
        registry=registry,
    )

    expect_scope_error(
        target_id="external-demo-001",
        scope_id="scope-demo-001",
        tool="nuclei",
        operation="safe_template_scan",
        registry=registry,
    )

    bad = copy.deepcopy(registry)
    bad["targets"]["webapp-demo-001"]["raw_destination_included"] = True
    expect_scope_error(
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        tool="zap",
        operation="authenticated_crawl",
        registry=bad,
    )

    print("Scope registry tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
