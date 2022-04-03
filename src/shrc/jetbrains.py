#!/usr/bin/env python3
"""
JetBrains package
"""
__all__ = (
    "aioclone",
    "aiocmd",
    "clone",
    "cmd",
    "dmg",
    "gz",
    "CmdError",
    'JetBrains',
)
import asyncio
import os
import tempfile

import subprocess
import sys
import tarfile
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from subprocess import CompletedProcess

import aiohttp

# https://github.com/0xbf00/dmglib/blob/master/docs/example.rst
# https://stackoverflow.com/questions/6357914/how-do-i-install-a-dmg-file-from-the-command-line/6358679
# https://serverfault.com/questions/13587/how-to-silently-install-dmg-in-macos
# TODO: la url, el repository, el enable, el de que sea el appcode para la plataforma., pyedit

REPO = "JetBrains"
JETBRAINS = Path(os.getenv("JETBRAINS", Path.home() / REPO)).expanduser()
API = "https://data.services.jetbrains.com/products/releases"
APPLICATIONS = JETBRAINS / "Applications"
CACHES = JETBRAINS / "Caches"
DEFAULT = "PyCharm"
GBIN = JETBRAINS / "gbin"
GITHUB = f"https://github.com/j5pu/{REPO}"
LIBRARY = JETBRAINS / "Library"
NAMES = {
    "AppCode": {"enable": True, "code": "AC", "linux": False, },
    "DataGrip": {"enable": True, "code": "DG", },
    "Gateway": {"enable": True, "code": "GW", },
    "GoLand": {"enable": True, "code": "GO", },
    "Idea": {"enable": True, "code": "IIU", },
    DEFAULT: {"enable": True, "code": "PCP", },
    "RubyMine": {"enable": True, "code": "RM", },
    "ToolBox": {"enable": True, "code": "TBA", },
    "WebStorm": {"enable": True, "code": "WS", },
}

LINUX = sys.platform == "Linux"
USER = os.getenv("USER")


async def aioclone(user: str = USER, repo: str = REPO, path: Path = None) -> CompletedProcess:
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
    if completed.returncode == 0:
        return completed
    raise CmdError(completed)


def clone(user: str = USER, repo: str = REPO, path: Path = None) -> CompletedProcess:
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

    if completed.returncode == 0:
        return completed
    raise CmdError(completed)


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


def sudo():
    if os.getuid() != 0:
        return subprocess.call(["sudo", sys.executable, sys.argv[0]])


@dataclass
class Application:
    """

    """
    name: str
    session: aiohttp.ClientSession
    application: Path = field(init=False)
    code: str = field(init=False)
    library: Path = field(init=False)
    options: Path = field(init=False)
    properties: Path = field(init=False)
    vmoptions: Path = field(init=False)

    def __post_init__(self):
        """
        Post initialization

        Returns:
            None
        """
        self.application = APPLICATIONS / self.name / "" if LINUX else ".app"
        self.code = NAMES[self.name]["code"]
        self.library = LIBRARY / self.name
        self.options = self.library / "options"
        self.properties = self.library / ".properties"
        self.vmoptions = self.library / ".vmoptions"

    async def install(self) -> None:
        """
        Installs JetBrains Applications

        Returns:
            None
        """
        print(await self.url)
        return
        if not self.application.exists():
            async with self.session.get(await self.url, stream=True) as response:
                async with tempfile.NamedTemporaryFile() as tmp:
                    async for chunk in response.content.iter_chunked(1024):
                        await tmp.write(chunk)
                    await (gz if LINUX else dmg)(tmp.name, self.application)

    @property
    async def url(self) -> str:
        """
        Get the url to download the application

        Returns:
            Url
        """
        async with self.session.get(API, params={"code": self.code, "latest": "true", "type": "release"}) as response:
            data = await response.json()
            return data[self.code][0]["downloads"][sys.platform if LINUX else "mac"]["link"]


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


@dataclass
class JetBrains:
    """
    JetBrains class
    """
    applications: list[Application] = field(default_factory=list, init=False)
    _session: aiohttp.ClientSession = field(default=None, init=False)

    @classmethod
    async def session(cls) -> None:
        """
        Start JetBrains Applications Install and Configuration

        Returns:
            None
        """
        await aioclone(path=JETBRAINS)
        jetbrains = cls()

        async with aiohttp.ClientSession() as jetbrains._session:
            jetbrains.applications = [Application(name, jetbrains._session) for name, data in NAMES.items()
                                      if data["enable"] and data.get(sys.platform, True)]

            rv = await asyncio.gather(*[application.install() for application in jetbrains.applications])
            print(rv)


if __name__ == "__main__":
    asyncio.run(JetBrains.session())
