from pydantic import BaseModel

class User(BaseModel):
    #tutor_id: int | None = None
    user: str

class UserInDB(User):
    password: str
