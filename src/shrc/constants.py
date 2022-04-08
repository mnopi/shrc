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

GITHUB_URL = {
    "api": f"https://api.{GITHUB_DOMAIN}/",
    "git+file": "git+file:///",
    "git+https": f"git+https://{GITHUB_DOMAIN}/",
    "git+ssh": f"git+ssh://git@{GITHUB_DOMAIN}/",
    "https": f"https://{GITHUB_DOMAIN}/",
    "ssh": f"git@{GITHUB_DOMAIN}:",
}
"""
GitHub: api, git+file, git+https, git+ssh, https, ssh and git URLs
(join directly the user or path without '/' or ':')
"""

GitScheme = Literal["git+file", "git+https", "git+ssh", "https", "ssh"]

PYTHON_FTP = "https://www.python.org/ftp/python"
"""Python FTP Server"""
