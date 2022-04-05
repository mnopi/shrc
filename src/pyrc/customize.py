# coding=utf-8
"""
Shrc Customize Module
Examples:

>>> import site  # doctest: +SKIP
>>> from pathlib import Path  # doctest: +SKIP
>>> (Path(site.__file__).parent / "sitecustomize.py").write_text("from pyrc.customize import *")  # doctest: +SKIP
"""
import importlib.util
from . import typings
from importlib.util import spec_from_file_location
print(typings.__spec__.name)
# "pyrc.customize" in sys.modules
print("__spec__" in globals())
type(importlib.util.find_spec('mierda'))
importlib.util.find_spec('pyrc')
import sys
print('pyrc' in sys.modules)
