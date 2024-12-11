import requests
from typing import Literal


class APIError(Exception):
    """The exception was raised due to an API error."""

    message: str
    request: str

    def __init__(self, message: str, request: requests.Request) -> None:
        super().__init__(message)
        self.message = """The exception was raised due to an API error."""
        self.request = request

    def __str__(self):
        if self.message:
            return f"{self.message}"


class APIStatusError(APIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: requests.Response
    status_code: int

    def __init__(
        self, message: str | None = None, *, response: requests.Response
    ) -> None:
        super().__init__(message, response.request)
        self.response = response
        self.status_code = response.status_code


class ForbiddenRequest(APIStatusError):
    """
    Means that the request was unsuccessful due to a forbidden request. Maybe your API key is wrong?
    """

    message: str | None
    status_code: Literal[401] = 401

    def __init__(self, response: requests.Response, message: str | None = None):
        super().__init__(message, response=response)
        self.message = "Means that the request was unsuccessful due to a forbidden request. Maybe your API key is wrong?"
        self.response = response
        self.status_code: Literal[401] = 401

    def __str__(self):
        if self.message:
            return f"{self.message} \n Status Code: {self.response.status_code} | Response: {self.response.text}"
        return self.response.content


class UnauthorizedRequest(APIStatusError):
    """
    Means that the request was unsuccessful due to a forbidden request. Maybe your API key doesn't have enought permissions
    """

    message: str | None
    status_code: Literal[403] = 403

    def __init__(self, response: requests.Response, message: str | None = None):
        super().__init__(message, response=response)
        self.message = "Means that the request was unsuccessful due to a forbidden request. Maybe your API key doesn't have enought permissions"
        self.response = response
        self.status_code: Literal[403] = 403

    def __str__(self):
        if self.message:
            return f"{self.message} | Status Code: {self.response.status_code} | Response: {self.response.text}"
        return self.response.content


class APIConnectionError(APIError):
    """The request was unsuccessful due to a connection error. Check your internet connection"""

    def __init__(
        self,
        *,
        message: str = "The request was unsuccessful due to a connection error. Check your internet connection",
        request: requests.Request,
    ) -> None:
        super().__init__(message, request)


class APITimeoutError(APIConnectionError):
    """The request got timed out. You might try checking your internet connection."""

    def __init__(self, request: requests.Request) -> None:
        super().__init__(
            message="Request timed out. Check your internet connection", request=request
        )


class BadRequestError(APIStatusError):
    """The request was unsuccessful due to a bad request. Maybe the request syntax is wrong"""

    status_code: Literal[400] = 400

    def __init__(self, response: requests.Response) -> None:
        self.response = response

    def __str__(self):
        return f"The request was unsuccessful due to a bad request. Maybe the request syntax is wrong. Message error: {self.response.json()}"


class NotFoundError(APIStatusError):
    status_code: Literal[404] = 404

    def __str__(self):
        return """The request was unsuccessful due to a not found error. Error status 404 | Requested URL: {}""".format(
            self.response.url
        )


class InternalServerError(APIStatusError):
    """The request was unsuccessful due to an internal server error."""

    status_code: Literal[500] = 500

    def __init__(self, response: requests.Response) -> None:
        super().__init__(
            message="The request was unsuccessful due to an internal server error. It's not your fault, just try again later.",
            response=response,
        )


def raise_for_status(response: requests.Response) -> None:
    if response.status_code == 200:
        return

    elif response.status_code == 400:
        raise BadRequestError(response=response)

    elif response.status_code == 401:
        raise ForbiddenRequest(response=response)

    elif response.status_code == 403:
        raise UnauthorizedRequest(response=response)

    elif response.status_code == 404:
        raise NotFoundError(response=response)

    elif response.status_code == 500:
        raise InternalServerError(response=response)

    elif response.status_code >= 400:
        raise APIStatusError(message=response.text, response=response)

    raise APIError(message=response.text, request=response.request)
