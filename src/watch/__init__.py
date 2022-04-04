# coding=utf-8
"""Watch Package."""
from .watchme import *
from . import watchme
from .watchman import *
from . import watchman 

__all__ = watchme.__all__ + watchman.__all__

if __name__ == "__main__":
    import typer
    from .cli import app
    try:
        typer.Exit(app())
    except KeyboardInterrupt:
        print('Aborted!')
        typer.Exit()
