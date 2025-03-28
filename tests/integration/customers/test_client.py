from abacatepay.customers.models import Customer, CustomerMetadata


def test_create_customer(customer_client, responses):
    customer = Customer(
        metadata=CustomerMetadata(
            tax_id="445.665.140-72",
            name="customer name",
            email="email@email.com",
            cellphone="(99) 9999-9999",
        ),
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


def test_list_customers(customer_client, customer_list_response):
    expected_tax_ids = ["445.665.140-72", "261.474.540-56"]
    customers = customer_client.list()

    assert all([c.tax_id == t_id  for c, t_id in zip(customers, expected_tax_ids)])
