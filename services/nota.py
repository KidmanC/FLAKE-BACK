from models.nota import Nota as NotaModel
from schemas.nota import Nota

class NotaService:
    def __init__(self, db):
        self.db = db

    def get_nota_by_id(self, nota_id):
        return self.db.query(NotaModel).filter(NotaModel.nota_id == nota_id).first()

    def get_notas(self):
        return self.db.query(NotaModel).all()
    
    def add_nota(self, nota: Nota):
        new_nota = NotaModel(**nota.dict())
        self.db.add(new_nota)
        self.db.commit()
        return new_nota

    def update_nota(self, nota_id, nota: Nota):
        query = self.db.query(NotaModel).filter(NotaModel.nota_id == nota_id).first()
        if not query:
            return None
        query.periodo_id = nota.periodo_id
        query.estudiante_id = nota.estudiante_id
        query.clase_id = nota.clase_id
        query.bloque = nota.bloque
        query.calificacion = nota.calificacion
        return query

    def delete_nota(self, nota_id):
        nota = self.db.query(NotaModel).filter(NotaModel.nota_id == nota_id).first()
        if not nota:
            return None
        self.db.delete(nota)
        self.db.commit()
        return nota