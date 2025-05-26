from abacatepay.coupons.models import (Coupon,
                                       CouponIn)


def test_coupon_input_creation():
    """Tests the creation of a CouponIn instance and checks its attributes."""
    data = {
        "code": "DISCOUNT2025",
        "discount_kind": "PERCENTAGE",
        "discount": 20,
        "notes": "Special discount for loyal customers",
        "max_redeems": 100,
        "metadata": {"category": "loyalty"}
    }
    coupon_in = CouponIn(**data)
    assert coupon_in.code == data["code"]
    assert coupon_in.discount_kind == data["discount_kind"]
    assert coupon_in.discount == data["discount"]
    assert coupon_in.notes == data["notes"]
    assert coupon_in.max_redeems == data["max_redeems"]
    assert coupon_in.metadata == data["metadata"]


def test_coupon_creation():
    """Tests the creation of a Coupon instance and checks its attributes."""
    data = {
        "id": "coupon_12345",
        "discountKind": "FIXED_AMOUNT",
        "discount": 50,
        "status": "ACTIVE",
        "notes": "Holiday discount",
        "maxRedeems": 500,
        "redeemsCount": 100,
        "createdAt": "2025-05-01T12:00:00Z",
        "updatedAt": "2025-05-15T12:00:00Z",
        "devMode": True
    }
    coupon = Coupon(**data)
    assert coupon.id == data["id"]
    assert coupon.discount_kind == data["discountKind"]
    assert coupon.discount == data["discount"]
    assert coupon.status == data["status"]
    assert coupon.notes == data["notes"]
    assert coupon.max_redeems == data["maxRedeems"]
    assert coupon.redeems_count == data["redeemsCount"]
    assert coupon.created_at == data["createdAt"]
    assert coupon.updated_at == data["updatedAt"]
    assert coupon.dev_mode == data["devMode"]


def test_coupon_in_serialization():
    """Tests the serialization of a CouponIn instance."""
    data = {
        "code": "DISCOUNT2025",
        "discount_kind": "PERCENTAGE",
        "discount": 20,
        "notes": "Special discount for loyal customers",
        "max_redeems": 100,
        "metadata": {"category": "loyalty"}
    }
    coupon_in = CouponIn(**data)
    serialized = coupon_in.model_dump(by_alias=True)
    assert serialized == {
        "code": "DISCOUNT2025",
        "discountKind": "PERCENTAGE",
        "discount": 20,
        "notes": "Special discount for loyal customers",
        "maxRedeems": 100,
        "metadata": {"category": "loyalty"}
    }