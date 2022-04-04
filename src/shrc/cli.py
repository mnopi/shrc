# coding=utf-8
"""
CLI Module
"""
__all__ = (
    'app',
)
from typer import Typer

from .constants import PACKAGE
from .utils import version

app = Typer(add_completion=False, name=PACKAGE, no_args_is_help=True, invoke_without_command=True)


@app.command()
def version() -> None:
    """
    Prints the version of the package.
    Returns:
        None
    """
    print(version(PACKAGE))

