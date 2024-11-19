from models.asistencia import Asistencia as AsistenciaModel
from schemas.asistencia import Asistencia

class AsistenciaService:
    def __init__(self, db):
        self.db = db

    def get_asistencia(self, filters: dict):
        query = self.db.query(AsistenciaModel)      
        for field, value in filters.items():
            if value is not None:
                query = query.filter(getattr(AsistenciaModel, field) == value)
        return query.all() 

    
    def add_asistencia(self, asistencia: Asistencia):
        new_asistencia = AsistenciaModel(**asistencia.model_dump())
        self.db.add(new_asistencia)
        self.db.commit()
        return new_asistencia

    def update_asistencia(self, filters: dict):
        query = self.db.query(AsistenciaModel).filter(AsistenciaModel.asistencia_id == filters['asistencia_id']).first()
        if not query:
            return None
        for field, value in filters.items():
            if value is not None:
                setattr(query, field, value)
        self.db.commit()
        return query

    def delete_asistencia(self, asistencia_id):
        asistencia = self.db.query(AsistenciaModel).filter(AsistenciaModel.asistencia_id == asistencia_id).first()
        if not asistencia:
            return None
        self.db.delete(asistencia)
        self.db.commit()
        return asistencia