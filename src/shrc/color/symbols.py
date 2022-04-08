# coding=utf-8
"""
Symbols Module
"""
__all__ = (
    'CRITICAL',
    'ERROR',
    'OK',
    'NOTICE',
    'SUCCESS',
    'VERBOSE',
    'WARNING',

    'MINUS',
    'MORE',
    'MULTIPLY',
    'PLUS',
    'WAIT',
)

import click

from .colors import BLUE
from .colors import CYAN
from .colors import GREEN
from .colors import MAGENTA
from .colors import RED
from .colors import YELLOW


CRITICAL = click.style('✘', fg=RED, blink=True, bold=True)
"""symbol: '✘', color: RED (bg)"""

ERROR = click.style('✘', fg=RED, bold=True)
"""symbol: '✘', color: RED"""

OK = click.style('✔', fg=GREEN, bold=True)
"""symbol: '✔', color: GREEN"""

NOTICE = click.style('‼', fg=CYAN, bold=True)
"""symbol: '‼', color: CYAN"""

SUCCESS = click.style('◉', fg=BLUE, bold=True)
"""symbol: '◉', color: BLUE"""

VERBOSE = click.style('＋', fg=MAGENTA, bold=True)
"""symbol: '＋', color: MAGENTA"""

WARNING = click.style('！', fg=YELLOW, bold=True)
"""symbol: '！', color: YELLOW"""


MINUS = click.style('－', fg=RED, bold=True)
"""letter: '-', color: RED"""

MORE = click.style('>', fg=MAGENTA, bold=True)
"""letter: '>, color: MAGENTA"""

MULTIPLY = click.style('×', fg=BLUE, bold=True)
"""letter: 'x', color: BLUE"""

PLUS = click.style('+', fg=GREEN, bold=True)
"""letter: '+', color: GREEN"""

WAIT = click.style('…', fg=YELLOW, blink=True, bold=True)
"""symbol: '…', color: YELLOW (blink)"""
