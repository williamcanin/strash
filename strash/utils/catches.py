from os.path import isdir
from re import sub
from subprocess import Popen, PIPE


def trash_roots(command_gio: str):
    """"""
    p = Popen(command_gio, shell=True, universal_newlines=True, stdout=PIPE)
    return p.communicate()[0]


def take_all_trash_cans(command_gio: str) -> set:
    """Function to get all ROOT directory from recycle bins on devices."""

    take_all_trash_cans_ = set()

    for i in trash_roots(command_gio).split():

        # unix: gio list trash: | sed 's/\\/\//g; s/%20/ /g; s/^/"/g; s/$/"/g; s/files\/.*$/files\//g' | sort -u
        # Replace backslashes with forward slashes
        bar_ = sub(r"\\", r"/", i)

        # Replace character %20 with space
        space_ = sub(r"%20", r" ", bar_)

        # Get the root folder of the recycle bins
        result = sub(r"files/.*$", r"files/", space_)

        take_all_trash_cans_.add(result) if isdir(result) else None

    return take_all_trash_cans_
