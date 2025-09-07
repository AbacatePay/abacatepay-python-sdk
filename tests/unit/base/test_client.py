from http import HTTPStatus as status

import pytest

import httpx

from requests import Response
from requests.exceptions import ConnectionError, Timeout

from abacatepay.base.client import BaseClient, BaseAsyncClient
from abacatepay.utils.exceptions import (
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
async_client = BaseAsyncClient('fake-api-key')


STATUS_TO_EXCEPTION = [
    (status.BAD_REQUEST, BadRequestError),
    (status.FORBIDDEN, ForbiddenRequest),
    (status.UNAUTHORIZED, UnauthorizedRequest),
    (status.NOT_FOUND, NotFoundError),
    (status.INTERNAL_SERVER_ERROR, InternalServerError),
    (status.IM_A_TEAPOT, APIError),
]


def test_request_return_the_response_if_status_200(responses):
    """test that the request returns the response if the status is 200"""

    responses.add(
        responses.GET,
        url,
        status=status.OK,
    )

    response = client._request(url, "GET")

    assert response is not None
    assert isinstance(response, Response)


@pytest.mark.asyncio
async def test_async_request_return_the_response_if_status_200(respx_mock):
    """test that the async request returns the response if the status is 200"""

    respx_mock.get(url).mock(
        return_value=httpx.Response(status.OK)
    )

    response = await async_client._request(url, "GET")

    assert response is not None
    assert isinstance(response, httpx.Response)


@pytest.mark.parametrize('status_code,exc_classname', STATUS_TO_EXCEPTION)


def test_request_raise_the_correct_exception_when_status_is_different_of_200(responses, exc_classname, status_code):
    """test that the request raises the correct exception when the status is different of 200"""

    responses.add(
        responses.GET,
        url,
        status=status_code,
    )
    
    with pytest.raises(exc_classname):
        client._request(url, "GET")


@pytest.mark.asyncio
@pytest.mark.parametrize('status_code,exc_classname', STATUS_TO_EXCEPTION)


async def test_async_request_raise_the_correct_exception_when_status_is_different_of_200(respx_mock, exc_classname, status_code):
    """test that the async request raises the correct exception when the status is different of 200"""

    respx_mock.get(url).mock(
        return_value=httpx.Response(status_code)
    )

    with pytest.raises(exc_classname):
        await async_client._request(url, "GET")


@pytest.mark.parametrize('requests_exc_class,api_exc_class', [
    (Timeout, APITimeoutError),
    (ConnectionError, APIConnectionError),
])


def test_request_override_requests_timeout_and_connection_error(mocker, requests_exc_class, api_exc_class):
    """test that the request overrides the requests timeout and connection error"""

    mocker.patch('abacatepay.base.client.requests.Session.send', side_effect=requests_exc_class)

    with pytest.raises(api_exc_class):
        client._request(url, "GET")


@pytest.mark.asyncio
@pytest.mark.parametrize('httpx_exc_class,api_exc_class', [
    (httpx.TimeoutException, APITimeoutError),
    (httpx.RequestError, APIConnectionError),
])


async def test_async_request_override_httpx_timeout_and_connection_error(mocker, httpx_exc_class, api_exc_class):
    """test that the async request overrides the httpx timeout and connection error"""

    request = httpx.Request('GET', url)
    exception_instance = httpx_exc_class("test", request=request)

    mocker.patch('abacatepay.base.client.httpx.AsyncClient.send', side_effect=exception_instance)

    with pytest.raises(api_exc_class):
        await async_client._request(url, "GET")
