# coding=utf-8
"""
Startup Module
"""
__all__ = ()

from shrc import IS_REPL

if IS_REPL:
    __all__ += (
        "pywatchman",
    )

    import pywatchman
