from pydantic import BaseModel
from schemas.grado import Grado


class Clase(BaseModel):
    #clase_id: int | None = None
    aula_id: int | None = None
    tutor_id: int | None = None
    periodo_id: int | None = None
    grado: Grado | None = None

    class Config:
        orm_mode = True