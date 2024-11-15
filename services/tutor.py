from models.tutor import Tutor as TutorModel
from schemas.tutor import Tutor

class TutorService:
    def __init__(self, db):
        self.db = db

    def get_tutor(self, filters: dict):
        query = self.db.query(TutorModel) 
        # Aplica los filtros dinámicamente si existen
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(TutorModel, field) == value)
        return query.all() 
    
    def add_tutor(self, tutor: Tutor):
        new_tutor = TutorModel(**tutor.dict())
        self.db.add(new_tutor)
        self.db.commit()
        return new_tutor

    def update_tutor(self, tutor_id, tutor: Tutor):
        query = self.db.query(TutorModel).filter(TutorModel.tutor_id == tutor_id).first()
        if not query:
            return None
        query.identificacion = tutor.identificacion
        query.tipo_identificacion = tutor.tipo_identificacion
        query.primer_nombre = tutor.primer_nombre
        query.segundo_nombre = tutor.segundo_nombre
        query.primer_apellido = tutor.primer_apellido
        query.segundo_apellido = tutor.segundo_apellido
        query.correo = tutor.correo
        query.celular = tutor.celular
        query.direccion = tutor.direccion
        query.periodo_id = tutor.periodo_id
        query.user = tutor.user
        query.password = tutor.password
        self.db.commit()
        return query

    def delete_tutor(self, tutor_id):
        tutor = self.db.query(TutorModel).filter(TutorModel.tutor_id == tutor_id).first()
        if not tutor:
            return None
        self.db.delete(tutor)
        self.db.commit()
        return tutor