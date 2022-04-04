# coding=utf-8
"""
Typings Module
"""
__all__ = (
    "cli_invoke",
    "TempDir",
)
import tempfile
from pathlib import Path

from typer.testing import CliRunner

cli_invoke = CliRunner().invoke


class TempDir(tempfile.TemporaryDirectory):
    """
    Wrapper for :class:`tempfile.TemporaryDirectory` that provides Path-like
    """
    def __enter__(self) -> Path:
        """
        Return the path of the temporary directory

        Returns:
            Path of the temporary directory
        """
        return Path(self.name)
