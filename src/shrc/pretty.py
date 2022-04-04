# coding=utf-8
"""
Pretty Printing and Console Module.

`IPython Configuration File <https://ipython.readthedocs.io/en/stable/config/intro.html>`_
~/.ipython/profile_default/startup/00-console.py
~/.ipython/profile_default/ipython_config.py

``c.InteractiveShellApp.extensions.extend(['autoreload', 'rich'])``
or include
``%load_ext rich``

`Rich Inspect <https://rich.readthedocs.io/en/stable/traceback.html?highlight=sitecustomize>`_

``rich.traceback.install(suppress=[click])``
To see the spinners: `python -m rich.spinner`
To print json from the comamand line: `python -m rich.json cats.json`

`Rich Console <https://rich.readthedocs.io/en/stable/console.html>`_

Examples:
    >>> import time
    >>> from rich.json import JSON
    >>>
    >>> with console.status("Working...", spinner="material"):
    ...    time.sleep(10)
    >>>
    >>> console.log(JSON('["foo", "bar"]'))
    >>> print_json('["foo", "bar"]')
    >>>
    >>> console.log("Hello, World!")
    >>> console.print([1, 2, 3])
    >>> console.print("[blue underline]Looks like a link")
    >>> console.print(locals())
    >>> console.print("FOO", style="white on blue")
    >>>
    >>> blue_console = Console(style="white on blue")
    >>> blue_console.print("I'm blue. Da ba dee da ba di.")
    >>>
    >>> console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")
"""
__all__ = (
    'IS_IPYTHON',
    'is_terminal',
    'print',
    'print_json',
    'Console',
    'console',
    'rinspect',
    'rich_inspect'
)
import os
import sys
from typing import Any, Optional

sys.path.extend(os.getcwd())

IS_IPYTHON = hasattr(__builtins__, '__IPYTHON__')


def is_terminal(self=None):
    """Patch for PyCharm.

    Returns:
        bool: True if the console writing to a device capable of
        understanding terminal codes, otherwise False.
    """
    if hasattr(self, "_force_terminal"):
        if self._force_terminal is not None:
            return self._force_terminal
    try:
        return hasattr(sys, 'ps1') or \
               IS_IPYTHON \
               or sys.argv[0] == '' \
               or hasattr(self, "file") and hasattr(self.file, "isatty") and self.file.satty() \
               or 'pythonconsole' in sys.stdout.__class__.__module__
    except ValueError:
        # in some situation (at the end of a pytest run for example) isatty() can raise
        # ValueError: I/O operation on closed file
        # return False because we aren't in a terminal anymore
        return False


try:
    import rich
    import rich.console
    import rich.pretty
    import rich.traceback
    # noinspection PyShadowingBuiltins
    from rich import print as print
    from rich import print_json as print_json
    from functools import partial

    setattr(rich.console.Console, "is_terminal", is_terminal)

    from rich.console import Console as Console
    console = Console()

    def rinspect(obj: Any, *, _console: Optional[Console] = None, title: Optional[str] = None,
                 _help: bool = False, methods: bool = True, docs: bool = False, private: bool = True,
                 dunder: bool = False, sort: bool = True, _all: bool = False, value: bool = True,) -> None:
        """
        :meth:`rich.inspect` wrapper, changing defaults to: ``docs=False, methods=True, private=True``.

        Inspect any Python object.

        * inspect(<OBJECT>) to see summarized info.
        * inspect(<OBJECT>, methods=True) to see methods.
        * inspect(<OBJECT>, help=True) to see full (non-abbreviated) help.
        * inspect(<OBJECT>, private=True) to see private attributes (single underscore).
        * inspect(<OBJECT>, dunder=True) to see attributes beginning with double underscore.
        * inspect(<OBJECT>, all=True) to see all attributes.

        Args:
            obj (Any): An object to inspect.
            _console (Console, optional): Rich Console.
            title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
            _help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
            methods (bool, optional): Enable inspection of callables. Defaults to False.
            docs (bool, optional): Also render doc strings. Defaults to True.
            private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
            dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
            sort (bool, optional): Sort attributes alphabetically. Defaults to True.
            _all (bool, optional): Show all attributes. Defaults to False.
            value (bool, optional): Pretty print value. Defaults to True.
        """
        rich.inspect(obj=obj, console=_console, title=title, help=_help, methods=methods, docs=docs, private=private,
                     dunder=dunder, sort=sort, all=_all, value=value)
    rich_inspect = rich.inspect
    # rprint = console.print
    rich.pretty.install(expand_all=True)
    rich.traceback.install(show_locals=True)

except ModuleNotFoundError:
    pass

try:
    from ghapi.all import GhApi  # type: ignore[name-defined]

    ghapi = GhApi()
except ModuleNotFoundError:
    pass

if IS_IPYTHON:
    '%rehashx'
    '%load_ext rich'
