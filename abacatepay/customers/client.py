from ..constants import (
    BASE_URL,
)
from .models import CustomerMetadata, Customer
from ..base.client import BaseClient
from logging import getLogger

logger = getLogger(__name__)


class CustomerClient(BaseClient):
    def create(self, customer: CustomerMetadata) -> Customer:
        logger.debug(f"Creating customer with URL: {BASE_URL}/customer/create")
        response = self._request(
            f"{BASE_URL}/customer/create",
            method="POST",
            json=customer.model_dump(by_alias=True),
        )
        return Customer(**response.json()["data"])

    def list(self) -> list[Customer]:
        logger.debug(f"Listing customers with URL: {BASE_URL}/customer/list")
        response = self._request(f"{BASE_URL}/customer/list", method="GET")
        return [Customer(**bill) for bill in response.json()["data"]]
