from abacatepay.billings.client import BillingClient
from abacatepay.billings.models import BillingList, BillingIn
from abacatepay.products import Product

client = BillingClient("dummy-token")


def test_list_billings(list_billings_response):
    """Tests if listing billings returns exactly one billing entry."""
    billings = client.list()
    assert len(billings) == 1


def test_list_more_than_one_billing(list_more_than_one_billing_response):
    """Tests if listing billings returns more than one billing entry when multiple billings exist."""
    billings = client.list()
    assert len(billings) == 2


def test_list_billings_return_type(list_billings_response):
    """Tests if the list method returns a BillingList instance."""
    billings = client.list()
    assert isinstance(billings, BillingList)


def test_create_billing_passing_a_dict(billing_response_sample, responses):
    """Tests if a billing can be created by passing a dictionary."""
    responses.add(
        responses.POST,
        'https://api.abacatepay.com/v1/billing/create',
        json={'data': billing_response_sample, 'error': None},
        status=200
    )

    billing = client.create(
        {
            'products': [
                Product(
                    external_id=billing_response_sample['products'][0]['externalId'],
                    name='test',
                    quantity=billing_response_sample['products'][0]['quantity'],
                    price=100,
                    description="test product",
                ),
            ],
            'returnUrl': billing_response_sample['metadata']['returnUrl'],
            'completionUrl': billing_response_sample['metadata']['completionUrl'],
        }
    )

    assert billing.id == billing_response_sample['id']
    assert billing.url == billing_response_sample['url']


def test_create_billing_passing_billing_in_model(billing_response_sample, responses):
    """Tests if a billing can be created by passing a BillingIn model instance."""
    responses.add(
        responses.POST,
        'https://api.abacatepay.com/v1/billing/create',
        json={'data': billing_response_sample, 'error': None},
        status=200
    )

    billing = client.create(
        BillingIn(
            products=[
                Product(
                    external_id=billing_response_sample['products'][0]['externalId'],
                    name='test',
                    quantity=billing_response_sample['products'][0]['quantity'],
                    price=100,
                    description="test product",
                ),
            ],
            return_url=billing_response_sample['metadata']['returnUrl'],
            completion_url=billing_response_sample['metadata']['completionUrl'],
        )
    )

    assert billing.id == billing_response_sample['id']
    assert billing.url == billing_response_sample['url']


def test_create_billing_passing_named_arguments(billing_response_sample, responses):
    """Tests if a billing can be created using named arguments."""
    responses.add(
        responses.POST,
        'https://api.abacatepay.com/v1/billing/create',
        json={'data': billing_response_sample, 'error': None},
        status=200
    )

    billing = client.create(
        products=[
            Product(
                external_id=billing_response_sample['products'][0]['externalId'],
                name='test',
                quantity=billing_response_sample['products'][0]['quantity'],
                price=100,
                description="test product",
            ),
        ],
        return_url=billing_response_sample['metadata']['returnUrl'],
        completion_url=billing_response_sample['metadata']['completionUrl'],
    )

    assert billing.id == billing_response_sample['id']
    assert billing.url == billing_response_sample['url']
