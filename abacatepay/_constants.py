from typing import Literal

MINIMUM_VALUE = 100
BASE_URL = "https://api.abacatepay.com/v1"
VERSION = "1.0.0"
USER_AGENT = f"Python SDK {VERSION}"

BILLING_STATUS = Literal['PENDING', 'EXPIRED', 'CANCELLED', 'PAID', 'REFUNDED']
BILLING_METHODS = Literal['pix']
BILLING_KINDS = Literal['ONE_TIME']
