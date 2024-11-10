from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.user import User as User
from services.user import UserService
from config.database import Session, get_db


user_router = APIRouter()

@user_router.get('/users', tags=["Users"])
def get_users():
    db = Session()
    users = UserService(db).get_users()
    if not users:
        return JSONResponse(content={"message": "Users not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(users), status_code=200)

@user_router.get('/users/{user_id}', tags=["Users"])
def get_user_by_id(user_id: int):
    db = Session()
    user = UserService(db).get_user_by_id(user_id)
    if user is None:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(user), status_code=200)

@user_router.post('/users', tags=["Users"])
def create_user(user: User):
    db = Session()
    query = UserService(db).add_user(user)
    if query is None:
        return JSONResponse(content={"message": "User not created"}, status_code=404)
    return JSONResponse(content={"message": "User created", "user": jsonable_encoder(query)}, status_code=201)

@user_router.put('/users/{user_id}', tags=["Users"])
def update_user(user_id: int, user: User):
    db = Session()
    query = UserService(db).update_user(user_id, user)
    if query is None:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    return JSONResponse(content={"message": "User updated", "user": jsonable_encoder(query)}, status_code=200)

@user_router.delete('/users/{user_id}', tags=["Users"])
def delete_user(user_id: int):
    db = Session()
    query = UserService(db).delete_user(user_id)
    if query is None:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    return JSONResponse(content={"message": "User deleted", "user": jsonable_encoder(query)}, status_code=200)
