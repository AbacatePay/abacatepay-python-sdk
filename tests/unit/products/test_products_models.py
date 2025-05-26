import pytest
from pydantic import ValidationError

from abacatepay.products.models import Product, ProductInline


def test_valid_product():
    """Should initialize the product as expected"""
    product = Product(
        external_id="123",
        name="Test Product",
        description="A great product",
        quantity=2,
        price=150
    )
    assert product.external_id == "123"
    assert product.name == "Test Product"
    assert product.description == "A great product"
    assert product.quantity == 2
    assert product.price == 150


def test_product_missing_optional_description():
    """Should initialize even that description was not sent"""
    product = Product(
        external_id="123",
        name="Test Product",
        quantity=2,
        price=150
    )
    assert product.description is None


def test_product_invalid_quantity():
    """Should raise validation error when quantity less than 0"""
    with pytest.raises(ValidationError, match="Input should be greater than or equal to 1"):
        Product(external_id="123", name="Invalid Product", quantity=0, price=150)


def test_product_invalid_price():
    """Should raise validation error when price less than 100"""
    with pytest.raises(ValidationError, match="Input should be greater than or equal to 100"):
        Product(external_id="123", name="Invalid Product", quantity=1, price=99)


def test_product_alias_handling():
    """Should parse correctly the key `externalId`"""
    data = {"externalId": "456", "name": "Aliased Product", "quantity": 3, "price": 200}
    product = Product.model_validate(data)
    assert product.external_id == "456"


def test_product_serialization():
    """Should serialize in JS key format correctly as expected by API
    when by alias equals to True
    """
    product = Product(
        external_id="789",
        name="Serialized Product",
        quantity=1,
        price=1000
    )
    serialized = product.model_dump(by_alias=True)
    assert "externalId" in serialized
    assert serialized["externalId"] == "789"


def test_valid_product_inline():
    """Should serialize correctly"""
    product = ProductInline(
        id="prod_001",
        external_id="ext_123",
        quantity=5
    )
    assert product.id == "prod_001"
    assert product.external_id == "ext_123"
    assert product.quantity == 5


def test_product_inline_invalid_quantity():
    """Should raise validation error because quantity is less than 1"""
    with pytest.raises(ValidationError, match="Input should be greater than or equal to 1"):
        ProductInline(id="prod_002", external_id="ext_456", quantity=0)


def test_product_inline_alias_handling():
    """Should validate correctly the key external id in JS format"""
    data = {"id": "prod_003", "externalId": "ext_789", "quantity": 2}
    product = ProductInline.model_validate(data)
    assert product.external_id == "ext_789"


def test_product_inline_serialization():
    """Should serialize in the format expected by API when by alias equals True"""
    product = ProductInline(
        id="prod_004",
        external_id="ext_999",
        quantity=3
    )
    serialized = product.model_dump(by_alias=True)
    assert "externalId" in serialized
    assert serialized["externalId"] == "ext_999"
