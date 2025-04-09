import pytest

from abacatepay.customers import CustomerClient
from abacatepay.customers.models import Customer, CustomerMetadata


@pytest.fixture
def customer_client():
    """returns an instance of the `CustomerClient` class using a fake api key"""
    return CustomerClient('fake api key')


@pytest.fixture
def customer_list_response(responses):
    """mocks the response to customer list with 2 customers
    """
    customers = [
        Customer(
            metadata=CustomerMetadata(
                tax_id="445.665.140-72",
                name="customer name",
                email="email@email.com",
                cellphone="(99) 9999-9999",
            ),
            id='cust_fdsjioe1'
        ),
        Customer(
            metadata=CustomerMetadata(
                tax_id="261.474.540-56",
                name="customer name",
                email="email@email.com",
                cellphone="(99) 9999-9999",
            ),
            id='cust_jfeios213'
        ),
    ]

    responses.add(
        responses.GET,
        "https://api.abacatepay.com/v1/customer/list",
        json={'data': [c.model_dump(by_alias=True) for c in customers], 'error': None},
        status=200,
    )
