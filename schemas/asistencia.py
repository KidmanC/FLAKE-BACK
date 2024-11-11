from pydantic import BaseModel
from datetime import date
from schemas.presente import Presente


class Asistencia(BaseModel):
    asistencia_id: int | None = None
    clase_id: int | None = None
    estudiante_id: int | None = None
    fecha: date | None = None  
    presente: Presente | None = None  

    class Config:
        orm_mode = True
