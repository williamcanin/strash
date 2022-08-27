import os
import locale
from os.path import isfile
from utils.exceptions import (
    IncompatibleVersion,
    AbsentDependency,
    InvalidOS,
    ApproachedUser,
)
from sys import version_info


def verify_os(appname: str) -> bool:
    """To verify OS (Compatible with Posix)."""

    if os.name != "posix":
        raise InvalidOS(appname, os.name)
    return True


def ignore_superuser(message: str) -> bool:
    """To check if script is running with superuser."""

    if os.geteuid() == 0:
        raise ApproachedUser(message)

    return True


def pyversion_required(pyversion: str, message: str) -> bool:
    """To check the version of Python that this script uses."""

    if version_info[0] != pyversion:
        raise IncompatibleVersion(message)

    return True


def verify_dependencies(message: str, dependencies: tuple) -> bool:
    """To check script dependencies."""

    for package in dependencies:
        if not isfile(f"/usr/bin/{package}"):
            raise AbsentDependency(f"{message}{package}")

    return True


def lang_sys(languages: dict) -> str:
    """Get the language of the operating system."""

    lang = locale.getdefaultlocale()[0]

    if lang in languages:
        return lang

    return "en_US"
