from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.periodolectivo import PeriodoLectivo
from config.database import Session
from config.database import get_db, Session
from services.periodolectivo import PeriodolectivoService


periodolectivo_router = APIRouter()

@periodolectivo_router.get('/periodolectivos', tags=["Periodolectivos"])
def get_periodolectivos():
    db = Session()
    periodolectivos = PeriodolectivoService(db).get_periodolectivos()
    if not periodolectivos:
        return JSONResponse(content={"message": "Periodolectivos not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(periodolectivos), status_code=200)

@periodolectivo_router.get('/periodolectivos/{periodolectivo_id}', tags=["Periodolectivos"])
def get_periodolectivo_by_id(periodolectivo_id: int):
    db = Session()
    periodolectivo = PeriodolectivoService(db).get_periodolectivo_by_id(periodolectivo_id)
    if periodolectivo is None:
        return JSONResponse(content={"message": "PeriodoLectivo not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(periodolectivo), status_code=200)

@periodolectivo_router.post('/periodolectivos', tags=["Periodolectivos"])
def create_periodolectivo(periodolectivo: PeriodoLectivo):
    db = Session()
    query = PeriodolectivoService(db).add_periodolectivo(periodolectivo)
    return JSONResponse(content={"message": "PeriodoLectivo created", "periodolectivo": jsonable_encoder(query)}, status_code=201)

@periodolectivo_router.put('/periodolectivos/{periodolectivo_id}', tags=["Periodolectivos"])
def update_periodolectivo(periodolectivo_id: int, periodolectivo: PeriodoLectivo):
    db = Session()
    query = PeriodolectivoService(db).update_periodolectivo(periodolectivo_id, periodolectivo)
    if query is None:
        return JSONResponse(content={"message": "PeriodoLectivo not found"}, status_code=404)
    return JSONResponse(content={"message": "PeriodoLectivo updated", "periodolectivo": jsonable_encoder(query)}, status_code=200)

@periodolectivo_router.delete('/periodolectivos/{periodolectivo_id}', tags=["Periodolectivos"])
def delete_periodolectivo(periodolectivo_id: int):
    db = Session()
    query = PeriodolectivoService(db).delete_periodolectivo(periodolectivo_id)
    if query is None:
        return JSONResponse(content={"message": "PeriodoLectivo not found"}, status_code=404)
    return JSONResponse(content={"message": "PeriodoLectivo deleted", "periodolectivo": jsonable_encoder(query)}, status_code=200)