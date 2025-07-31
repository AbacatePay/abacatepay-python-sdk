from logging import getLogger
from typing import Any

from ..base.client import BaseClient
from ..constants import BASE_URL
from ..utils.helpers import prepare_data
from .models import Billing, BillingIn, BillingList

logger = getLogger(__name__)


class BillingClient(BaseClient):
    def create(self, data: BillingIn | dict[str, Any] | None = None, **kwargs: Any) -> Billing:
        """
        Create a new billing.

        Args:
            data (BillingIn | dict[str, Any] | None): an instance of
                `abacatepay.billings.models.BillingIn` a dict
                or the named params following the model schema.

        Keyword args:
            products (List[Product]): List of products to be billed.
            returnURL (str): The URL the user will be redirected to after the
                billing is completed.
            completionUrl (str): The URL the API will make a POST request after
                the billing is completed.
            methods (List[BILLING_METHODS]): The payment methods to be
                accepted. Defaults to ["PIX"].
            frequency (BILLING_KINDS): The frequency of the billing. Defaults
                to "ONE_TIME".
            customerId (str): The ID of the customer. If provided, the customer
                information won't be required.
            customer (CustomerMetadata): The customer information. If
                customerId is provided, this parameter is ignored.

        Returns:
            Billing: The response with the billing data.
        """
        json_data = prepare_data(data or kwargs, BillingIn)
        logger.debug('creating billing: %s', json_data)

        response = self._request(
            f'{BASE_URL}/billing/create',
            method='POST',
            json=json_data,
        )
        return Billing(**response.json()['data'])

    def list(self) -> BillingList:
        """
        List all bills.

        Returns:
            BillingList: A list of billing objects.
        """
        logger.debug(f'Listing bills with URL: {BASE_URL}/billing/list')
        response = self._request(f'{BASE_URL}/billing/list', method='GET')
        return BillingList.model_validate({'data': response.json()['data']})
