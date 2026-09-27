"""Capability protocols — interface placeholders (depth A)."""

from __future__ import annotations

from typing import Any, Callable, Protocol


class HookBus(Protocol):
    def register_hook(self, event: str, handler: Callable[..., Any]) -> None: ...
    def emit(self, event: str, payload: Any) -> Any: ...


class ToolRegistry(Protocol):
    def invoke_tool(self, name: str, args: dict[str, Any]) -> Any: ...


class PluginManager(Protocol):
    def load_plugin(self, manifest: Any) -> str: ...
    def unload_plugin(self, plugin_id: str) -> None: ...
