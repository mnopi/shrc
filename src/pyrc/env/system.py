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
  "PWD",
  "RHEL",
  "RHEL_LIKE",
  "SSH",
  "SUDO_GID",
  "SUDO_UID",
  "SUDO_USER",
  "UBUNTU",
  "UNAME",
  "USER",
  "VIRTUAL_ENV",
)

from pathlib import Path

from .noset import NOSET

"""'DIST_ID' is 'alpine' and not: nix or busybox"""
ALPINE: bool | NOSET | None = NOSET

"""'DIST_ID' is 'alpine'"""
ALPINE_LIKE: bool | NOSET | None = NOSET

"""'DIST_ID' is 'arch' for archlinux"""
ARCH: bool | NOSET | None = NOSET

"""if not '/etc/os-release' and not '/sbin'."""
BUSYBOX: bool | NOSET | None = NOSET

"""'DIST_ID' is 'centos'"""
CENTOS: bool | NOSET | None = NOSET

"""Command Line Tools /usr directory (xcode-select -p)"""
CLT: Path | NOSET | None = NOSET

"""BASH completion instalation path"""
COMPLETION: Path | NOSET | None = NOSET

"""Running in docker container"""
CONTAINER: bool | NOSET | None = NOSET

"""'DIST_ID' is 'debian'"""
DEBIAN: bool | NOSET | None = NOSET

"""'noninteractive' if 'IS_CONTAINER' and 'DEBIAN_LIKE' are set"""
DEBIAN_FRONTEND: str | NOSET | None = NOSET

"""'DIST_ID_LIKE is 'debian'"""
DEBIAN_LIKE: bool | NOSET | None = NOSET

"""Distribution Codename: Catalina, Big Sur, kali-rolling, focal, etc."""
DIST_CODENAME: str | NOSET | None = NOSET

"""alpine|centos|debian|kali|macOS|ubuntu|..."""
DIST_ID: str | NOSET | None = NOSET

"""One of: alpine|debian|rhel fedora"""
DIST_ID_LIKE: str | NOSET | None = NOSET

"""'DIST_ID' is unknown"""
DIST_UNKNOWN: str | NOSET | None = NOSET

"""Distribution Version: macOS (10.15.1, 10.16, ...), kali (2021.2, ...), ubuntu (20.04, ...)"""
DIST_VERSION: str | NOSET | None = NOSET

"""'DIST_ID' is 'fedora'"""
FEDORA: bool | NOSET | None = NOSET

"""'DIST_ID' is 'fedora' or 'fedora' in 'DIST_ID_LIKE'"""
FEDORA_LIKE: bool | NOSET | None = NOSET

"""Cask Versions (similar to opt)"""
HOMEBREW_CASK: Path | NOSET | None = NOSET

"""Version of formula, $HOMEBREW_PREFIX/opt is a symlink to $HOMEBREW_CELLAR"""
HOMEBREW_CELLAR: Path | NOSET | None = NOSET

"""Homebrew etc"""
HOMEBREW_ETC: Path | NOSET | None = NOSET

"""Homebrew unlinked Kegs (in $HOMEBREW_OPT) to add to PATH"""
HOMEBREW_KEGS: Path | NOSET | None = NOSET

"""Homebrew $HOMEBREW_PREFIX/lib"""
HOMEBREW_LIB: Path | NOSET | None = NOSET

"""Symlink for the latest version of formula to $HOMEBREW_CELLAR"""
HOMEBREW_OPT: Path | NOSET | None = NOSET

"""Homebrew prefix (brew shellenv)"""
HOMEBREW_PREFIX: Path | NOSET | None = NOSET

"""Profile compat dir (profile.d), under etc"""
HOMEBREW_PROFILE: Path | NOSET | None = NOSET

"""Repository and Library with homebrew gems and Taps (brew shellenv)"""
HOMEBREW_REPOSITORY: Path | NOSET | None = NOSET

"""Taps path under '$HOMEBREW_REPOSITORY/Library'"""
HOMEBREW_TAPS: Path | NOSET | None = NOSET

"""First part of hostname: foo.com (foo), example.foo.com (example)"""
HOST: str | NOSET | None = NOSET

"""Symbol and 'HOST' if 'CONTAINER' or 'SSH'"""
HOST_PROMPT: str | NOSET | None = NOSET

"""'DIST_ID' is 'kali'"""
KALI: bool | NOSET | None = NOSET

"""'DIST_ID' is 'alpine' and '/etc/nix'"""
NIXOS: bool | NOSET | None = NOSET

"""Default Package Manager: apk, apt, brew, nix and yum"""
PM: str | NOSET | None = NOSET

"""Default Package Manager with Install Options (Quiet and no cache for containers)"""
PM_INSTALL: str | NOSET | None = NOSET

"""OS PWD"""
PWD: Path | NOSET | None = NOSET

"""'DIST_ID' is 'rhel'"""
RHEL: bool | NOSET | None = NOSET

"""'DIST_ID' is 'rhel' or 'rhel' in 'DIST_ID_LIKE'"""
RHEL_LIKE: bool | NOSET | None = NOSET

"""'SSH_CLIENT' or 'SSH_TTY' or 'SSH_CONNECTION'"""
SSH: bool | NOSET | None = NOSET

"""'DIST_ID' is 'ubuntu'"""
UBUNTU: bool | NOSET | None = NOSET

"""Operating System System Name: darwin or linux (same as 'sys.platform')"""
UNAME: str | NOSET | None = NOSET

USER: str | NOSET | None = NOSET
