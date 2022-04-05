# coding=utf-8
"""
Constants and Variables Module
"""
__all__ = (
    "IS_IPYTHON",
    "IS_REPL",
)
import sys

"""True if running on iPython when imported, otherwise False"""
IS_IPYTHON = "__IPYTHON__" in globals()["__builtins__"]

"""True if running on REPL, otherwise False."""
IS_REPL = IS_IPYTHON or hasattr(sys, 'ps1') or 'pythonconsole' in sys.stdout.__class__.__module__
