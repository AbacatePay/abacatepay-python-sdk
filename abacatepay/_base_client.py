import requests
from typing import Literal
from ._constants import USER_AGENT

class BaseClient:
    def __init__(self, api_key: str):
        self.__api_key = api_key

    def _request(
        self,
        url: str,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"] = "GET",
        **kwargs,
    ):
        return requests.request(
            method,
            url,
            headers={
                "Authorization": f"Bearer {self.__api_key}",
                "User-Agent": USER_AGENT,
            },
            **kwargs,
        )
