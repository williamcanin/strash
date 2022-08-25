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
from subprocess import check_output
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
    "dependencies": ["find", "shred", "gio", "sed"],
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

{CONFIG['appname']} © 2018-{date.today().year} - All Right Reserved.
Home: http://github.com/williamcanin/strash
"""


class Strash:
    @staticmethod
    def credits():
        """
        Function to show credits.
        """

        print(CREDITS)

    @staticmethod
    def take_all_trash_cans() -> set:
        """
        Function to get all ROOT directory from recycle bins on devices
        """

        # unix: gio list trash: | sed 's/\\/\//g; s/%20/ /g; s/^/"/g; s/$/"/g; s/files\/.*$/files\//g' | sort -u
        out = check_output("gio list trash:", shell=True, universal_newlines=True)
        take_all_trash_cans_ = set()

        for i in out.split():

            # Replace backslashes with forward slashes
            bar_ = sub(r"\\", r"/", i)

            # Replace character %20 with space
            space_ = sub(r"%20", r" ", bar_)

            # Get the root folder of the recycle bins
            result = sub(r"files/.*$", r"files/", space_)

            take_all_trash_cans_.add(result) if isdir(result) else None

        return take_all_trash_cans_

    @staticmethod
    def command(dir_) -> str:
        return f'find "{dir_}" -depth -type f -exec shred -v -n 4 -z -u {{}} \\;'

    def verify_user(self, uid) -> bool(object):
        """
        Function to check if script is running with superuser.
        """

        if os.geteuid() == uid:
            print(f'{CONFIG["appname"]} can not be run with superuser (root). Aborted!')
            return False

        return True

    def python_version_required(self) -> bool(object):
        """
        Function to check the version of Python that this script uses.
        """

        try:
            if version_info[0] != CONFIG["python_version"]:
                raise Exception(
                    "You are not using a version of Python that the script supports. "
                    + "Must be using Python {}.".format(CONFIG["python_version"])
                )
            return True
        except Exception as err:
            print("Error!", err)

    def verify_dependencies(self) -> bool(object):
        """
        Function to check script dependencies.
        """

        for item in CONFIG["dependencies"]:
            if not isfile("/usr/bin/" + item):
                raise Exception(f"The following dependencies are missing: {item}")
        return True

    def clean(self) -> bool(object):
        # print("Cleaning the trash can safely ...")

        path_trash_user = join(CONFIG["userhome"], ".local/share/Trash/files/")
        clean_trash_user = self.command(path_trash_user)

        try:
            # Clearing the system's default recycle bin.
            check_output(clean_trash_user, shell=True, universal_newlines=True)

            # Clearing other trash cans from other devices
            for item in self.take_all_trash_cans():
                check_output(self.command(item), shell=True, universal_newlines=True)

            # Cleaning up blank folders
            check_output("gio trash --empty", shell=True, universal_newlines=True)

            # print("Done!")
            return True
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
                "-k",
                "--kill",
                action="store_true",
                help="clean the trash safely and close the terminal.",
            )
            parser.add_argument(
                "-c",
                "--credits",
                action="store_true",
                help="show credits.",
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

        if self.menu().credits:
            self.credits()
        elif self.menu().kill:
            self.clean()
            # Closed console
            os.kill(os.getppid(), signal.SIGHUP)
        elif not self.menu().credits and not self.menu().kill:
            self.clean()


if __name__ == "__main__":
    s = Strash()
    s.main()
