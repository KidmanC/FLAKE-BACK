from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.tutor import Tutor as TutorModel
from config.database import Session
from services.auth import AuthService

from schemas.user import User, UserInDB



auth_router = APIRouter()
db = Session()
auth_service = AuthService(db)


@auth_router.post('/tokens', tags=["Auth"])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = auth_service.get_user(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(user=user_dict.user, password=user_dict.password)
    print('user:',user)
    password = AuthService(db).fake_hash_password(form_data.password)
    print('password:',password)
    if not password == user.password:
        print('malo')
        raise HTTPException(status_code=400, detail="Incorrect username or password")
        

    return {"access_token": user.user, "token_type": "bearer"}


@auth_router.get("/users/me" , tags=["Auth"])
async def read_users_me(
    current_user: Annotated[User, Depends(auth_service.get_current_user)],
):
    return current_user