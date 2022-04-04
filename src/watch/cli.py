# coding=utf-8
"""
Cli Module for Watch Package.
"""
from pathlib import Path

from typer import Option
from typer import Typer

from pyrc import version

from .watchme import WatchMe

package = Path(__file__).name
app = Typer(add_completion=False, name=package, no_args_is_help=True, invoke_without_command=True)


@app.command(name='fg-diff')
def fg_diff(
        exclude: list[Path] | None = Option([], '--exclude', '-e',
                                            help='Additional directories or files to exclude'),
        git: bool | None = Option(False, help='Use git diff for output instead of custom diff'),
        loop: bool | None = Option(True,
                                   help='Loop until keyboard interrupt, instead of exiting on first change'),
        path: Path | None = Option('.', '--path', '-p', help='Path to subscribe'),
):
    """
    Watch for changes in the foreground and shows pretty diff output per file against previous token (1 time run or
    loop)
   
    watchme fg-diff --path .config --git --no-loop --exclude cache --exclude 'Applications Support'
    """
    WatchMe.run(exclude=exclude, git=git, loop=loop, path=path)


@app.command(name='fg-files')
def fg_files(
        exclude: list[Path] | None = Option([], '--exclude', '-e',
                                            help='Additional directories or files to exclude'),
        loop: bool | None = Option(True,
                                   help='Loop until keyboard interrupt, instead of exiting on first change'),
        path: Path | None = Option('.', '--path', '-p', help='Path to subscribe'),
):
    """
    Watch for changes in the foreground and shows pretty output of file changes against previous token (1 time run or
    loop)
    
    `watchme fg-files --no-loop --exclude cache --exclude 'Applications Support'`
    """
    WatchMe.run(exclude=exclude, loop=loop, path=path)


@app.command(name='--version')
def version():
    """Show version and exit."""
    print(version())


if __name__ == '__main__':
    app()
