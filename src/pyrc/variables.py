# coding=utf-8
"""
Constants and Variables Module
"""
__all__ = (
    "IPYTHON",
    "IS_REPL",
)
import sys


try:
    IPYTHON = get_ipython()  # type: ignore[name-defined]
    """Global :class:``IPython.core.interactiveshell.InteractiveShell`` instance,
     None if no InteractiveShell instance is registered."""
except NameError:
    IPYTHON = None

IS_REPL = bool(IPYTHON) or hasattr(sys, 'ps1') or 'pythonconsole' in sys.stdout.__class__.__module__
"""True if running on REPL, otherwise False."""
