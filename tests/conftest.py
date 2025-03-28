import pytest
from abacatepay.products import Product
from abacatepay.customers.models import CustomerMetadata


@pytest.fixture
def invalid_token_response(responses):
    responses.add(
        responses.GET,
        "https://api.abacatepay.com/v1/billing/list",
        status=401,
    )
    return responses

@pytest.fixture
def list_billings_response(responses):
    responses.add(
        responses.GET,
        "https://api.abacatepay.com/v1/billing/list",
        json={
            "data": [
                {
                    "allowCoupons": False,
                    "amount": 100,
                    "coupons": [],
                    "couponsUsed": [],
                    "createdAt": "2025-03-17T17:41:46.306Z",
                    "customer": {
                        "metadata": {
                            "cellphone": "(99) 9999-9999",
                            "email": "john@email.com",
                            "name": "John Doe",
                            "taxId": "445.665.140-72"
                        }
                    },
                    "devMode": True,
                    "frequency": "ONE_TIME",
                    "id": "bill_sccfTWMq5DLxWj1MeRqgBpzU",
                    "metadata": {
                        "completionUrl": "https://example/completion",
                        "fee": 100,
                        "returnUrl": "https://example.com/return"
                    },
                    "methods": [
                        "PIX"
                    ],
                    "products": [
                        {
                            "externalId": "1",
                            "id": "prod_0g0GhPwBBRKX1qBjzjJr2HaK",
                            "quantity": 1
                        }
                    ],
                    "status": "PENDING",
                    "updatedAt": "2025-03-17T17:41:46.306Z",
                    "url": "https://abacatepay.com/pay/bill_sccfTWMq5DLxWj1MeRqgBpzU"
                },
            ],
            "error": None
        },
        status=200,
    )
    return responses

@pytest.fixture
def list_more_than_one_billing_response(responses):
    responses.add(
        responses.GET,
        "https://api.abacatepay.com/v1/billing/list",
        json={
            "data": [
                {
                    "allowCoupons": False,
                    "amount": 100,
                    "coupons": [],
                    "couponsUsed": [],
                    "createdAt": "2025-03-17T17:41:46.306Z",
                    "customer": {
                        "metadata": {
                            "cellphone": "(99) 9999-9999",
                            "email": "john@email.com",
                            "name": "John Doe",
                            "taxId": "445.665.140-72"
                        }
                    },
                    "devMode": True,
                    "frequency": "ONE_TIME",
                    "id": "bill_sccfTWMq5DLxWj1MeRqgBpzU",
                    "metadata": {
                        "completionUrl": "https://example/completion",
                        "fee": 100,
                        "returnUrl": "https://example.com/return"
                    },
                    "methods": [
                        "PIX"
                    ],
                    "products": [
                        {
                            "externalId": "1",
                            "id": "prod_0g0GhPwBBRKX1qBjzjJr2HaK",
                            "quantity": 1
                        }
                    ],
                    "status": "PENDING",
                    "updatedAt": "2025-03-17T17:41:46.306Z",
                    "url": "https://abacatepay.com/pay/bill_sccfTWMq5DLxWj1MeRqgBpzU"
                },{
                    "allowCoupons": False,
                    "amount": 100,
                    "coupons": [],
                    "couponsUsed": [],
                    "createdAt": "2025-03-17T17:41:46.306Z",
                    "customer": {
                        "metadata": {
                            "cellphone": "(99) 9999-9999",
                            "email": "john@email.com",
                            "name": "John Doe",
                            "taxId": "445.665.140-72"
                        }
                    },
                    "devMode": True,
                    "frequency": "ONE_TIME",
                    "id": "bill_sccfTWMq5DLxWj1MeRqgBpzU",
                    "metadata": {
                        "completionUrl": "https://example/completion",
                        "fee": 100,
                        "returnUrl": "https://example.com/return"
                    },
                    "methods": [
                        "PIX"
                    ],
                    "products": [
                        {
                            "externalId": "1",
                            "id": "prod_0g0GhPwBBRKX1qBjzjJr2HaK",
                            "quantity": 1
                        }
                    ],
                    "status": "PENDING",
                    "updatedAt": "2025-03-17T17:41:46.306Z",
                    "url": "https://abacatepay.com/pay/bill_sccfTWMq5DLxWj1MeRqgBpzU"
                },
            ],
            "error": None
        },
        status=200,
    )
    return responses

@pytest.fixture
def billing_response_sample():
    """return a sample data of the billing returned by API"""
    return {
        "allowCoupons": False,
        "amount": 100,
        "coupons": [],
        "couponsUsed": [],
        "createdAt": "2025-03-17T17:41:46.306Z",
        "customer": {
            "metadata": {
                "cellphone": "(99) 9999-9999",
                "email": "john@email.com",
                "name": "John Doe",
                "taxId": "445.665.140-72"
            }
        },
        "devMode": True,
        "frequency": "ONE_TIME",
        "id": "bill_sccfTWMq5DLxWj1MeRqgBpzU",
        "metadata": {
            "completionUrl": "https://8c75-45-7-165-133.ngrok-free.app/completion",
            "fee": 100,
            "returnUrl": "https://8c75-45-7-165-133.ngrok-free.app/return"
        },
        "methods": [
            "PIX"
        ],
        "products": [
            {
                "externalId": "1",
                "id": "prod_0g0GhPwBBRKX1qBjzjJr2HaK",
                "quantity": 1
            }
        ],
        "status": "PENDING",
        "updatedAt": "2025-03-17T17:41:46.306Z",
        "url": "https://abacatepay.com/pay/bill_sccfTWMq5DLxWj1MeRqgBpzU"
    }


@pytest.fixture
def one_product_sample():
    """returns an instance of the product model"""
    return Product(
        external_id='ext_999',
        name='sample prod',
        description='sample',
        quantity=1,
        price=100,
    )

@pytest.fixture
def one_customer_metadata_sample():
    """returns an instance of the CustomerMetadata model"""
    return CustomerMetadata(
        name='sample customer',
        tax_id='445.665.140-72',
        email='cust@email.com',
        cellphone="(11) 4002-8922"
    )
