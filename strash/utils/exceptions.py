# Exceptions class
from sys import version_info


class IncompatibleVersion(Exception):
    """Raised when the installed Python version is incompatible"""

    def __init__(self, appname, pyversion):
        self.pyversion = pyversion
        self.appname = appname
        self.message = (
            f"{self.appname} requires Python version {self.pyversion}. "
            f"Are you using version {version_info[0]}"
        )
        super().__init__(self.message)


class AbsentDependency(Exception):
    """Raised when there is a lack of dependency"""

    def __init__(self, pkg):
        self.pkg = pkg
        self.message = f"The following dependencies are missing: {self.pkg}"
        super().__init__(self.message)


class InvalidOS(Exception):
    """Created when OS is not posix"""

    def __init__(self, appname, os):
        self.os = os
        self.appname = appname
        self.message = f'{self.appname} is only compatible with "posix" systems. Your system is a: {self.os}'
        super().__init__(self.message)
