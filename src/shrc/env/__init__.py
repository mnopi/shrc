# coding=utf-8
"""
shrc environment package
"""
from .colorize import *
from .default import *
from .secrets import *
from .system import *
from .utils import *

from . import colorize
from . import default
from . import secrets
from . import system
from . import utils

__all__ = \
    colorize.__all__ + \
    default.__all__ + \
    secrets.__all__ + \
    system.__all__ + \
    utils.__all__
