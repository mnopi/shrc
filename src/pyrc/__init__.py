# coding=utf-8
"""
src package
"""
from .alias import *
from .bools import *
from .color import *
from .constants import *
from .env import *
from .jetbrains import *
from .out import *
from .pretty import *
from .show import *
from .startup import *
from .style import *
from .symbols import *
from .typings import *
from .utils import *
from .variables import *

from . import alias
from . import bools as bools
from . import color as color
from . import constants
from . import env
from . import jetbrains
from . import out as out
from . import pretty
from . import show as show
from . import startup
from . import style as style
from . import symbols as symbols
from . import typings
from . import utils
from . import variables

__all__ = \
    alias.__all__ + \
    bools.__all__ + \
    color.__all__ + \
    constants.__all__ + \
    env.__all__ + \
    jetbrains.__all__ + \
    out.__all__ +  \
    pretty.__all__ + \
    startup.__all__ + \
    show.__all__ +  \
    style.__all__ +  \
    symbols.__all__ +  \
    typings.__all__ + \
    utils.__all__ + \
    variables.__all__ + \
    ("bools", ) + \
    ("color", ) + \
    ("out", ) + \
    ("show", ) + \
    ("style", ) + \
    ("symbols", )

if __name__ == "__main__":
    import typer
    from .jetbrains import app
    try:
        typer.Exit(app())
    except KeyboardInterrupt:
        print('Aborted!')
        typer.Exit()
