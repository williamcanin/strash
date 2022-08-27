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

    def __init__(self, message: str, os_name: str):
        self.os_name = os_name
        self.message = message
        super().__init__(f"{self.message}{self.os_name}")
