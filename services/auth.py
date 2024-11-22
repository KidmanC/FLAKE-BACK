
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.user import UserInDB
from models.tutor import Tutor as TutorModel

class AuthService:
    def __init__(self, db):
        self.db = db

    def get_user(self, username: str):
        user_dict = self.db.query(TutorModel).filter(TutorModel.user == username).first()
        print('user_dict:',user_dict.user)
        print('user_dict:',user_dict.password)
        if not user_dict:
            return None
        return UserInDB(user=user_dict.user, password = user_dict.password)
    
    def fake_hash_password(self, password: str):
        return "hashed" + password


    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="tokens")

    def fake_decode_token(self, token):
        # This doesn't provide any security at all
        # Check the next version
        user = self.get_user(token)
        return user

    async def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]):
        user = self.fake_decode_token(token)
        print('hola:',user)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return user

    