#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Information:
#
# ******************************************************************************
# Type: Python
# Linux Compatibility: Linux distros
# Description: Script that cleans the trash safely without leaving a trace.
# Script Name: strash

# Author: William C. Canin
#   Contacts:
#   Personal page: https://williamcanin.github.io
#   GitHub: https://github.com/williamcanin

import os
import sys
import signal
from os.path import join, expanduser, isfile, isdir
from datetime import date
from tkinter.messagebox import askyesno
from subprocess import (
    PIPE,
    STDOUT,
    Popen,
    CalledProcessError,
)
from re import sub
from sys import version_info
from argparse import ArgumentParser, RawTextHelpFormatter


# # Import for debugging.
# from pdb import set_trace

CONFIG = {
    "appname": ["sTrash", "strash"],  # Application/Script name
    "appversion": "0.2.0",  # Version script
    "pyversion": 3,  # Python version required
    "home": expanduser("~"),  # HOME user
    "dep": ["find", "shred", "gio"],  # Dependencies
    "author1": {
        "name": "William C. Canin",
        "email": "william.costa.canin@gmail.com",
        "website": "https://williamcanin.github.io",
        "github": "https://github.com/williamcanin",
        "locale": "Brasil - SP",
    },
}

CREDITS = f"""
*************************
{CONFIG['appname'][0]} - Version {CONFIG['appversion']}
*************************

Credits:

Author: {CONFIG['author1']['name']}
E-Mail: {CONFIG['author1']['email']}
Website: {CONFIG['author1']['website']}
GitHub: {CONFIG['author1']['github']}
Locale: {CONFIG['author1']['locale']}

Thanks dependencies:
> {CONFIG["dep"]}

{CONFIG['appname'][0]} © 2018-{date.today().year} - All Right Reserved.
Home: http://github.com/williamcanin/strash
"""


# Exceptions class
class IncompatibleVersion(Exception):
    """Raised when the installed Python version is incompatible"""

    def __init__(
        self,
        pyversion,
        message=f"{CONFIG['appname'][0]} requires Python version {CONFIG['pyversion']}."
        f"Are you using version {version_info[0]}",
    ):
        self.pyversion = pyversion
        self.message = message
        super().__init__(f"{self.message}{self.pyversion}")


class AbsentDependency(Exception):
    """Raised when there is a lack of dependency"""

    def __init__(self, pkg, message="The following dependencies are missing: "):
        self.pkg = pkg
        self.message = message
        super().__init__(f"{self.message}{self.pkg}")


class InvalidOS(Exception):
    """Created when OS is not posix"""

    def __init__(
        self,
        os,
        message=f"{CONFIG['appname'][0]} is only compatible with \"posix\" systems."
        "Your system is a: ",
    ):
        self.os = os
        self.message = message
        super().__init__(f"{self.message}{self.os}")


