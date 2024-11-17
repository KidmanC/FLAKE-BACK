from models.periodolectivo import Periodo_lectivo as PeriodolectivoModel
from schemas.periodolectivo import PeriodoLectivo

class PeriodolectivoService:
    def __init__(self, db):
        self.db = db

    def get_periodolectivo(self, filters:dict):
        query = self.db.query(PeriodolectivoModel) 

        if not any(value is not None for value in filters.values()):
            return query.all()
        
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(PeriodolectivoModel, field) == value)
        return query.all()
    
    def add_periodolectivo(self, periodolectivo: PeriodoLectivo):
        new_periodolectivo = PeriodolectivoModel(**periodolectivo.model_dump())
        self.db.add(new_periodolectivo)
        self.db.commit()
        return new_periodolectivo

    def update_periodolectivo(self, periodo_id, periodolectivo: PeriodoLectivo):
        query = self.db.query(PeriodolectivoModel).filter(PeriodolectivoModel.periodo_id == periodo_id).first()
        if not query:
            return None
        query.anio = periodolectivo.anio
        query.bloques = periodolectivo.bloques
        query.semanas = periodolectivo.semanas
        self.db.commit()
        return query

    def delete_periodolectivo(self, periodo_id):
        periodolectivo = self.db.query(PeriodolectivoModel).filter(PeriodolectivoModel.periodo_id == periodo_id).first()
        if not periodolectivo:
            return None
        self.db.delete(periodolectivo)
        self.db.commit()
        return periodolectivo