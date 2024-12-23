from pydantic import BaseModel

class Product(BaseModel):
    externalId: str
    name: str
    quantity: int
    price: int
    description: str
