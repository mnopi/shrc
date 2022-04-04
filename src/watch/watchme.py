# coding=utf-8
"""
pywatchman.client wrapper
"""
from __future__ import annotations

__all__ = (
    'WatchMe',
)

from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import TypeAlias
from typing import Optional

from .watchman import WatchMan

WatchMeType: TypeAlias = 'WatchMe'


@dataclass
class WatchMe(WatchMan):
    """Wrapper for `pywatchman.client` to handles the communication with the watchman service."""
    """True to use `git diff`, False to use custom diff and None for files only"""
    git: bool | None = None
    exclude: list[Path | str] | None = None
    loop: bool | None = None
    root: Path | str = '.'
    files: dict[str, dict[str, bool]] = field(default=None, init=False)
    delete: bool = field(default=False, init=False)

    @classmethod
    def run(cls, exclude: list[Path | str] | None = None,
            git: bool | None = None,
            loop: bool | None = None,
            path: Path | str | None = None) -> WatchMeType:
        """

        Args:
            exclude:
            git:
            loop:
            path:
        """
        with cls(exclude=exclude, git=git, loop=loop) as client:
            print(client.query('get-config', path))
            return client
