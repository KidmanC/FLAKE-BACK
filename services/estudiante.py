from models.estudiante import Estudiante as EstudianteModel
from schemas.estudiante import Estudiante

class EstudianteService:
    def __init__(self, db):
        self.db = db

    def get_estudiante(self, filters:dict):
        query = self.db.query(EstudianteModel) 
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(EstudianteModel, field) == value)
        return query.limit(200).all()
    
    def get_nota_final(self, estudiante_id, periodo_id):
        notas = self.db.query(EstudianteModel).filter(EstudianteModel.estudiante_id == estudiante_id).first().notas
        notas = [nota for nota in notas if nota.periodo_id == periodo_id]

        return sum(nota.calificacion for nota in notas if nota.periodo_id == periodo_id) / 4

    def add_estudiante(self, estudiante: Estudiante):
        new_estudiante = EstudianteModel(**estudiante.model_dump())
        self.db.add(new_estudiante)
        self.db.commit()
        return estudiante

    def update_estudiante(self,filters: dict):
        query = self.db.query(EstudianteModel).filter(EstudianteModel.estudiante_id == filters['estudiante_id']).first()
        if not query:
            return None
        for field, value in filters.items():
            if value is not None:
                setattr(query, field, value)
        self.db.commit()
        query = self.db.query(EstudianteModel).filter(EstudianteModel.estudiante_id == filters['estudiante_id']).first()
        return query






    def delete_estudiante(self, estudiante_id):
        estudiante = self.db.query(EstudianteModel).filter(EstudianteModel.estudiante_id == estudiante_id).first()
        if not estudiante:
            return None
        self.db.delete(estudiante)
        self.db.commit()
        return estudiante