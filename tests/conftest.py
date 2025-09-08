import pytest
import respx
import httpx
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


@pytest.fixture
def list_billings_json_data():
    """Returns JSON data for single billing list response"""
    return {
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
                "methods": ["PIX"],
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
        ],
        "error": None
    }


@pytest.fixture
def respx_mock():
    """Fixture that returns a configured respx mock"""
    with respx.mock() as mock:
        yield mock


@pytest.fixture
def async_list_billings_mock(respx_mock, list_billings_json_data):
    """Fixture that configures the mock for async list_billings"""

    respx_mock.get('https://api.abacatepay.com/v1/billing/list').mock(
        return_value=httpx.Response(200, json=list_billings_json_data)
    )
    return respx_mock


@pytest.fixture
def async_list_multiple_billings_mock(respx_mock, list_more_than_one_billing_json_data):
    """Fixture that configures the mock for async list_billings with multiple items"""
    respx_mock.get('https://api.abacatepay.com/v1/billing/list').mock(
        return_value=httpx.Response(200, json=list_more_than_one_billing_json_data)
    )
    return respx_mock


@pytest.fixture
def async_create_billing_mock(respx_mock, billing_response_sample):
    """Fixture that configures the mock for async create_billing"""
    respx_mock.post('https://api.abacatepay.com/v1/billing/create').mock(
        return_value=httpx.Response(200, json={'data': billing_response_sample, 'error': None})
    )
    return respx_mock


@pytest.fixture
def list_more_than_one_billing_json_data():
    """Returns JSON data for multiple billings list response"""
    return {
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
                "methods": ["PIX"],
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
                "methods": ["PIX"],
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
        ],
        "error": None
    }

@pytest.fixture
def customer_response_sample(one_customer_metadata_sample):
    """return a sample data of the customer returned by API"""
    return {
        "id": "cust_avjgeigjge",
        "metadata": one_customer_metadata_sample.model_dump(by_alias=True)
    }

@pytest.fixture
def list_customers_json_data():
    """Returns JSON data for customer list response"""
    return {
        "data": [
            {
                "metadata": {
                    "taxId": "445.665.140-72",
                    "name": "customer name",
                    "email": "email@email.com",
                    "cellphone": "(99) 9999-9999",
                },
                "id": 'cust_fdsjioe1'
            },
            {
                "metadata": {
                    "taxId": "261.474.540-56",
                    "name": "customer name",
                    "email": "email@email.com",
                    "cellphone": "(99) 9999-9999",
                },
                "id": 'cust_jfeios213'
            },
        ],
        "error": None
    }

@pytest.fixture
def list_multiple_customers_json_data():
    """Returns JSON data for multiple customers list response"""
    # Similar to above but with more if needed, but for now duplicate
    return {
        "data": [
            {
                "metadata": {
                    "taxId": "445.665.140-72",
                    "name": "customer name",
                    "email": "email@email.com",
                    "cellphone": "(99) 9999-9999",
                },
                "id": 'cust_fdsjioe1'
            },
            {
                "metadata": {
                    "taxId": "261.474.540-56",
                    "name": "customer name",
                    "email": "email@email.com",
                    "cellphone": "(99) 9999-9999",
                },
                "id": 'cust_jfeios213'
            },
        ],
        "error": None
    }


@pytest.fixture
def async_list_customers_mock(respx_mock, list_customers_json_data):
    """Fixture that configures the mock for async list_customers"""
    respx_mock.get('https://api.abacatepay.com/v1/customer/list').mock(
        return_value=httpx.Response(200, json=list_customers_json_data)
    )
    return respx_mock


@pytest.fixture
def async_list_multiple_customers_mock(respx_mock, list_multiple_customers_json_data):
    """Fixture that configures the mock for async list_customers with multiple items"""
    respx_mock.get('https://api.abacatepay.com/v1/customer/list').mock(
        return_value=httpx.Response(200, json=list_multiple_customers_json_data)
    )
    return respx_mock


@pytest.fixture
def async_create_customer_mock(respx_mock, customer_response_sample):
    """Fixture that configures the mock for async create_customer"""
    respx_mock.post('https://api.abacatepay.com/v1/customer/create').mock(
        return_value=httpx.Response(200, json={'data': customer_response_sample, 'error': None})
    )
    return respx_mock


@pytest.fixture
def async_invalid_token_response(respx_mock):
    respx_mock.get("https://api.abacatepay.com/v1/billing/list").mock(
        return_value=httpx.Response(401)
    )
    return respx_mock