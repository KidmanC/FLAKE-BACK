from models.horario import Horario as HorarioModel
from schemas.horario import Horario
from datetime import time
from typing import Optional

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
        self.validate_horario(
            hora_inicio = horario.hora_inicio, 
            hora_fin = horario.hora_fin, 
            query_hora_inicio = None, 
            query_hora_fin = None
        )
        new_horario = HorarioModel(**horario.model_dump())
        self.db.add(new_horario)
        self.db.commit()
        return horario

    def update_horario(self, filters: dict):
        query = self.db.query(HorarioModel).filter(HorarioModel.horario_id == filters['horario_id']).first()
        if not query:
            return None
        
        hora_inicio = filters.get("hora_inicio")
        hora_fin = filters.get("hora_fin")
        
        self.validate_horario(hora_inicio, hora_fin, query.hora_inicio, query.hora_fin)

        for field, value in filters.items():
            if value is not None:
                setattr(query, field, value)
        self.db.commit()
        query = self.db.query(HorarioModel).filter(HorarioModel.horario_id == filters['horario_id']).first()
        return query

    def delete_horario(self, horario_id):
        horario = self.db.query(HorarioModel).filter(HorarioModel.horario_id == horario_id).first()
        if not horario:
            return None
        self.db.delete(horario)
        self.db.commit()
        return horario
    
    def validate_horario(self, 
        hora_inicio: Optional[time], 
        hora_fin: Optional[time], 
        query_hora_inicio: Optional[time], 
        query_hora_fin: Optional[time]
    ):
# Caso Post y Put
        # hora_fin del filtro debe ser mayor que hora_inicio del filtro
        if hora_inicio and hora_fin:
            if hora_inicio >= hora_fin:
                raise ValueError("La hora de fin debe ser posterior a la hora de inicio.")

## Casos Put
        # Si solo se envió hora_inicio esta debe ser menor que la hora_fin del horario a actualizar
        elif hora_inicio: 
            if hora_inicio >= query_hora_fin:
                raise ValueError("La hora de inicio no puede ser mayor o igual que la hora de fin existente.")

        # Si solo se envió hora_fin esta debe ser mayor que la hora_inicio del horario a actualizar
        elif hora_fin:
            if hora_fin <= query_hora_inicio:
                raise ValueError("La hora de fin no puede ser menor o igual que la hora de inicio existente.")