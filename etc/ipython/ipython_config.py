# coding=utf-8
"""
Shrc Ipython_config Module
"""
c.InteractiveShellApp.extensions = ["asynciomagic", "autoreload", "restmagic", "rich"]  # type: ignore[name-defined]
c.InteractiveShellApp.exec_lines = ['%autoreload 2']  # type: ignore[name-defined]
c.InteractiveShell.autoindent = True  # type: ignore[name-defined]
c.InteractiveShell.automagic = True    # type: ignore[name-defined]
c.InteractiveShellApp.exec_lines = [ "import asyncio", "%rehashx", ]  # type: ignore[name-defined]
c.TerminalIPythonApp.display_banner = False  # type: ignore[name-defined]
c.TerminalInteractiveShell.confirm_exit = False  # type: ignore[name-defined]
