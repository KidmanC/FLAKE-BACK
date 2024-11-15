from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.tipo_identificacion import Tipo_identificacion
from schemas.tutor import Tutor
from config.database import Session
from config.database import get_db, Session
from services.tutor import TutorService


tutor_router = APIRouter()

@tutor_router.get('/tutores/filter', tags=["Tutores"])
def clase_filter(
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
    clase = TutorService(db).get_tutor(filter)
    if not clase:
        return JSONResponse(content={"message": "Clase not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(clase), status_code=200)

@tutor_router.post('/tutors', tags=["Tutors"])
def create_tutor(tutor: Tutor):
    db = Session()
    query = TutorService(db).add_tutor(tutor)
    return JSONResponse(content={"message": "Tutor created", "tutor": jsonable_encoder(query)}, status_code=201)

@tutor_router.put('/tutors/{tutor_id}', tags=["Tutors"])
def update_tutor(tutor_id: int, tutor: Tutor):
    db = Session()
    query = TutorService(db).update_tutor(tutor_id, tutor)
    if query is None:
        return JSONResponse(content={"message": "Tutor not found"}, status_code=404)
    return JSONResponse(content={"message": "Tutor updated", "tutor": jsonable_encoder(query)}, status_code=200)

@tutor_router.delete('/tutors/{tutor_id}', tags=["Tutors"])
def delete_tutor(tutor_id: int):
    db = Session()
    query = TutorService(db).delete_tutor(tutor_id)
    if query is None:
        return JSONResponse(content={"message": "Tutor not found"}, status_code=404)
    return JSONResponse(content={"message": "Tutor deleted", "tutor": jsonable_encoder(query)}, status_code=200)