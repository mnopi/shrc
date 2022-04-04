# coding=utf-8
"""
Start
"""

from shrc.jetbrains import app
from shrc import cli_invoke


def test_help():
    """
    cli --help
    """
    result = cli_invoke(app, ["--help"])
    assert result.exit_code == 0
    assert result.output.startswith("Usage:")
