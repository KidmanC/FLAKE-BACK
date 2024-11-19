from typing import Optional, List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.aula import Aula
from config.database import Session
from config.database import get_db, Session
from schemas.grado import Grado
from schemas.jornada import Jornada
from services.aula import AulaService


aula_router = APIRouter()


@aula_router.get('/aulas/filter', tags=["Aulas"], response_model=List[Aula])
def aula_filter(
    aula_id: Optional[int] = None,
    institucion_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    grado_texto: Optional[Grado] = None, 
    grado_num: Optional[int] = None,
    grupo: Optional[str] = None,
    jornada: Optional[Jornada] = None
):
    db = Session()
    filter = {"aula_id": aula_id,
    "institucion_id": institucion_id,
    "periodo_id": periodo_id,
    "grado_texto": grado_texto,
    "grado_num": grado_num,
    "grupo": grupo,
    "jornada": jornada}
    aula = AulaService(db).get_aula(filter)
    if not aula:
        return JSONResponse(content={"message": "Aula no encontrada"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(aula), status_code=200)

@aula_router.post('/aulas', tags=["Aulas"])
def create_aula(aula: Aula):
    db = Session()
    query = AulaService(db).add_aula(aula)
    return JSONResponse(content={"message": "Aula creada exitosamente", "aula": jsonable_encoder(query)}, status_code=201)

@aula_router.put('/aulas/edit/{aula_id}', tags=["Aulas"])
def update_aula(aula_id: int,
    institucion_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    grado_texto: Optional[Grado] = None, 
    grado_num: Optional[int] = None,
    grupo: Optional[str] = None,
    jornada: Optional[Jornada] = None):
    db = Session()
    filter = {"aula_id": aula_id,
    "institucion_id": institucion_id,
    "periodo_id": periodo_id,
    "grado_texto": grado_texto,
    "grado_num": grado_num,
    "grupo": grupo,
    "jornada": jornada}
    query = AulaService(db).update_aula(filter)
    if query is None:
        return JSONResponse(content={"message": "Aula no encontrada"}, status_code=404)
    return JSONResponse(content={"message": "Aula actualizada exitosamente", "aula": jsonable_encoder(query)}, status_code=200)

@aula_router.delete('/aulas/{aula_id}', tags=["Aulas"])
def delete_aula(aula_id: int):
    db = Session()
    query = AulaService(db).delete_aula(aula_id)
    if query is None:
        return JSONResponse(content={"message": "Aula no encontrada"}, status_code=404)
    return JSONResponse(content={"message": "Aula eliminada exitosamente", "aula": jsonable_encoder(query)}, status_code=200)