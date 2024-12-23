"""
The Python SDK for the AbacatePay API

Basic usage:
```python
import abacatepay
from abacatepay.models import Product

token = "<your api token>"
client = AbacatePay(token)

billing = client.billing.create_billing(products=[Product(externalId="123", name="Teste", quantity=1, price=101, description="Teste")], returnURL="https://abacatepay.com", completionUrl="https://abacatepay.com")
print(billing.data.url)
# > https://abacatepay.com/pay/aaaaaaa
```

More examples found on https://abacatepay.readme.io/
"""

from .billing import BillingClient
from .customers import CustomerClient

class AbacatePay:
    def __init__(self, api_key: str):
        self.billing = BillingClient(api_key)
        self.customers = CustomerClient(api_key)
