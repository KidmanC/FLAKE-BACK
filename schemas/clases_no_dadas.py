from pydantic import BaseModel
from schemas.motivo import Motivo
from datetime import date

class Clases_no_dadas(BaseModel):
    clase_no_dada_id: int | None = None
    clase_id: int | None = None
    fecha_clase_no_dada: date | None = None
    motivo: Motivo | None = None

    class Config:
        orm_mode = True