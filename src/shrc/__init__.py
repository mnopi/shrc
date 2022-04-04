# coding=utf-8
"""
src package
"""
import pathlib

from .bools import *

from .cli import app

from .color import *
from . import color as color

from .out import *
from . import out as out

from .show import *
from . import show as show

from .style import *
from . import style as style

from .symbols import *
from . import symbols as symbols

from .system import *

from .utils import *

__all__ = \
    bools.__all__ + \
    color.__all__ + ('color', ) + \
    out.__all__ + ('out', ) + \
    show.__all__ + ('show', ) + \
    style.__all__ + ('style', ) + \
    symbols.__all__ + ('symbols', ) + \
    system.__all__ + \
    utils.__all__

app = lambda: print(version(pathlib.Path(__file__).parent.name))
