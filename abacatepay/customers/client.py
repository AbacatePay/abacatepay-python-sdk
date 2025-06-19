from logging import getLogger
from typing import Any

from ..base.client import BaseClient
from ..constants import (
    BASE_URL,
)
from ..utils.helpers import prepare_data
from .models import Customer, CustomerMetadata

logger = getLogger(__name__)


class CustomerClient(BaseClient):
    def create(
        self,
        customer: CustomerMetadata | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Customer:
        """creates a new customer using an or named arguments

        Args:
            customer (Optional[CustomerMetadata  |  dict], optional): You
                customer data, it can be a dict, an instance of
                `abacatepay.customers.CustomerMetadata`.

        Returns:
            Customer: An instance of the new customer.
        """
        logger.debug(f'Creating customer with URL: {BASE_URL}/customer/create')

        json_data = prepare_data(customer or kwargs, CustomerMetadata)
        response = self._request(
            f'{BASE_URL}/customer/create',
            method='POST',
            json=json_data,
        )
        return Customer(**response.json()['data'])

    def list(self) -> list[Customer]:
        logger.debug(f'Listing customers with URL: {BASE_URL}/customer/list')
        response = self._request(f'{BASE_URL}/customer/list', method='GET')
        return [Customer(**bill) for bill in response.json()['data']]
