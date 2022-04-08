# coding=utf-8
"""
Typings Module
"""
__all__ = (
    'ExcType',
)

from typing import Type
from typing import TypeAlias

ExcType: TypeAlias = Type[Exception] | tuple[Type[Exception], ...]
