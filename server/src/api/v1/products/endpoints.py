from fastapi import APIRouter

from .services import Services
from .schemas import Product, Products, UpdateProduct, DeleteProduct


router = APIRouter(prefix="/products")


@router.get(path="", response_model=Products)
async def get_products() -> Products:
    products = await Services().get_all()
    return products


@router.get(path="/{product_id}", response_model=Product)
async def get_product(product_id: str) -> Product:
    product = await Services().get(product_id=product_id)
    return product


@router.post(path="", response_model=Product)
async def post_products(product: Product) -> Product:
    product = await Services().create(product=product)
    return product


@router.put(path="/{product_id}", response_model=Product)
async def update_products(product: UpdateProduct) -> Product:
    product = await Services().update(product=product)
    return product


@router.delete(path="/{product_id}", response_model=Product)
async def delete_product(product: DeleteProduct) -> Product:
    product = await Services().delete(product=product)
    return product
