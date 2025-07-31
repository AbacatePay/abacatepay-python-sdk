from http import HTTPStatus
from typing import Literal

import requests


class APIError(Exception):
    """The exception was raised due to an API error."""

    message: str
    request: str

    def __init__(self, message: str, request: requests.Request) -> None:
        super().__init__(message)
        self.message = """The exception was raised due to an API error."""
        self.request = request

    def __str__(self) -> str:
        if self.message:
            return f'{self.message}'
        return ''


class APIStatusError(APIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: requests.Response
    status_code: int

    def __init__(self, message: str = '', *, response: requests.Response) -> None:
        super().__init__(message, response.request)
        self.response = response
        self.status_code = response.status_code


class ForbiddenRequest(APIStatusError):
    """
    Means that the request was unsuccessful due to a forbidden request.
    Maybe your API key is wrong?
    """

    status_code: Literal[HTTPStatus.FORBIDDEN]

    def __init__(self, response: requests.Response, message: str = ''):
        super().__init__(message, response=response)
        self.message = (
            'Means that the request was unsuccessful due to a '
            'forbidden request. Maybe your API key is wrong?'
        )
        self.response = response
        self.status_code = HTTPStatus.FORBIDDEN

    def __str__(self) -> str:
        if self.message:
            return (
                f'{self.message} \n Status Code: {self.response.status_code}'
                f' | Response: {self.response.text}'
            )
        return str(self.response.content, 'utf-8')


class UnauthorizedRequest(APIStatusError):
    """
    Means that the request was unsuccessful due to a forbidden request.
    Maybe your API key doesn't have enought permissions
    """

    status_code: Literal[HTTPStatus.UNAUTHORIZED]

    def __init__(self, response: requests.Response, message: str = ''):
        super().__init__(message, response=response)
        self.message = (
            'Means that the request was unsuccessful due to a forbidden '
            "request. Maybe your API key doesn't have enought permissions"
        )
        self.response = response
        self.status_code = HTTPStatus.UNAUTHORIZED

    def __str__(self) -> str:
        if self.message:
            return (
                f'{self.message} | Status Code: {self.response.status_code}'
                f' | Response: {self.response.text}'
            )
        return str(self.response.content, 'utf-8')


class APIConnectionError(APIError):
    """The request was unsuccessful due to a connection error.
    Check your internet connection"""

    def __init__(
        self,
        *,
        message: str = (
            'The request was unsuccessful due to a connection error. Check your internet connection'
        ),
        request: requests.Request,
    ) -> None:
        super().__init__(message, request)


class APITimeoutError(APIConnectionError):
    """The request got timed out. You might try checking
    your internet connection."""

    def __init__(self, request: requests.Request) -> None:
        super().__init__(
            message='Request timed out. Check your internet connection',
            request=request,
        )


class BadRequestError(APIStatusError):
    """The request was unsuccessful due to a bad request.
    Maybe the request syntax is wrong"""

    status_code: Literal[HTTPStatus.BAD_REQUEST]

    def __init__(self, response: requests.Response) -> None:
        self.response = response
        self.status_code = HTTPStatus.BAD_REQUEST

    def __str__(self) -> str:
        return (
            f'The request was unsuccessful due to a bad request. '
            'Maybe the request syntax is wrong. Message error: '
            f'{self.response.json()}'
        )


class NotFoundError(APIStatusError):
    status_code: Literal[HTTPStatus.NOT_FOUND]

    def __init__(self, message: str = '', *, response: requests.Response) -> None:
        super().__init__(message, response=response)
        self.status_code = HTTPStatus.NOT_FOUND

    def __str__(self) -> str:
        return (
            'The request was unsuccessful due to a not found error. '
            f'Error status 404 | Requested URL: {self.response.url}'
        )


class InternalServerError(APIStatusError):
    """The request was unsuccessful due to an internal server error."""

    status_code: Literal[500] = 500

    def __init__(self, response: requests.Response) -> None:
        super().__init__(
            message=(
                'The request was unsuccessful due to an internal server error.'
                " It's not your fault, just try again later."
            ),
            response=response,
        )


def raise_for_status(response: requests.Response) -> None:
    code_exc_dict = {
        HTTPStatus.BAD_REQUEST: BadRequestError(response=response),
        HTTPStatus.UNAUTHORIZED: UnauthorizedRequest(response=response),
        HTTPStatus.FORBIDDEN: ForbiddenRequest(response=response),
        HTTPStatus.NOT_FOUND: NotFoundError(response=response),
        HTTPStatus.INTERNAL_SERVER_ERROR: InternalServerError(response=response),
    }

    code = response.status_code
    if code == HTTPStatus.OK:
        return

    if code not in code_exc_dict and code >= HTTPStatus.BAD_REQUEST:
        raise APIStatusError(message=response.text, response=response)

    raise code_exc_dict.get(
        response.status_code,
        APIError(message=response.text, request=response.request),
    )
