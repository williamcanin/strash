from os.path import isdir
from re import sub
from subprocess import Popen, PIPE


def trash_roots(command_gio: str):
    """Gets the directories of all the system recycle bins"""
    p = Popen(command_gio, shell=True, universal_newlines=True, stdout=PIPE)
    return p.communicate()[0].split()


def take_all_trash_cans(list_trash: list) -> set:
    """Get all ROOT directory from recycle bins on devices."""

    take_all_trash_cans_ = set()

    if list_trash:
        for path in list_trash:

            # unix: gio list trash: | sed 's/\\/\//g; s/%20/ /g; s/^/"/g; s/$/"/g; s/files\/.*$/files\//g' | sort -u
            # Replace backslashes with forward slashes
            bar_ = sub(r"\\", r"/", path)

            # Replace character %20 with space
            space_ = sub(r"%20", r" ", bar_)

            # Get the root folder of the recycle bins
            result = sub(r"files/.*$", r"files/", space_)

            take_all_trash_cans_.add(result) if isdir(result) else None

    return take_all_trash_cans_
