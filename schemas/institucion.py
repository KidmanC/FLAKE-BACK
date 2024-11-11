from pydantic import BaseModel

class Institucion(BaseModel):
    #institucion_id: int | None = None
    numero : str | None = None
    localidad : str | None = None
    codigo_dane : str | None = None
    nombre : str | None = None
    rector : str | None = None
    direccion : str | None = None
    barrio : str | None = None

    class Config:
        orm_mode = True