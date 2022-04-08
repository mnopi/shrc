# coding=utf-8
"""
src package
"""
from .alias import *
from .color import *
from .constants import *
from .jetbrains import *
from .pretty import *
from .startup import *
from .typings import *
from .utils import *
from .variables import *

from . import alias
from . import color as color
from . import constants
from . import env as env
from . import jetbrains
from . import pretty
from . import startup
from . import typings
from . import utils
from . import variables

__all__ = \
    alias.__all__ + \
    color.__all__ + \
    constants.__all__ + \
    jetbrains.__all__ + \
    pretty.__all__ + \
    startup.__all__ + \
    typings.__all__ + \
    utils.__all__ + \
    variables.__all__ + \
    ("color", "env", )

if __name__ == "__main__":
    import typer
    from .jetbrains import app
    try:
        typer.Exit(app())
    except KeyboardInterrupt:
        print('Aborted!')
        typer.Exit()
