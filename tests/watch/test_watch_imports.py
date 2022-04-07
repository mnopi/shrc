# coding=utf-8
"""
Start
"""
import pytest
import types

from pyrc import IS_REPL
from watch import *


def test_imports_cli():
    """
    cli None
    """
    with pytest.raises(NameError) as exception:
        isinstance(cli, types.ModuleType)   # type: ignore[name-defined]
    assert "name 'cli' is not defined" in str(exception.value)
    assert "cli" not in globals()


def test_imports_startup():
    """
    repl __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(startup, types.ModuleType)
    assert "name 'startup' is not defined" in str(exception.value)
    assert "startup" not in globals()

    if IS_REPL:
        assert isinstance(pywatchman, types.ModuleType)
    else:
        with pytest.raises(NameError) as exception:
            isinstance(pywatchman, types.ModuleType)
        assert "name 'asyncio' is not defined" in str(exception.value)
        assert "asyncio" not in globals()


def test_imports_watchme():
    """
    watchme __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(watchme, types.ModuleType)
    assert "name 'watchme' is not defined" in str(exception.value)
    assert "watchme" not in globals()

    assert issubclass(WatchMe, WatchMan)


def test_imports_watchman():
    """
    watchman __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(watchman, types.ModuleType)
    assert "name 'watchman' is not defined" in str(exception.value)
    assert "watchman" not in globals()

    assert issubclass(WatchMan, pywatchman.client)
