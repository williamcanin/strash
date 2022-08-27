from sys import stdout
from subprocess import PIPE, STDOUT, Popen
from re import sub


def command(cmd, appname):
    """"""
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
