from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.clase import Clase
from config.database import Session
from config.database import get_db, Session
from services.clase import ClaseService

## diego se besó a mi abuelo
clase_router = APIRouter()

@clase_router.get('/clases', tags=["Clases"])
def get_clases():
    db = Session()
    clases = ClaseService(db).get_clases()
    if not clases:
        return JSONResponse(content={"message": "Clases not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(clases), status_code=200)

@clase_router.get('/clases/{clase_id}', tags=["Clases"])
def get_clase_by_id(clase_id: int):
    db = Session()
    clase = ClaseService(db).get_clase_by_id(clase_id)
    if clase is None:
        return JSONResponse(content={"message": "Clase not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(clase), status_code=200)

@clase_router.post('/clases', tags=["Clases"])
def create_clase(clase: Clase):
    db = Session()
    query = ClaseService(db).add_clase(clase)
    return JSONResponse(content={"message": "Clase created", "clase": jsonable_encoder(query)}, status_code=201)

@clase_router.put('/clases/{clase_id}', tags=["Clases"])
def update_clase(clase_id: int, clase: Clase):
    db = Session()
    query = ClaseService(db).update_clase(clase_id, clase)
    if query is None:
        return JSONResponse(content={"message": "Clase not found"}, status_code=404)
    return JSONResponse(content={"message": "Clase updated", "clase": jsonable_encoder(query)}, status_code=200)

@clase_router.delete('/clases/{clase_id}', tags=["Clases"])
def delete_clase(clase_id: int):
    db = Session()
    query = ClaseService(db).delete_clase(clase_id)
    if query is None:
        return JSONResponse(content={"message": "Clase not found"}, status_code=404)
    return JSONResponse(content={"message": "Clase deleted", "clase": jsonable_encoder(query)}, status_code=200)