from fastapi import HTTPException, status

from .repositories import CRUD
from .schemas import Product, Products, DeleteProduct, UpdateProduct
from .models import Product as ProductModel


class Services:
    def __init__():
        pass

    async def get_all() -> Products:
        products_models = await CRUD().read_all()
        products = [Product(**product) for product in products_models]
        return Products(products=products)

    async def get(product_id: str) -> Product:
        product = await CRUD().read(product_id=product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="no product with that id",
            )
        return product

    async def create(product: Product) -> Product:
        product_model = ProductModel(**product.model_dump())
        product_model = await CRUD().create(ProductModel(**product.model_dump()))
        if not product_model:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error when creating product",
            )
        return product

    async def update(product: UpdateProduct) -> Product:
        product_model = ProductModel(**product.model_dump())
        product_model = await CRUD().update(product=product_model)
        if not product_model:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error when updating product",
            )
        return product

    async def delete(product: DeleteProduct) -> Product:
        product_model = ProductModel(**product.model_dump())
        product_model = await CRUD().delete(product=product_model)
        if not product_model:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error when deleting product",
            )
        return product
