import subprocess
import sys

from catio import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "catio", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
