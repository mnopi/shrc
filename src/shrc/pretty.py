# coding=utf-8
__all__ = (
)

try:
    from ghapi.all import GhApi  # type: ignore[name-defined]
    ghapi = GhApi()
except ModuleNotFoundError:
    ghapi = object()
