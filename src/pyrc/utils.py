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
    "aiodmg",
    "aiogz",
    "clone",
    "cmd",
    "dmg",
    "github_url",
    "gz",
    "suppress",
    "syssudo",
    "tardir",
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
from pathlib import Path
from subprocess import CompletedProcess
from typing import Callable
from typing import ParamSpec
from typing import TypeVar

import semver

from .alias import TempDir
from .constants import GITHUB_URL
from .constants import GitScheme
from .constants import PROJECT
from .environment import USER
from .typings import ExcType

T = TypeVar('T')
P = ParamSpec('P')

git_default_scheme = "https"


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

    Examples:
        >>> amI(USER)
        True
        >>> amI()
        False

    Arguments:
        user: to check against current user (Default: False)

    Returns:
        CompletedProcess if the current user is not the same as user, None otherwise
    """
    return os.getuid() == pwd.getpwnam(user or getpass.getuser()).pw_uid


async def aioclone(owner: str = USER, repo: str = PROJECT, scheme: GitScheme = git_default_scheme,
                   path: Path | str = None) -> CompletedProcess:
    """
    Async Clone Repository

    Examples:
        >>> with TempDir() as tmp:
        ...     directory = tmp / "1" / "2" / "3"
        ...     rv = asyncio.run(aioclone("octocat", "Hello-World", path=directory))
        ...     assert rv.returncode == 0
        ...     assert (directory / "README").exists()

    Args:
        owner: github owner (Default: `USER`)
        repo: github repository (Default: `PROJECT`)
        scheme: url scheme (Default: "https")
        path: path to clone (Default: `repo`)

    Returns:
        CompletedProcess
    """
    path = path or Path.cwd() / repo
    path = Path(path)
    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        return await aiocmd("git", "clone", github_url(owner, repo, scheme), path)


async def aiocmd(*args, **kwargs) -> CompletedProcess:
    """
    Async Exec Command

    Examples:
        >>> with TempDir() as tmp:
        ...     rv = asyncio.run(aiocmd("git", "clone", github_url("octocat", "Hello-World", scheme="ssh"), cwd=tmp))
        ...     assert rv.returncode == 0
        ...     assert (tmp / "Hello-World" / "README").exists()

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


async def aiodmg(src: Path | str, dest: Path | str) -> None:
    """
    Async Open dmg file and copy the app to dest

    Examples:
        # >>> await dmg(Path("/tmp/JetBrains.dmg"), Path("/tmp/JetBrains"))

    Args:
        src: dmg file
        dest: path to copy to

    Returns:
        CompletedProcess
    """
    with TempDir() as tmpdir:
        await aiocmd("hdiutil", "attach", "-mountpoint", tmpdir, "-nobrowse", "-quiet", src)
        for item in src.iterdir():
            if item.name.endswith(".app"):
                await aiocmd("cp", "-r", tmpdir / item.name, dest)
                await aiocmd("xattr", "-r", "-d", "com.apple.quarantine", dest)
                await aiocmd("hdiutil", "detach", tmpdir, "-force")
                break


async def aiogz(src: Path | str, dest: Path | str = ".") -> Path:
    """
    Async ncompress .gz src to dest (default: current directory)

    It will be uncompressed to the same directory name as src basename.
    Uncompressed directory will be under dest directory.

    Examples:
        >>> await aiogz("test.tar.gz", "/tmp")  # doctest: +SKIP
        PosixPath('/tmp/test')
        >>>
        >>> cwd = Path.cwd()
        >>> with TempDir() as workdir:
        ...     os.chdir(workdir)
        ...     with TempDir() as compress:
        ...         file = compress / "test.txt"
        ...         file.touch()  # doctest: +ELLIPSIS
        ...         compressed = tardir(compress)
        ...         with TempDir() as uncompress:
        ...             uncompressed = asyncio.run(aiogz(compressed, uncompress))
        ...             assert uncompressed.is_dir()
        ...             assert Path(uncompressed).joinpath(file.name).exists()
        >>> os.chdir(cwd)

    Args:
        src: file to uncompress
        dest: destination directory to where uncompress directory will be created (default: current directory)

    Returns:
        Absolute Path of the Uncompressed Directory
    """
    return await asyncio.to_thread(gz, src, dest)


def clone(owner: str = USER, repo: str = PROJECT, scheme: GitScheme = git_default_scheme,
          path: Path | str = None) -> CompletedProcess:
    """
    Clone Repository

    Examples:
        >>> with TempDir() as tmp:
        ...     directory = tmp / "1" / "2" / "3"
        ...     rv = clone("octocat", "Hello-World", "git+ssh", directory)
        ...     assert rv.returncode == 0
        ...     assert (directory / "README").exists()

    Args:
        owner: github owner (Default: `USER`)
        repo: github repository (Default: `PROJECT`)
        scheme: url scheme (Default: "https")
        path: path to clone (Default: `repo`)

    Returns:
        CompletedProcess
    """
    path = path or Path.cwd() / repo
    path = Path(path)
    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        return cmd("git", "clone", github_url(owner, repo, scheme), path)


