from models.aula import Aula as AulaModel
from schemas.aula import Aula

class AulaService:
    def __init__(self, db):
        self.db = db

    def get_aula(self, filters: dict):
        query = self.db.query(AulaModel) 
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(AulaModel, field) == value) ###filtra dinamicamente
        return query.limit(200).all()
    
    def add_aula(self, aula: Aula):
        new_aula = AulaModel(**aula.model_dump())
        self.db.add(new_aula)
        self.db.commit()
        return aula

    def update_aula(self, filters: dict):
        query = self.db.query(AulaModel).filter(AulaModel.aula_id == filters['aula_id']).first()
        if not query:
            return None
        for field, value in filters.items():
            if value is not None:
                setattr(query, field, value) ###actualiza dinamicamente
        self.db.commit()
        query = self.db.query(AulaModel).filter(AulaModel.aula_id == filters['aula_id']).first()
        return query

    def delete_aula(self, aula_id):
        aula = self.db.query(AulaModel).filter(AulaModel.aula_id == aula_id).first()
        if not aula:
            return None
        self.db.delete(aula)
        self.db.commit()
        return aula