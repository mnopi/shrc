# coding=utf-8
"""
Constants and Variables Module
"""
__all__ = (
    "GITHUB_DOMAIN",
    "GITHUB_URL",
    "LINUX",
    "PACKAGE",
    "USER"
)
import os
import pathlib
import sys

GITHUB_DOMAIN = "github.com"
"""GitHub: api, git+file, git+https, git+ssh, https, ssh and git URLs 
(join directly the user or path without '/' or ':')"""
GITHUB_URL = {
    "api": f"https://{GITHUB_DOMAIN}/",
    "git+file": f"git+file:///",
    "git+https": f"git+https://git@{GITHUB_DOMAIN}/",
    "git+ssh": f"git+ssh://git@{GITHUB_DOMAIN}/",
    "https": f"https://{GITHUB_DOMAIN}/",
    "ssh": f"git@{GITHUB_DOMAIN}:",
}
LINUX = sys.platform == "Linux"
PACKAGE: str = pathlib.Path(__file__).parent.name
USER: str = os.getenv("USER")
