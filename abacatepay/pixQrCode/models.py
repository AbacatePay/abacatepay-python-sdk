from typing import Any

from pydantic import BaseModel, Field

from ..constants import PIX_QR_CODE_STATUS
from ..customers.models import CustomerMetadata


class PixQrCode(BaseModel):
    """
    A representation of a Pix QRCode.

    Attributes:
        id (str): Unique identifier of the Pix QRCode.
        amount (int): Amount to be paid.
        status (str): Information about the status of the Pix QRCode.
        dev_mode (bool): Environment in which the Pix QRCode was created.
        brcode (str): Copy-and-paste code of the Pix QRCode.
        brcode_base64 (str): Base64 image of the Pix QRCode.
        platform_fee (int): Platform fees.
        created_at (str): Creation date of the Pix QRCode.
        updated_at (str): Update date of the Pix QRCode.
        expires_at (str): Expiration date of the Pix QRCode.
    """

    id: str = Field(
        description='Unique identifier of the Pix QRCode.',
        examples=['pix_char_123456'],
    )
    amount: int = Field(description='Amount to be paid.', examples=[100])
    status: PIX_QR_CODE_STATUS = Field(
        description=(
            'Information about the status of the Pix QRCode.'
            'Options: PENDING, EXPIRED, CANCELLED, PAID, REFUNDED'
        ),
        examples=['PENDING'],
    )
    dev_mode: bool = Field(
        description='Environment in which the Pix QRCode was created.',
        examples=[True],
        validation_alias='devMode',
    )
    brcode: str = Field(
        description='Copy-and-paste code of the Pix QRCode.',
        examples=['00020101021226950014br.gov.bcb.pix'],
        validation_alias='brCode',
    )
    brcode_base64: str = Field(
        description='Base64 image of the Pix QRCode.',
        examples=['data:image/png;base64,iVBORw0KGgoAAA'],
        validation_alias='brCodeBase64',
    )
    platform_fee: int = Field(
        description='Platform fees.',
        examples=[80],
        validation_alias='platformFee',
    )
    created_at: str = Field(
        description='Creation date of the Pix QRCode.',
        examples=['2025-03-24T21:50:20.772Z'],
        validation_alias='createdAt',
    )
    updated_at: str = Field(
        description='Update date of the Pix QRCode.',
        examples=['2025-03-24T21:50:20.772Z'],
        validation_alias='updatedAt',
    )
    expires_at: str = Field(
        description='Expiration date of the Pix QRCode.',
        examples=['2025-03-25T21:50:20.772Z'],
        validation_alias='expiresAt',
    )


class PixStatus(BaseModel):
    """Represents the status of a Pix QRCode.

    Attributes:
        status (str): Information about the status of the Pix QRCode.
        expires_at (str): Expiration date of the Pix QRCode.
    """

    status: PIX_QR_CODE_STATUS = Field(
        description=(
            'Information about the status of the Pix QRCode. '
            'Options: PENDING, EXPIRED, CANCELLED, PAID, REFUNDED'
        ),
        examples=['PENDING'],
    )
    expires_at: str | None = Field(
        None,
        description='Expiration date of the Pix QRCode.',
        examples=['2025-03-25T21:50:20.772Z'],
    )


class PixQrCodeIn(BaseModel):
    """Represents a Pix QRCode model for creation.

    Attributes:
        amount (int): Amount to be paid in cents.
        expires_in (int | None): Expiration time in seconds. Defaults to None.
        description (str | None): A description for the Pix QR Code. Defaults
            to None.
        customer (dict[str, Any] | CustomerMetadata): Customer information.
            Optional.
    """

    amount: int = Field(
        description='Amount to be paid in cents.',
        examples=[100],
    )
    expires_in: int | None = Field(
        None,
        description='Expiration time in seconds. Defaults to None.',
        examples=[3600],
    )
    description: str | None = Field(
        None,
        description='A description for the Pix QR Code. Defaults to None.',
        examples=['Payment for services'],
    )
    customer: dict[str, Any] | CustomerMetadata = Field(
        {}, description='Customer information. Optional.'
    )
