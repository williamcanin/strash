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
import signal
from os.path import join, expanduser, isfile, isdir
from datetime import date
from subprocess import check_output, PIPE, Popen
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
    def command(dir_, steps) -> str:
        """Function that stores the recycle bin cleanup code structure."""
        return f'{CONFIG["dep"][0]} "{dir_}" -depth -type f -exec {CONFIG["dep"][1]} -v -n {steps} -z -u {{}} \\;'

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

    def clean(self, steps) -> bool:
        """Function that performs the entire trash disposal operation."""

        path_trash_user = join(CONFIG["home"], ".local/share/Trash/files/")
        clean_trash_user = self.command(path_trash_user, steps)

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
                print("Cleaning the trash can safely ...")

                # Clearing the system's default recycle bin.
                check_output(clean_trash_user, shell=True, universal_newlines=True)

                # Clearing other trash cans from other devices
                for item in self.take_all_trash_cans(check):
                    cmd = self.command(item, steps)
                    check_output(cmd, shell=True, universal_newlines=True)

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
                help="clean the trash safely and close the terminal",
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

        iterations = self.menu().iterations

        if self.menu().credits:
            self.credits()
        elif self.menu().kill:
            self.clean(iterations)
            # Closed console
            os.kill(os.getppid(), signal.SIGHUP)
        elif not self.menu().credits and not self.menu().kill:
            self.clean(iterations)


if __name__ == "__main__":
    Strash().main()
