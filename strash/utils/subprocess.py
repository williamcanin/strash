from sys import stdout
from subprocess import PIPE, STDOUT, Popen
from re import sub


def command(cmd: str, appname: str) -> None:
    """Get a code in string and run modifying some output values"""
    p = Popen(
        cmd,
        shell=True,
        universal_newlines=True,
        stdout=PIPE,
        stderr=STDOUT,
    )
    for line in p.stdout:
        out = sub(r"shred:", f"{appname}:", line)
        stdout.write(out)
