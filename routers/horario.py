from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.horario import Horario
from config.database import Session
from config.database import get_db, Session
from services.horario import HorarioService


horario_router = APIRouter()

@horario_router.get('/horarios', tags=["Horarios"])
def get_horarios():
    db = Session()
    horarios = HorarioService(db).get_horarios()
    if not horarios:
        return JSONResponse(content={"message": "Horarios not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(horarios), status_code=200)

@horario_router.get('/horarios/{horario_id}', tags=["Horarios"])
def get_horario_by_id(horario_id: int):
    db = Session()
    horario = HorarioService(db).get_horario_by_id(horario_id)
    if horario is None:
        return JSONResponse(content={"message": "Horario not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(horario), status_code=200)

@horario_router.post('/horarios', tags=["Horarios"])
def create_horario(horario: Horario):
    db = Session()
    query = HorarioService(db).add_horario(horario)
    return JSONResponse(content={"message": "Horario created", "horario": jsonable_encoder(query)}, status_code=201)

@horario_router.put('/horarios/{horario_id}', tags=["Horarios"])
def update_horario(horario_id: int, horario: Horario):
    db = Session()
    query = HorarioService(db).update_horario(horario_id, horario)
    if query is None:
        return JSONResponse(content={"message": "Horario not found"}, status_code=404)
    return JSONResponse(content={"message": "Horario updated", "horario": jsonable_encoder(query)}, status_code=200)

@horario_router.delete('/horarios/{horario_id}', tags=["Horarios"])
def delete_horario(horario_id: int):
    db = Session()
    query = HorarioService(db).delete_horario(horario_id)
    if query is None:
        return JSONResponse(content={"message": "Horario not found"}, status_code=404)
    return JSONResponse(content={"message": "Horario deleted", "horario": jsonable_encoder(query)}, status_code=200)