from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.user import User as UserSchema
from models.user import User
from config.database import Session, get_db


user_router = APIRouter()

@user_router.get('/users', tags=["Users"])
def get_users():
    db = Session()
    users = db.query(User).all()
    return JSONResponse(content= jsonable_encoder(users), status_code=200)