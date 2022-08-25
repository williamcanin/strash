#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Information:
#
# ******************************************************************************
# Type: Python Script
# Linux Compatibility: Linux distros
# Description: Script that cleans the trash safely without leaving a trace.
# Script Name: strash

# Author: William C. Canin
#   Contacts:
#   E-Mail: william.costa.canin@gmail.com
#   WebSite: https://williamcanin.github.io
#   GitHub: https://github.com/williamcanin
#   License: MIT.

import os
import signal
from os.path import join, expanduser, isfile, isdir
from datetime import date
from subprocess import check_output, PIPE, STDOUT, run, Popen, PIPE
from re import sub
from sys import version_info
from argparse import ArgumentParser, RawTextHelpFormatter

# # Import for debugging.
# from pdb import set_trace

CONFIG = {
    "appname": "strash",
    "appscript": "strash",
    "appversion": "0.2.0",
    "python_version": 3,
    "userhome": expanduser("~"),
    "dependencies": ["find", "shred", "gio"],
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
{CONFIG['appname']} - Version {CONFIG['appversion']}
*************************

Credits:

Author: {CONFIG['author1']['name']}
E-Mail: {CONFIG['author1']['email']}
Website: {CONFIG['author1']['website']}
GitHub: {CONFIG['author1']['github']}
Locale: {CONFIG['author1']['locale']}

Thanks dependencies:
> {CONFIG["dependencies"]}

{CONFIG['appname']} © 2018-{date.today().year} - All Right Reserved.
Home: http://github.com/williamcanin/strash
"""


# Exceptions class
class IncompatibleVersion(Exception):
    """Raised when the installed Python version is incompatible"""

    def __init__(
        self,
        pyversion,
        message="You are not using a version of Python that the script supports. "
        "Must be using Python: ",
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


# Strash class
class Strash:
    @staticmethod
    def credits():
        """
        Function to show credits.
        """

        print(CREDITS)

    @staticmethod
    def take_all_trash_cans(check) -> set:
        """
        Function to get all ROOT directory from recycle bins on devices
        """

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
        return f'find "{dir_}" -depth -type f -exec shred -v -n {steps} -z -u {{}} \\;'

    def verify_user(self, uid) -> bool(object):
        """
        Function to check if script is running with superuser.
        """

        if os.geteuid() == uid:
            raise PermissionError(
                f'"{CONFIG["appname"]}" can not be run with superuser (root). Aborted!'
            )
        return True

    def python_version_required(self) -> bool(object):
        """
        Function to check the version of Python that this script uses.
        """

        if version_info[0] != CONFIG["python_version"]:
            raise IncompatibleVersion(CONFIG["python_version"])
        return True

    def verify_dependencies(self) -> bool(object):
        """
        Function to check script dependencies.
        """

        for pkg in CONFIG["dependencies"]:
            if not isfile(f"/usr/bin/{pkg}"):
                raise AbsentDependency(pkg)
        return True

    def clean(self, steps) -> bool(object):
        # print("Cleaning the trash can safely ...")

        path_trash_user = join(CONFIG["userhome"], ".local/share/Trash/files/")
        clean_trash_user = self.command(path_trash_user, steps)

        try:
            p = Popen(
                "gio list trash:", shell=True, universal_newlines=True, stdout=PIPE
            )
            check = p.communicate()[0]
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
            print("All empty trash.")
        except Exception as err:
            print("There was an error with the program code !!!", err)
            return False

    def menu(self):
        """
        Function to create menu.
        """

        try:
            parser = ArgumentParser(
                prog=CONFIG["appname"],
                usage=f"{CONFIG['appscript']} [options]",
                description=f'{CONFIG["appname"].title()} that cleans the trash safely without leaving a trace.',
                formatter_class=RawTextHelpFormatter,
                epilog=f"{CONFIG['appname']} © 2018-{date.today().year} - All Right Reserved.",
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
        """
        Function main. Where the logic will be.
        """

        self.python_version_required()
        self.verify_user(0)
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
    s = Strash()
    s.main()
