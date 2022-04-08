# coding=utf-8
"""
shrc environment package
"""
from .colors import *
from .out import *
from .show import *
from .style import *
from .symbols import *

from . import colors as colors
from . import out as out
from . import show as show
from . import style as style
from . import symbols as symbols

__all__ = \
    colors.__all__ + \
    out.__all__ +  \
    show.__all__ +  \
    style.__all__ +  \
    symbols.__all__ +  \
    ("colors", "out", "show", "style", "symbols", )
