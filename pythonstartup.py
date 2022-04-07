# coding=utf-8
"""
Python startup script to run IPython if available.

`export PYTHONSTARTUP=<path to this file>`
"""

import os
os.environ['PYTHONSTARTUP'] = ''  # Prevent running this again
try:
    import IPython
    IPython.start_ipython()
    raise SystemExit
except ImportError:
    pass