# Strash class
class Strash:
    @staticmethod
    def credits():
        """Function to show credits."""

        print(CREDITS)

    @staticmethod
    def take_all_trash_cans(check) -> set:
        """Function to get all ROOT directory from recycle bins on devices."""

        take_all_trash_cans_ = set()

        for i in check.split():

            # unix: gio list trash: | sed 's/\\/\//g; s/%20/ /g; s/^/"/g; s/$/"/g; s/files\/.*$/files\//g' | sort -u
            # Replace backslashes with forward slashes
            bar_ = sub(r"\\", r"/", i)

            # Replace character %20 with space
            space_ = sub(r"%20", r" ", bar_)

            # Get the root folder of the recycle bins
            result = sub(r"files/.*$", r"files/", space_)

            take_all_trash_cans_.add(result) if isdir(result) else None

        return take_all_trash_cans_

    @staticmethod
    def code_shred_dir(obj, iterations) -> str:
        """Function that stores the recycle bin cleanup code structure."""
        return f'{CONFIG["dep"][0]} "{obj}" -depth -type f -exec {CONFIG["dep"][1]} -n {iterations} -v -z -u {{}} \\;'

    @staticmethod
    def code_shred_file(obj, iterations) -> str:
        """Returns a string for shred command for files"""
        return f"{CONFIG['dep'][1]} -n {iterations} -v -z -u {obj};"

    @staticmethod
    def code_empty(obj) -> str:
        """Function that returns string to delete empty folders."""
        return f'{CONFIG["dep"][0]} "{obj}" -type d -empty -delete'

    @staticmethod
    def command(cmd):
        p = Popen(
            cmd,
            stdout=PIPE,
            stderr=STDOUT,
            shell=True,
            universal_newlines=True,
        )
        for line in p.stdout:
            out = sub(r"shred:", rf"{CONFIG['appname'][1]}:", line)
            sys.stdout.write(out)

    @staticmethod
    def verify_os() -> bool:
        """Function to verify OS (Compatible with Posix)."""

        if os.name != "posix":
            raise InvalidOS(os.name)
        return True

    @staticmethod
    def ignore_superuser() -> bool:
        """Function to check if script is running with superuser."""

        if os.geteuid() == 0:
            raise PermissionError(
                f'"{CONFIG["appname"][0]}" can not be run with superuser (root) with ID 0. Aborted!'
            )
        return True

    def pyversion_required(self) -> bool:
        """Function to check the version of Python that this script uses."""

        if version_info[0] != CONFIG["pyversion"]:
            raise IncompatibleVersion(CONFIG["pyversion"])
        return True

    def verify_dependencies(self) -> bool:
        """Function to check script dependencies."""

        for pkg in CONFIG["dep"]:
            if not isfile(f"/usr/bin/{pkg}"):
                raise AbsentDependency(pkg)
        return True

    def clean_object(self, obj, iterations, yes=False):
        """This function performs safe cleaning of a directory (recursively) or a specified file."""

        def core():
            print(">>> Starting Safe Removal...")
            if isdir(obj):
                clean_dir = self.code_shred_dir(obj, iterations)
                self.command(clean_dir)
                empty_dir = self.code_empty(obj)
                self.command(empty_dir)
            else:
                clean_file = self.code_shred_file(obj, iterations)
                self.command(clean_file)

            print("Done!")

        try:
            if not yes:
                answer = askyesno(
                    title="confirmation",
                    message="Do you really want to permanently safely remove this object(s)?",
                )
                if answer:
                    core()
                    return True
                return False
            core()
        except CalledProcessError:
            print(">>> ERRO: Incorrect directory path or file path.")
            exit(1)

    def clean_trash(self, iterations) -> bool:
        """Function that performs the entire trash disposal operation."""

        path_trash_user = join(CONFIG["home"], ".local/share/Trash/files/")
        clean_trash_user = self.code_shred_dir(path_trash_user, iterations)

        try:
            p = Popen(
                f"{CONFIG['dep'][2]} list trash:",
                shell=True,
                universal_newlines=True,
                stdout=PIPE,
            )

            # Checks if there is a recycle bin with content
            check = p.communicate()[0]

            # If there is a full trash can, do the whole process.
            if check:
                print(">>> Cleaning the trash can safely...")

                # Clearing the system's default recycle bin.
                self.command(clean_trash_user)

                # Clearing other trash cans from other devices
                for item in self.take_all_trash_cans(check):
                    cmd = self.code_shred_dir(item, iterations)
                    self.command(cmd)

                # Cleaning up blank folders
                Popen("gio trash --empty", shell=True)

                print("Done!")

                return True

            # Show message only if all recycle bins are empty.
            print("All empty trash. :)")

        except Exception as err:
            print(
                f"An unexpected error occurred that {CONFIG['appname'][0]} cannot identify.",
                err,
            )
            exit(1)
        except PermissionError as err:
            print(f"{CONFIG['appname'][0]} is not allowed to perform the tasks.", err)
            exit(1)

    def menu(self):
        """Function to create menu."""

        try:
            parser = ArgumentParser(
                prog=CONFIG["appname"][0],
                usage=f"{CONFIG['appname'][1]} [options]",
                description=f'{CONFIG["appname"][0]} that cleans the trash safely without leaving a trace.',
                formatter_class=RawTextHelpFormatter,
                epilog=f"{CONFIG['appname'][0]} © 2018-{date.today().year} - All Right Reserved.",
            )
            parser.add_argument(
                "-p",
                "--path",
                action="store",
                metavar="",
                help="removes a specified (recursive) folder or file",
            )
            parser.add_argument(
                "-y",
                "--yes",
                action="store_true",
                help="do not show dialog for action confirmation. (Just for --path option)",
            )
            parser.add_argument(
                "-n",
                "--iterations",
                action="store",
                default="3",
                metavar="",
                help="overwrites N times instead of 3, the default",
            )
            parser.add_argument(
                "-k",
                "--kill",
                action="store_true",
                help="safely remove and close the terminal (Only for Terminal)",
            )
            parser.add_argument(
                "-c",
                "--credits",
                action="store_true",
                help="show credits",
            )
            args = parser.parse_args()
            return args

        except Exception as err:
            print("Error in passing arguments..", err)

    def main(self):
        """Function main. Where the logic will be."""

        self.verify_os()
        self.pyversion_required()
        self.ignore_superuser()
        self.verify_dependencies()

        credits = self.menu().credits
        iterations = self.menu().iterations
        path = self.menu().path
        kill = self.menu().kill
        yes = self.menu().yes

        if credits:
            self.credits()
        elif path:
            self.clean_object(path, iterations, yes=yes)
            if kill:
                os.kill(os.getppid(), signal.SIGHUP)
            return True
        else:
            self.clean_trash(iterations)


if __name__ == "__main__":
    Strash().main()
