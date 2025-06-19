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

from .billings import BillingClient
from .coupons import CouponClient
from .customers import CustomerClient
from .pixQrCode import PixQrCodeClient


class AbacatePay:
    def __init__(self, api_key: str):
        self.billing = BillingClient(api_key)
        self.customers = CustomerClient(api_key)
        self.coupons = CouponClient(api_key)
        self.pixQrCode = PixQrCodeClient(api_key)
