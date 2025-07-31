from typing import Any, Optional

from pydantic import (
    BaseModel,
    Field,
)

from ..constants import DISCOUNT_KINDS


class CouponIn(BaseModel):
    """
    Represents a coupon model for creation.

    Attributes:
        code (str): The unique code for the coupon.
        discount_kind (DISCOUNT_KINDS): The type of discount (e.g., percentage
            or fixed amount).
        discount (int): The value of the discount.
        notes (Optional[str]): A description or note about the coupon. Defaults
            to None.
            - Serialization alias: 'notes'
            - Example: "Cupom de desconto pro meu público"
        max_redeems (Optional[int]): The maximum number of times the coupon can
            be redeemed.
            Defaults to -1 for unlimited redemptions.
        metadata (Optional[dict]): Additional metadata for the coupon. Defaults
            to None.
    """

    code: str
    discount_kind: DISCOUNT_KINDS = Field(
        serialization_alias='discountKind',
        description='Type of discount (e.g., percentage or fixed amount)',
        examples=['PERCENTAGE', 'FIXED_AMOUNT'],
    )
    discount: int
    notes: Optional[str] = Field(
        None,
        serialization_alias='notes',
        description="Coupon's description",
        examples=['Cupom de desconto pro meu público'],
    )
    max_redeems: Optional[int] = Field(
        -1,
        description=(
            'Maximum number of times the coupon can be redeemed. Defaults to -1 for unlimited.'
        ),
        serialization_alias='maxRedeems',
    )
    metadata: dict[str, Any] = Field({}, description='Additional metadata for the coupon.')


class Coupon(BaseModel):
    """
    Represents a coupon model.

    Attributes:
        id (str): The unique identifier for the coupon.
        discount_kind (str): The type of discount (e.g., percentage or
            fixed amount).
        discount (int): The value of the discount.
        status (str): The current status of the coupon (e.g., ACTIVE, INACTIVE)
        notes (Optional[str]): A description or note about the coupon.
        max_redeems (int): The maximum number of times the coupon can be
            redeemed.
        redeems_count (int): The number of times the coupon has been redeemed.
        created_at (str): The timestamp when the coupon was created.
        updated_at (str): The timestamp when the coupon was last updated.
    """

    id: str
    discount_kind: str = Field(
        ...,
        alias='discountKind',
        description='Type of discount (e.g., percentage or fixed amount)',
    )
    discount: int
    status: str
    notes: str | None = Field(None, validation_alias='notes', description="Coupon's description")
    max_redeems: int = Field(
        -1,
        validation_alias='maxRedeems',
        description='Maximum number of times the coupon can be redeemed.',
    )
    redeems_count: int = Field(
        0,
        validation_alias='redeemsCount',
        description='Number of times the coupon has been redeemed.',
    )
    created_at: str = Field(
        ...,
        validation_alias='createdAt',
        description='Timestamp when the coupon was created.',
    )
    updated_at: str = Field(
        ...,
        validation_alias='updatedAt',
        description='Timestamp when the coupon was last updated.',
    )
    dev_mode: bool = Field(
        ...,
        validation_alias='devMode',
        description='Indicates if the coupon is in development mode.',
    )
