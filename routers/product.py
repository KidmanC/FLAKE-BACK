from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.product import Product as ProductSchema
from models.product import Product 
from config.database import Session
from config.database import get_db, Session


product_router = APIRouter()

@product_router.get('/products', tags=["Products"])
def get_products():
    db = Session()
    products = db.query(Product).all()
    return JSONResponse(content=jsonable_encoder(products), status_code=200)