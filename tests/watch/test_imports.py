# coding=utf-8
"""
Start
"""
import pytest
import types

import pywatchman

from watch import *


def test_imports_cli():
    """
    cli None
    """
    with pytest.raises(NameError) as exception:
        isinstance(cli, types.ModuleType)
    assert "name 'cli' is not defined" in str(exception.value)
    assert "cli" not in globals()


def test_imports_watchme():
    """
    watchme __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(watchme, types.ModuleType)
    assert "name 'watchme' is not defined" in str(exception.value)
    assert "watchme" not in globals()

    assert isinstance(WatchMe, WatchMan)


def test_imports_watchman():
    """
    watchman __all__
    """
    with pytest.raises(NameError) as exception:
        isinstance(watchman, types.ModuleType)
    assert "name 'watchman' is not defined" in str(exception.value)
    assert "watchman" not in globals()

    assert isinstance(watchman, pywatchman.client)
