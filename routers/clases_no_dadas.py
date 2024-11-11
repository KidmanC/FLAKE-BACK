from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.clases_no_dadas import Clases_no_dadas
from config.database import Session
from config.database import get_db, Session
from services.clases_no_dadas import Clases_no_dadas_Service


clases_no_dadas_router = APIRouter()

@clases_no_dadas_router.get('/clases_no_dadas', tags=["Clases_no_dadas"])
def get_clases_no_dadas():
    db = Session()
    clases_no_dadass = Clases_no_dadas_Service(db).get_clases_no_dadas()
    if not clases_no_dadass:
        return JSONResponse(content={"message": "Clases_no_dadas not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(clases_no_dadass), status_code=200)

@clases_no_dadas_router.get('/clases_no_dadas/{clase_no_dada_id}', tags=["Clases_no_dadas"])
def get_clases_no_dadas_by_id(clase_no_dada_id: int):
    db = Session()
    clase_no_dada = Clases_no_dadas_Service(db).get_clase_no_dada_by_id(clase_no_dada_id)
    if clase_no_dada is None:
        return JSONResponse(content={"message": "Clase_no_dada not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(clase_no_dada), status_code=200)

@clases_no_dadas_router.post('/clases_no_dadas', tags=["Clases_no_dadas"])
def create_clase_no_dada(clase_no_dada: Clases_no_dadas):
    db = Session()
    query = Clases_no_dadas_Service(db).add_clase_no_dada(clase_no_dada)
    return JSONResponse(content={"message": "Clase_no_dada created", "clase_no_dada": jsonable_encoder(query)}, status_code=201)

@clases_no_dadas_router.put('/clases_no_dadas/{clase_no_dada_id}', tags=["Clases_no_dadas"])
def update_clases_no_dadas(clase_no_dada_id: int, clase_no_dada: Clases_no_dadas):
    db = Session()
    query = Clases_no_dadas_Service(db).update_clases_no_dadas(clase_no_dada_id, clase_no_dada)
    if query is None:
        return JSONResponse(content={"message": "Clases_no_dadas not found"}, status_code=404)
    return JSONResponse(content={"message": "Clases_no_dadas updated", "clase_no_dada": jsonable_encoder(query)}, status_code=200)

@clases_no_dadas_router.delete('/clases_no_dadas/{clases_no_dadas_id}', tags=["Clases_no_dadas"])
def delete_clase_no_dada(clase_no_dada_id: int):
    db = Session()
    query = Clases_no_dadas_Service(db).delete_clase_no_dada(clase_no_dada_id)
    if query is None:
        return JSONResponse(content={"message": "Clase_no_dada not found"}, status_code=404)
    return JSONResponse(content={"message": "Clase_no_dada deleted", "clase_no_dada": jsonable_encoder(query)}, status_code=200)