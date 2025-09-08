from typing import Any, Literal

import httpx
import requests

from ..constants import USER_AGENT
from ..utils.exceptions import (
    APIConnectionError,
    APITimeoutError,
    raise_for_status,
)


class BaseClient:
    def __init__(self, api_key: str):
        self.__api_key = api_key

    def _request(
        self,
        url: str,
        method: Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] = 'GET',
        **kwargs: Any,
    ) -> requests.Response:
        request = requests.Request(
            method,
            url,
            headers={
                'Authorization': f'Bearer {self.__api_key}',
                'User-Agent': USER_AGENT,
            },
            **kwargs,
        )
        try:
            prepared_request = request.prepare()
            with requests.Session() as s:
                response = s.send(prepared_request)

            raise_for_status(response)
            return response

        except requests.exceptions.Timeout:
            raise APITimeoutError(request=request)

        except requests.exceptions.ConnectionError:
            raise APIConnectionError(message='Connection error.', request=request)


class BaseAsyncClient:
    def __init__(self, api_key: str):
        self.__api_key = api_key

    async def _request(
        self,
        url: str,
        method: Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] = 'GET',
        **kwargs: Any,
    ) -> httpx.Response:
        request = httpx.Request(
            method,
            url,
            headers={
                'Authorization': f'Bearer {self.__api_key}',
                'User-Agent': USER_AGENT,
            },
            **kwargs,
        )

        try:
            async with httpx.AsyncClient() as client:
                response = await client.send(request)

            raise_for_status(response)
            return response

        except httpx.TimeoutException:
            raise APITimeoutError(request=request)

        except httpx.RequestError:
            raise APIConnectionError(message='Connection error.', request=request)
