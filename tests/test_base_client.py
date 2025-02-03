from http import HTTPStatus as status

import pytest
from requests import Response
from requests.exceptions import ConnectionError, Timeout

from abacatepay._base_client import BaseClient
from abacatepay.utils._exceptions import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    BadRequestError,
    ForbiddenRequest,
    InternalServerError,
    NotFoundError,
    UnauthorizedRequest,
)

url = "https://api.abacatepay.com/v1/billing/list"
client = BaseClient('fake-api-key')


def test_request_return_the_response_if_status_200(responses):
    responses.add(
        responses.GET,
        url,
        status=status.OK,
    )

    response = client._request(url, "GET")

    assert response is not None
    assert isinstance(response, Response)


@pytest.mark.parametrize('status_code,exc_classname', [
    (status.BAD_REQUEST, BadRequestError),
    (status.FORBIDDEN, ForbiddenRequest),
    (status.UNAUTHORIZED, UnauthorizedRequest),
    (status.NOT_FOUND, NotFoundError),
    (status.INTERNAL_SERVER_ERROR, InternalServerError),
    (status.IM_A_TEAPOT, APIError)
])
def test_request_raise_the_correct_exception_when_status_is_different_of_200(responses, exc_classname, status_code):
    responses.add(
        responses.GET,
        url,
        status=status_code,
    )
    
    with pytest.raises(exc_classname):
        client._request(url, "GET")


@pytest.mark.parametrize('requests_exc_class,api_exc_class', [
    (Timeout, APITimeoutError),
    (ConnectionError, APIConnectionError),
])
def test_request_override_requests_timeout_and_connection_error(mocker, requests_exc_class, api_exc_class):
    mocker.patch('abacatepay._base_client.requests.Session.send', side_effect=requests_exc_class)
    with pytest.raises(api_exc_class):
        client._request(url, "GET")
