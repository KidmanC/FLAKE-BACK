from pydantic import BaseModel
from schemas.dia_semana import Dia_semana
from datetime import time

class Horario(BaseModel):
    horario_id: int | None = None
    clase_id: int | None = None
    dia_semana: Dia_semana | None = None
    hora_inicio: time | None = None
    hora_fin: time | None = None

    class Config:
        orm_mode = True