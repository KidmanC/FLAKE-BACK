from pydantic import BaseModel

class PeriodoLectivo(BaseModel):
    periodo_id: int | None = None
    anio: int | None = None
    bloques: int | None = None
    semanas: int | None = None

    class Config:
        orm_mode = True