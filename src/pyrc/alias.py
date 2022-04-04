# coding=utf-8
"""
Typings Module
"""
__all__ = (
    "cli_invoke",
)

from typer.testing import CliRunner

cli_invoke = CliRunner().invoke
