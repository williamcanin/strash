import os
import locale
from os.path import isfile
from utils.exceptions import IncompatibleVersion, AbsentDependency, InvalidOS
from sys import version_info


def verify_os(appname: str) -> bool:
    """To verify OS (Compatible with Posix)."""

    if os.name != "posix":
        raise InvalidOS(appname, os.name)
    return True


def ignore_superuser(appname: str) -> bool:
    """To check if script is running with superuser."""

    if os.geteuid() == 0:
        raise PermissionError(
            f'"{appname}" can not be run with superuser (root) with ID 0. Aborted!'
        )
    return True


def pyversion_required(pyversion: str, appname: str) -> bool:
    """To check the version of Python that this script uses."""

    if version_info[0] != pyversion:
        raise IncompatibleVersion(appname, pyversion)
    return True


def verify_dependencies(dependencies: tuple) -> bool:
    """To check script dependencies."""

    for pkg in dependencies:
        if not isfile(f"/usr/bin/{pkg}"):
            raise AbsentDependency(pkg)
    return True


def lang_sys(languages: dict) -> str:
    lang = locale.getdefaultlocale()[0]
    if lang in languages:
        return lang
    return "en_US"
