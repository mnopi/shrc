# coding=utf-8
"""
Colors Constants Module
"""
__all__ = (
    'PRETTY',
    'BLACK',
    'BLUE',
    'CYAN',
    'GREEN',
    'MAGENTA',
    'RED',
    'WHITE',
    'YELLOW',
)

import os

PRETTY = False if os.getenv('NO_PRETTY') else os.getenv('PRETTY')

BLACK: str = 'black'
BLUE: str = 'blue'
CYAN: str = 'cyan'
GREEN: str = 'green'
MAGENTA: str = 'magenta'
RED: str = 'red'
WHITE: str = 'white'
YELLOW: str = 'yellow'
