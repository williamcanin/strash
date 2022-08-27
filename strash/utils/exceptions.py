class IncompatibleVersion(Exception):
    """Raised when the installed Python version is incompatible"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ApproachedUser(PermissionError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AbsentDependency(Exception):
    """Raised when there is a lack of dependency"""

    def __init__(self, message: str, package: str):
        self.package = package
        self.message = message
        super().__init__(f"{self.message}{self.package}")


class InvalidOS(Exception):
    """Created when OS is not posix"""

    def __init__(self, appname: str, os: str):
        self.os = os
        self.appname = appname
        self.message = f'{self.appname} is only compatible with "posix" systems. Your system is a: {self.os}'
        super().__init__(self.message)
