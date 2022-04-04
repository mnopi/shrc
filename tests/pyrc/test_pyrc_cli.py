# coding=utf-8
"""
Start
"""

from pyrc import cli_invoke
from pyrc.jetbrains import app


def test_help():
    """
    cli --help
    """
    result = cli_invoke(app, ["--help"])
    assert result.exit_code == 0
    assert result.output.startswith("Usage:")
