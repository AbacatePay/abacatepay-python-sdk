from typing import Annotated, Optional

from pydantic import AliasChoices, BaseModel, Field, StringConstraints


class CustomerMetadata(BaseModel):
    """Customer model

    Args:
        tax_id (str):  the customer identifier such as CPF or CNPJ.
        name (str): the customer name
        email (str): the customer email address
        cellphone: (str): the customer phone number.
    """

    tax_id: str = Field(
        serialization_alias='taxId',
        validation_alias=AliasChoices('taxId', 'tax_id'),
    )
    name: str
    email: str
    cellphone: str


class CustomerInline(BaseModel):
    """The customer model attached to other models

    Args:
        metadata (Customer): the metadata of the customer.
    """

    metadata: Optional[CustomerMetadata] = None


CustomerID = Annotated[str, StringConstraints(pattern=r'^cust_[A-Za-z0-9]+$')]


class Customer(CustomerInline):
    """
    Customer returned by API.

    Args:
        id (CustomerID): the customer unique ID in abacatepay.
        tax_id (str) the customer identification (CPF or CNPJ).
        email (str): the customer's email
        name (str): the customer's name
        cellphone (str): the customer's phone number
    """

    id: CustomerID

    @property
    def tax_id(self) -> str:
        """the customer identification (CPF or CNPJ)."""
        return self.metadata.tax_id

    @property
    def name(self) -> str:
        """the customer's name"""
        return self.metadata.name

    @property
    def email(self) -> str:
        """the customer's email"""
        return self.metadata.email

    @property
    def cellphone(self) -> str:
        """the customer's phone number"""
        return self.metadata.cellphone
