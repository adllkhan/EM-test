from sqlalchemy import select

from .database import Session
from .models import Product


class CRUD:
    def __init__():
        pass

    async def create(product: Product) -> Product:
        async with Session.begin() as session:
            session.add(instance=product)
            await session.commit()
            return product

    async def read(product_id: str) -> Product:
        async with Session.begin() as session:
            product = await session.get(entity=Product, ident=product_id)
            return product

    async def read_all() -> list[Product]:
        async with Session.begin() as session:
            products = session.scalars(select(Product))
            return products

    async def update(product: Product) -> Product:
        async with Session.begin() as session:
            await session.delete(instance=product)
            await session.add(instance=product)
            await session.commit()
            return product

    async def delete(product: Product) -> Product:
        async with Session.begin() as session:
            await session.delete(instance=product)
            await session.commit()
            return product
