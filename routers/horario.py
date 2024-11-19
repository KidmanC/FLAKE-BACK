from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.horario import Horario
from config.database import Session
from config.database import get_db, Session
from services.horario import HorarioService
from schemas.dia_semana import Dia_semana
from datetime import time
from typing import Optional, List


horario_router = APIRouter()

@horario_router.get('/horarios/filter', tags=["Horarios"], response_model=List[Horario])
def horarios_filter(
    horario_id: Optional[int] = None,
    clase_id: Optional[int] = None,
    dia_semana: Optional[Dia_semana] = None,
    hora_inicio: Optional[time] = None,
    hora_fin: Optional[time] = None
):
    db = Session()
    filter = {
        "horario_id": horario_id,
        "clase_id": clase_id,
        "dia_semana": dia_semana,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin
    }
    horarios = HorarioService(db).get_horario(filter)
    if not horarios:
        return JSONResponse(content={"message": "Horario no encontrado"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(horarios), status_code=200)

@horario_router.post('/horarios', tags=["Horarios"])
def create_horario(horario: Horario):
    db = Session()
    try:
        query = HorarioService(db).add_horario(horario)
        return JSONResponse(content={"message": "Horario creado exitosamente", "horario": jsonable_encoder(query)}, status_code=201)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@horario_router.put('/horarios/edit/{horario_id}', tags=["Horarios"])
def update_horario(
    horario_id: int,
    clase_id: Optional[int] = None,
    dia_semana: Optional[Dia_semana] = None,
    hora_inicio: Optional[time] = None,
    hora_fin: Optional[time] = None
):
    db = Session()
    filter = {
        "horario_id": horario_id,
        "clase_id": clase_id,
        "dia_semana": dia_semana,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin
    }
    try:
        query = HorarioService(db).update_horario(filter)
        if query is None:
            return JSONResponse(content={"message": "Horario no encontrado"}, status_code=404)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return JSONResponse(content={"message": "Horario actualizado exitosamente", "horario": jsonable_encoder(query)}, status_code=200)

@horario_router.delete('/horarios/{horario_id}', tags=["Horarios"])
def delete_horario(horario_id: int):
    db = Session()
    query = HorarioService(db).delete_horario(horario_id)
    if query is None:
        return JSONResponse(content={"message": "Horario no encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Horario eliminado exitosamente", "horario": jsonable_encoder(query)}, status_code=200)