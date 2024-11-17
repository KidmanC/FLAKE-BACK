from models.tutor import Tutor as TutorModel
from schemas.tutor import Tutor

class TutorService:
    def __init__(self, db):
        self.db = db

    def get_tutor(self, filters: dict):
        query = self.db.query(TutorModel) 
        
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(TutorModel, field) == value) ###filtra dinamicamente
        return query.all() 
    
    def add_tutor(self, tutor: Tutor):
        new_tutor = TutorModel(**tutor.dict())
        self.db.add(new_tutor)
        self.db.commit()
        return new_tutor

    def update_tutor(self, filters: dict):
        query = self.db.query(TutorModel).filter(TutorModel.tutor_id == filters['tutor_id']).first()
        if not query:
            return None
        for field, value in filters.items():
            if value is not None:
                setattr(query, field, value) ###actualiza dinamicamente
        self.db.commit()
        return query

    def delete_tutor(self, tutor_id):
        tutor = self.db.query(TutorModel).filter(TutorModel.tutor_id == tutor_id).first()
        if not tutor:
            return None
        self.db.delete(tutor)
        self.db.commit()
        return tutor