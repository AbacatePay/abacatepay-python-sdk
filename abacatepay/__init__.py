"""
The Python SDK for the AbacatePay API

Basic usage:
```python
import abacatepay
from abacatepay.products import Product

token = "<your api token>"
client = abacatepay.AbacatePay(token)

billing = client.billing.create(
    products=[
        Product(
            external_id="123",
            name="Teste",
            quantity=1,
            price=101,
            description="Teste"
        )
    ],
    return_url="https://abacatepay.com",
    completion_url="https://abacatepay.com"
)
print(billing.data.url)
# > https://abacatepay.com/pay/aaaaaaa
```

More examples found on https://docs.abacatepay.com/
"""

from typing import Literal, overload

from .billings import BillingAsyncClient, BillingClient
from .coupons import CouponAsyncClient, CouponClient
from .customers import CustomerAsyncClient, CustomerClient
from .pixQrCode import PixQrCodeAsyncClient, PixQrCodeClient


class AbacatePayClient:
    def __init__(self, api_key: str):
        self.billing = BillingClient(api_key)
        self.customers = CustomerClient(api_key)
        self.coupons = CouponClient(api_key)
        self.pixQrCode = PixQrCodeClient(api_key)


class AbacatePayAsyncClient:
    def __init__(self, api_key: str):
        self.billing = BillingAsyncClient(api_key)
        self.customers = CustomerAsyncClient(api_key)
        self.coupons = CouponAsyncClient(api_key)
        self.pixQrCode = PixQrCodeAsyncClient(api_key)


@overload
def AbacatePay(api_key: str, *, async_mode: Literal[False] = False) -> AbacatePayClient: ...
@overload
def AbacatePay(api_key: str, *, async_mode: Literal[True] = True) -> AbacatePayAsyncClient: ...


def AbacatePay(api_key: str, async_mode: bool = False) -> AbacatePayClient | AbacatePayAsyncClient:
    """
    Create an instance of AbacatePayClient or AbacatePayAsyncClient,
    based on the async_mode parameter.

    Args:
        api_key (str): The API key for the AbacatePay client.
        async_mode (bool): Whether to use the asynchronous client.
    """
    if async_mode:
        return AbacatePayAsyncClient(api_key)

    return AbacatePayClient(api_key)
