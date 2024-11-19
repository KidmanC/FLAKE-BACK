from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.institucion import Institucion
from config.database import Session
from config.database import get_db, Session
from services.institucion import InstitucionService
from typing import Optional, List


institucion_router = APIRouter()

@institucion_router.get('/instituciones/filter', tags=["Instituciones"], response_model=List[Institucion])
def institucion_filter(
    institucion_id: Optional[int] = None,
    numero: Optional[str] = None,
    localidad: Optional[str] = None,
    codigo_dane: Optional[str] = None,
    nombre: Optional[str] = None,
    rector: Optional[str] = None,
    direccion: Optional[str] = None,
    barrio: Optional[str] = None
):
    db = Session()
    filter = {
        "institucion_id": institucion_id,
        "numero": numero,
        "localidad": localidad,
        "codigo_dane": codigo_dane,
        "nombre": nombre,
        "rector": rector,
        "direccion": direccion,
        "barrio": barrio
    }
    institucions = InstitucionService(db).get_institucion(filter)
    if not institucions:
        return JSONResponse(content={"message": "Institucion no encontrada"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(institucions), status_code=200)

@institucion_router.post('/instituciones', tags=["Instituciones"])
def create_institucion(institucion: Institucion):
    db = Session()
    query = InstitucionService(db).add_institucion(institucion)
    return JSONResponse(content={"message": "Institucion creada exitosamente", "institucion": jsonable_encoder(query)}, status_code=201)

@institucion_router.put('/instituciones/edit/{institucion_id}', tags=["Instituciones"])
def update_institucion(
    institucion_id: int,
    numero: Optional[str] = None,
    localidad: Optional[str] = None,
    codigo_dane: Optional[str] = None,
    nombre: Optional[str] = None,
    rector: Optional[str] = None,
    direccion: Optional[str] = None,
    barrio: Optional[str] = None):
    db = Session()
    filter = {
        "institucion_id": institucion_id,
        "numero": numero,
        "localidad": localidad,
        "codigo_dane": codigo_dane,
        "nombre": nombre,
        "rector": rector,
        "direccion": direccion,
        "barrio": barrio
    }
    query = InstitucionService(db).update_institucion(filter)
    if query is None:
        return JSONResponse(content={"message": "Institucion no encontrada"}, status_code=404)
    return JSONResponse(content={"message": "Institucion actualizada exitosamente"}, status_code=200)

@institucion_router.delete('/instituciones/{institucion_id}', tags=["Instituciones"])
def delete_institucion(institucion_id: int):
    db = Session()
    query = InstitucionService(db).delete_institucion(institucion_id)
    if query is None:
        return JSONResponse(content={"message": "Institucion no encontrada"}, status_code=404)
    return JSONResponse(content={"message": "Institucion eliminada exitosamente", "institucion": jsonable_encoder(query)}, status_code=200)