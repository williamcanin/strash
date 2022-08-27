from os.path import isdir
from re import sub
from subprocess import Popen, PIPE


def take_all_trash_cans(gio) -> set:
    """Function to get all ROOT directory from recycle bins on devices."""

    take_all_trash_cans_ = set()

    p = Popen(gio, shell=True, universal_newlines=True, stdout=PIPE)
    list_trash = p.communicate()[0]

    for i in list_trash.split():

        # unix: gio list trash: | sed 's/\\/\//g; s/%20/ /g; s/^/"/g; s/$/"/g; s/files\/.*$/files\//g' | sort -u
        # Replace backslashes with forward slashes
        bar_ = sub(r"\\", r"/", i)

        # Replace character %20 with space
        space_ = sub(r"%20", r" ", bar_)

        # Get the root folder of the recycle bins
        result = sub(r"files/.*$", r"files/", space_)

        take_all_trash_cans_.add(result) if isdir(result) else None

    return take_all_trash_cans_
