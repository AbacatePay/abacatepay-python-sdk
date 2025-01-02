import pytest
from abacatepay import AbacatePay
from abacatepay.utils._exceptions import ForbiddenRequest


def test_wrong_key_running_function(invalid_token_response):
    rightKey = "Bearer 123456789"

    client = AbacatePay(rightKey)
    with pytest.raises(ForbiddenRequest):
        client.billing.list()