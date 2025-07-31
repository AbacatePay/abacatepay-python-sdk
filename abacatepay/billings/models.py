from typing import Annotated, Any, Iterator, List, Optional

from pydantic import (
    AliasChoices,
    AwareDatetime,
    BaseModel,
    Field,
    StringConstraints,
)

from ..constants import BILLING_KINDS, BILLING_METHODS, BILLING_STATUS
from ..customers.models import CustomerID, CustomerInline, CustomerMetadata
from ..products.models import Product, ProductInline

HttpUrl = Annotated[
    str,
    StringConstraints(
        pattern=(
            r'^(https?:\/\/)'  # Protocol (http or https)
            r'(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'  # Domain (including subdomains)  # noqa: E501
            r'(\/[^\s]*)?$'  # Optional path
        )
    ),
]


class BillingIn(BaseModel):
    """Represents a billing model to creation

    Args:
        frequency (BILLING_KINDS): The billing frequency. Defaults to
            `ONE_TIME`.
        methods (List[BILLING_METHODS]): the allowed method to the billing.
            Defaults to ['PIX']
        products (List[Product]): The list of products in the billing.
        completion_url (HttpUrl): the redirect URL when the payment is
            completed.
        return_url (HttpUrl): the redirect URL when the user clicks on the
            "back" button.
        customer_id (Optional[CustomerID]): Unique identifier of the billing.
        customer (CustomerMetadata): Your customer information. Defaults to {}.
    """

    frequency: BILLING_KINDS = 'ONE_TIME'
    methods: List[BILLING_METHODS] = ['PIX']
    products: List[Product]
    return_url: HttpUrl = Field(serialization_alias='returnUrl')
    completion_url: HttpUrl = Field(serialization_alias='completionUrl')
    customer_id: Optional[CustomerID] = Field(None, serialization_alias='customerId')
    customer: CustomerMetadata | dict[str, Any] = {}


class BillingMetadata(BaseModel):
    """model of a billing metadata

    Args:
        completion_url (str): the redirect URL when the payment is completed.
        return_url (str): the redirect URL when the user clicks on the "back"
            button.
        fee (int): the billing fee.
    """

    completion_url: str = Field(
        validation_alias=AliasChoices('completion_url', 'completionUrl'),
        serialization_alias='completionUrl',
    )
    return_url: str = Field(
        validation_alias=AliasChoices('return_url', 'returnUrl'),
        serialization_alias='returnUrl',
    )
    fee: int


class Billing(BaseModel):
    """Billing model

    Args:
        id (str): Unique identifier of the billing.
        url (str): the URL which the user can complete the payment.
        amount (int): the amount to be paid (in cents).
        status (BILLING_STATUS): the current billing status.
        dev_mode (bool): if it's operating in dev mode.
        methods (List[BILLING_METHODS]): the allowed method to the billing.
        products (List[ProductInline]): The list of products in the billing.
        frequency (BILLING_KINDS): The billing frequency.
        next_billing (Optional[AwareDatetime]): date and time of the next
            billing.
        customer (Optional[CustomerInline]): the data of the customer that the
            billing belongs to.
        created_at (AwareDatetime): The date and time when the billing was
            created.
        updated_at (AwareDatetime): the date and time of the last billing
            update.
        allow_cupons (bool): If the billing has allowed coupons or not.
        coupons (List[Coupon]): the available coupons.
        coupons_used (List[Coupon]): active coupons for this billing.
        metadata (BillingMetadata): the billing metadata.
    """

    id: str
    url: str
    amount: int
    status: BILLING_STATUS
    dev_mode: bool = Field(validation_alias='devMode')
    methods: List[BILLING_METHODS]
    products: List[ProductInline]
    frequency: BILLING_KINDS
    next_billing: Optional[AwareDatetime] = Field(
        None,
        validation_alias=AliasChoices('next_billing', 'nextBilling'),
        serialization_alias='nextBilling',
    )
    customer: Optional[CustomerInline] = None
    created_at: AwareDatetime = Field(validation_alias='createdAt')
    updated_at: AwareDatetime = Field(validation_alias='updatedAt')
    coupons: List[str]
    coupons_used: List[str] = Field(
        validation_alias='couponsUsed', serialization_alias='couponsUsed'
    )
    metadata: BillingMetadata


class BillingList(BaseModel):
    """Represents a list of Billings. It can be directly iterated and
    supports the usage of the `len` function.

    Args:
        data (List[Billing]): the list object having all the billings.
    """

    data: List[Billing]

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator[Billing]:  # type: ignore
        return self.data.__iter__()
