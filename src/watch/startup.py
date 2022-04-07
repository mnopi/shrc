# coding=utf-8
"""
Startup Module
"""
__all__ = ()

from pyrc import IS_REPL

if IS_REPL:
    __all__ += (
        "pywatchman",
    )

    import pywatchman
