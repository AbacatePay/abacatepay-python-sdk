from logging import getLogger
from functools import singledispatchmethod
from typing import Any
from ..base.client import BaseClient
from ..constants import BASE_URL
from .models import Billing, BillingIn, BillingList

logger = getLogger(__name__)


class BillingClient(BaseClient):
    @singledispatchmethod
    def _prepare_billing_data(self, data, kwargs) -> dict[str, Any]:
        """Returns the final data that will be sent to API"""
        if not (data or kwargs):
            raise ValueError('data or named arguments must be provided')
        
        elif kwargs:
            return self._parse_dict_or_kwargs(None, kwargs)
        
    
    def _parse_billing_in_schema(self, data: BillingIn, kwargs) -> dict[str, Any]:
        """It parse the output data when user pass an instance of the model BillingIn
        to `data` positional argument.
        """
        return data.model_dump(by_alias=True)
    
    def _parse_dict_or_kwargs(self, data: dict, kwargs) -> dict[str, Any]:
        """It parses the output data to when the user send a dict to `data` or named
        arguments.
        """
        obj = data if data is not None else kwargs
        return BillingIn.model_validate(obj).model_dump(by_alias=True)
    
    def create(self, data: BillingIn = None, **kwargs) -> Billing:
        """
        Create a new billing.

        Args:
            data (BillingIn): an instance of `abacatepay.billings.models.BillingIn` a dict \
            or the named params following the model schema.
        
        Keyword args:
            products (List[Product]): List of products to be billed.
            returnURL (str): The URL the user will be redirected to after the billing is completed.
            completionUrl (str): The URL the API will make a POST request after the billing is completed.
            methods (List[BILLING_METHODS]): The payment methods to be accepted. Defaults to ["PIX"].
            frequency (BILLING_KINDS): The frequency of the billing. Defaults to "ONE_TIME".
            customerId (str): The ID of the customer. If provided, the customer information won't be required.
            customer (CustomerMetadata): The customer information. If customerId is provided, this parameter is ignored.

        Returns:
            Billing: The response with the billing data.
        """
        json_data = self._prepare_billing_data(data, kwargs)
        logger.debug('creating billing: %s', json_data)

        response = self._request(
            f"{BASE_URL}/billing/create",
            method="POST",
            json=json_data,
        )
        return Billing(**response.json()["data"])

    def list(self) -> BillingList:
        """
        List all bills.

        Returns:
            BillingList: A list of billing objects.
        """
        logger.debug(f"Listing bills with URL: {BASE_URL}/billing/list")
        response = self._request(f"{BASE_URL}/billing/list", method="GET")
        return BillingList.model_validate({'data': response.json()["data"]})
