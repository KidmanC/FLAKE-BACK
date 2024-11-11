from pydantic import BaseModel
from schemas.grado import Grado
from schemas.tipo_identificacion import Tipo_identificacion
from schemas.genero import Genero
from datetime import date

class Estudiante(BaseModel):
    estudiante_id: int | None = None
    aula_id: int | None = None
    periodo_id: int | None = None
    grado_texto: Grado | None = None
    grado_num: int | None = None
    identificacion: str | None = None
    tipo_identificacion: Tipo_identificacion | None = None
    primer_nombre: str | None = None
    segundo_nombre: str | None = None
    primer_apellido: str | None = None
    segundo_apellido: str | None = None
    genero: Genero | None = None
    fecha_nacimiento: date | None = None
    estrato: int | None = None

    class Config:
        orm_mode = True