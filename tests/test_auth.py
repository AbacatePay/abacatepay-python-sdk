import pytest
from abacatepay import AbacatePay
from abacatepay.utils._exceptions import UnauthorizedRequest


def test_wrong_key_running_function(invalid_token_response):
    rightKey = "Bearer 123456789"

    client = AbacatePay(rightKey)
    with pytest.raises(UnauthorizedRequest):
        client.billing.list()