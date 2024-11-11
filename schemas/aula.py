from pydantic import BaseModel
from schemas.grado import Grado
from schemas.jornada import Jornada


class Aula(BaseModel):
    #aula_id: int | None = None
    institucion_id: int | None = None
    periodo_id: int | None = None
    grado_texto: Grado | None = None
    grado_num: int | None = None
    grupo: str | None = None
    jornada: Jornada | None = None

    class Config:
        orm_mode = True