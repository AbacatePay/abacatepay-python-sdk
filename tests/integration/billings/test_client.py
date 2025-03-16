from abacatepay.billings import BillingClient

client = BillingClient("dummy-token")


def test_list_billings(list_billings_response):
    billings = client.list()
    assert len(billings) == 1

def test_list_more_than_one_billing(list_more_than_one_billing_response):
    billings = client.list()
    assert len(billings) == 2
