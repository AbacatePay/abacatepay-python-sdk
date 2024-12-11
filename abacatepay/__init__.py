"""
The Python SDK for the AbacatePay API

Basic usage:
```python
import abacatepay

token = "<your api token>"
client = AbacatePay(token)

billing = client.create_billing(products=[Product(externalId="123", name="Teste", quantity=1, price=101, description="Teste")], returnURL="https://abacatepay.com", completionUrl="https://abacatepay.com")
print(billing.data.url)
# > https://abacatepay.com/pay/aaaaaaa
```

More examples found on https://abacatepay.readme.io/
"""

import requests
import logging
from abacatepay.src.use_cases.billing import Billing
from abacatepay.domain.entities.product import Product
from abacatepay.domain.entities.customer import Customer
from abacatepay.domain.response_models import BillingResponse
from abacatepay.infrastructure.utils.constants import BILLING_KINDS, BILLING_METHODS, BASEURL, USERAGENT
from abacatepay.infrastructure.utils.exceptions import *


logger = logging.getLogger(__name__)


class AbacatePay:
    """
    The AbacatePay sdk client.
    """

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
                "User-Agent": USERAGENT,
            },
            **kwargs,
        )

    def create_billing(
        self,
        products: list[Product],
        returnURL: str,
        completionUrl: str,
        methods: list[BILLING_METHODS] = ["PIX"],
        frequency: BILLING_KINDS = "ONE_TIME",
        customerId: str | None = None,
        customer: Customer | None = None,
    ):
        return Billing(
            products,
            returnURL,
            completionUrl,
            self.__api_key,
            methods,
            frequency=frequency,
            customerId=customerId,
            customer=customer,
        )

    def list_bills(self) -> list[Billing]:
        logger.debug(f"Listing bills with URL: {BASEURL}/billing/list")
        response = self._request(f"{BASEURL}/billing/list", method="GET")

        try:
            if response.status_code == 200:
                return [BillingResponse(data=bill) for bill in response.json()["data"]]
            else:
                raise_for_status(response)
        except requests.exceptions.Timeout:
            raise APITimeoutError(request=response)
        except requests.exceptions.ConnectionError:
            raise APIConnectionError(message="Connection error", request=response)


    def create_customer(self, customer: Customer) -> Customer:
        logger.debug(f"Creating customer with URL: {BASEURL}/customer/create")
        response = self._request(f"{BASEURL}/customer/create", method="POST", json=customer.model_dump())

        try:
            if response.status_code == 200:
                return Customer.from_dict(data=response.json()["data"])
            else:
                raise_for_status(response)
        except requests.exceptions.Timeout:
            raise APITimeoutError(request=response)
        except requests.exceptions.ConnectionError:
            raise APIConnectionError(message="Connection error", request=response)

    def list_customers(self) -> list[Customer]:
        logger.debug(f"Listing customers with URL: {BASEURL}/customer/list")
        response = self._request(f"{BASEURL}/customer/list", method="GET")

        try:
            if response.status_code == 200:
                return [Customer.from_dict(data=bill) for bill in response.json()["data"]]
            else:
                raise_for_status(response)
        except requests.exceptions.Timeout:
            raise APITimeoutError(request=response)
        except requests.exceptions.ConnectionError:
            raise APIConnectionError(message="Connection error", request=response)
