# coding=utf-8
"""
Start
"""

from watch.cli import app
from pyrc import cli_invoke


def test_help():
    """
    cli --help
    """
    result = cli_invoke(app, ["--help"])
    assert result.exit_code == 0
    assert result.output.startswith("Usage:")
