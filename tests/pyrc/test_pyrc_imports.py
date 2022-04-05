# coding=utf-8
"""
Start
"""
import pytest
import types

from pyrc import *


def test_imports():
    """
    Library Imports
    """
    assert isinstance(aiohttp, types.ModuleType)
    assert isinstance(asyncio, types.ModuleType)
    assert isinstance(click, types.ModuleType)
    assert isinstance(typer, types.ModuleType)


def test_imports_alias():
    """
    alias __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(alias, types.ModuleType)
    assert "name 'alias' is not defined" in str(exception.value)
    assert "alias" not in globals()

    assert isinstance(cli_invoke, types.MethodType)


def test_imports_bools():
    """
    bools __all__ and module
    """
    assert isinstance(bools, types.ModuleType)
    assert "bools" in globals()

    assert isinstance(LINUX, bool)


def test_imports_color():
    """
    color __all__ and module
    """
    assert isinstance(color, types.ModuleType)
    assert "color" in globals()

    assert BLUE == 'blue'
    # assert print(BLUE) == '\033[34m'


def test_imports_constants():
    """
    constants __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(constants, types.ModuleType)
    assert "name 'constants' is not defined" in str(exception.value)
    assert "constants" not in globals()

    assert isinstance(LINUX, bool)


def test_imports_environment():
    """
    environment __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(environment, types.ModuleType)
    assert "name 'environment' is not defined" in str(exception.value)
    assert "environment" not in globals()

    assert isinstance(USER, str)


def test_imports_jetbrains():
    """
    jetbrains __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(jetbrains, types.ModuleType)
    assert "name 'jetbrains' is not defined" in str(exception.value)
    assert "jetbrains" not in globals()

    assert isinstance(JetBrains, type)


def test_imports_out():
    """
    out __all__ and module
    """
    assert isinstance(out, types.ModuleType)
    assert "out" in globals()

    assert isinstance(black, types.FunctionType)


def test_imports_pretty():
    """
    pretty __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(pretty, types.ModuleType)
    assert "name 'pretty' is not defined" in str(exception.value)
    assert "pretty" not in globals()

    assert isinstance(print, types.FunctionType)
    assert isinstance(is_terminal, types.FunctionType)


def test_imports_show():
    """
    show __all__ and module
    """
    assert isinstance(show, types.ModuleType)
    assert "show" in globals()

    assert isinstance(critical, types.FunctionType)


def test_imports_style():
    """
    style __all__ and module
    """
    assert isinstance(style, types.ModuleType)
    assert "style" in globals()

    assert isinstance(black, types.FunctionType)


def test_imports_symbols():
    """
    symbols __all__ and module
    """
    assert isinstance(symbols, types.ModuleType)
    assert "symbols" in globals()

    assert isinstance(black, types.FunctionType)


def test_imports_typings():
    """
    typings __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(typings, types.ModuleType)
    assert "name 'typings' is not defined" in str(exception.value)
    assert "typings" not in globals()

    import typing
    # noinspection PyUnresolvedReferences
    assert isinstance(ExcType, typing._UnionGenericAlias)


def test_imports_utils():
    """
    utils __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(utils, types.ModuleType)
    assert "name 'utils' is not defined" in str(exception.value)
    assert "utils" not in globals()

    assert isinstance(cmd, types.FunctionType)


def test_imports_variables():
    """
    vars __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(variables, types.ModuleType)
    assert "name 'variables' is not defined" in str(exception.value)
    assert "variables" not in globals()

    assert isinstance(IS_IPYTHON, bool)