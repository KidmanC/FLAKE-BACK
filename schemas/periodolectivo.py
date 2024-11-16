from pydantic import BaseModel

class PeriodoLectivo(BaseModel):
    #periodo_id: int | None = None
    anio: int | None = None
    esta_activo: int | None = None

    class Config:
        orm_mode = True