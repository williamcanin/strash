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
from textwrap import dedent
from os.path import isdir
from datetime import date
from tkinter.messagebox import askyesno
from subprocess import CalledProcessError
from argparse import ArgumentParser, RawTextHelpFormatter

from utils.catches import trash_roots, take_all_trash_cans
from utils.commands import (
    str__shred_file_recursive,
    str__shred_file,
    str__delete_folder_empty,
)
from utils.subprocess import command
from utils.checking import (
    verify_os,
    ignore_superuser,
    pyversion_required,
    verify_dependencies,
)
from __init__ import CONFIG

# # Import for debugging.
# from pdb import set_trace


# Strash class
class Strash:
    def credits(self):
        """Method to show credits."""

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

        print(dedent(CREDITS))

    def clean_path(
        self,
        obj: str,
        iterations: str,
        yes: bool = False,
        close_term: bool = False,
    ):
        """This method performs safe cleaning of a directory (recursively) or a specified file."""

        def core():
            print(">>> Starting Safe Removal...")
            if isdir(obj):
                command(
                    str__shred_file_recursive(obj, iterations), CONFIG["appname"][1]
                )
                command(str__delete_folder_empty(obj), CONFIG["appname"][1])
            else:
                command(str__shred_file(obj, iterations), CONFIG["appname"][1])

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

            if close_term:
                os.kill(os.getppid(), signal.SIGHUP)

        except CalledProcessError:
            print(">>> ERRO: Incorrect directory path or file path.")
            exit(1)

    def clean_trash(self, iterations: str, close_term: bool = False) -> bool:
        """Function that performs the entire trash disposal operation."""

        try:

            # If there is a full trash can, do the whole process.
            list_trash = trash_roots("gio list trash:")
            if list_trash:
                print(">>> Cleaning the trash can safely...")

                # Clearing the system's default recycle bin.
                trash_user_command = str__shred_file_recursive(
                    CONFIG["trash_user"], iterations
                )
                command(trash_user_command, CONFIG["appname"][1])

                # Clearing other trash cans from other devices
                for item in take_all_trash_cans(list_trash):
                    cmd = str__shred_file_recursive(item, iterations)
                    command(cmd, CONFIG["appname"][1])

                    # Cleaning up blank folders
                    blank = str__delete_folder_empty(item)
                    command(blank, CONFIG["appname"][1])

                print("Done!")

                if close_term:
                    os.kill(os.getppid(), signal.SIGHUP)

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
        """Method to create menu."""

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
            print("Error in passing arguments...", err)

    def main(self):
        """Method main. Where the logic will be."""

        # Verifications
        verify_os(CONFIG["appname"][0])
        ignore_superuser(CONFIG["appname"][0])
        pyversion_required(CONFIG["pyversion"], CONFIG["appname"][0])
        verify_dependencies(CONFIG["dep"])

        # Get values parameters
        credits = self.menu().credits
        iterations = self.menu().iterations
        path = self.menu().path
        close_term = self.menu().kill
        yes = self.menu().yes

        # Check used option
        if credits:
            self.credits()
        elif path:
            self.clean_path(path, iterations, yes=yes, close_term=close_term)
        else:
            self.clean_trash(iterations, close_term=close_term)


if __name__ == "__main__":
    Strash().main()
