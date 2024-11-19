from models.horario import Horario as HorarioModel
from schemas.horario import Horario

class HorarioService:
    def __init__(self, db):
        self.db = db

    def get_horario(self, filters: dict):
        query = self.db.query(HorarioModel)
        for field, value in filters.items():
            if value is not None:
                query = query.filter(getattr(HorarioModel, field) == value)
        return query.all() 
    
    def add_horario(self, horario: Horario):
        new_horario = HorarioModel(**horario.model_dump())
        self.db.add(new_horario)
        self.db.commit()
        return new_horario

    def update_horario(self, filters: dict):
        query = self.db.query(HorarioModel).filter(HorarioModel.horario_id == filters['horario_id']).first()
        if not query:
            return None
        for field, value in filters.items():
            if value is not None:
                setattr(query, field, value)
        self.db.commit()
        return query

    def delete_horario(self, horario_id):
        horario = self.db.query(HorarioModel).filter(HorarioModel.horario_id == horario_id).first()
        if not horario:
            return None
        self.db.delete(horario)
        self.db.commit()
        return horario