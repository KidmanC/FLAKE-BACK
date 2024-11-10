from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.product import Product as Product
from config.database import Session
from config.database import get_db, Session
from services.product import ProductService


product_router = APIRouter()

@product_router.get('/products', tags=["Products"])
def get_products():
    db = Session()
    products = ProductService(db).get_products()
    if not products:
        return JSONResponse(content={"message": "Products not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(products), status_code=200)

@product_router.get('/products/{product_id}', tags=["Products"])
def get_product_by_id(product_id: int):
    db = Session()
    product = ProductService(db).get_product_by_id(product_id)
    if product is None:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(product), status_code=200)

@product_router.post('/products', tags=["Products"])
def create_product(product: Product):
    db = Session()
    query = ProductService(db).add_product(product)
    return JSONResponse(content={"message": "Product created", "product": jsonable_encoder(query)}, status_code=201)

@product_router.put('/products/{product_id}', tags=["Products"])
def update_product(product_id: int, product: Product):
    db = Session()
    query = ProductService(db).update_product(product_id, product)
    if query is None:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    return JSONResponse(content={"message": "Product updated", "product": jsonable_encoder(query)}, status_code=200)

@product_router.delete('/products/{product_id}', tags=["Products"])
def delete_product(product_id: int):
    db = Session()
    query = ProductService(db).delete_product(product_id)
    if query is None:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    return JSONResponse(content={"message": "Product deleted", "product": jsonable_encoder(query)}, status_code=200)

