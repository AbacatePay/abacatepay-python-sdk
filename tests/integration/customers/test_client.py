from abacatepay.customers.models import Customer, CustomerMetadata
import pytest


def test_create_customer_with_model(customer_client, responses, one_customer_metadata_sample):
    customer = Customer(
        metadata=one_customer_metadata_sample,
        id='cust_avjgeigjge'
    )
    responses.add(
        responses.POST,
        "https://api.abacatepay.com/v1/customer/create",
        json={'data': customer.model_dump(by_alias=True), 'error': None},
        status=200,
    )

    client = customer_client.create(customer.metadata)

    assert client == customer


def test_create_customer_with_dict(customer_client, responses, one_customer_metadata_sample):
    customer = Customer(
        metadata=one_customer_metadata_sample,
        id='cust_avjgeigjge'
    )
    responses.add(
        responses.POST,
        "https://api.abacatepay.com/v1/customer/create",
        json={'data': customer.model_dump(by_alias=True), 'error': None},
        status=200,
    )

    client = customer_client.create(one_customer_metadata_sample.model_dump())

    assert client == customer


def test_create_customer_with_kwargs(customer_client, responses, one_customer_metadata_sample):
    customer = Customer(
        metadata=one_customer_metadata_sample,
        id='cust_avjgeigjge'
    )
    responses.add(
        responses.POST,
        "https://api.abacatepay.com/v1/customer/create",
        json={'data': customer.model_dump(by_alias=True), 'error': None},
        status=200,
    )

    client = customer_client.create(**one_customer_metadata_sample.model_dump())

    assert client == customer


def test_list_customers(customer_client, customer_list_response):
    expected_tax_ids = ["445.665.140-72", "261.474.540-56"]
    customers = customer_client.list()

    assert all([c.tax_id == t_id  for c, t_id in zip(customers, expected_tax_ids)])


def test_customer_metadata_serialization(one_customer_metadata_sample):
    result = one_customer_metadata_sample.model_dump(by_alias=True)
    assert result['taxId'] == one_customer_metadata_sample.tax_id


def test_customer_metadata_deserialization(one_customer_metadata_sample):
    data = one_customer_metadata_sample.model_dump(by_alias=True)
    result = CustomerMetadata.model_validate(data)
    assert result.tax_id == data['taxId']


# Async Tests
@pytest.mark.asyncio
async def test_async_create_customer_with_model(async_create_customer_mock, async_customer_client, one_customer_metadata_sample):
    customer = Customer(
        metadata=one_customer_metadata_sample,
        id='cust_avjgeigjge'
    )

    result = await async_customer_client.create(one_customer_metadata_sample)

    assert result == customer


@pytest.mark.asyncio
async def test_async_create_customer_with_dict(async_create_customer_mock, async_customer_client, one_customer_metadata_sample):
    customer = Customer(
        metadata=one_customer_metadata_sample,
        id='cust_avjgeigjge'
    )

    result = await async_customer_client.create(one_customer_metadata_sample.model_dump())

    assert result == customer


@pytest.mark.asyncio
async def test_async_create_customer_with_kwargs(async_create_customer_mock, async_customer_client, one_customer_metadata_sample):
    customer = Customer(
        metadata=one_customer_metadata_sample,
        id='cust_avjgeigjge'
    )

    result = await async_customer_client.create(**one_customer_metadata_sample.model_dump())

    assert result == customer


@pytest.mark.asyncio
async def test_async_list_customers(async_list_customers_mock, async_customer_client):
    expected_tax_ids = ["445.665.140-72", "261.474.540-56"]
    customers = await async_customer_client.list()

    assert all([c.metadata.tax_id == t_id for c, t_id in zip(customers, expected_tax_ids)])
