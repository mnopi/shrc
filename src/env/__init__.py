# coding=utf-8
"""
pyrc environment package
"""
import os
import ipaddress
import sys
import urllib.parse

from ipaddress import IPv4Address
from ipaddress import IPv6Address
from pathlib import Path
from urllib.parse import ParseResult

from .default import *
from .noset import *
from .secrets import *
from .system import *

from . import default
from . import noset
from . import secrets
from . import system

__all__ = \
    default.__all__ + \
    noset.__all__ + \
    secrets.__all__ + \
    system.__all__ + \
    ("environment",)


def environment(variable: bool | str = None) -> \
        bool | Path | ParseResult | IPv4Address | IPv6Address | int | str | None:
    """
    Parses variable from environment or parses and sets caller globals in :mod:``pyrc.env``
    from environment variables if they are not set

    If called with True, will overwirte again the globals associated to the environment variables

    Parses:
        - bool: 1, 0, True, False, yes, no, on, off (case insensitive)
        - int: integer only numeric characters but 1 and 0 or SUDO_UID or SUDO_GID
        - ipaddress: ipv4/ipv6 address
        - url: if "//" or "@" is found it will be parsed as url
        - path: start with / or ~ or .
        - others as string

    Arguments:
        variable: variable name to parse from environment, True to force reading again,
            or None to parse all in :mod:``pyrc.env`` (default: None)

    Examples:
        >>> cwd = Path.cwd()
        >>> assert USER == NOSET
        >>> assert PWD == NOSET
        >>> environment()
        >>> assert USER == os.environ.get('USER')
        >>> assert PWD == cwd.absolute()
        >>>
        >>> tmp = Path('/tmp').resolve()
        >>> os.environ['PWD'] = str(tmp)
        >>> os.chdir(tmp)
        >>> environment()
        >>> assert PWD == cwd.absolute()
        >>> environment(True)
        >>> assert PWD == tmp
        >>>
        >>> os.environ['FOO'] = '1'
        >>> assert environment("FOO") is True
        >>>
        >>> os.environ['FOO'] = '0'
        >>> assert environment("FOO") is False
        >>>
        >>> os.environ['FOO'] = 'TrUe'
        >>> assert environment("FOO") is True
        >>>
        >>> os.environ['FOO'] = 'OFF'
        >>> assert environment("FOO") is False
        >>>
        >>> os.environ['FOO'] = '~/foo'
        >>> assert environment("FOO") == Path('~/foo')
        >>>
        >>> os.environ['FOO'] = '/foo'
        >>> assert environment("FOO") == Path('/foo')
        >>>
        >>> os.environ['FOO'] = './foo'
        >>> assert environment("FOO") == Path('./foo')
        >>>
        >>> os.environ['FOO'] = './foo'
        >>> assert environment("FOO") == Path('./foo')
        >>>
        >>> v = "https://github.com"
        >>> os.environ['FOO'] = v
        >>> assert environment("FOO").geturl() == v
        >>>
        >>> v = "git@github.com"
        >>> os.environ['FOO'] = v
        >>> assert environment("FOO").geturl() == v
        >>>
        >>> v = "0.0.0.0"
        >>> os.environ['FOO'] = v
        >>> assert environment("FOO").exploded == v
        >>>
        >>> os.environ['FOO'] = "::1"
        >>> assert environment("FOO").exploded.endswith(":0001")
        >>>
        >>> v = "2"
        >>> os.environ['FOO'] = v
        >>> assert environment("FOO") == int(v)
        >>>
        >>> v = "2.0"
        >>> os.environ['FOO'] = v
        >>> assert environment("FOO") == v
        >>>
        >>> del os.environ['FOO']
        >>> assert environment("FOO") is None

    Returns:
        None
    """
    def parse(var: str) -> bool | Path | ParseResult | IPv4Address | IPv6Address | int | str | None:
        last = None
        if value := os.environ.get(var):
            if var in ("SUDO_UID", "SUDO_GID"):
                return int(value)
            elif value.lower() in ['1', 'true', 'yes', 'on']:
                return True
            elif value.lower() in ['0', 'false', 'no', 'off']:
                value = False
            elif value[0] in ['/', '~', '.'] and var != "PATH":
                value = Path(value)
            elif '://' in value or '@' in value:
                value = urllib.parse.urlparse(value)
            else:
                try:
                    last = ipaddress.ip_address(value)
                except ValueError:
                    if value.isnumeric():
                        last = int(value)
        return last or value

    force = variable

    if variable and force is not True:
        return parse(variable)

    data = data if (data := sys._getframe(1).f_globals).get(__all__[0]) else globals()
    data = sys._getframe(1).f_globals

    for variable in sorted(set(__all__)):
        if variable.lower() == NOSET.name or variable == environment.__name__:
            continue

        if data[variable] != NOSET and force is not True:
            return

        data[variable] = parse(variable)
