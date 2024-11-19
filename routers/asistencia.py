from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.asistencia import Asistencia
from schemas.presente import Presente
from config.database import Session
from config.database import get_db, Session
from services.asistencia import AsistenciaService
from datetime import date
from typing import Optional, List

asistencia_router = APIRouter()

@asistencia_router.get('/asistencias/filter', tags=["Asistencias"], response_model=List[Asistencia])
def asistencia_filter(
    asistencia_id: int,
    clase_id: Optional[int] = None,
    estudiante_id: Optional[int] = None,
    fecha: Optional[date] = None,
    presente: Optional[Presente] = None
):
    db = Session()
    filter = {
        "asistencia_id": asistencia_id,
        "clase_id": clase_id,
        "estudiante_id": estudiante_id,
        "fecha": fecha,
        "presente": presente
    }
    asistencias = AsistenciaService(db).get_asistencia(filter)
    if not asistencias:
        return JSONResponse(content={"message": "Asistencias not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(asistencias), status_code=200)

@asistencia_router.post('/asistencias', tags=["Asistencias"])
def create_asistencia(asistencia: Asistencia):
    db = Session()
    query = AsistenciaService(db).add_asistencia(asistencia)
    return JSONResponse(content={"message": "Asistencia created", "asistencia": jsonable_encoder(query)}, status_code=201)

@asistencia_router.put('/asistencias/edit/{asistencia_id}', tags=["Asistencias"])
def update_asistencia(
    asistencia_id: Optional[int] = None,
    clase_id: Optional[int] = None,
    estudiante_id: Optional[int] = None,
    fecha: Optional[date] = None,
    presente: Optional[Presente] = None
):
    db = Session()
    filter = {
        "asistencia_id": asistencia_id,
        "clase_id": clase_id,
        "estudiante_id": estudiante_id,
        "fecha": fecha,
        "presente": presente
    }
    query = AsistenciaService(db).update_asistencia(filter)
    if query is None:
        return JSONResponse(content={"message": "Asistencia not found"}, status_code=404)
    return JSONResponse(content={"message": "Asistencia updated"}, status_code=200)

@asistencia_router.delete('/asistencias/{asistencia_id}', tags=["Asistencias"])
def delete_asistencia(asistencia_id: int):
    db = Session()
    query = AsistenciaService(db).delete_asistencia(asistencia_id)
    if query is None:
        return JSONResponse(content={"message": "Asistencia not found"}, status_code=404)
    return JSONResponse(content={"message": "Asistencia deleted", "asistencia": jsonable_encoder(query)}, status_code=200)