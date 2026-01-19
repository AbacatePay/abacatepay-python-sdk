import pytest
import httpx
from abacatepay import AbacatePay
from abacatepay.utils.exceptions import UnauthorizedRequest


def test_wrong_key_running_function(invalid_token_response):
    rightKey = "Bearer 123456789"

    client = AbacatePay(rightKey)
    with pytest.raises(UnauthorizedRequest):
        client.billing.list()


@pytest.mark.asyncio
async def test_async_wrong_key_running_function(async_invalid_token_response):
    rightKey = "Bearer 123456789"

    client = AbacatePay(rightKey, async_mode=True)
    with pytest.raises(UnauthorizedRequest):
        await client.billing.list()