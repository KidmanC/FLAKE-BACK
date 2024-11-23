from models.tutor import Tutor as TutorModel
from schemas.tutor import Tutor
from services.auth import AuthService

class TutorService:
    def __init__(self, db):
        self.db = db

    def get_tutor(self, filters: dict):
        query = self.db.query(TutorModel)
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(TutorModel, field) == value) ###filtra dinamicamente
        return query.limit(200).all()
    
    def add_tutor(self, tutor: Tutor):
        new_tutor = TutorModel(**tutor.model_dump())
        self.db.add(new_tutor)
        self.db.commit()
        return tutor

    def update_tutor(self, filters: dict):
        query = self.db.query(TutorModel).filter(TutorModel.tutor_id == filters['tutor_id']).first()
        if not query:
            return None
        for field, value in filters.items():
            if value is not None:
                setattr(query, field, value) ###actualiza dinamicamente
        self.db.commit()
        query = self.db.query(TutorModel).filter(TutorModel.tutor_id == filters['tutor_id']).first()
        return query

    def delete_tutor(self, tutor_id):
        tutor = self.db.query(TutorModel).filter(TutorModel.tutor_id == tutor_id).first()
        if not tutor:
            return None
        self.db.delete(tutor)
        self.db.commit()
        return tutor
    
    def change_password(self, tutor_id, old_password, new_password):
        tutor = self.db.query(TutorModel).filter(TutorModel.tutor_id == tutor_id).first()
        password = AuthService(self.db).fake_hash_password(old_password)
        if not tutor:
            return None
        if tutor.password == password:
            tutor.password = AuthService(self.db).fake_hash_password(new_password)
            self.db.commit()
            return self.db.query(TutorModel).filter(TutorModel.tutor_id == tutor_id).first()
        return 0