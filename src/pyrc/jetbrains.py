#!/usr/bin/env python3
# coding=utf-8
"""
JetBrains package
"""
__all__ = (
    "aiohttp",
    "JetBrains",
)
import asyncio
import os
import tempfile

import sys
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path

import aiohttp as aiohttp
import typer

from .bools import LINUX
from .constants import PROJECT
from .utils import aioclone
from .utils import aiodmg
from .utils import aiogz

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

app = typer.Typer(add_completion=False, context_settings=dict(help_option_names=['-h', '--help']),
                  name=Path(__file__).stem)


@dataclass
class Application:
    """
    JetBrains Application Class
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
        if not self.application.exists():
            async with self.session.get(await self.url, stream=True) as response:
                async with tempfile.NamedTemporaryFile() as tmp:
                    async for chunk in response.content.iter_chunked(1024):
                        await tmp.write(chunk)
                    await (aiogz if LINUX else aiodmg)(tmp.name, self.application)

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
        await aioclone(repo=REPO, path=JETBRAINS)
        jetbrains = cls()

        async with aiohttp.ClientSession() as jetbrains._session:
            jetbrains.applications = [Application(name, jetbrains._session) for name, data in NAMES.items()
                                      if data["enable"] and data.get(sys.platform, True)]

            rv = await asyncio.gather(*[application.install() for application in jetbrains.applications])
            print(rv)


@app.command()
def version() -> None:
    """
    Prints the version of the package.
    Returns:
        None
    """
    print(version(PROJECT))


if __name__ == "__main__":
    asyncio.run(JetBrains.session())
