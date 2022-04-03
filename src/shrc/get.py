
__all__ = (
    'ExcType',
    'suppress',
    'tilde',
    'version',    
)

import importlib.metadata
import contextlib
from pathlib import Path
from typing import Callable
from typing import ParamSpec
from typing import TypeAlias
from typing import Type
from typing import TypeVar


T = TypeVar('T')
P = ParamSpec('P')

ExcType: TypeAlias = Type[Exception] | tuple[Type[Exception], ...]

# TODO: aqui lo dejo mirar lo que no encuentro de packaging y lo que tenia de typer del comando donde lo guarde.
#   si esta en watcman o si esta en gglobal o como se llamaran que los borre.
# y quitar este puto warning y ponerme con el gen de jetbrains de una puta vez.


def suppress(func: Callable[P, T], exc: ExcType | None = None, *args: P.args, **kwargs: P.kwargs) -> T:
    """Try and supress exception"""
    with contextlib.suppress(exc or Exception): 
        return func(*args, **kwargs)


def tilde(path: str | Path = '.') -> str:
    """Replaces $HOME with ~"""
    return str(path).replace(str(Path.home()), '~')


def version(package: str = None) -> str:
    """Package installed version"""
    return suppress(importlib.metadata.version, importlib.metadata.PackageNotFoundError, 
                    package or Path(__file__).parent.name)