def cmd(*args, **kwargs) -> CompletedProcess:
    """
    Exec Command

    Examples:
        >>> with TempDir() as tmp:
        ...     rv = cmd("git", "clone", github_url(), tmp)
        ...     assert rv.returncode == 0
        ...     assert (tmp / "README.md").exists()

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


def dmg(src: Path | str, dest: Path | str) -> None:
    """
    Open dmg file and copy the app to dest

    Examples:
        # >>> await dmg(Path("/tmp/JetBrains.dmg"), Path("/tmp/JetBrains"))

    Args:
        src: dmg file
        dest: path to copy to

    Returns:
        CompletedProcess
    """
    with TempDir() as tmpdir:
        cmd("hdiutil", "attach", "-mountpoint", tmpdir, "-nobrowse", "-quiet", src)
        for item in src.iterdir():
            if item.name.endswith(".app"):
                cmd("cp", "-r", tmpdir / item.name, dest)
                cmd("xattr", "-r", "-d", "com.apple.quarantine", dest)
                cmd("hdiutil", "detach", tmpdir, "-force")
                break


def github_url(owner: str = USER, repo: str | Path = PROJECT, scheme: GitScheme = git_default_scheme) -> str:
    """
    Get Repository URL

    if scheme is "git+file" will only use repo argument as the path

    Examples:
        >>> github_url() # doctest: +ELLIPSIS
        'https://github.com/.../....git'
        >>> github_url(repo="test") # doctest: +ELLIPSIS
        'https://github.com/.../test.git'
        >>> github_url("cpython", "cpython")
        'https://github.com/cpython/cpython.git'
        >>> github_url(repo="/tmp/cpython", scheme="git+file")
        'git+file:///tmp/cpython.git'
        >>> github_url("cpython", "cpython", scheme="git+https")
        'git+https://github.com/cpython/cpython.git'
        >>> github_url("cpython", "cpython", scheme="git+ssh")
        'git+ssh://git@github.com/cpython/cpython.git'
        >>> github_url("cpython", "cpython", scheme="ssh")
        'git@github.com:cpython/cpython.git'

    Args:
        owner: github user (Default: `USER`)
        repo: github repository (Default: `PROJECT`)
        scheme: url scheme (Default: "https")

    Returns:
        str
    """
    if scheme == "git+file":
        return f"git+file://{repo}.git"
    return f"{GITHUB_URL[scheme]}{owner}/{repo}.git"

# TODO: aqui lo dejo, meter el Path de los viejos y meter el tempdir y el tempfile y el
#   gz y el otro a lo mejor. Terminar con el dmg.
# https://github.com/create-dmg/create-dmg/blob/master/create-dmg


def gz(src: Path | str, dest: Path | str = ".") -> Path:
    """
    Uncompress .gz src to dest (default: current directory)

    It will be uncompressed to the same directory name as src basename.
    Uncompressed directory will be under dest directory.

    Examples:
        >>> cwd = Path.cwd()
        >>> with TempDir() as workdir:
        ...     os.chdir(workdir)
        ...     with TempDir() as compress:
        ...         file = compress / "test.txt"
        ...         file.touch()  # doctest: +ELLIPSIS
        ...         compressed = tardir(compress)
        ...         with TempDir() as uncompress:
        ...             uncompressed = gz(compressed, uncompress)
        ...             assert uncompressed.is_dir()
        ...             assert Path(uncompressed).joinpath(file.name).exists()
        >>> os.chdir(cwd)

    Args:
        src: file to uncompress
        dest: destination directory to where uncompress directory will be created (default: current directory)

    Returns:
        Absolute Path of the Uncompressed Directory
    """
    dest = Path(dest)
    with tarfile.open(src, "r:gz") as tar:
        tar.extractall(dest)
        return (dest / tar.getmembers()[0].name).parent.absolute()


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


def tardir(src: Path | str) -> Path:
    """
    Compress directory src to <basename src>.tar.gz in cwd

    Examples:
        >>> cwd = Path.cwd()
        >>> with TempDir() as workdir:
        ...     os.chdir(workdir)
        ...     with TempDir() as compress:
        ...         file = compress / "test.txt"
        ...         file.touch()  # doctest: +ELLIPSIS
        ...         compressed = tardir(compress)
        ...         with TempDir() as uncompress:
        ...             uncompressed = gz(compressed, uncompress)
        ...             assert uncompressed.is_dir()
        ...             assert Path(uncompressed).joinpath(file.name).exists()
        >>> os.chdir(cwd)

    Args:
        src: directory to compress

    Raises:
        FileNotFoundError: No such file or directory
        ValueError: Can't compress current working directory

    Returns:
        Compressed Absolute File Path
    """
    src = Path(src)
    if not src.exists():
        raise FileNotFoundError(f"{src}: No such file or directory")

    if src.resolve() == Path.cwd().resolve():
        raise ValueError("Can't compress current working directory")

    name = Path(src).name + ".tar.gz"
    dest = Path(name)
    with tarfile.open(dest, 'w:gz') as tar:
        for root, dirs, files in os.walk(src):
            for file_name in files:
                tar.add(os.path.join(root, file_name))
        return dest.absolute()


def tilde(path: str | Path = '.') -> str:
    """
    Replaces $HOME with ~

    Examples:
        >>> assert tilde(f"{Path.home()}/file") == f"~/file"

    Arguments
        path: path to replace (default: '.')

    Returns:
        str
    """
    return str(path).replace(str(Path.home()), '~')


def version(package: str = PROJECT) -> str:
    """
    Package installed version

    Examples:
        >>> assert semver.VersionInfo.parse(version("pip"))

    Arguments:
        package: package name (Default: `PROJECT`)

    Returns
        Installed version
    """
    return suppress(importlib.metadata.version, importlib.metadata.PackageNotFoundError, 
                    package or Path(__file__).parent.name)
