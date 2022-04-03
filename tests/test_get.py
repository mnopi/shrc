import sys
from subprocess import check_output
from hasis.get import *

pip_version = check_output([sys.executable, '-m', 'pip', '--version'])

def test_version():
    print(pip_version)
    # assert == 