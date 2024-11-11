from models.clases_no_dadas import Clases_no_dadas as Clases_no_dadas_Model
from schemas.clases_no_dadas import Clases_no_dadas

class Clases_no_dadas_Service:
    def __init__(self, db):
        self.db = db

    def get_clases_no_dadas_by_id(self, clase_no_dada_id):
        return self.db.query(Clases_no_dadas_Model).filter(Clases_no_dadas_Model.clase_no_dada_id == clase_no_dada_id).first()

    def get_clases_no_dadass(self):
        return self.db.query(Clases_no_dadas_Model).all()
    
    def add_clases_no_dadas(self, clases_no_dadas: Clases_no_dadas):
        new_clases_no_dadas = Clases_no_dadas_Model(**clases_no_dadas.dict())
        self.db.add(new_clases_no_dadas)
        self.db.commit()
        return new_clases_no_dadas

    def update_clases_no_dadas(self, clase_no_dada_id, clases_no_dadas: Clases_no_dadas):
        query = self.db.query(Clases_no_dadas_Model).filter(Clases_no_dadas_Model.clase_no_dada_id == clase_no_dada_id).first()
        if not query:
            return None
        query.clase_id = clases_no_dadas.clase_id
        query.fecha_clase_no_dada = clases_no_dadas.fecha_clase_no_dada
        query.motivo = clases_no_dadas.motivo
        self.db.commit()
        return query

    def delete_clases_no_dadas(self, clase_no_dada_id):
        clases_no_dadas = self.db.query(Clases_no_dadas_Model).filter(Clases_no_dadas_Model.clase_no_dada_id == clase_no_dada_id).first()
        if not clases_no_dadas:
            return None
        self.db.delete(clases_no_dadas)
        self.db.commit()
        return clases_no_dadas