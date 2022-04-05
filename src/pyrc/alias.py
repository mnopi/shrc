# coding=utf-8
"""
Typings Module
"""
__all__ = (
    "cli_invoke",
    "rich_inspect",
)

import rich
from typer.testing import CliRunner

cli_invoke = CliRunner().invoke
rich_inspect = rich.inspect


