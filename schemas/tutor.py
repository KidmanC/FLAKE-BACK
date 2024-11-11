from pydantic import BaseModel
from schemas.tipo_identificacion import Tipo_identificacion

class Tutor(BaseModel):
    tutor_id: int | None = None
    identificacion: str | None = None
    tipo_identificacion: Tipo_identificacion | None = None
    primer_nombre: str | None = None
    segundo_nombre: str | None = None
    primer_apellido: str | None = None
    segundo_apellido: str | None = None
    correo: str | None = None
    celular: str | None = None
    direccion: str | None = None
    periodo_id: int | None = None
    user: str | None = None
    password: str | None = None

    class Config:
        orm_mode = True