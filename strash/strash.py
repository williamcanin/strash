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
from tkinter.messagebox import askyesno
from subprocess import CalledProcessError
from argparse import ArgumentParser, RawTextHelpFormatter

from utils.catches import trash_roots, take_all_trash_cans
from utils.commands import (
    shred_cli,
    shred_run_recursive,
    delete_folders_empty,
)
from utils.subprocess import command
from utils.checking import (
    verify_os,
    ignore_superuser,
    pyversion_required,
    verify_dependencies,
    lang_sys,
)
from __init__ import CONFIG, LANG

# # Import for debugging.
# from pdb import set_trace


# Strash class
class Strash:
    def credits(self):
        """Method to show credits."""

        CREDITS = f"""
            *************************
            {CONFIG['appname'][0]} - {LANG[lang_sys(LANG)]["str18"]} {CONFIG['appversion']}
            *************************

            {LANG[lang_sys(LANG)]["str19"]}:

            {LANG[lang_sys(LANG)]["str20"]}: {CONFIG['author1']['name']}
            E-Mail: {CONFIG['author1']['email']}
            {LANG[lang_sys(LANG)]["str21"]}: {CONFIG['author1']['website']}
            GitHub: {CONFIG['author1']['github']}
            {LANG[lang_sys(LANG)]["str22"]}: {CONFIG['author1']['locale']}

            {LANG[lang_sys(LANG)]["str23"]}:
            > {CONFIG["dep"]}

            {LANG[lang_sys(LANG)]["str11"]}
            {LANG[lang_sys(LANG)]["str24"]}: {CONFIG["url"]}
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
            print(LANG[lang_sys(LANG)]["str1"])
            if isdir(obj):
                shred_run_recursive(command, obj, iterations, CONFIG["appname"][1])
                delete_folders_empty(obj)
            else:
                command(shred_cli(obj, iterations), CONFIG["appname"][1])

            print(LANG[lang_sys(LANG)]["done"])

        try:
            if not yes:
                answer = askyesno(
                    title=LANG[lang_sys(LANG)]["str2"],
                    message=LANG[lang_sys(LANG)]["str3"],
                )
                if answer:
                    core()
                    return True
                return False

            core()

            if close_term:
                os.kill(os.getppid(), signal.SIGHUP)

        except CalledProcessError:
            print(LANG[lang_sys(LANG)]["str4"])
            exit(1)

    def clean_trash(self, iterations: str, close_term: bool = False) -> bool:
        """Function that performs the entire trash disposal operation."""

        try:

            # If there is a full trash can, do the whole process.
            list_trash = trash_roots("gio list trash:")
            if list_trash:
                print(LANG[lang_sys(LANG)]["str5"])

                # Clearing the system's default recycle bin.
                shred_run_recursive(
                    command,
                    CONFIG["trash_user"],
                    iterations,
                    CONFIG["appname"][1],
                )

                # Clearing other trash cans from other devices
                for trash_path in take_all_trash_cans(list_trash):
                    shred_run_recursive(
                        command,
                        trash_path,
                        iterations,
                        CONFIG["appname"][1],
                    )

                    # Cleaning up blank folders
                    delete_folders_empty(trash_path, istrash=True)

                print(LANG[lang_sys(LANG)]["done"])

                if close_term:
                    os.kill(os.getppid(), signal.SIGHUP)

                return True

            # Show message only if all recycle bins are empty.
            print(LANG[lang_sys(LANG)]["str6"])

        except Exception as err:
            print(LANG[lang_sys(LANG)]["str7"], err)
            exit(1)
        except PermissionError as err:\
            print(LANG[lang_sys(LANG)]["str8"], err)
            exit(1)

    def menu(self) -> dict:
        """Method to create menu."""

        try:
            parser = ArgumentParser(
                prog=CONFIG["appname"][0],
                usage=LANG[lang_sys(LANG)]["str9"],
                description=LANG[lang_sys(LANG)]["str10"],
                formatter_class=RawTextHelpFormatter,
                epilog=LANG[lang_sys(LANG)]["str11"],
            )
            parser.add_argument(
                "-p",
                "--path",
                action="store",
                metavar="",
                help=LANG[lang_sys(LANG)]["str12"],
            )
            parser.add_argument(
                "-y",
                "--yes",
                action="store_true",
                help=LANG[lang_sys(LANG)]["str13"],
            )
            parser.add_argument(
                "-n",
                "--iterations",
                action="store",
                default="3",
                metavar="",
                help=LANG[lang_sys(LANG)]["str14"],
            )
            parser.add_argument(
                "-k",
                "--kill",
                action="store_true",
                help=LANG[lang_sys(LANG)]["str15"],
            )
            parser.add_argument(
                "-c",
                "--credits",
                action="store_true",
                help=LANG[lang_sys(LANG)]["str16"],
            )
            parser.add_argument(
                "--version",
                action="store_true",
                help=LANG[lang_sys(LANG)]["str25"],
            )
            args = parser.parse_args()
            return vars(args)

        except Exception as err:
            print(LANG[lang_sys(LANG)]["str17"], err)

    def main(self):
        """Method main. Where the logic will be."""

        # Verifications
        verify_os(LANG[lang_sys(LANG)]["InvalidOS"])
        ignore_superuser(LANG[lang_sys(LANG)]["ApproachedUser"])
        pyversion_required(
            CONFIG["pyversion"], LANG[lang_sys(LANG)]["IncompatibleVersion"]
        )
        verify_dependencies(LANG[lang_sys(LANG)]["AbsentDependency"], CONFIG["dep"])

        # Get values parameters
        credits = self.menu()["credits"]
        version = self.menu()["version"]
        iterations = self.menu()["iterations"]
        path = self.menu()["path"]
        close_term = self.menu()["kill"]
        yes = self.menu()["yes"]

        # Check used option
        if credits:
            self.credits()
        elif version:
            print(f'{CONFIG["appname"][0]}: {CONFIG["appversion"]}')
        elif path:
            self.clean_path(path, iterations, yes=yes, close_term=close_term)
        else:
            self.clean_trash(iterations, close_term=close_term)


if __name__ == "__main__":
    Strash().main()
