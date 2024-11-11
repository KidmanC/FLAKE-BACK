from pydantic import BaseModel


class Nota(BaseModel):
    nota_id: int | None = None
    periodo_id: int | None = None
    estudiante_id: int | None = None
    clase_id: int | None = None
    bloque: int | None = None
    calificacion: float | None = None

    class Config:
        orm_mode = True