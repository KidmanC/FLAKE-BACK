from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.clase import Clase
from config.database import Session
from config.database import get_db, Session
from schemas.grado import Grado
from services.clase import ClaseService

clase_router = APIRouter()

@clase_router.get('/clases/filter', tags=["Clases"])
def clase_filter(
    clase_id: Optional[int] = None,
    aula_id: Optional[int] = None,
    tutor_id: Optional[int] = None,
    periodo_id: Optional[int] = None, 
    grado: Optional[Grado] = None,
):
    db = Session()
    filter = {"clase_id": clase_id,
    "aula_id": aula_id,
    "tutor_id": tutor_id,
    "periodo_id": periodo_id,
    "grado": grado}
    clase = ClaseService(db).get_clase(filter)
    if not clase:
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
