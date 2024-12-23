import requests
from typing import Literal
from ._constants import USERAGENT

class BaseClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

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
                "Authorization": f"Bearer {self.api_key}",
                "User-Agent": USERAGENT,
            },
            **kwargs,
        )
