from ..constants import (
    BASE_URL,
)
from .models import CustomerMetadata, Customer
from ..base.client import BaseClient
from logging import getLogger
from ..utils.helpers import prepare_data
from typing import Optional

logger = getLogger(__name__)


class CustomerClient(BaseClient):
    def create(self, customer: Optional[CustomerMetadata | dict] = None, **kwargs) -> Customer:
        """creates a new customer using an or named arguments

        Args:
            customer (Optional[CustomerMetadata  |  dict], optional): You customer data, it can be \
            a dict, an instance of `abacatepay.customers.CustomerMetadata`.

        Returns:
            Customer: An instance of the new customer.
        """
        logger.debug(f"Creating customer with URL: {BASE_URL}/customer/create")

        json_data = prepare_data(customer or kwargs, CustomerMetadata)
        response = self._request(
            f"{BASE_URL}/customer/create",
            method="POST",
            json=json_data,
        )
        return Customer(**response.json()["data"])

    def list(self) -> list[Customer]:
        logger.debug(f"Listing customers with URL: {BASE_URL}/customer/list")
        response = self._request(f"{BASE_URL}/customer/list", method="GET")
        return [Customer(**bill) for bill in response.json()["data"]]
