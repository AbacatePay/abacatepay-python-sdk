from abacatepay.customers.models import (
    CustomerMetadata, CustomerInline, Customer
)


def test_customer():
    """Tests the creation of a Customer instance and checks its attributes."""
    data = {
        'id': 'cust_xjf4iS21i1',
        "metadata": {
            "cellphone": "(99) 9999-9999",
            "email": "john@email.com",
            "name": "John Doe",
            "taxId": "445.665.140-72"
        }
    }
    cus = Customer(**data)
    assert cus.id == data["id"]
    assert cus.metadata.tax_id == data["metadata"]["taxId"]

def test_customer_properties():
    """Tests if Customer properties correctly map to metadata values."""
    data = {
        'id': 'cust_xjf4iS21i1',
        "metadata": {
            "cellphone": "(99) 9999-9999",
            "email": "john@email.com",
            "name": "John Doe",
            "taxId": "445.665.140-72"
        }
    }
    cus = Customer(**data)
    assert cus.tax_id == "445.665.140-72"
    assert cus.cellphone == "(99) 9999-9999"
    assert cus.email == "john@email.com"
    assert cus.name == "John Doe"

def test_customer_inline_validation():
    """Tests if CustomerInline correctly handles metadata validation."""
    data = {
        "metadata": {
            "cellphone": "(99) 9999-9999",
            "email": "john@email.com",
            "name": "John Doe",
            "taxId": "445.665.140-72"
        }
    }
    cus = CustomerInline(**data)
    assert cus.metadata.tax_id == "445.665.140-72"

def test_customer_for_creation():
    """Tests the creation of a CustomerMetadata instance and its serialization."""
    data = {
        "cellphone": "(99) 9999-9999",
        "email": "john@email.com",
        "name": "John Doe",
        "taxId": "445.665.140-72"
    }
    cus = CustomerMetadata(**data)
    assert cus.tax_id == "445.665.140-72"
    dumped = cus.model_dump(by_alias=True)
    assert dumped == data
