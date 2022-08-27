from random import random
from os import rename, walk
from os.path import join
from shutil import rmtree
from subprocess import run


def shred_cli(filepath: str, iterations: str) -> str:
    """Returns a string for shred command for files"""
    return f'shred -n {iterations} -v -z -u "{filepath}";'


def delete_folders_empty(directory: str, istrash: bool = False) -> bool:
    """Bulk rename all empty folders and the root folder and then remove"""

    # Create a new name for the root folder
    new_root_name = str(random()).split(".")[1]

    # Go through the root folder
    for root, dirs, files in walk(directory, topdown=False):

        # If you don't have a file in the folders (which you shouldn't) start renaming
        if not files:
            for d in dirs:
                # Create a folder name
                new_name = str(random()).split(".")[1]
                # Get the path of the current folder
                path = join(root, d)
                # Create new path to new folder
                new_path = join(root, new_name)
                # rename folder
                rename(path, new_path)

    if not istrash:
        # Makes slicing taking the previous folder from the root
        slicing_root = "/".join(directory.split("/")[:-1])

        # Rename root folder
        rename(directory, join(slicing_root, new_root_name))

        # Remove root folder
        rmtree(join(slicing_root, new_root_name))

        return True

    run("gio trash --empty", shell=True, universal_newlines=True)

    return True


def shred_run_recursive(command, directory: str, iterations: str, appname: str) -> None:
    """Do all cleaning recursively in a given folder."""

    for root, _, files in walk(directory, topdown=False):
        for file in files:
            # Get current file
            filepath = join(root, file)

            command(shred_cli(filepath, iterations), appname)
