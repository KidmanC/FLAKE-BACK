from models.asistencia import Asistencia as AsistenciaModel
from schemas.asistencia import Asistencia

class AsistenciaService:
    def __init__(self, db):
        self.db = db

    def get_asistencia_by_id(self, asistencia_id):
        return self.db.query(AsistenciaModel).filter(AsistenciaModel.asistencia_id == asistencia_id).first()

    def get_asistencias(self):
        return self.db.query(AsistenciaModel).all()
    
    def add_asistencia(self, asistencia: Asistencia):
        new_asistencia = AsistenciaModel(**asistencia.dict())
        self.db.add(new_asistencia)
        self.db.commit()
        return new_asistencia

    def update_asistencia(self, asistencia_id, asistencia: Asistencia):
        query = self.db.query(AsistenciaModel).filter(AsistenciaModel.asistencia_id == asistencia_id).first()
        if not query:
            return None
        query.clase_id = asistencia.clase_id
        query.estudiante_id = asistencia.estudiante_id
        query.fecha = asistencia.fecha
        query.presente = asistencia.presente
        self.db.commit()
        return query

    def delete_asistencia(self, asistencia_id):
        asistencia = self.db.query(AsistenciaModel).filter(AsistenciaModel.asistencia_id == asistencia_id).first()
        if not asistencia:
            return None
        self.db.delete(asistencia)
        self.db.commit()
        return asistencia