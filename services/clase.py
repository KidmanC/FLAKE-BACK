from models.clase import Clase as ClaseModel
from schemas.clase import Clase

class ClaseService:
    def __init__(self, db):
        self.db = db

    def get_clase(self, filters: dict):
        query = self.db.query(ClaseModel) 
        # Aplica los filtros dinámicamente si existen
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(ClaseModel, field) == value)
        return query.all() 
    
    def add_clase(self, clase: Clase):
        new_clase = ClaseModel(**clase.dict())
        self.db.add(new_clase)
        self.db.commit()
        return new_clase

    def update_clase(self, clase_id, clase: Clase):
        query = self.db.query(ClaseModel).filter(ClaseModel.clase_id == clase_id).first()
        if not query:
            return None
        query.aula_id = clase.aula_id
        query.tutor_id = clase.tutor_id
        query.periodo_id = clase.periodo_id
        query.grado = clase.grado
        self.db.commit()
        return query

    def delete_clase(self, clase_id):
        clase = self.db.query(ClaseModel).filter(ClaseModel.clase_id == clase_id).first()
        if not clase:
            return None
        self.db.delete(clase)
        self.db.commit()
        return clase