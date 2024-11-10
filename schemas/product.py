from pydantic import BaseModel

class Product(BaseModel):
    #id: int | None = None
    name: str | None = None
    brand: str | None = None
    created_by: int | None = None