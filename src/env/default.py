# coding=utf-8
"""
System Environment Variables
"""
__all__ = (
  "LOGNAME",
  "OLDPWD",
  "PATH",
  "PWD",
  "SHELL",
  "SUDO_COMMAND",
  "SUDO_GID",
  "SUDO_UID",
  "SUDO_USER",
  "USER",
  "VIRTUAL_ENV",

)

from pathlib import Path

from .noset import Noset
from .noset import NOSET

LOGNAME: str | Noset | None = NOSET
OLDPWD: Path | Noset | None = NOSET
PATH: str | Noset | None = NOSET
PWD: Path | Noset | None = NOSET
SHELL: str | Noset | None = NOSET
SUDO_COMMAND: str | Noset | None = NOSET
SUDO_GID: int | Noset | None = NOSET
SUDO_UID: int | Noset | None = NOSET
SUDO_USER: str | Noset | None = NOSET
USER: str | Noset | None = NOSET
VIRTUAL_ENV: str | Noset | None = NOSET
