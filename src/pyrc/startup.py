# coding=utf-8
"""
Startup Module

    Performs the following always when imported:
        - Aliases :func:`rich.inspect` as :func:`rich_inspect` for :class:`rich._inspect.Inspect`
        - Replaces :builtin:`print` with :rich:`rich.print`.
        - Imports: :func:`rich.print_json`
        - Patches :class:`rich.console.Console` to detect PyCharm console and other consoles.
        - Installs: :class:`rich.pretty.Pretty`.
        - Installs :class:`rich.traceback.Traceback`.
        - Installs :class:`rich.inspect.Inspect`.

    and the following if running in a console:
        - Imports modules used in package
        - Set environment vars in :mod:``pyrc.env``
        - Imports :class:`ghapi.all.GhApi` and initializes it with `GITHUB_TOKEN` environment variable.
        - Preprends current working dir to :obj:`sys.path`

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


References:
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
"""
__all__ = (
    "rich_inspect",
    "print",
    "print_json",

    "Console",
    "console",
)
import rich.pretty
import rich.traceback
from rich import inspect as rich_inspect
from rich import print as print
from rich import print_json as print_json

from .utils import is_terminal
from .variables import IS_IPYTHON
from .variables import IS_REPL

setattr(rich.console.Console, "is_terminal", is_terminal)
Console = rich.console.Console
console: Console = rich.console.Console()

if IS_REPL:
    __all__ += (
        "aiohttp",
        "asyncio",
        "dataclasses",
        "getpass",
        "contextlib",
        "os",
        "pathlib",
        "platform",
        "pwd",
        "re",
        "subprocess",
        "sys",
        "tarfile",
        "tempfile",

        'dataclass',
        'Path',
        "CompletedProcess",

        "bs4",
        "click",
        "requests",
        "typer",

        'GhApi',
        "VersionInfo",
    )

    import aiohttp as aiohttp
    import asyncio as asyncio
    import contextlib as contextlib
    import dataclasses as dataclasses
    import getpass as getpass
    import os as os
    import pathlib as pathlib
    import platform as platform
    import pwd as pwd
    import re as re
    import subprocess as subprocess
    import sys as sys
    import tarfile as tarfile
    import tempfile as tempfile

    from dataclasses import dataclass as dataclass
    from pathlib import Path as Path
    from subprocess import CompletedProcess as CompletedProcess

    import bs4 as bs4
    import click as click
    import requests as requests
    import typer as typer

    from ghapi.all import GhApi as GhApi
    from semver import VersionInfo as VersionInfo

    from .env import *

    environment()

    ghpai = GhApi(token=GITHUB_TOKEN or GH_TOKEN or TOKEN)

    if os.getcwd() not in sys.path:
        sys.path = [os.getcwd()] + sys.path

if IS_IPYTHON:
    __all__ += (
        "warnings",
    )

    import warnings as warnings
    warnings.filterwarnings("ignore", category=UserWarning)
    '%rehashx'
    '%load_ext rich'

rich.pretty.install(expand_all=True)
rich.traceback.install(show_locals=True)

