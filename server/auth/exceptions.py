from http import HTTPStatus


class ApiException(Exception):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        if status_code:
            self.status_code = status_code


class IncorrectPasswordException(ApiException):
    # default status code, of course can be overwritten by constructor call
    status_code = HTTPStatus.BAD_REQUEST

