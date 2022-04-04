from pathlib import Path
from typing import Optional
from typing import Union

import hasis
from typer import Argument
from typer import Option
from typer import Typer

from ..src.wbox.fg import WatchMe

command = Path(__file__).name
app = Typer(add_completion=False, name=command, no_args_is_help=True, invoke_without_command=True)

version = print(hasis.version(Path(__file__).parent.name))
  
@app.command()
def main(
    diff: Optional[bool] = Option(WatchMe.diff, help='Copy files to show diffences'),
    exclude: Optional[list[Path]] = Option([], '--exclude', '-e', help='Additional directories or files to exclude'),
    loop: Optional[bool] = Option(WatchMe.loop,
        help='Loop until keyboard interrupt, instead of exiting on first change'), 
    root: Optional[Path] = Argument('.', help='Path to watch'), 
):
    """
    Watch me doing changes.
    
    watchme .config --diff --no-loop --exclude cache --exclude 'Applications Support'
    """
    with WatchMe(diff=diff, exclude=exclude, loop=loop, root=root) as client:
        client.query('get-config', '.')
        print(client)
        
if __name__ == '__main__':
    app()
