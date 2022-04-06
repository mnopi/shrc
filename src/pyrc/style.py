# coding=utf-8
"""
Style Module

Add style
"""
__all__ = (
    'black',
    'blue',
    'cyan',
    'green',
    'magenta',
    'red',
    'white',
    'yellow',
)

from typing import Any
from typing import Optional
from typing import Union

import click

from .color import BLACK
from .color import BLUE
from .color import CYAN
from .color import GREEN
from .color import MAGENTA
from .color import RED
from .color import WHITE
from .color import YELLOW


# noinspection DuplicatedCode
def black(text: Any,
          bg: Union[str, int, tuple[int, int, int]] = None,
          bold: Optional[bool] = None,
          dim: Optional[bool] = None,
          underline: Optional[bool] = None,
          overline: Optional[bool] = None,
          italic: Optional[bool] = None,
          blink: Optional[bool] = None,
          reverse: Optional[bool] = None,
          strikethrough: Optional[bool] = None,
          reset: bool = True) -> str:
    """
    Format with fg=BLACK

    Arguments:
      text: text to apply style
      bg: background color (default: None)
      bold: bold text (default: None)
      dim: dim (default: None)
      underline: underline (default: None)
      overline: overline (default: None)
      italic: italic (default: None)
      blink: blink (default: None)
      reverse: reverse (default: None)
      strikethrough: strikethrough (default: None)
      reset: reset (default: True)
    """
    return click.style(text,
                       fg=BLACK, bg=bg, bold=bold, dim=dim, underline=underline,
                       overline=overline, italic=italic, blink=blink, reverse=reverse,
                       strikethrough=strikethrough, reset=reset)


def blue(text: Any,
         bg: Union[str, int, tuple[int, int, int]] = None,
         bold: Optional[bool] = None,
         dim: Optional[bool] = None,
         underline: Optional[bool] = None,
         overline: Optional[bool] = None,
         italic: Optional[bool] = None,
         blink: Optional[bool] = None,
         reverse: Optional[bool] = None,
         strikethrough: Optional[bool] = None,
         reset: bool = True) -> str:
    """
    Format with fg=BLUE

    Arguments:
      text: text to apply style
      bg: background color (default: None)
      bold: bold text (default: None)
      dim: dim (default: None)
      underline: underline (default: None)
      overline: overline (default: None)
      italic: italic (default: None)
      blink: blink (default: None)
      reverse: reverse (default: None)
      strikethrough: strikethrough (default: None)
      reset: reset (default: True)
    """
    return click.style(text,
                       fg=BLUE, bg=bg, bold=bold, dim=dim, underline=underline,
                       overline=overline, italic=italic, blink=blink, reverse=reverse,
                       strikethrough=strikethrough, reset=reset)


def cyan(text: Any,
         bg: Union[str, int, tuple[int, int, int]] = None,
         bold: Optional[bool] = None,
         dim: Optional[bool] = None,
         underline: Optional[bool] = None,
         overline: Optional[bool] = None,
         italic: Optional[bool] = None,
         blink: Optional[bool] = None,
         reverse: Optional[bool] = None,
         strikethrough: Optional[bool] = None,
         reset: bool = True) -> str:
    """
    Format with fg=CYAN

    Arguments:
      text: text to apply style
      bg: background color (default: None)
      bold: bold text (default: None)
      dim: dim (default: None)
      underline: underline (default: None)
      overline: overline (default: None)
      italic: italic (default: None)
      blink: blink (default: None)
      reverse: reverse (default: None)
      strikethrough: strikethrough (default: None)
      reset: reset (default: True)
    """
    return click.style(text,
                       fg=CYAN, bg=bg, bold=bold, dim=dim, underline=underline,
                       overline=overline, italic=italic, blink=blink, reverse=reverse,
                       strikethrough=strikethrough, reset=reset)


def green(text: Any,
          bg: Union[str, int, tuple[int, int, int]] = None,
          bold: Optional[bool] = None,
          dim: Optional[bool] = None,
          underline: Optional[bool] = None,
          overline: Optional[bool] = None,
          italic: Optional[bool] = None,
          blink: Optional[bool] = None,
          reverse: Optional[bool] = None,
          strikethrough: Optional[bool] = None,
          reset: bool = True) -> str:
    """
    Format with fg=GREEN

    Arguments:
      text: text to apply style
      bg: background color (default: None)
      bold: bold text (default: None)
      dim: dim (default: None)
      underline: underline (default: None)
      overline: overline (default: None)
      italic: italic (default: None)
      blink: blink (default: None)
      reverse: reverse (default: None)
      strikethrough: strikethrough (default: None)
      reset: reset (default: True)
    """
    return click.style(text,
                       fg=GREEN, bg=bg, bold=bold, dim=dim, underline=underline,
                       overline=overline, italic=italic, blink=blink, reverse=reverse,
                       strikethrough=strikethrough, reset=reset)


