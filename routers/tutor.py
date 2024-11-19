from typing import Optional, List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.tipo_identificacion import Tipo_identificacion
from schemas.tutor import Tutor
from config.database import Session
from config.database import get_db, Session
from services.tutor import TutorService


tutor_router = APIRouter()

@tutor_router.get('/tutores/filter', tags=["Tutores"], response_model=List[Tutor])
def tutor_filter(
    tutor_id: Optional[int] = None,
    identificacion: Optional[str] = None,
    tipo_identificacion: Optional[Tipo_identificacion] = None,
    primer_nombre: Optional[str] = None,
    segundo_nombre: Optional[str] = None,
    primer_apellido: Optional[str] = None,
    segundo_apellido: Optional[str] = None,
    correo: Optional[str] = None,
    celular: Optional[str] = None,
    direccion: Optional[str] = None,
    periodo_id: Optional[int] = None,
):
    db = Session()
    filter = {"tutor_id": tutor_id,
    "identificacion": identificacion,
    "tipo_identificacion": tipo_identificacion,
    "primer_nombre": primer_nombre,
    "segundo_nombre": segundo_nombre,
    "primer_apellido": primer_apellido,
    "segundo_apellido": segundo_apellido,
    "correo": correo,
    "celular": celular,
    "direccion": direccion,
    "periodo_id": periodo_id}
    tutor = TutorService(db).get_tutor(filter)
    if not tutor:
        return JSONResponse(content={"message": "Tutor no encontrado"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(tutor), status_code=200)

@tutor_router.post('/tutores', tags=["Tutores"])
def create_tutor(tutor: Tutor):
    db = Session()
    query = TutorService(db).add_tutor(tutor)
    return JSONResponse(content={"message": "Tutor creado correctamente", "tutor": jsonable_encoder(query)}, status_code=201)

@tutor_router.put('/tutores/edit/{tutor_id}', tags=["Tutores"])
def update_tutor(tutor_id: int,
    identificacion: Optional[str] = None,
    tipo_identificacion: Optional[Tipo_identificacion] = None,
    primer_nombre: Optional[str] = None,
    segundo_nombre: Optional[str] = None,
    primer_apellido: Optional[str] = None,
    segundo_apellido: Optional[str] = None,
    correo: Optional[str] = None,
    celular: Optional[str] = None,
    direccion: Optional[str] = None,
    periodo_id: Optional[int] = None,
    user: Optional[str] = None,
    password: Optional[str] = None):
    db = Session()
    filter = {"tutor_id": tutor_id,
    "identificacion": identificacion,
    "tipo_identificacion": tipo_identificacion,
    "primer_nombre": primer_nombre,
    "segundo_nombre": segundo_nombre,
    "primer_apellido": primer_apellido,
    "segundo_apellido": segundo_apellido,
    "correo": correo,
    "celular": celular,
    "direccion": direccion,
    "periodo_id": periodo_id,
    "user": user,
    "password": password}
    query = TutorService(db).update_tutor(filter)
    if query is None:
        return JSONResponse(content={"message": "Tutor no encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Tutor actualizado correctamente", "tutor": jsonable_encoder(query)}, status_code=200)

@tutor_router.delete('/tutores/{tutor_id}', tags=["Tutores"])
def delete_tutor(tutor_id: int):
    db = Session()
    query = TutorService(db).delete_tutor(tutor_id)
    if query is None:
        return JSONResponse(content={"message": "Tutor no encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Tutor eliminado correctamente", "tutor": jsonable_encoder(query)}, status_code=200)