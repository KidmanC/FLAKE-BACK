from models.clases_no_dadas import Clases_no_dadas as Clases_no_dadas_Model
from schemas.clases_no_dadas import Clases_no_dadas

class Clases_no_dadas_Service:
    def __init__(self, db):
        self.db = db

    def get_clase_no_dada(self, filters: dict):
        query = self.db.query(Clases_no_dadas_Model)
        for field, value in filters.items():
            if value is not None:
                query = query.filter(getattr(Clases_no_dadas_Model, field) == value)
        return query.all() 
    
    def add_clase_no_dada(self, clase_no_dada: Clases_no_dadas):
        new_clase_no_dada = Clases_no_dadas_Model(**clase_no_dada.model_dump())
        self.db.add(new_clase_no_dada)
        self.db.commit()
        return new_clase_no_dada

    def update_clases_no_dadas(self, clase_no_dada_id, clase_no_dada: Clases_no_dadas):
        query = self.db.query(Clases_no_dadas_Model).filter(Clases_no_dadas_Model.clase_no_dada_id == clase_no_dada_id).first()
        if not query:
            return None
        query.clase_id = clase_no_dada.clase_id
        query.fecha_clase_no_dada = clase_no_dada.fecha_clase_no_dada
        query.motivo = clase_no_dada.motivo
        self.db.commit()
        return query

    def delete_clase_no_dada(self, clase_no_dada_id):
        clase_no_dada = self.db.query(Clases_no_dadas_Model).filter(Clases_no_dadas_Model.clase_no_dada_id == clase_no_dada_id).first()
        if not clase_no_dada:
            return None
        self.db.delete(clase_no_dada)
        self.db.commit()
        return clase_no_dada