# noinspection DuplicatedCode
def magenta(text: Any,
            bg: Union[str, int, tuple[int, int, int]] = None,
            bold: Optional[bool] = None,
            dim: Optional[bool] = None,
            underline: Optional[bool] = None,
            overline: Optional[bool] = None,
            italic: Optional[bool] = None,
            blink: Optional[bool] = None,
            reverse: Optional[bool] = None,
            strikethrough: Optional[bool] = None,
            reset: bool = True) -> str:
    """
    Format with fg=MAGENTA

    Arguments:
      text: text to apply style
      bg: background color (default: None)
      bold: bold text (default: None)
      dim: dim (default: None)
      underline: underline (default: None)
      overline: overline (default: None)
      italic: italic (default: None)
      blink: blink (default: None)
      reverse: reverse (default: None)
      strikethrough: strikethrough (default: None)
      reset: reset (default: True)
    """
    return click.style(text,
                       fg=MAGENTA, bg=bg, bold=bold, dim=dim, underline=underline,
                       overline=overline, italic=italic, blink=blink, reverse=reverse,
                       strikethrough=strikethrough, reset=reset)


def red(text: Any,
        bg: Union[str, int, tuple[int, int, int]] = None,
        bold: Optional[bool] = None,
        dim: Optional[bool] = None,
        underline: Optional[bool] = None,
        overline: Optional[bool] = None,
        italic: Optional[bool] = None,
        blink: Optional[bool] = None,
        reverse: Optional[bool] = None,
        strikethrough: Optional[bool] = None,
        reset: bool = True) -> str:
    """
    Format with fg=RED

    Arguments:
      text: text to apply style
      bg: background color (default: None)
      bold: bold text (default: None)
      dim: dim (default: None)
      underline: underline (default: None)
      overline: overline (default: None)
      italic: italic (default: None)
      blink: blink (default: None)
      reverse: reverse (default: None)
      strikethrough: strikethrough (default: None)
      reset: reset (default: True)
    """
    return click.style(text,
                       fg=RED, bg=bg, bold=bold, dim=dim, underline=underline,
                       overline=overline, italic=italic, blink=blink, reverse=reverse,
                       strikethrough=strikethrough, reset=reset)


def white(text: Any,
          bg: Union[str, int, tuple[int, int, int]] = None,
          bold: Optional[bool] = None,
          dim: Optional[bool] = None,
          underline: Optional[bool] = None,
          overline: Optional[bool] = None,
          italic: Optional[bool] = None,
          blink: Optional[bool] = None,
          reverse: Optional[bool] = None,
          strikethrough: Optional[bool] = None,
          reset: bool = True) -> str:
    """
    Format with fg=WHITE

    Arguments:
      text: text to apply style
      bg: background color (default: None)
      bold: bold text (default: None)
      dim: dim (default: None)
      underline: underline (default: None)
      overline: overline (default: None)
      italic: italic (default: None)
      blink: blink (default: None)
      reverse: reverse (default: None)
      strikethrough: strikethrough (default: None)
      reset: reset (default: True)
    """
    return click.style(text,
                       fg=WHITE, bg=bg, bold=bold, dim=dim, underline=underline,
                       overline=overline, italic=italic, blink=blink, reverse=reverse,
                       strikethrough=strikethrough, reset=reset)


def yellow(text: Any,
           bg: Union[str, int, tuple[int, int, int]] = None,
           bold: Optional[bool] = None,
           dim: Optional[bool] = None,
           underline: Optional[bool] = None,
           overline: Optional[bool] = None,
           italic: Optional[bool] = None,
           blink: Optional[bool] = None,
           reverse: Optional[bool] = None,
           strikethrough: Optional[bool] = None,
           reset: bool = True) -> str:
    """
    Format with fg=YELLOW

    Arguments:
      text: text to apply style
      bg: background color (default: None)
      bold: bold text (default: None)
      dim: dim (default: None)
      underline: underline (default: None)
      overline: overline (default: None)
      italic: italic (default: None)
      blink: blink (default: None)
      reverse: reverse (default: None)
      strikethrough: strikethrough (default: None)
      reset: reset (default: True)
    """
    return click.style(text,
                       fg=YELLOW, bg=bg, bold=bold, dim=dim, underline=underline,
                       overline=overline, italic=italic, blink=blink, reverse=reverse,
                       strikethrough=strikethrough, reset=reset)
