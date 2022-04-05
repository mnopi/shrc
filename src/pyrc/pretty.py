# coding=utf-8
"""
Pretty Printing and Console Module.

`IPython Configuration File <https://ipython.readthedocs.io/en/stable/config/intro.html>`_
~/.ipython/profile_default/startup/00-console.py
~/.ipython/profile_default/ipython_config.py

``c.InteractiveShellApp.extensions.extend(['autoreload', 'rich'])``
or include
``%load_ext rich``

Test with: `print("[italic red]Hello[/italic red] World!", locals())`

`Rich Inspect <https://rich.readthedocs.io/en/stable/traceback.html?highlight=sitecustomize>`_

``rich.traceback.install(suppress=[click])``

To see the spinners: `python -m rich.spinner`
To print json from the comamand line: `python -m rich.json cats.json`

`Rich Console <https://rich.readthedocs.io/en/stable/console.html>`_

Input: `console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")`

Examples:
    >>> import time
    >>> from rich.json import JSON
    >>>
    >>> with console.status("Working...", spinner="material"):  # doctest: +SKIP
    ...    time.sleep(2)
    >>>
    >>> console.log(JSON('["foo", "bar"]'))  # doctest: +SKIP
    >>>
    >>> print_json('["foo", "bar"]')  # doctest: +SKIP
    >>>
    >>> console.log("Hello, World!")  # doctest: +SKIP
    >>> console.print([1, 2, 3])  # doctest: +SKIP
    >>> console.print("[blue underline]Looks like a link")  # doctest: +SKIP
    >>> console.print(locals())  # doctest: +SKIP
    >>> console.print("FOO", style="white on blue")  # doctest: +SKIP
    >>>
    >>> blue_console = Console(style="white on blue")  # doctest: +SKIP
    >>> blue_console.print("I'm blue. Da ba dee da ba di.")  # doctest: +SKIP
    >>>
    >>> console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")  # doctest: +SKIP
"""
__all__ = (
    'IS_IPYTHON',
    'is_terminal',
    'print',
    'print_json',
    'Console',
    'console',
    'rinspect',
    'rich_inspect',
    'ic',
    'icc',
)
import os
import sys
from typing import Any, Optional

if os.getcwd() not in sys.path:
    sys.path = [os.getcwd()] + sys.path


def is_terminal(self=None) -> bool:
    """
    Patch of :data:``rich.Console.is_terminal`` for PyCharm.

    Check if the console is writing to a terminal.

    Returns:
        bool: True if the console writing to a device capable of
        understanding terminal codes, otherwise False.
    """
    if hasattr(self, "_force_terminal"):
        if self._force_terminal is not None:
            return self._force_terminal
    try:
        return IS_REPL or (hasattr(self, "file") and hasattr(self.file, "isatty") and self.file.isatty())
    except ValueError:
        # in some situation (at the end of a pytest run for example) isatty() can raise
        # ValueError: I/O operation on closed file
        # return False because we aren't in a terminal anymore
        return False


try:
    import rich  # type: ignore[name-defined]
    import rich.console  # type: ignore[name-defined]
    import rich.pretty  # type: ignore[name-defined]
    import rich.traceback  # type: ignore[name-defined]
    # noinspection PyShadowingBuiltins
    from rich import print as print  # type: ignore[name-defined]
    from rich import print_json as print_json  # type: ignore[name-defined]

    setattr(rich.console.Console, "is_terminal", is_terminal)


      # type: ignore[name-defined]
    console = Console()

    # rprint = console.print
    rich.pretty.install(expand_all=True)
    rich.traceback.install(show_locals=True)
except ModuleNotFoundError:
    print_json = print
    Console = object
    console = Console()
    rinspect = print
    rich_inspect = print

try:
    from icecream import IceCreamDebugger  # type: ignore[name-defined]
    ic = IceCreamDebugger(prefix=str())
    icc = IceCreamDebugger(prefix=str(), includeContext=True)
except ModuleNotFoundError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa
    ics = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

try:
    from ghapi.all import GhApi  # type: ignore[name-defined]
    ghapi = GhApi()
except ModuleNotFoundError:
    ghapi = object()


if IS_IPYTHON:
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)
    '%rehashx'
    '%load_ext rich'
