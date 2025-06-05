from pydantic import BaseModel, Field
from typing import Optional, Union
from ..constants import PIX_QR_CODE_STATUS
from ..customers.models import CustomerMetadata

class PixQrCode(BaseModel):
  id: str = Field(..., description="Unique identifier of the Pix QRCode.", example="pix_char_123456")
  amount: int = Field(..., description="Amount to be paid.", example=100)
  status: PIX_QR_CODE_STATUS = Field(..., description="Information about the status of the Pix QRCode. Options: PENDING, EXPIRED, CANCELLED, PAID, REFUNDED", example="PENDING")
  dev_mode: bool = Field(..., description="Environment in which the Pix QRCode was created.", example=True, validation_alias="devMode")
  brcode: str = Field(..., description="Copy-and-paste code of the Pix QRCode.", example="00020101021226950014br.gov.bcb.pix", validation_alias="brCode")
  brcode_base64: str = Field(..., description="Base64 image of the Pix QRCode.", example="data:image/png;base64,iVBORw0KGgoAAA", validation_alias="brCodeBase64")
  platform_fee: int = Field(..., description="Platform fees.", example=80, validation_alias="platformFee")
  created_at: str = Field(..., description="Creation date of the Pix QRCode.", example="2025-03-24T21:50:20.772Z", validation_alias="createdAt")
  updated_at: str = Field(..., description="Update date of the Pix QRCode.", example="2025-03-24T21:50:20.772Z", validation_alias="updatedAt")
  expires_at: str = Field(..., description="Expiration date of the Pix QRCode.", example="2025-03-25T21:50:20.772Z", validation_alias="expiresAt")

class PixStatus(BaseModel):
  status: PIX_QR_CODE_STATUS = Field(..., description="Information about the status of the Pix QRCode. Options: PENDING, EXPIRED, CANCELLED, PAID, REFUNDED", example="PENDING")
  expires_at: str = Field(None, description="Expiration date of the Pix QRCode.", example="2025-03-25T21:50:20.772Z")

class PixQrCodeIn(BaseModel):
  amount: int = Field(..., description="Amount to be paid in cents.", example=100)
  expires_in: Optional[int] = Field(None, description="Expiration time in seconds. Defaults to None.", example=3600)
  description: Optional[str] = Field(None, description="A description for the Pix QR Code. Defaults to None.", example="Payment for services")
  customer: Optional[Union[dict, CustomerMetadata]] = Field(
        {}, description="Customer information. Optional."
  )