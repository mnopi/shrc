# coding=utf-8
"""
Bools Module
"""
__all__ = (
    'LINUX',
    'MACOS',
)

import sys

"""Is Linux? sys.platform == 'linux'"""
LINUX = sys.platform == "linux"

"""Is macOS? sys.platform == 'darwin'"""
MACOS = sys.platform == "darwin"
