from models.aula import Aula as AulaModel
from schemas.aula import Aula

class AulaService:
    def __init__(self, db):
        self.db = db

    def get_aula_by_id(self, aula_id):
        return self.db.query(AulaModel).filter(AulaModel.aula_id == aula_id).first()

    def get_aulas(self):
        return self.db.query(AulaModel).all()
    
    def add_aula(self, aula: Aula):
        new_aula = AulaModel(**aula.dict())
        self.db.add(new_aula)
        self.db.commit()
        return new_aula

    def update_aula(self, aula_id, aula: Aula):
        query = self.db.query(AulaModel).filter(AulaModel.aula_id == aula_id).first()
        if not query:
            return None
        query.institucion_id = aula.institucion_id
        query.periodo_id = aula.periodo_id
        query.grado_texto = aula.grado_texto
        query.grado_num = aula.grado_num
        query.grupo = aula.grupo
        query.jornada = aula.jornada
        self.db.commit()
        return query

    def delete_aula(self, aula_id):
        aula = self.db.query(AulaModel).filter(AulaModel.aula_id == aula_id).first()
        if not aula:
            return None
        self.db.delete(aula)
        self.db.commit()
        return aula