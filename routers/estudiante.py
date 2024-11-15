from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.estudiante import Estudiante
from config.database import Session
from config.database import get_db, Session
from services.estudiante import EstudianteService


estudiante_router = APIRouter()

@estudiante_router.get('/estudiantes', tags=["Estudiantes"])
def get_estudiantes():
    db = Session()
    estudiantes = EstudianteService(db).get_estudiantes()
    if not estudiantes:
        return JSONResponse(content={"message": "Estudiantes not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(estudiantes), status_code=200)

@estudiante_router.get('/estudiantes/{estudiante_id}', tags=["Estudiantes"])
def get_estudiante_by_id(estudiante_id: int):
    db = Session()
    estudiante = EstudianteService(db).get_estudiante_by_id(estudiante_id)
    if estudiante is None:
        return JSONResponse(content={"message": "Estudiante not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(estudiante), status_code=200)

@estudiante_router.post('/estudiantes', tags=["Estudiantes"])
def create_estudiante(estudiante: Estudiante):
    db = Session()
    query = EstudianteService(db).add_estudiante(estudiante)
    return JSONResponse(content={"message": "Estudiante created", "estudiante": jsonable_encoder(query)}, status_code=201)

@estudiante_router.put('/estudiantes/{estudiante_id}', tags=["Estudiantes"])
def update_estudiante(estudiante_id: int, estudiante: Estudiante):
    db = Session()
    query = EstudianteService(db).update_estudiante(estudiante_id, estudiante)
    if query is None:
        return JSONResponse(content={"message": "Estudiante not found"}, status_code=404)
    return JSONResponse(content={"message": "Estudiante updated", "estudiante": jsonable_encoder(query)}, status_code=200)

@estudiante_router.delete('/estudiantes/{estudiante_id}', tags=["Estudiantes"])
def delete_estudiante(estudiante_id: int):
    db = Session()
    query = EstudianteService(db).delete_estudiante(estudiante_id)
    if query is None:
        return JSONResponse(content={"message": "Estudiante not found"}, status_code=404)
    return JSONResponse(content={"message": "Estudiante deleted", "estudiante": jsonable_encoder(query)}, status_code=200)

@estudiante_router.get('/estudiantes/{estudiante_id}/notas', tags=["Estudiantes"])
def get_notas(estudiante_id: int):
    db = Session()
    notas = EstudianteService(db).get_notas(estudiante_id)
    if not notas:
        return JSONResponse(content={"message": "Notas not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(notas), status_code=200)