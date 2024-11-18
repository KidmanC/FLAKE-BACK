from models.institucion import Institucion as InstitucionModel
from schemas.institucion import Institucion

class InstitucionService:
    def __init__(self, db):
        self.db = db

    def get_institucion(self, filters: dict):
        query = self.db.query(InstitucionModel)
        for field, value in filters.items():
            if value is not None:
                query = query.filter(getattr(InstitucionModel, field) == value)
        return query.all() 

    def add_institucion(self, institucion: Institucion):
        new_institucion = InstitucionModel(**institucion.model_dump())
        self.db.add(new_institucion)
        self.db.commit()
        return new_institucion

    def update_institucion(self, institucion_id, institucion: Institucion):
        query = self.db.query(InstitucionModel).filter(InstitucionModel.institucion_id == institucion_id).first()
        if not query:
            return None
        query.localidad = institucion.localidad
        query.codigo_dane = institucion.codigo_dane
        query.nombre = institucion.nombre
        query.rector = institucion.rector
        query.direccion = institucion.direccion
        query.barrio = institucion.barrio
        self.db.commit()
        return query

    def delete_institucion(self, institucion_id):
        institucion = self.db.query(InstitucionModel).filter(InstitucionModel.institucion_id == institucion_id).first()
        if not institucion:
            return None
        self.db.delete(institucion)
        self.db.commit()
        return institucion