from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.nota import Nota
from config.database import Session
from config.database import get_db, Session
from services.nota import NotaService

nota_router = APIRouter()

@nota_router.get('/notas/filter', tags=["Notas"])
def notas_filter(
    nota_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    estudiante_id: Optional[int] = None,
    clase_id: Optional[int] = None,
    bloque: Optional[int] = None,
    calificacion: Optional[str] = None,
):
    db = Session()
    filter = {
        "nota_id": nota_id,
        "periodo_id": periodo_id,
        "estudiante_id": estudiante_id,
        "clase_id": clase_id,
        "bloque": bloque,
        "calificacion": calificacion,
    }

    notas = NotaService(db).get_nota(filter)
    if not notas:
        return JSONResponse(content={"message": "Nota(s) not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(notas), status_code=200)

@nota_router.post('/notas', tags=["Notas"])
def create_nota(nota: Nota):
    db = Session()
    query = NotaService(db).add_nota(nota)
    return JSONResponse(content={"message": "Nota created", "nota": jsonable_encoder(query)}, status_code=201)

@nota_router.put('/notas/edit', tags=["Notas"])
def update_nota(
    nota_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    estudiante_id: Optional[int] = None,
    clase_id: Optional[int] = None,
    bloque: Optional[int] = None,
    calificacion: Optional[str] = None,
):
    db = Session()
    filter = {
        "nota_id": nota_id,
        "periodo_id": periodo_id,
        "estudiante_id": estudiante_id,
        "clase_id": clase_id,
        "bloque": bloque,
        "calificacion": calificacion,
    }

    query = NotaService(db).update_nota(filter)
    if query is None:
        return JSONResponse(content={"message": "Nota not found"}, status_code=404)
    return JSONResponse(content={"message": "Nota updated"}, status_code=200)




@nota_router.delete('/notas/{nota_id}', tags=["Notas"])
def delete_nota(nota_id: int):
    db = Session()
    query = NotaService(db).delete_nota(nota_id)
    if query is None:
        return JSONResponse(content={"message": "Nota not found"}, status_code=404)
    return JSONResponse(content={"message": "Nota deleted", "nota": jsonable_encoder(query)}, status_code=200)