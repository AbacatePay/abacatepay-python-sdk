from typing import Annotated, Optional

from annotated_types import Ge
from pydantic import AliasChoices, BaseModel, Field


class Product(BaseModel):
    """A product to be appended to a billing when it's being created

    Args:
        external_id (str): the product ID in your application.
        name (str): the product name.
        description (Optional[str]): a detailed description of the product.
        quantity (int): the number of units of the given product (min: 1).
        price (int): the price of the product in cents (min: 100).
    """

    external_id: str = Field(
        validation_alias=AliasChoices('externalId', 'external_id'),
        serialization_alias='externalId',
    )
    name: str
    description: Optional[str] = None
    quantity: Annotated[int, Ge(1)]
    price: Annotated[int, Ge(100)]


class ProductInline(BaseModel):
    """Represents a product inside a Billing.

    Args:
        id (str): the product ID.
        external_id (str): the product ID in your application.
        quantity (int): the number of units of the given product.
    """

    id: str
    external_id: str = Field(
        validation_alias=AliasChoices('external_id', 'externalId'),
        serialization_alias='externalId',
    )
    quantity: Annotated[int, Ge(1)]
