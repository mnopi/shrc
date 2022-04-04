# coding=utf-8
"""
Utils Module
"""
__all__ = (
    "ExcType",
    "amI",
    "CmdError",
    "aioclone",
    "aiocmd",
    "clone",
    "cmd",
    "dmg",
    "github_url",
    "gz",
    "suppress",
    "syssudo",
    "tilde",
    "version",
)

import asyncio
import getpass
import importlib.metadata
import contextlib
import os
import pwd
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from subprocess import CompletedProcess
from typing import Callable
from typing import Literal
from typing import ParamSpec
from typing import TypeAlias
from typing import Type
from typing import TypeVar

from .constants import GITHUB_URL
from .constants import PACKAGE
from .constants import USER

T = TypeVar('T')
P = ParamSpec('P')

ExcType: TypeAlias = Type[Exception] | tuple[Type[Exception], ...]


class CmdError(subprocess.CalledProcessError):
    """
    Raised when run() and the process returns a non-zero exit status.

    Attributes:
      process: The CompletedProcess object returned by run().
    """
    def __init__(self, process: subprocess.CompletedProcess = None):
        super().__init__(process.returncode, process.args, output=process.stdout, stderr=process.stderr)

    def __str__(self):
        rv = super().__str__()
        if self.stderr is not None:
            rv += "\n" + self.stderr
        if self.stdout is not None:
            rv += "\n" + self.stdout
        return rv


def amI(user: str = "root") -> bool:
    """
    Check if Current User is User in Argument (default: root)

    Arguments:
        user: to check against current user (Default: False)

    Returns:
        CompletedProcess if the current user is not the same as user, None otherwise
    """
    return os.getuid() == pwd.getpwnam(user or getpass.getuser()).pw_uid


async def aioclone(user: str = USER, repo: str = PACKAGE, path: Path = None) -> CompletedProcess:
    """
    Async Clone Repository

    Examples:
        >>> await aioclone("cpython", "cpython")
        >>> await aioclone("cpython", "cpython", Path("/tmp/cpython")

    Args:
        user: github user (Default: `USER`)
        repo: github repository (Default: `REPO`)
        path: path to clone (Default: `repo`)

    Returns:
        CompletedProcess
    """
    path = path or Path.cwd() / repo
    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        return await aiocmd("git", "clone", f"https://github.com/{user}/{repo}.git", path)


async def aiocmd(*args, **kwargs) -> CompletedProcess:
    """
    Async Exec Command

    Examples:
        >>> await aiocmd("git", "clone", GITHUB, JETBRAINS)

    Args:
        *args: command and args
        **kwargs: subprocess.run kwargs

    Raises:
        JetBrainsError

    Returns:
        None
    """
    proc = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE,
                                                stderr=asyncio.subprocess.PIPE, **kwargs)

    stdout, stderr = await proc.communicate()
    completed = subprocess.CompletedProcess(args, returncode=proc.returncode,
                                            stdout=stdout.decode() if stdout else None,
                                            stderr=stderr.decode() if stderr else None)
    if completed.returncode != 0:
        raise CmdError(completed)
    return completed


def clone(user: str = USER, repo: str = PACKAGE, path: Path = None) -> CompletedProcess:
    """
    Clone Repository

    Examples:
        >>> clone("cpython", "cpython")
        >>> clone("cpython", "cpython", Path("/tmp/cpython")

    Args:
        user: github user (Default: `USER`)
        repo: github repository (Default: `REPO`)
        path: path to clone (Default: `repo`)

    Returns:
        CompletedProcess
    """
    path = path or Path.cwd() / repo
    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        return cmd("git", "clone", f"https://github.com/{user}/{repo}.git", path)


def cmd(*args, **kwargs) -> CompletedProcess:
    """
    Exec Command

    Examples:
        >>> cmd("git", "clone", GITHUB, JETBRAINS)

    Args:
        *args: command and args
        **kwargs: subprocess.run kwargs

    Raises:
        JetBrainsError

    Returns:
        None
    """

    completed = subprocess.run(args, **kwargs, capture_output=True, text=True)

    if completed.returncode != 0:
        raise CmdError(completed)
    return completed


def cmdsudo(*args, user: str = "root", **kwargs) -> CompletedProcess | None:
    """
    Run Program with sudo if user is different that the current user

    Arguments:
        *args: command and args to run
        user: run as user (Default: False)
        **kwargs: subprocess.run kwargs

    Returns:
        CompletedProcess if the current user is not the same as user, None otherwise
    """
    if not amI(user):
        return cmd(["sudo", "-u", user, *args], **kwargs)


async def dmg(src: Path, dest: Path) -> None:
    """
    Open dmg file and copy the app to dest

    Examples:
        >>> await dmg(Path("/tmp/JetBrains.dmg"), Path("/tmp/JetBrains"))

    Args:
        src: dmg file
        dest: path to copy to

    Returns:
        CompletedProcess
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        await aiocmd("hdiutil", "attach", "-mountpoint", tmpdir, "-nobrowse", "-quiet", src)
        for item in src.iterdir():
            if item.name.endswith(".app"):
                await aiocmd("cp", "-r", tmpdir + item.name, dest)
                await aiocmd("xattr", "-r", "-d", "com.apple.quarantine", dest)
                await aiocmd("hdiutil", "detach", tmpdir, "-force")
                break


def github_url(owner: str = USER, repo: str = PACKAGE,
               scheme: Literal["api", "git+file", "git+https", "git+ssh", "https", "ssh"] = "https") -> str:
    """
    Get Repository URL

    Examples:
        >>> github_url("cpython", "cpython")

    Args:
        owner: github user (Default: `USER`)
        repo: github repository (Default: `REPO`)
        scheme: use https (Default: True)

    Returns:
        str
    """
    return f"{GITHUB_URL[scheme]}{owner}/{repo}.git"


async def gz(src: Path, dest: Path) -> None:
    """
    Uncompress .gz src to dest

    Examples:
        >>> await gz(Path("/tmp/JetBrains.dmg"), Path("/tmp/JetBrains.gz"))

    Args:
        src: file to uncompress
        dest: path to compress to

    Returns:
        CompletedProcess
    """
    await asyncio.to_thread(tarfile.open(src, "r:gz").extractall, dest)


def suppress(func: Callable[P, T], exc: ExcType | None = None, *args: P.args, **kwargs: P.kwargs) -> T:
    """
    Try and supress exception.

    """
    with contextlib.suppress(exc or Exception): 
        return func(*args, **kwargs)


def syssudo(user: str = "root") -> CompletedProcess | None:
    """
    Rerun Program with sudo ``sys.executable`` and ``sys.argv`` if user is different that the current user

    Arguments:
        user: run as user (Default: False)

    Returns:
        CompletedProcess if the current user is not the same as user, None otherwise
    """
    if not amI(user):
        return cmd(["sudo", "-u", user, sys.executable, *sys.argv])


def tilde(path: str | Path = '.') -> str:
    """
    Replaces $HOME with ~

    Examples:
        >>> tilde(f"{Path.home}/file")

    Arguments
        path: path to replace (default: '.')

    Returns:
        str
    """
    return str(path).replace(str(Path.home()), '~')


def version(package: str = PACKAGE) -> str:
    """
    Package installed version

    Examples:
        >>> version("pip")

    Arguments:
        package: package name (Default: `PACKAGE`)

    Returns
        Installed version
    """
    return suppress(importlib.metadata.version, importlib.metadata.PackageNotFoundError, 
                    package or Path(__file__).parent.name)
