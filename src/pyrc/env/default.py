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

from .noset import NOSET

LOGNAME: str | NOSET | None = NOSET
OLDPWD: Path | NOSET | None = NOSET
PATH: str | NOSET | None = NOSET
PWD: Path | NOSET | None = NOSET
SHELL: str | NOSET | None = NOSET
SUDO_COMMAND: str | NOSET | None = NOSET
SUDO_GID: int | NOSET | None = NOSET
SUDO_UID: int | NOSET | None = NOSET
SUDO_USER: str | NOSET | None = NOSET
USER: str | NOSET | None = NOSET
VIRTUAL_ENV: str | NOSET | None = NOSET
