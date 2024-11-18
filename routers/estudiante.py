from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.estudiante import Estudiante
from schemas.grado import Grado
from schemas.tipo_identificacion import Tipo_identificacion
from schemas.genero import Genero
from config.database import Session
from config.database import get_db, Session
from services.estudiante import EstudianteService
from datetime import date


estudiante_router = APIRouter()

@estudiante_router.get('/estudiantes/filter', tags=["Estudiantes"])
def Estudiantes_filter(
    estudiante_id: Optional[int] = None,
    aula_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    grado_texto: Optional[Grado] = None,
    grado_num: Optional[int] = None,
    identificacion: Optional[str] = None,
    tipo_identificacion: Optional[Tipo_identificacion] = None,
    primer_nombre: Optional[str] = None,
    segundo_nombre: Optional[str] = None,
    primer_apellido: Optional[str] = None,
    segundo_apellido: Optional[str] = None,
    genero: Optional[Genero] = None,
    fecha_nacimiento: Optional[date] = None,
    estrato: Optional[int] = None, 
    
):
    db = Session()
    filter = {
        "estudiante_id": estudiante_id,
        "aula_id": aula_id,
        "periodo_id": periodo_id,
        "grado_texto": grado_texto,
        "grado_num": grado_num,
        "identificacion": identificacion,
        "tipo_identificacion": tipo_identificacion,
        "primer_nombre": primer_nombre,
        "segundo_nombre": segundo_nombre,
        "primer_apellido": primer_apellido,
        "segundo_apellido": segundo_apellido,
        "genero": genero,
        "fecha_nacimiento": fecha_nacimiento,
        "estrato": estrato,
    }

    estudiantes = EstudianteService(db).get_estudiante(filter)
    if not estudiantes:
        return JSONResponse(content={"message": "Estudiante(s) not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(estudiantes), status_code=200)

@estudiante_router.post('/estudiantes', tags=["Estudiantes"])
def create_estudiante(estudiante: Estudiante):
    db = Session()
    query = EstudianteService(db).add_estudiante(estudiante)
    return JSONResponse(content={"message": "Estudiante created", "estudiante": jsonable_encoder(query)}, status_code=201)

@estudiante_router.get('/estudiantes/edit', tags=["Estudiantes"])
def update_estudiante(
    estudiante_id: int = None,
    aula_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    grado_texto: Optional[Grado] = None,
    grado_num: Optional[int] = None,
    identificacion: Optional[str] = None,
    tipo_identificacion: Optional[Tipo_identificacion] = None,
    primer_nombre: Optional[str] = None,
    segundo_nombre: Optional[str] = None,
    primer_apellido: Optional[str] = None,
    segundo_apellido: Optional[str] = None,
    genero: Optional[Genero] = None,
    fecha_nacimiento: Optional[date] = None,
    estrato: Optional[int] = None, 
    
):
    db = Session()
    filter = {
        "estudiante_id": estudiante_id,
        "aula_id": aula_id,
        "periodo_id": periodo_id,
        "grado_texto": grado_texto,
        "grado_num": grado_num,
        "identificacion": identificacion,
        "tipo_identificacion": tipo_identificacion,
        "primer_nombre": primer_nombre,
        "segundo_nombre": segundo_nombre,
        "primer_apellido": primer_apellido,
        "segundo_apellido": segundo_apellido,
        "genero": genero,
        "fecha_nacimiento": fecha_nacimiento,
        "estrato": estrato
    }

    query = EstudianteService(db).update_estudiante(filter)
    if query is None:
        return JSONResponse(content={"message": "Estudiante not found"}, status_code=404)
    return JSONResponse(content={"message": "Estudiante updated"}, status_code=200)


@estudiante_router.delete('/estudiantes/{estudiante_id}', tags=["Estudiantes"])
def delete_estudiante(estudiante_id: int):
    db = Session()
    query = EstudianteService(db).delete_estudiante(estudiante_id)
    if query is None:
        return JSONResponse(content={"message": "Estudiante not found"}, status_code=404)
    return JSONResponse(content={"message": "Estudiante deleted", "estudiante": jsonable_encoder(query)}, status_code=200)

@estudiante_router.get('/estudiantes/{estudiante_id}/periodo/{periodo_id}', tags=["Estudiantes"])
def get_nota_final(estudiante_id: int, periodo_id: int):
    db = Session()
    notas = EstudianteService(db).get_nota_final(estudiante_id, periodo_id)
    if not notas:
        return JSONResponse(content={"message": "Notas not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(notas), status_code=200)