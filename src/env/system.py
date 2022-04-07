# coding=utf-8
"""
System Environment Variables
"""
__all__ = (
  "ALPINE",
  "ALPINE_LIKE",
  "ARCH",
  "BUSYBOX",
  "CENTOS",
  "CLT",
  "COMPLETION",
  "CONTAINER",
  "DEBIAN",
  "DEBIAN_FRONTEND",
  "DEBIAN_LIKE",
  "DIST_CODENAME",
  "DIST_ID",
  "DIST_ID_LIKE",
  "DIST_UNKNOWN",
  "DIST_VERSION",
  "FEDORA",
  "FEDORA_LIKE",
  "HOMEBREW_CASK",
  "HOMEBREW_CELLAR",
  "HOMEBREW_ETC",
  "HOMEBREW_KEGS",
  "HOMEBREW_LIB",
  "HOMEBREW_OPT",
  "HOMEBREW_PREFIX",
  "HOMEBREW_PROFILE",
  "HOMEBREW_REPOSITORY",
  "HOMEBREW_TAPS",
  "HOST",
  "HOST_PROMPT",
  "KALI",
  "NIXOS",
  "PM",
  "PM_INSTALL",
  "RHEL",
  "RHEL_LIKE",
  "SSH",
  "UBUNTU",
  "UNAME",
)

from pathlib import Path

from .noset import Noset
from .noset import NOSET

"""'DIST_ID' is 'alpine' and not: nix or busybox"""
ALPINE: bool | Noset | None = NOSET

"""'DIST_ID' is 'alpine'"""
ALPINE_LIKE: bool | Noset | None = NOSET

"""'DIST_ID' is 'arch' for archlinux"""
ARCH: bool | Noset | None = NOSET

"""if not '/etc/os-release' and not '/sbin'."""
BUSYBOX: bool | Noset | None = NOSET

"""'DIST_ID' is 'centos'"""
CENTOS: bool | Noset | None = NOSET

"""Command Line Tools /usr directory (xcode-select -p)"""
CLT: Path | Noset | None = NOSET

"""BASH completion instalation path"""
COMPLETION: Path | Noset | None = NOSET

"""Running in docker container"""
CONTAINER: bool | Noset | None = NOSET

"""'DIST_ID' is 'debian'"""
DEBIAN: bool | Noset | None = NOSET

"""'noninteractive' if 'IS_CONTAINER' and 'DEBIAN_LIKE' are set"""
DEBIAN_FRONTEND: str | Noset | None = NOSET

"""'DIST_ID_LIKE is 'debian'"""
DEBIAN_LIKE: bool | Noset | None = NOSET

"""Distribution Codename: Catalina, Big Sur, kali-rolling, focal, etc."""
DIST_CODENAME: str | Noset | None = NOSET

"""alpine|centos|debian|kali|macOS|ubuntu|..."""
DIST_ID: str | Noset | None = NOSET

"""One of: alpine|debian|rhel fedora"""
DIST_ID_LIKE: str | Noset | None = NOSET

"""'DIST_ID' is unknown"""
DIST_UNKNOWN: str | Noset | None = NOSET

"""Distribution Version: macOS (10.15.1, 10.16, ...), kali (2021.2, ...), ubuntu (20.04, ...)"""
DIST_VERSION: str | Noset | None = NOSET

"""'DIST_ID' is 'fedora'"""
FEDORA: bool | Noset | None = NOSET

"""'DIST_ID' is 'fedora' or 'fedora' in 'DIST_ID_LIKE'"""
FEDORA_LIKE: bool | Noset | None = NOSET

"""Cask Versions (similar to opt)"""
HOMEBREW_CASK: Path | Noset | None = NOSET

"""Version of formula, $HOMEBREW_PREFIX/opt is a symlink to $HOMEBREW_CELLAR"""
HOMEBREW_CELLAR: Path | Noset | None = NOSET

"""Homebrew etc"""
HOMEBREW_ETC: Path | Noset | None = NOSET

"""Homebrew unlinked Kegs (in $HOMEBREW_OPT) to add to PATH"""
HOMEBREW_KEGS: Path | Noset | None = NOSET

"""Homebrew $HOMEBREW_PREFIX/lib"""
HOMEBREW_LIB: Path | Noset | None = NOSET

"""Symlink for the latest version of formula to $HOMEBREW_CELLAR"""
HOMEBREW_OPT: Path | Noset | None = NOSET

"""Homebrew prefix (brew shellenv)"""
HOMEBREW_PREFIX: Path | Noset | None = NOSET

"""Profile compat dir (profile.d), under etc"""
HOMEBREW_PROFILE: Path | Noset | None = NOSET

"""Repository and Library with homebrew gems and Taps (brew shellenv)"""
HOMEBREW_REPOSITORY: Path | Noset | None = NOSET

"""Taps path under '$HOMEBREW_REPOSITORY/Library'"""
HOMEBREW_TAPS: Path | Noset | None = NOSET

"""First part of hostname: foo.com (foo), example.foo.com (example)"""
HOST: str | Noset | None = NOSET

"""Symbol and 'HOST' if 'CONTAINER' or 'SSH'"""
HOST_PROMPT: str | Noset | None = NOSET

"""'DIST_ID' is 'kali'"""
KALI: bool | Noset | None = NOSET

"""'DIST_ID' is 'alpine' and '/etc/nix'"""
NIXOS: bool | Noset | None = NOSET

"""Default Package Manager: apk, apt, brew, nix and yum"""
PM: str | Noset | None = NOSET

"""Default Package Manager with Install Options (Quiet and no cache for containers)"""
PM_INSTALL: str | Noset | None = NOSET

"""'DIST_ID' is 'rhel'"""
RHEL: bool | Noset | None = NOSET

"""'DIST_ID' is 'rhel' or 'rhel' in 'DIST_ID_LIKE'"""
RHEL_LIKE: bool | Noset | None = NOSET

"""'SSH_CLIENT' or 'SSH_TTY' or 'SSH_CONNECTION'"""
SSH: bool | Noset | None = NOSET

"""'DIST_ID' is 'ubuntu'"""
UBUNTU: bool | Noset | None = NOSET

"""Operating System System Name: darwin or linux (same as 'sys.platform')"""
UNAME: str | Noset | None = NOSET
