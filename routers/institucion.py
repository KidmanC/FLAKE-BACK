from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.institucion import Institucion
from config.database import Session
from config.database import get_db, Session
from services.institucion import InstitucionService


institucion_router = APIRouter()

@institucion_router.get('/institucions', tags=["Institucions"])
def get_institucions():
    db = Session()
    institucions = InstitucionService(db).get_institucions()
    if not institucions:
        return JSONResponse(content={"message": "Institucions not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(institucions), status_code=200)

@institucion_router.get('/institucions/{institucion_id}', tags=["Institucions"])
def get_institucion_by_id(institucion_id: int):
    db = Session()
    institucion = InstitucionService(db).get_institucion_by_id(institucion_id)
    if institucion is None:
        return JSONResponse(content={"message": "Institucion not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(institucion), status_code=200)

@institucion_router.post('/institucions', tags=["Institucions"])
def create_institucion(institucion: Institucion):
    db = Session()
    query = InstitucionService(db).add_institucion(institucion)
    return JSONResponse(content={"message": "Institucion created", "institucion": jsonable_encoder(query)}, status_code=201)

@institucion_router.put('/institucions/{institucion_id}', tags=["Institucions"])
def update_institucion(institucion_id: int, institucion: Institucion):
    db = Session()
    query = InstitucionService(db).update_institucion(institucion_id, institucion)
    if query is None:
        return JSONResponse(content={"message": "Institucion not found"}, status_code=404)
    return JSONResponse(content={"message": "Institucion updated", "institucion": jsonable_encoder(query)}, status_code=200)

@institucion_router.delete('/institucions/{institucion_id}', tags=["Institucions"])
def delete_institucion(institucion_id: int):
    db = Session()
    query = InstitucionService(db).delete_institucion(institucion_id)
    if query is None:
        return JSONResponse(content={"message": "Institucion not found"}, status_code=404)
    return JSONResponse(content={"message": "Institucion deleted", "institucion": jsonable_encoder(query)}, status_code=200)