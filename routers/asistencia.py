from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.asistencia import Asistencia
from config.database import Session
from config.database import get_db, Session
from services.asistencia import AsistenciaService


asistencia_router = APIRouter()

@asistencia_router.get('/asistencias', tags=["Asistencias"])
def get_asistencias():
    db = Session()
    asistencias = AsistenciaService(db).get_asistencias()
    if not asistencias:
        return JSONResponse(content={"message": "Asistencias not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(asistencias), status_code=200)

@asistencia_router.get('/asistencias/{asistencia_id}', tags=["Asistencias"])
def get_asistencia_by_id(asistencia_id: int):
    db = Session()
    asistencia = AsistenciaService(db).get_asistencia_by_id(asistencia_id)
    if asistencia is None:
        return JSONResponse(content={"message": "Asistencia not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(asistencia), status_code=200)

@asistencia_router.post('/asistencias', tags=["Asistencias"])
def create_asistencia(asistencia: Asistencia):
    db = Session()
    query = AsistenciaService(db).add_asistencia(asistencia)
    return JSONResponse(content={"message": "Asistencia created", "asistencia": jsonable_encoder(query)}, status_code=201)

@asistencia_router.put('/asistencias/{asistencia_id}', tags=["Asistencias"])
def update_asistencia(asistencia_id: int, asistencia: Asistencia):
    db = Session()
    query = AsistenciaService(db).update_asistencia(asistencia_id, asistencia)
    if query is None:
        return JSONResponse(content={"message": "Asistencia not found"}, status_code=404)
    return JSONResponse(content={"message": "Asistencia updated", "asistencia": jsonable_encoder(query)}, status_code=200)

@asistencia_router.delete('/asistencias/{asistencia_id}', tags=["Asistencias"])
def delete_asistencia(asistencia_id: int):
    db = Session()
    query = AsistenciaService(db).delete_asistencia(asistencia_id)
    if query is None:
        return JSONResponse(content={"message": "Asistencia not found"}, status_code=404)
    return JSONResponse(content={"message": "Asistencia deleted", "asistencia": jsonable_encoder(query)}, status_code=200)