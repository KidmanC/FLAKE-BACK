from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.periodolectivo import PeriodoLectivo
from config.database import Session
from services.periodolectivo import PeriodolectivoService


periodolectivo_router = APIRouter()

@periodolectivo_router.get('/periodolectivos/filter', tags=["Periodolectivos"])
def periodolectivo_filter(
    periodo_id: Optional[int] = None,
    anio: Optional[int] = None,
    esta_activo: Optional[str] = None,
):
    db = Session()
    filter = {
        "periodo_id": periodo_id,
        "anio": anio,
        "esta_activo": esta_activo,
    }

    periodoslectivos = PeriodolectivoService(db).get_periodolectivo(filter)
    if not periodoslectivos:
        return JSONResponse(content={"message": "Periodo(s) not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(periodoslectivos), status_code=200)

@periodolectivo_router.post('/periodolectivos', tags=["Periodolectivos"])
def create_periodolectivo(periodolectivo: PeriodoLectivo):
    db = Session()
    query = PeriodolectivoService(db).add_periodolectivo(periodolectivo)
    return JSONResponse(content={"message": "PeriodoLectivo created", "periodolectivo": jsonable_encoder(query)}, status_code=201)

@periodolectivo_router.put('/periodolectivos/edit', tags=["Periodolectivos"])
def update_periodolectivo(
    periodo_id: int = None,
    anio: Optional[int] = None,
    esta_activo: Optional[str] = None,
):
    db = Session()
    filter = {
        "periodo_id": periodo_id,
        "anio": anio,
        "esta_activo": esta_activo,
    }

    query = PeriodolectivoService(db).update_periodolectivo(filter)
    if query is None:
        return JSONResponse(content={"message": "Periodo not found"}, status_code=404)
    return JSONResponse(content={"message": "Periodo updated"}, status_code=200)


@periodolectivo_router.delete('/periodolectivos/{periodolectivo_id}', tags=["Periodolectivos"])
def delete_periodolectivo(periodolectivo_id: int):
    db = Session()
    query = PeriodolectivoService(db).delete_periodolectivo(periodolectivo_id)
    if query is None:
        return JSONResponse(content={"message": "PeriodoLectivo not found"}, status_code=404)
    return JSONResponse(content={"message": "PeriodoLectivo deleted", "periodolectivo": jsonable_encoder(query)}, status_code=200)