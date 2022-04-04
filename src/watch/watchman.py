# coding=utf-8
"""
WatchMan module.

Dataclass wrapper for :class:``pywatchman.client``.
"""
__all__ = ("WatchMan", )

from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Type
from typing import Union
from typing import Literal
import pywatchman
from pywatchman import Transport

TransportType = Union[
    pywatchman.Transport,
    pywatchman.CLIProcessTransport,
    pywatchman.UnixSocketTransport,
    Type[Transport],
    Literal["local", "cli"],
]


@dataclass
class WatchMan(pywatchman.client):
    """
    Dataclass wrapper for `pywatchman.client` to handles the communication
    with the watchman service.

    bser encoding for sockets and local:
https://earth.bsc.es/gitlab/wuruchi/autosubmitreact/-/tree/f065660f7d9c019f5c4e21fc7fdf7d6f8c903e6b/node_modules/bser

    Receive method gets everything from the socket, and it is marked as
    "unilateral" if subscription or log raised.

    Query method writes to the socket any CLI command (is not a query as in
    the CLI).
    Query blocks receiving "unilateral" but they are returned by the method
    when gets confirmation on the query.

    Writing to the socket activates the server.

    log-level = 2 makes a raise so logs would be accesible with getLog method.

    For syncing, the "fsmonitor" of git should be used, so it would be faster.
    There is a default hook in perl and
    https://githubhelp.com/jgavris/rs-git-fsmonitor.
    """

    """Env var: WATCHMAN_SOCK, or
    `watchman --output-encoding=bser get-sockname"""
    sockpath: Optional[str] = None
    timeout: float = 1.0
    """Env var: WATCHMAN_TRANSPORT,
    (default: 'local' for `pywatchman.UnixSocketTransport`"""
    transport: Optional[TransportType] = None
    """Env var: WATCHMAN_ENCODING (default: 'bser' for 'local'
    and 'json' for 'cli')"""
    sendEncoding: Optional[Literal["bser", "json"]] = None
    """Env var: WATCHMAN_ENCODING (default: 'bser' for 'local'
     and 'json' for 'cli')"""
    recvEncoding: Optional[Literal["bser", "json"]] = None
    useImmutableBser: bool | None = False
    """
    Use False for the next two (sendCodec and recvCodec) because None
    has a special meaning.
    False is default to act like the native OS methods as much as possible.
    """
    valueEncoding: bool | None = (False,)
    valueErrors: bool | None = (False,)
    binpath: Path | str = "watchman"

    sendCodec: bool | None = field(default=None, init=False)
    recvCodec: bool | None = field(default=None, init=False)
    sendConn: Any = field(default=None, init=False)
    recvConn: Any = field(default=None, init=False)
    """Subscriptions keyed by subscription name"""
    subs: dict = field(default_factory=dict, init=False)
    """Subscriptions keyed by root, then by subscription name"""
    sub_by_root: dict = field(default_factory=dict, init=False)
    """When log level is raised"""
    logs: list = field(default_factory=list, init=False)
    unilateral: list = field(
        default_factory=lambda: ["log", "subscription"], init=False
    )
    tport: pywatchman.Transport | None = field(default=None, init=False)

    fields: ClassVar[tuple[str, str, str]] = ('exists', 'name', 'new')
    tmp: TemporaryDirectory = field(default_factory=TemporaryDirectory, init=False)

    def __post_init__(self):
        super().__init__()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.tmp.cleanup()
        self.close()
