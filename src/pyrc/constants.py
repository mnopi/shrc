# coding=utf-8
"""
Constants and Variables Module
"""
__all__ = (
    "GIT_DEFAULT_SCHEME",
    "GITHUB_DOMAIN",
    "GITHUB_URL",
    "GitScheme",
    "PYTHON_FTP",
)
from typing import Literal


GIT_DEFAULT_SCHEME = "https"

GITHUB_DOMAIN = "github.com"

"""
GitHub: api, git+file, git+https, git+ssh, https, ssh and git URLs
(join directly the user or path without '/' or ':')
"""
GITHUB_URL = {
    "api": f"https://api.{GITHUB_DOMAIN}/",
    "git+file": "git+file:///",
    "git+https": f"git+https://{GITHUB_DOMAIN}/",
    "git+ssh": f"git+ssh://git@{GITHUB_DOMAIN}/",
    "https": f"https://{GITHUB_DOMAIN}/",
    "ssh": f"git@{GITHUB_DOMAIN}:",
}

GitScheme = Literal["git+file", "git+https", "git+ssh", "https", "ssh"]

"""Repository/PyPi/Homebrew Formula Project Name"""
PROJECT: str = "shrc"

"""Python FTP Server"""
PYTHON_FTP = "https://www.python.org/ftp/python"
