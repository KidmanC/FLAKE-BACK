from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.clases_no_dadas import Clases_no_dadas
from config.database import Session
from config.database import get_db, Session
from services.clases_no_dadas import Clases_no_dadas_Service


clases_no_dadas_router = APIRouter()

@clases_no_dadas_router.get('/clases_no_dadass', tags=["Clases_no_dadass"])
def get_clases_no_dadass():
    db = Session()
    clases_no_dadass = Clases_no_dadas_Service(db).get_clases_no_dadass()
    if not clases_no_dadass:
        return JSONResponse(content={"message": "Clases_no_dadass not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(clases_no_dadass), status_code=200)

@clases_no_dadas_router.get('/clases_no_dadass/{clase_no_dada_id}', tags=["Clases_no_dadass"])
def get_clases_no_dadas_by_id(clase_no_dada_id: int):
    db = Session()
    clases_no_dadas = Clases_no_dadas_Service(db).get_clases_no_dadas_by_id(clase_no_dada_id)
    if clases_no_dadas is None:
        return JSONResponse(content={"message": "Clases_no_dadas not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(clases_no_dadas), status_code=200)

@clases_no_dadas_router.post('/clases_no_dadass', tags=["Clases_no_dadass"])
def create_clases_no_dadas(clases_no_dadas: Clases_no_dadas):
    db = Session()
    query = Clases_no_dadas_Service(db).add_clases_no_dadas(clases_no_dadas)
    return JSONResponse(content={"message": "Clases_no_dadas created", "clases_no_dadas": jsonable_encoder(query)}, status_code=201)

@clases_no_dadas_router.put('/clases_no_dadass/{clase_no_dada_id}', tags=["Clases_no_dadass"])
def update_clases_no_dadas(clase_no_dada_id: int, clases_no_dadas: Clases_no_dadas):
    db = Session()
    query = Clases_no_dadas_Service(db).update_clases_no_dadas(clase_no_dada_id, clases_no_dadas)
    if query is None:
        return JSONResponse(content={"message": "Clases_no_dadas not found"}, status_code=404)
    return JSONResponse(content={"message": "Clases_no_dadas updated", "clases_no_dadas": jsonable_encoder(query)}, status_code=200)

@clases_no_dadas_router.delete('/clases_no_dadass/{clase_no_dada_id}', tags=["Clases_no_dadass"])
def delete_clases_no_dadas(clase_no_dada_id: int):
    db = Session()
    query = Clases_no_dadas_Service(db).delete_clases_no_dadas(clase_no_dada_id)
    if query is None:
        return JSONResponse(content={"message": "Clases_no_dadas not found"}, status_code=404)
    return JSONResponse(content={"message": "Clases_no_dadas deleted", "clases_no_dadas": jsonable_encoder(query)}, status_code=200)