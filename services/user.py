from models.user import User as UserModel
from schemas.user import User

class UserService:
    def __init__(self, db):
        self.db = db

    def get_user_by_id(self, user_id):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def get_users(self):
        return self.db.query(UserModel).all()
    
    def add_user(self, user: User):
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return new_user

    def update_user(self, user_id, user: User):
        query = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not query:
            return None
        query.name = user.name
        query.age = user.age
        query.email = user.email
        self.db.commit()
        return query

    def delete_user(self, user_id):
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        return user