from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.aula import Aula
from config.database import Session
from config.database import get_db, Session
from services.aula import AulaService


aula_router = APIRouter()

@aula_router.get('/aulas', tags=["Aulas"])
def get_aulas():
    db = Session()
    aulas = AulaService(db).get_aulas()
    if not aulas:
        return JSONResponse(content={"message": "Aulas not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(aulas), status_code=200)

@aula_router.get('/aulas/{aula_id}', tags=["Aulas"])
def get_aula_by_id(aula_id: int):
    db = Session()
    aula = AulaService(db).get_aula_by_id(aula_id)
    if aula is None:
        return JSONResponse(content={"message": "Aula not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(aula), status_code=200)

@aula_router.post('/aulas', tags=["Aulas"])
def create_aula(aula: Aula):
    db = Session()
    query = AulaService(db).add_aula(aula)
    return JSONResponse(content={"message": "Aula created", "aula": jsonable_encoder(query)}, status_code=201)

@aula_router.put('/aulas/{aula_id}', tags=["Aulas"])
def update_aula(aula_id: int, aula: Aula):
    db = Session()
    query = AulaService(db).update_aula(aula_id, aula)
    if query is None:
        return JSONResponse(content={"message": "Aula not found"}, status_code=404)
    return JSONResponse(content={"message": "Aula updated", "aula": jsonable_encoder(query)}, status_code=200)

@aula_router.delete('/aulas/{aula_id}', tags=["Aulas"])
def delete_aula(aula_id: int):
    db = Session()
    query = AulaService(db).delete_aula(aula_id)
    if query is None:
        return JSONResponse(content={"message": "Aula not found"}, status_code=404)
    return JSONResponse(content={"message": "Aula deleted", "aula": jsonable_encoder(query)}, status_code=200)