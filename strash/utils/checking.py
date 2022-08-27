import os
from os.path import isfile
from utils.exceptions import IncompatibleVersion, AbsentDependency, InvalidOS
from sys import version_info


def verify_os(appname: str) -> bool:
    """Method to verify OS (Compatible with Posix)."""

    if os.name != "posix":
        raise InvalidOS(appname, os.name)
    return True


def ignore_superuser(appname: str) -> bool:
    """Method to check if script is running with superuser."""

    if os.geteuid() == 0:
        raise PermissionError(
            f'"{appname}" can not be run with superuser (root) with ID 0. Aborted!'
        )
    return True


def pyversion_required(pyversion: str, appname: str) -> bool:
    """Method to check the version of Python that this script uses."""

    if version_info[0] != pyversion:
        raise IncompatibleVersion(appname, pyversion)
    return True


def verify_dependencies(dependencies: tuple) -> bool:
    """Method to check script dependencies."""

    for pkg in dependencies:
        if not isfile(f"/usr/bin/{pkg}"):
            raise AbsentDependency(pkg)
    return True
