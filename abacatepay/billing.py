import requests
from ._constants import (
    BASE_URL,
    USER_AGENT,
    BILLING_KINDS,
    BILLING_METHODS,
    BILLING_STATUS,
)
from ._exceptions import *
from ._models import Product, BillingResponse, Customer


class Billing:
    def __init__(
        self,
        products: list[Product],
        returnURL: str,
        completionUrl: str,
        api_key: str,
        methods: list[BILLING_METHODS] = ["PIX"],
        frequency: BILLING_KINDS = "ONE_TIME",
        customerId: str | None = None,
        customer: Customer | None = None,
    ):
        self.products = products
        self.returnURL = returnURL
        self.completionUrl = completionUrl
        self.methods = methods

        response = requests.post(
            f"{BASE_URL}/billing/create",
            json={
                "products": [product.model_dump() for product in products],
                "returnUrl": returnURL,
                "completionUrl": completionUrl,
                "methods": methods,
                "frequency": frequency,
                "customerId": customerId,
                **({"customer": customer.model_dump()} if customer is not None else {}),
            },
            headers={
                "Authorization": f"Bearer {api_key}",
                "User-Agent": USER_AGENT,
                "Content-Type": "application/json",
            },
        )

        try:
            if response.status_code == 200:
                billing_data = BillingResponse(data=response.json()["data"])
                self.data = billing_data
            else:
                raise_for_status(response)

        except requests.exceptions.Timeout:
            raise APITimeoutError(request=response)

        except requests.exceptions.ConnectionError:
            raise APIConnectionError(message="Connection error.", request=response)
