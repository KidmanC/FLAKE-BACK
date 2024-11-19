from models.nota import Nota as NotaModel
from schemas.nota import Nota

class NotaService:
    def __init__(self, db):
        self.db = db

    def get_nota(self, filters:dict):
        query = self.db.query(NotaModel) 
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(NotaModel, field) == value)
        return query.all()
    
    def add_nota(self, nota: Nota):
        new_nota = NotaModel(**nota.model_dump())
        self.db.add(new_nota)
        self.db.commit()
        return new_nota

    def update_nota(self,filters: dict):
        query = self.db.query(NotaModel).filter(NotaModel.nota_id == filters['nota_id']).first()
        if not query:
            return None
        for field, value in filters.items():
            if value is not None:
                setattr(query, field, value)

        self.db.commit()
        return query


    def delete_nota(self, nota_id):
        nota = self.db.query(NotaModel).filter(NotaModel.nota_id == nota_id).first()
        if not nota:
            return None
        self.db.delete(nota)
        self.db.commit()
        return nota