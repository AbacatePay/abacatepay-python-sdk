import pytest
from pydantic import ValidationError

from abacatepay.billings.models import (
    Billing,
    BillingIn,
    BillingList,
    BillingMetadata,
)


def test_billing_metadata_validate():
    data = {
        "completionUrl": "https://example.com/completion_url",
        "returnUrl": "https://example.com/return_url",
        "fee": 100,
    }
    bm = BillingMetadata.model_validate(data)

    assert (
        bm.completion_url == data["completionUrl"]
        and bm.return_url == data["returnUrl"]
        and bm.fee == data["fee"]
    )


def test_billing_metadata_dump_by_alias():
    expected_dump_result = {
        "completionUrl": "https://example.com/completion_url",
        "returnUrl": "https://example.com/return_url",
        "fee": 100,
    }
    dump_result = BillingMetadata(
        completion_url=expected_dump_result["completionUrl"],
        return_url=expected_dump_result["returnUrl"],
        fee=expected_dump_result["fee"],
    ).model_dump(by_alias=True)

    assert dump_result == expected_dump_result


def test_billing_list(billing_response_sample):
    data = [billing_response_sample]
    bl = BillingList(data=data)
    assert len(bl) == 1 and bl.data[0].id == billing_response_sample["id"]


def test_iterate_billing_list(billing_response_sample):
    billings = BillingList(data=[billing_response_sample])
    for billing in billings:
        assert billing == Billing(**billing_response_sample)


def test_billing_validate(billing_response_sample):
    result = Billing.model_validate(billing_response_sample)
    assert result.id == billing_response_sample["id"]


def test_billing_dump_by_alias(billing_response_sample):
    result = Billing(**billing_response_sample).model_dump(by_alias=True)
    assert_keys = [
        "id",
        "customer",
        "metadata",
        "products",
        "methods",
        "url",
        "coupons",
        "couponsUsed",
    ]
    assert all([result[k] == billing_response_sample[k] for k in assert_keys])


def test_billing_in_valid(one_product_sample, one_customer_metadata_sample):
    """Tests the creation of a valid BillingIn instance."""
    billing = BillingIn(
        frequency="ONE_TIME",
        methods=["PIX"],
        products=[one_product_sample],
        return_url="https://example.com/return",
        completion_url="https://example.com/completion",
        customer_id="cust_001",
        customer=one_customer_metadata_sample,
    )
    assert billing.frequency == "ONE_TIME"
    assert billing.methods == ["PIX"]
    assert billing.products[0] == one_product_sample
    assert str(billing.return_url) == "https://example.com/return"
    assert str(billing.completion_url) == "https://example.com/completion"
    assert billing.customer_id == "cust_001"
    assert billing.customer == one_customer_metadata_sample


def test_billing_in_missing_optional_fields(one_product_sample):
    """Tests the creation of a BillingIn instance without optional fields."""
    billing = BillingIn(
        frequency="ONE_TIME",
        methods=["PIX"],
        products=[one_product_sample],
        return_url="https://example.com/return",
        completion_url="https://example.com/completion",
    )
    assert billing.customer_id is None
    assert billing.customer == {}


def test_billing_in_invalid_url(one_product_sample):
    """Tests if invalid URLs raise a validation error."""
    with pytest.raises(ValidationError):
        BillingIn(
            frequency="ONE_TIME",
            methods=["PIX"],
            products=[one_product_sample],
            return_url="invalid_url",
            completion_url="invalid_url",
        )


def test_billing_in_serialization(one_product_sample):
    """Tests if serialization includes the correct aliases."""
    billing = BillingIn(
        frequency="ONE_TIME",
        methods=["PIX"],
        products=[one_product_sample],
        return_url="https://example.com/return",
        completion_url="https://example.com/completion",
        customer_id="cust_003",
    )
    serialized = billing.model_dump(by_alias=True)
    assert "returnUrl" in serialized
    assert "completionUrl" in serialized
    assert "customerId" in serialized
    assert str(serialized["returnUrl"]) == "https://example.com/return"
    assert str(serialized["completionUrl"]) == "https://example.com/completion"
    assert serialized["customerId"] == "cust_003"
