import pytest
from pydantic import ValidationError
from abacatepay.utils.helpers import prepare_data
from abacatepay.customers.models import CustomerMetadata


def test_prepare_data_with_model_instance(one_customer_metadata_sample):
    """Tests if prepare_data correctly serializes a BaseModel instance."""
    result = prepare_data(one_customer_metadata_sample, CustomerMetadata, use_alias=True)
    assert result["name"] == one_customer_metadata_sample.name
    assert result["email"] == one_customer_metadata_sample.email


def test_prepare_data_with_dict(one_customer_metadata_sample):
    """Tests if prepare_data correctly validates and serializes a dictionary."""
    data = one_customer_metadata_sample.model_dump()
    result = prepare_data(data, CustomerMetadata, use_alias=True)
    assert result["taxId"] == one_customer_metadata_sample.tax_id


def test_prepare_data_invalid_type():
    """Tests if prepare_data raises TypeError for invalid data types."""
    with pytest.raises(TypeError):
        prepare_data(123, CustomerMetadata)

def test_prepare_data_invalid_dict():
    """Tests if prepare_data raises ValidationError for an invalid dictionary."""
    invalid_data = {"invalid_field": "value"}  # Missing required fields
    with pytest.raises(ValidationError):
        prepare_data(invalid_data, CustomerMetadata)
