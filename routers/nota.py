from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.nota import Nota
from config.database import Session
from config.database import get_db, Session
from services.nota import NotaService


nota_router = APIRouter()

@nota_router.get('/notas', tags=["Notas"])
def get_notas():
    db = Session()
    notas = NotaService(db).get_notas()
    if not notas:
        return JSONResponse(content={"message": "Notas not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(notas), status_code=200)

@nota_router.get('/notas/{nota_id}', tags=["Notas"])
def get_nota_by_id(nota_id: int):
    db = Session()
    nota = NotaService(db).get_nota_by_id(nota_id)
    if nota is None:
        return JSONResponse(content={"message": "Nota not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(nota), status_code=200)

@nota_router.post('/notas', tags=["Notas"])
def create_nota(nota: Nota):
    db = Session()
    query = NotaService(db).add_nota(nota)
    return JSONResponse(content={"message": "Nota created", "nota": jsonable_encoder(query)}, status_code=201)

@nota_router.put('/notas/{nota_id}', tags=["Notas"])
def update_nota(nota_id: int, nota: Nota):
    db = Session()
    query = NotaService(db).update_nota(nota_id, nota)
    if query is None:
        return JSONResponse(content={"message": "Nota not found"}, status_code=404)
    return JSONResponse(content={"message": "Nota updated", "nota": jsonable_encoder(query)}, status_code=200)

@nota_router.delete('/notas/{nota_id}', tags=["Notas"])
def delete_nota(nota_id: int):
    db = Session()
    query = NotaService(db).delete_nota(nota_id)
    if query is None:
        return JSONResponse(content={"message": "Nota not found"}, status_code=404)
    return JSONResponse(content={"message": "Nota deleted", "nota": jsonable_encoder(query)}, status_code=200)