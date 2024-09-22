from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    description: str | None = None
    count: int
    price: str


class Products(BaseModel):
    products: list[Product]


class UpdateProduct(BaseModel):
    id: str
    name: str | None = None
    description: str | None = None
    count: str | None = None
    price: str | None = None


class DeleteProduct(BaseModel):
    id: str
