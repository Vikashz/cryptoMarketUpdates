class ApiUserException(Exception):
    """Base class for all exceptions related to api user"""


class ApiUserNotFound(ApiUserException):
    """api user not found"""
    pass
