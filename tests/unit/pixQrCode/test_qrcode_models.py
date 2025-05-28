# Tests for abacatepay.pixQrCode.models

from abacatepay.pixQrCode.models import PixQrCode, PixStatus, PixQrCodeIn
from abacatepay.customers.models import CustomerMetadata

def test_pix_qrcode_creation():
    """Tests the creation of a PixQrCode instance and checks its attributes."""
    data = {
        "id": "pix_char_Gbg2XSFQmntL0Lzsb4SeL1zx",
        "amount": 1000,
        "status": "PENDING",
        "devMode": True,
        "brCode": "00020101021226820014br.gov.bcb.pix2560pix-h.asaas.com/qr/cobv/42f6026f-1cf4-4969-b168-ad77a3ae16e85204000053039865802BR5925PURPLE BOX TECNOLOGIA LTD6015Sao Jose dos Ca61081224600062070503***630418E5",
        "brCodeBase64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPQAAAD0CAYAAACsLwv+AAAAAklEQVR4AewaftIAAA38SURBVO3B...",
        "platformFee": 80,
        "createdAt": "2025-05-28T19:24:45.884Z",
        "updatedAt": "2025-05-28T19:24:45.884Z",
        "expiresAt": "2025-05-29T19:24:45.883Z",
    }
    pix = PixQrCode(**data)
    assert pix.id == data["id"]
    assert pix.amount == data["amount"]
    assert pix.status == data["status"]
    assert pix.dev_mode == data["devMode"]
    assert pix.brcode == data["brCode"]
    assert pix.brcode_base64 == data["brCodeBase64"]
    assert pix.platform_fee == data["platformFee"]
    assert pix.created_at == data["createdAt"]
    assert pix.updated_at == data["updatedAt"]
    assert pix.expires_at == data["expiresAt"]

def test_pix_status_creation():
    """Tests the creation of a PixStatus instance and checks its attributes."""
    data = {
        "status": "PAID",
        "expires_at": "2025-05-29T19:45:03.256Z"
    }
    status = PixStatus(**data)
    assert status.status == data["status"]
    assert status.expires_at == data["expires_at"]

def test_pix_qrcode_in_creation_with_customer():
    """Tests the creation of a PixQrCodeIn instance with a CustomerMetadata."""
    customer = CustomerMetadata(
        tax_id="123.456.789-00",
        name="Test Customer",
        email="test@example.com",
        cellphone="(11) 99999-9999"
    )
    data = {
        "amount": 1500,
        "expires_in": 3600,
        "description": "Test payment",
        "customer": customer
    }
    pix_in = PixQrCodeIn(**data)
    assert pix_in.amount == data["amount"]
    assert pix_in.expires_in == data["expires_in"]
    assert pix_in.description == data["description"]
    assert isinstance(pix_in.customer, CustomerMetadata)
    assert pix_in.customer.tax_id == customer.tax_id

def test_pix_qrcode_in_creation_with_customer_dict():
    """Tests the creation of a PixQrCodeIn instance with a customer as dict."""
    customer_dict = {
        "tax_id": "123.456.789-00",
        "name": "Test Customer",
        "email": "test@example.com",
        "cellphone": "(11) 99999-9999"
    }
    data = {
        "amount": 2000,
        "expires_in": 1800,
        "description": "Another payment",
        "customer": customer_dict
    }
    pix_in = PixQrCodeIn(**data)
    assert pix_in.amount == data["amount"]
    assert pix_in.expires_in == data["expires_in"]
    assert pix_in.description == data["description"]
    assert isinstance(pix_in.customer, dict)
    assert pix_in.customer["tax_id"] == customer_dict["tax_id"]

def test_pix_qrcode_in_serialization():
    """Tests the serialization of a PixQrCodeIn instance."""
    data = {
        "amount": 500,
        "expires_in": 600,
        "description": "Serialize test",
        "customer": {
            "tax_id": "987.654.321-00",
            "name": "Serialize Customer",
            "email": "serialize@example.com",
            "cellphone": "(22) 88888-8888"
        }
    }
    pix_in = PixQrCodeIn(**data)
    serialized = pix_in.model_dump(by_alias=True)
    assert serialized["amount"] == 500
    assert serialized["expires_in"] == 600
    assert serialized["description"] == "Serialize test"
    assert serialized["customer"]["tax_id"] == "987.654.321-00"