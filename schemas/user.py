from pydantic import BaseModel

class User(BaseModel):
    #id: int | None = None
    name: str | None = None
    age: int | None = None
    email: str | None = None
