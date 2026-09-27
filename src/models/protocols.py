"""Model protocols — interface placeholders (depth A)."""

from __future__ import annotations

from typing import Any, Protocol


class ModelAdapter(Protocol):
    def complete(self, request: Any) -> Any: ...


class ProviderRegistry(Protocol):
    def list_providers(self) -> list[str]: ...
