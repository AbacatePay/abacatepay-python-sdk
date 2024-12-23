from pydantic import BaseModel

class Customer(BaseModel):
    """
    Customer model

    Attributes:
        id: str | None
        taxId: str | None
        name: str | None
        email: str
        cellphone: str | None
    Note: never pass `id` as an argument, it is supposed to be returned by the API!
    """
    id: str | None = None
    taxId: str | None = None
    name: str | None = None
    email: str
    cellphone: str | None = None

    @classmethod
    def from_dict(cls, data: dict):
        metadata = data.get("metadata", {})
        return cls(
            id = data.get("id"),
            taxId=metadata.get("taxId"),
            name=metadata.get("name"),
            email=metadata.get("email"),
            cellphone=metadata.get("cellphone"),
        )